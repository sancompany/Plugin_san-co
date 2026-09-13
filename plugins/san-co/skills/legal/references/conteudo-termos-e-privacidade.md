# O que entra em cada documento

Referência de conteúdo para projetos da San & Co. no Brasil. **Não é parecer jurídico** — é a lista de fatos a cobrir, para o rascunho sair completo e a revisão de um advogado ser curta e barata.

---

## Parte 1 — Inventário de dados (`docs/inventario-de-dados.md`)

O documento que se mantém durante a construção. Uma linha por dado coletado:

| Dado | De quem | Finalidade | Base legal | Onde fica (região) | Quem mais recebe | Retenção | Como é apagado | Medida de segurança |
|---|---|---|---|---|---|---|---|---|
| Nome | comprador | identificar a compra e emitir nota | execução de contrato | Supabase do projeto (sa-east-1) | Asaas (cobrança) | 5 anos (fiscal) | anonimizado após o prazo | RLS; acesso só pela aplicação |
| CPF | comprador | exigência da Asaas para cobrança | obrigação legal | Supabase do projeto (sa-east-1) | Asaas | 5 anos (fiscal) | idem | idem; nunca em log |
| E-mail | comprador | enviar confirmação e nota | execução de contrato | Supabase do projeto (sa-east-1) | Asaas, Google Workspace (EUA — transferência internacional) | enquanto a conta existir | exclusão a pedido | idem |

Registrar também o que **não** é dado de pessoa mas vale rastrear: IP em log, cookie, identificador de sessão.

Terceiros comuns no ecossistema, que viram linha de compartilhamento: **Asaas** (pagamento e nota), **Google Workspace** (e-mail, Drive), **Northflank** (hospedagem), **Supabase** (banco), **Cloudflare** (DNS e tráfego). Anotar se algum transfere dado para fora do Brasil — isso precisa ser declarado.

---

## Parte 2 — Termos de Uso

Contrato entre o projeto e quem usa. Cobrir:

**Identificação**
- Razão social, CNPJ, endereço e e-mail de contato do fornecedor. Obrigatório: o CDC exige que o consumidor saiba com quem está contratando.

**O serviço**
- O que o serviço faz, em linguagem clara.
- O que ele **não** faz — limita expectativa e reclamação.
- Requisitos para usar (idade mínima, conta, dispositivo).

**Regras de uso**
- Condutas proibidas e o que acontece se ocorrerem.
- Responsabilidade do usuário pelo conteúdo que envia, se houver envio.

**Dinheiro** (quando há cobrança)
- Preço, o que está incluído, forma de pagamento aceita.
- Quando a cobrança acontece e, em assinatura, que é **renovação automática** e como cancelar.
- **Direito de arrependimento: 7 dias** para compra feita fora do estabelecimento, incluindo internet (CDC, art. 49). É obrigatório, não é escolha, e precisa estar escrito.
- Política de reembolso e estorno: em quanto tempo, por qual meio, quem aciona. Para projetos que usam o San Checkout, lembrar que estorno é sempre integral e que boleto tem etapa a mais dependendo do pagador.
- Quando **não** há reembolso (evento realizado, serviço já entregue) — e isso precisa ser compatível com o CDC, não o contrário.

**Entrega**
- O que o comprador recebe, em quanto tempo e por qual canal.
- O que acontece se a entrega falhar.

**Cancelamento e encerramento**
- Como o usuário encerra a conta ou a assinatura.
- Em que casos o projeto pode suspender ou encerrar o acesso, e com qual aviso.

**Propriedade intelectual**
- De quem é a marca, o conteúdo e o software.
- O que o usuário pode e não pode fazer com isso.

**Responsabilidade**
- Limites da responsabilidade do fornecedor — sabendo que o CDC restringe muito o que se pode excluir em relação a consumidor. Cláusula que exclui toda responsabilidade tende a ser considerada abusiva e não protege.
- Indisponibilidade do serviço, manutenção, falha de terceiro (ex.: instabilidade do meio de pagamento).

**Fechamento**
- Como os termos podem mudar e como o usuário é avisado.
- Lei aplicável e foro.
- **Data da última atualização e versão.**

---

## Parte 3 — Política de Privacidade (LGPD)

**Quem trata os dados**
- Controlador: razão social, CNPJ, endereço.
- Canal de contato para assuntos de privacidade (e-mail dedicado, ex.: `privacidade@`). A LGPD prevê a figura do encarregado; independentemente do porte, tem que haver um canal real que responde.

**O que é coletado**
- Lista item por item, não "dados necessários à prestação do serviço". Nome, e-mail, CPF/CNPJ, telefone, endereço, IP, cookies, o que for.
- Separar o que o usuário fornece do que o sistema coleta sozinho.

**Para que serve cada dado**
- Finalidade específica por dado ou por grupo. Genérico demais não cumpre a exigência de transparência.

**Base legal de cada tratamento**
- Execução de contrato (a maior parte numa venda), obrigação legal (guarda fiscal), consentimento (marketing, cookie não essencial), legítimo interesse (segurança, prevenção a fraude).
- Consentimento precisa ser específico e revogável — e não serve de base para o que já é necessário para executar o contrato.

**Com quem é compartilhado**
- Nomear os terceiros, não dizer "parceiros". Para o ecossistema San & Co.: Asaas, Google, Northflank, Supabase, Cloudflare, conforme o projeto.
- Dizer se há transferência internacional.

**Por quanto tempo**
- Prazo de retenção por tipo de dado e o critério. Dado fiscal tem prazo legal; o resto não deve ser guardado "para sempre" por inércia.

**Direitos do titular**
- Confirmação, acesso, correção, anonimização, portabilidade, eliminação, informação sobre compartilhamento, revogação de consentimento.
- **Como exercer**, concretamente: qual canal e em quanto tempo responde. Esta é a parte que mais aparece incompleta.

**Segurança**
- Medidas adotadas, em termos verdadeiros. Não prometer o que não existe: prometer criptografia que não foi implementada é pior que não citar.
- O que acontece em caso de incidente (comunicação ao titular e à ANPD, quando cabível).

**Cookies e rastreamento**
- Quais existem, para quê, e como recusar os não essenciais — se houver banner, ele precisa realmente respeitar a recusa.

**Menores**
- Se o serviço pode ser usado por criança ou adolescente, o tratamento exige cuidado adicional e consentimento de responsável. Se não é o público, dizer isso.

**Fechamento**
- Como a política muda e como o usuário fica sabendo.
- **Data de vigência e versão**, com as versões anteriores arquivadas.

---

## Erros que mais aparecem

- Copiar política de outro site e deixar nome, dado ou terceiro que não correspondem ao sistema real. Isso é pior que não ter: vira declaração falsa sobre o próprio tratamento.
- Prometer segurança inexistente.
- Listar direito do titular sem dar o canal para exercê-lo.
- Esquecer o direito de arrependimento de 7 dias em venda online.
- Não declarar um terceiro que recebe dado (o meio de pagamento é o mais esquecido).
- Trocar o texto em silêncio depois de publicado, sem versão nem aviso.
- Deixar os documentos escritos, mas sem link acessível no rodapé e no fluxo de compra.
