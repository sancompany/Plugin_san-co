---
name: novo-projeto
description: Conduz a definição de escopo de um projeto novo da San & Co. em gates sequenciais, incluindo os contrapontos à ideia. Use quando o usuário disser que tem uma ideia, quer criar um app, site, sistema ou automação, ou pedir para começar/escopar um projeto.
---

# Novo projeto — escopo em gates

## Porta de entrada — isso é projeto ou tarefa?

Checar antes de qualquer coisa. **Não rodar este processo em tarefa.**

É **tarefa** (ir direto para a skill `construir`) quando: cabe em um arquivo ou um script, não guarda dado que alguém vai consultar depois, não fica rodando sozinho, não é exposto à internet, e ninguém além de quem pediu depende dela. Exemplos: renomear arquivos em lote, converter uma planilha, ajustar um texto numa página existente, consertar um valor errado.

É **projeto** (seguir as fases abaixo) quando qualquer uma destas for verdadeira: guarda dado que precisa existir amanhã, roda sem alguém olhando, tem usuário além de quem pediu, é exposto à internet, ou toca dinheiro, senha ou documento.

Na dúvida entre os dois, perguntar ao usuário em uma linha em vez de assumir. Burocratizar tarefa pequena é o jeito mais rápido de fazer o processo ser abandonado — e processo abandonado não protege nada.

Sendo projeto: nenhum é simples demais para as fases abaixo. É no "óbvio" que premissa escondida passa despercebida.

## Condução

Conduzir as fases **uma de cada vez**, esperando confirmação antes de avançar. Nunca despejar todas numa resposta só e assumir aprovação silenciosa. Perguntas de esclarecimento vêm uma de cada vez, preferindo múltipla escolha.

## Fase 0 — Escopo

Obter resposta escrita para:

- Qual problema real resolve, e para quem especificamente (nomear a pessoa ou papel, não "usuários").
- O que acontece hoje sem isso? Alguém sofre de verdade ou é dor pequena?
- Já existe pronto (planilha, app, serviço pago)? Por que construir vence adotar?
- Quantos usuários em 3 meses, 1 ano, 3 anos? (mesmo que seja "só eu" — isso define a arquitetura)
- Existe mais de um perfil de acesso? Quais permissões?
- Por que agora? O que muda se adiar 3 meses?
- Como saber objetivamente que deu certo? Uma métrica, não uma sensação — e ela vai ser instrumentada: a estação 4 nomeia os eventos que a alimentam, a 6 só fecha respondendo "quantos ontem?" com número.
- O que está explicitamente **fora de escopo** na v1?

Sem resposta clara, o projeto ainda é ideia, não especificação — não avançar.

## Fase 0.5 — Um projeto ou vários?

Checar se o pedido descreve mais de um subsistema independente disfarçado de um só. Sinal: junta duas coisas que não compartilham usuário, dado nem motivo. Se houver decomposição, cada sub-projeto ganha sua própria Fase 0 e seu próprio documento.

## Fase 1 — Classificação

| Eixo | Opções |
|---|---|
| Porte | Pessoal · Familiar/pequeno grupo · Produto externo/cliente |
| Dado sensível | Nenhum · Pessoal comum · Financeiro/senha/documento |
| Vida útil | Descartável · Vai crescer · Nasce para durar anos · **Tem data de morte** |
| Tipo | Institucional/landing · SaaS/painel com login · E-commerce/catálogo · PWA/mobile-first (pode combinar) |

Os três primeiros eixos definem o rigor das demais leis (Lei 0). O **tipo** define qual referência de desenvolvimento a estação 5 carrega (skill `construir`, "O mapa do que todo site tem").

**Projeto com data de morte** (evento, campanha, sazonal) exige três respostas antes de nascer, porque depois do fim ninguém volta para pensar nelas: o que acontece com o dado das pessoas que usaram, quem desliga o serviço e quando, e o que precisa ser guardado por obrigação fiscal ou legal mesmo depois de tudo desligado.

## Fase 2 — Validação técnica

- Depende de outro projeto do ecossistema? Qual o contrato entre eles?
- Onde roda, e por quê (custo real, não hábito)?
- Qual stack, e por quê? Se a resposta for "é a que eu sei", escrever isso honestamente.
- Mais de uma pessoa vai mexer no código algum dia?

Ao responder "onde roda" e "qual stack", apresentar **2 a 3 opções com trade-offs**, liderando pela recomendada. Nunca uma única opção já fechada.

## Fase 3 — Contrapontos (atacar a ideia antes de se apaixonar)

- **Necessidade**: se não construir, o que quebra de verdade? Existe ferramenta pronta que resolve 80% em um dia?
- **Manutenção**: quem mantém isso em 1 ano? Adiciona mais uma senha, domínio ou serviço pago para gerenciar?
- **Escala**: e se 10x mais gente usar? Existe ponto único de falha? A arquitetura está superdimensionada para um problema pequeno?
- **Segurança**: se vazasse hoje, qual o pior dado exposto? Alguém de fora teria motivo para atacar?
- **Sobreposição**: duplica algo que já existe no ecossistema? Se duplica, é intencional ou deveria ser feature do projeto existente?
- **Prazo**: existe data que não se move (evento, campanha, obrigação legal)? Se sim, o que acontece se atrasar — o projeto perde valor ou perde sentido inteiro? Qual é a versão reduzida que ainda entrega o essencial na data? Projeto com data imóvel e sem versão reduzida definida falha por atraso mesmo estando tecnicamente correto.

Fechar com um veredito de 2-3 frases: sobrevive como está, precisa ser reduzido, ou é descartado.

## Fase 3.5 — Autorrevisão antes de apresentar

Revisar o escopo inteiro procurando: placeholder esquecido ("TBD", campo em branco), contradição entre seções, ambiguidade que dá para ler de duas formas, e vazamento de escopo (algo que deveria estar fora da v1 ainda aparecendo como parte dela). Corrigir direto, e só então apresentar para aprovação final.

## Fechamento

O inventário de dados começa junto com o código, e as obrigações legais que exigem código entram no `docs/funcional.md` na estação 4 (skill `legal`).

Antes de qualquer implementação começar, o resultado vira **dois arquivos** (a Lei 10 explica a diferença entre eles). Eles nascem escritos agora e são **commitados na estação 3**, quando o repositório passa a existir:

- **`docs/specs/AAAA-MM-DD-<projeto>.md`** — o escopo validado: problema, usuário, classificação, contrapontos e veredito. Registro de decisão, escrito uma vez.
- **`CONSTRAINTS.md`** — o que ficou **fora** de escopo, com o porquê de cada item, mais os limites assumidos. É o que impede alguém de construir depois o que foi decidido não construir.

O que ficou fora da v1 se divide em dois: veto vai para o `CONSTRAINTS.md`; o que se quer para depois vai para `docs/proximas-versoes.md` (Lei 10).

**Esta é a estação 1 da esteira.** Com os dois arquivos escritos, ela fecha e a próxima é **Fronteiras** — skill `classificar`: estrutura ou projeto, o que consome da plataforma, onde roda e onde o dado mora. A esteira completa está na skill `leis`.
