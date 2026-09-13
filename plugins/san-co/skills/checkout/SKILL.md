---
name: checkout
description: Integra um projeto da San & Co. ao San Checkout, o motor de pagamento do ecossistema. Use quando o projeto precisar receber pagamento, cobrar assinatura, estornar, ou quando alguém propuser construir cobrança do zero.
---

# San Checkout — integração

**Nenhum projeto da San & Co. constrói cobrança própria.** Pagamento é estrutura, já existe e já está em produção. Projeto novo que precisa receber dinheiro consome o Checkout — Pix, boleto, cartão em até 12x, assinatura por cartão e assinatura por Pix Automático já estão resolvidos.

**Contrato versão 1.** O documento canônico é o `API.md` na raiz do repositório do San Checkout — ele tem todos os campos, códigos de erro, limites e exemplos de verificação de webhook em três linguagens. Ler de lá antes de escrever a integração. O antigo `INTEGRACAO.md` virou só um redirecionamento e não deve ser usado. Esta skill carrega o que é estrutural e raramente muda; detalhe de campo consulta-se na fonte.

## O modelo: pull

O Checkout **não guarda catálogo**. Não sabe o que o projeto vende, por quanto, nem para quem.

1. O projeto cria o pedido **no próprio banco** e gera um id.
2. Manda o comprador para o link do Checkout levando só esse id.
3. O Checkout liga de volta na API do projeto (`GET /pedido/{id}`) para saber o que é aquele pedido.
4. Cobra o valor que **recebeu da API**, nunca o que veio na URL.
5. Avisa o projeto por webhook assinado quando o dinheiro entra.

Consequência de desenho: adulterar o link não muda valor nenhum, e o dado do projeto continua no projeto. Isso é o isolamento de banco da skill `classificar` valendo na prática.

## O que o projeto expõe

Duas rotas `GET` (só a que corresponder ao que vende) e uma `POST` para receber notificação:

- `GET {base}/pedido/{pedidoId}` — venda avulsa
- `GET {base}/plano/{planoId}` — assinatura
- `POST {webhook_url}` — notificações

Prazo de resposta: **45 segundos**, calibrado para o pior cold start de hospedagem gratuita. O Checkout não tenta de novo sozinho: estourou, o comprador vê erro.

O Checkout **não soma nada** — o projeto manda o total pronto, em reais com centavos (`80.00`, nunca `8000`).

## As seis regras que não se negocia

1. **Id imprevisível.** UUID, hash ou token opaco — nunca o id sequencial da tabela. A rota do pedido é pública por necessidade (o comprador chega antes de qualquer login); com id sequencial, qualquer um varre `?pedido=1,2,3` e lê valor, itens e dados do pagador de **todos** os pedidos do projeto. O Checkout recusa (400) id só de dígitos com menos de 8 caracteres.
2. **Conferir a `X-Checkout-Key`** em toda chamada recebida, respondendo 401 se não bater. Sem isso o endpoint de pedido é público para a internet inteira.
3. **Verificar a assinatura HMAC de todo webhook** antes de confiar nele: recusar timestamp fora da janela de 300s, montar `"{timestamp}.{corpo cru}"` sem reserializar o JSON, comparar em tempo constante. Sem isso, qualquer um que descubra a URL manda `"status": "confirmado"` e o sistema libera pedido **sem ninguém ter pagado**.
4. **A chave é segredo de servidor.** Nunca em front-end, variável de build ou repositório. Quem tem a chave consulta, **estorna** e forja webhook assinado.
5. **Processamento idempotente** — chave natural `chargeId` + `status`. O mesmo webhook pode chegar mais de uma vez.
6. **Ignorar campo, `status` e `evento` desconhecidos**, respondendo 200 assim mesmo. O contrato promete só adicionar, nunca remover nem renomear; validar com lista fechada quebra na primeira melhoria.

## Conciliação diária não é opcional

A fila de reenvio do Checkout é **em memória**: se o processo reiniciar entre as tentativas, aquela notificação se perde — e o pagamento continua confirmado do lado do Checkout, só o aviso some. Reinício acontece em deploy, em queda e no despertar de hospedagem que dorme por inatividade. Plano pago reduz muito a frequência; não elimina o caso.

Rodar uma vez por dia sobre tudo que ainda está "aguardando pagamento" no projeto — são **duas rotas**, uma para cada tipo:

