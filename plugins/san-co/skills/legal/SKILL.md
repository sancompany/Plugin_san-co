---
name: legal
description: Cuida das obrigações legais de um projeto da San & Co. — inventário de dados durante a construção, direitos do titular e arrependimento no código, procedimento de incidente, e Termos de Uso e Política de Privacidade antes do lançamento. Use ao coletar dado novo, integrar terceiro, construir conta de usuário ou cobrança, ou preparar um projeto para ir ao ar.
---

# Obrigações legais — San & Co.

**Não sou advogado e isto não é parecer jurídico.** Este material organiza os fatos e monta o rascunho; projeto que movimenta dinheiro ou guarda dado de terceiro merece revisão de um advogado antes de ir ao ar.

## O que a lei exige não cabe num texto no fim

Termos e Política são a parte visível. O que costuma faltar é o que exige **código ou procedimento**: exportar e excluir conta, revogar consentimento, botão de arrependimento com estorno, log de acesso de seis meses, runbook de incidente com prazo de seis dias úteis, nota fiscal por cobrança, acessibilidade. Nada disso se escreve na véspera — cada um tem estação certa, e a lista completa com prazo, fonte e o que **não** é obrigatório para empresa pequena está em **`references/obrigacoes-brasil.md`**. Ler na estação 4.

## Por estação

**4 — Contratos.** Começar o `docs/inventario-de-dados.md`: que dado, de quem, para quê, onde fica, quem mais recebe, por quanto tempo, como é apagado, e a base legal. **Ele é o registro de operações que a LGPD exige** — mantido, já cumpre a obrigação. Listar os subprocessadores (banco, hospedagem, e-mail, pagamento) e a região de cada um: dado fora do Brasil é transferência internacional, e não há dispensa para pequeno porte.

**5 — Construção.** Os direitos do titular são funcionalidade, não texto: exportar os dados da conta, excluir a conta de verdade (preservando só o que tem guarda legal, com registro do que ficou e por quê), revogar consentimento com um clique, canal do titular, registro de requerimentos com data. Em venda a consumidor: confirmação da contratação por e-mail com o contrato, ticket com auto-resposta, **botão de arrependimento na mesma ferramenta em que se contratou, com estorno no mesmo fluxo**. Log de acesso — data, hora, IP — com retenção de seis meses. Uma nota fiscal por cobrança. Tudo isso está no `docs/funcional.md` como comportamento, e é construído como qualquer outro.

**6 — Prontidão.** O procedimento de incidente pronto antes de precisar: runbook de uma página no `RUNBOOK.md`, conta gov.br testada no peticionamento da ANPD, modelo de e-mail de notificação, tabela de registro de incidentes. Acessibilidade verificada — é obrigação legal para site privado no Brasil, e o padrão é WCAG 2.2 AA.

**7 — Lançamento.** Os dois documentos, escritos a partir do inventário — é quase tradução, porque o inventário já respondeu as perguntas difíceis. No site, em destaque: razão social, CNPJ, endereço, e-mail; sumário do contrato antes de fechar; preço sem despesa escondida. Banner de cookies **só se houver cookie não necessário** — app autenticado sem analytics de terceiro não precisa.

## Gatilhos que reabrem o inventário

Campo novo em formulário; integração nova com terceiro; log novo que grave algo de pessoa; mudança de onde o dado fica; funcionalidade que cruza dados antes separados. Atualizar o inventário faz parte da tarefa que criou o dado, como o teste faz.

## O que decidir cedo, porque é caro desfazer

1. **Caminho de exclusão.** Se apagar quebra histórico ou obrigação fiscal, é problema de modelagem, não de texto — decidir no dia 1 o que se apaga, o que se anonimiza, o que se guarda por lei.
2. **Coletar o mínimo.** Dado que não existe não vaza e não precisa ser declarado.
3. **Quem mais recebe, e onde.** Todo terceiro é uma linha de compartilhamento, e a região dele decide se há transferência internacional.

## Gate de lançamento

Projeto com usuário externo **não é divulgado nem aberto a terceiros** sem os documentos publicados — o deploy da estação 5, sem anúncio, continua permitido (skill `leis`). O que trava é a estação 7.

## Manutenção

Os documentos têm data e versão. Mudança relevante — dado novo, terceiro novo, finalidade nova — atualiza o texto **e** avisa quem já usava; versões antigas ficam arquivadas, porque quem aceitou a anterior aceitou aquela.

## Referências

- `references/obrigacoes-brasil.md` — cada obrigação com prazo, fonte, estação, e o que não se aplica a empresa pequena.
- `references/conteudo-termos-e-privacidade.md` — o que entra em cada documento, item por item.
