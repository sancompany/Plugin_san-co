# Definição funcional — o que o sistema faz, em detalhe suficiente para construir

Artefato obrigatório da **estação 4**, em `docs/funcional.md`. É o documento que permite a estação 5 construir o projeto inteiro **sem perguntar nada** — e é a diferença entre um agente que entrega o sistema pronto e um que entrega um esqueleto e uma lista de dúvidas.

**Como ele se distingue dos vizinhos:** o spec diz *por que o projeto existe*; o `CONSTRAINTS.md` diz *o que ele não faz*; este diz *o que ele faz*, com detalhe de comportamento. Pergunta que ele responde: "posso construir esta tela agora, sem inventar nada?"

**A regra que dá sentido a ele:** a construção não começa com pergunta em aberto aqui. Se a sessão de construção precisar decidir comportamento por conta própria, a estação 4 não fechou — volta, completa, e só então a 5 abre. Comportamento inventado na hora de codar é o que produz tela que ninguém pediu e regra que ninguém combinou.

---

## O modelo

### 1. Público-alvo

Quem usa, **nomeado por papel**, nunca "usuários". Para cada papel: o que essa pessoa quer resolver, em uma frase, e o que ela sabe fazer sozinha.

> Exemplo: *Comprador* — quer pagar rápido no celular, no meio de outra coisa; não vai criar conta nem ler instrução. *Administrador* — acompanha pedidos do dia e estorna quando o cliente reclama; usa no computador, conhece o sistema.

Papel sem tela é papel que não existe. Tela sem papel é tela que ninguém abre.

### 2. Jornada principal

Do primeiro contato até o objetivo cumprido, **numerado**, uma linha por passo, com o que o sistema faz em cada um. Uma jornada por papel.

Terminada a jornada, a pergunta de controle: *isso é tudo que essa pessoa precisa fazer?* O que sobrar vira jornada secundária, listada do mesmo jeito.

### 3. Telas

Uma linha por tela: **nome · URL · quem acessa · o que mostra · o que dá para fazer nela · para onde leva**. A URL já nasce aqui, minúscula e com hífen, porque é a lista que a estação 5 confere contra as rotas (`construir/references/desenvolvimento-web.md`, item 1).

A lista tem que fechar: toda tela citada em alguma jornada existe aqui, e toda tela daqui aparece em alguma jornada. Tela órfã é funcionalidade que ninguém pediu — sai, ou vira jornada.

### 4. Estados de cada tela

Para cada tela, o que aparece em: **vazio, carregando, erro, sucesso, sem permissão, lista longa demais**. Não é detalhe visual — é comportamento, e é a maior fonte de "ficou meia-boca": tela construída só com o caminho feliz está pela metade, e a metade que falta é a que o usuário encontra no pior dia dele.

Estado que não se aplica é escrito como "não se aplica", nunca omitido — omissão não distingue "pensei e não precisa" de "esqueci".

### 5. Regras de negócio

Numeradas, cada uma com **o que vale, o que acontece quando é violada, e quem vê a violação**.

> Exemplo: *RN-03 — pedido expira em 30 minutos sem pagamento. Expirado, a página de status mostra "pedido expirado" com botão de refazer, e o pedido não pode mais ser pago. O comprador vê; o administrador vê na listagem como expirado.*

Regra sem consequência escrita não é regra, é intenção — e vira `if` inventado na hora de codar.

### 6. Textos que o sistema diz

As mensagens que o usuário lê, **no texto final**: rótulo de botão, mensagem de erro por campo, confirmação, aviso, e-mail. Escrever aqui, não na tela de código.

Isso evita duas coisas de uma vez: texto de exemplo que vai para produção, e a mesma mensagem escrita diferente em três lugares — que é a lição nº 1 na forma de texto.

### 7. Quando dá errado

Por fluxo: o que acontece se o terceiro não responder, se a rede cair no meio, se o usuário der duplo clique, se ele voltar no navegador, se o pagamento cair depois do tempo. Cada um com o que o sistema faz e o que a pessoa vê.

Este bloco é o que separa o que sobrevive ao mundo real do que só funciona na demonstração.

### 8. Direitos e obrigações que viram tela

O que a lei exige do produto entra aqui como comportamento, não como texto (skill `legal`): exportar dados da conta, excluir conta com o que fica e por quê, revogar consentimento, canal do titular, e — havendo venda a consumidor — confirmação da contratação, ticket de atendimento com auto-resposta, botão de arrependimento com estorno no mesmo fluxo. Cada um é tela ou fluxo listado nas seções 2 a 7, não uma seção à parte.

### 9. A métrica de sucesso e os eventos que a alimentam

A estação 1 definiu como saber que deu certo. Aqui isso vira instrumentação: **a métrica principal** em uma linha, e **cinco a dez eventos** que a alimentam, nomeados por convenção antes da primeira linha de código (`categoria:objeto_acao`, verbo no presente; propriedades `objeto_adjetivo`). Para cada evento: onde é emitido — os críticos (cadastro, ação central, pagamento confirmado) **no servidor** —, quais propriedades carrega, e qual pergunta de negócio responde.

Sem esta seção o projeto lança sem conseguir medir o próprio sucesso, e a estação 6 não fecha: ela exige responder "quantos ontem?" com número.

### 10. O que fica fora desta versão

Uma linha apontando para o `CONSTRAINTS.md` e para `docs/proximas-versoes.md`, sem repetir a lista.

---

## Como saber que está pronto

Quatro perguntas, e as quatro precisam ser "sim" antes de a estação 4 fechar:

1. Consigo construir cada tela lendo só isto, sem inventar comportamento?
2. Cada papel tem jornada completa, e cada tela pertence a alguma jornada?
3. Cada regra de negócio tem consequência escrita?
4. Cada fluxo tem o caminho de quando dá errado — e os eventos da métrica estão nomeados?

Faltando qualquer uma, o que falta é pergunta para o dono — feita **agora**, na estação 4, não na hora de construir. Pergunta feita aqui custa uma linha; a mesma pergunta na estação 5 custa a tela inteira refeita.

## Como ele é mantido

É o único documento de definição que **muda durante o projeto**, porque comportamento se ajusta ao construir. Mudou o comportamento, muda aqui na mesma tarefa — código e definição divergindo é a lição nº 2 esperando acontecer.

Na volta da esteira (versão nova), ele é atualizado com o delta, não reescrito: o que já existe e continua valendo permanece com o texto que tinha.