- **Pedido avulso**: `GET /api/checkout/cobranca/{contratanteId}/{pedidoId}`
- **Assinatura**: `POST /api/checkout/consultar-assinatura` com `{ planoId, documento }` — a rota de pedido não alcança recorrência, porque cobrança de assinatura é gravada por `planoId`. É `POST` de propósito: documento em caminho de URL vazaria para log de acesso e referer.

As duas **reconsultam a Asaas** quando a cobrança ainda parece pendente e corrigem o registro antes de responder — havendo divergência, **o que elas respondem é o correto**.

Na resposta de assinatura, ler as **duas metades**: `status` diz se o vínculo existe (`ativa`, `pausada`, `cancelada`), e `ultimaCobranca.status` diz se o último ciclo entrou. Assinante `ativa` com última cobrança `vencido` ou recusada é exatamente quem precisa receber o link `&renovar=1` — e é o caso que passa despercebido se só olhar o vínculo.

Ausência de notificação nunca significa "pago".

## O que é responsabilidade do projeto, não do Checkout

- **Nota fiscal e e-mail ao comprador** no `confirmado`. A Asaas está configurada para não notificar o cliente final.
- **Manter o `status` do pedido atualizado** (`pendente`/`pago`/`cancelado`): `pago` e `cancelado` fazem o Checkout recusar cobrar (409), e é isso que protege quem recarregou a página ou abriu duas abas.
- **Decidir cancelamento e pausa de assinatura.** O pagador nunca cancela sozinho pelo Checkout.
- **Mandar o link de renovação (`&renovar=1`)** ao receber `cobranca_falhou`.

## Detalhes que costumam pegar de surpresa

- `expiraEm` (reserva com prazo) **desliga o boleto** naquele pedido — boleto leva até 3 dias para compensar, incompatível com reserva curta.
- Cartão e assinatura **exigem telefone**; cartão exige também endereço completo, por antifraude da Asaas.
- Dado de cartão não passa pelo Checkout nem pelo projeto — é digitado em pop-up da própria Asaas, o que mantém os dois lados fora do escopo PCI-DSS. Por isso não existe "trocar o cartão": a troca é o link `&renovar=1`, que gera um id de assinatura novo na Asaas.
- A taxa do Checkout é **somada por cima**, nunca descontada: o projeto recebe `valorComDesconto + frete` integral.
- Nada é autoatendimento: `contratante_id`, URL base, chave, `webhook_url`, `wallet_id` e métodos habilitados são cadastrados manualmente por quem administra o Checkout.

## O contratante de teste

O Checkout é estrutura, e estrutura não se testa sozinha: precisa de alguém do outro lado da integração. Por isso existe um **contratante de teste** permanente — um consumidor mínimo do Checkout, versionado, no ar, que serve para exercitar o contrato inteiro sem tocar em projeto real.

Ele tem dois papéis, e o segundo costuma ser esquecido:

1. **Bancada de teste.** É contra ele que os seis passos rodam na estação 6 do Checkout, e é ele que permite testar estorno e cancelamento sem mexer no histórico de um cliente de verdade.
2. **Implementação de referência.** Projeto novo que vai integrar lê o código dele em vez de reconstruir a partir do `API.md`. Documento explica o contrato; código funcionando mostra a ordem das chamadas, o formato real do corpo e como a assinatura do webhook é conferida na prática.

**Credenciais próprias, sempre.** `contratante_id`, chave e `wallet_id` do contratante de teste são só dele. Reaproveitar os de um projeto real faz um estorno de teste cair no extrato de um cliente — e ninguém percebe até a conciliação daquele mês.

**Ele é mantido, não é descartável.** Contrato do Checkout que muda e não é refletido nele deixa a bancada medindo a versão anterior — e uma bancada desatualizada aprova integração quebrada, que é a lição nº 14 no lugar mais caro possível. Alterar o Checkout inclui atualizar o contratante de teste, na mesma tarefa.

## Antes de anunciar

O `API.md` tem o checklist completo de integração e o teste de ponta a ponta. Rodar os seis passos — pedido de valor baixo, pagar por Pix, conferir webhook assinado, reabrir a página de status, conciliar, estornar — **na estação 6, antes do ciclo de segurança**, e de novo na Passada 5 da varredura final. Nunca depois do primeiro comprador real. Vendendo recorrência, incluir o ciclo de assinar, pausar, retomar e cancelar.

Se este documento e o `API.md` divergirem, **o `API.md` está certo**. Se o contrato virar `versao: 2`, esta skill precisa ser revisada.
