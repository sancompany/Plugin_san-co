---
name: leis
description: Aplica as leis de construção da San & Co. — a esteira de sete estações, as onze leis, o ciclo de conformidade, modelo por estação, deploy, prontidão operacional e documentação. Use ao abrir um projeto, ao fechar ou abrir uma estação, ao montar estrutura de pastas, ao revisar contra os padrões, ou antes de subir algo para produção.
---

# Leis de construção — San & Co.

## Para que esta esteira existe

Ela foi feita para **projeto nascendo do zero** — da primeira conversa sobre a ideia até o projeto completo, no ar e medindo o próprio resultado. As sete estações descrevem esse caminho, nessa ordem, e cada uma entrega o que a próxima precisa. Projeto que nasce aqui não tem etapa faltando: cada coisa chega na hora em que ainda é barata de decidir.

**Projeto que já existe entra pela auditoria, não pelo meio.** Atravessar as estações anteriores **como verificação, não como construção**: a 1 pergunta se existe spec e escopo negativo; a 2, se a classificação foi feita; a 3, se há repositório, segredo fora do código e CI. O que faltar vira pendência no `CLAUDE.md` e entra no ciclo de conformidade — não vira motivo para refazer o projeto. Quase sempre o que falta lá atrás é o que trava a estação 6 ou 7 no pior momento.

## A esteira: sete estações, em ordem de criação

**Estação não fecha, esteira não anda.** Todo projeto atravessa estas estações nesta ordem; na última, o projeto está no ar, legal, e medido.

| # | Estação | O que acontece | Fecha quando | Leis e referências |
|---|---|---|---|---|
| 1 | **Escopo** | Skill `novo-projeto`: é projeto ou tarefa, Fases 0 a 3.5, contrapontos, a métrica de sucesso | `docs/specs/` e `CONSTRAINTS.md` **escritos** (o repositório nasce na 3) | — |
| 2 | **Fronteiras** | Skill `classificar`: estrutura ou projeto, o que consome da plataforma, onde roda, banco próprio | classificação registrada, capacidades a consumir listadas, hospedagem escolhida por número e não por hábito | Lei 0; `classificar/references/plataformas-san-co.md` |
| 3 | **Fundação** | Repositório, árvore, segredos, CI com as verificações automáticas de segurança, `CLAUDE.md`, `RUNBOOK.md` iniciado | `git init` e push feitos; spec e `CONSTRAINTS.md` commitados; segredo fora do código; CI verde num push real quando a classificação exigir (dispensa escrita no `CONSTRAINTS.md`); `CLAUDE.md` verdadeiro | Leis 1, 3, 9; `seguranca-san/references/verificacoes-automaticas.md` |
| 4 | **Contratos** | Modelo de dados e migrations, contrato de API, integração de pagamento, inventário de dados, **definição funcional** com os eventos da métrica de sucesso | contratos escritos; inventário com as primeiras linhas; `docs/funcional.md` respondendo "sim" às perguntas de prontidão de `references/definicao-funcional.md` | Lei 6; skills `checkout`, `legal`; `references/definicao-funcional.md` |
| 5 | **Construção** | Skill `construir`, em fatias verticais, construindo o que o `docs/funcional.md` descreve — sem inventar comportamento — inclusive os direitos do titular e os eventos de medição, e seguindo **o mapa do que todo site tem** mais a referência do tipo. `depurar` e `revisar` são ciclos dentro desta estação | escopo da v1 implementado; a lista "O que fecha" da referência-mãe e da do tipo com evidência; teste no caminho crítico; ciclo de revisão limpo; Access aplicado antes do deploy quando há área administrativa; **a versão inicial no ar** | Leis 2, 5, 6; skill `seguranca-san`; `construir/references/desenvolvimento-web.md` e `tipo-*.md` |
| 6 | **Prontidão** | Segurança em ciclos no local **e no domínio no ar**; conferência dos serviços; a **prontidão operacional** — e-mail que chega, alerta que acorda alguém, backup que restaura, desempenho medido, custo com teto, runbook, métrica respondendo "quantos ontem?"; procedimento de incidente e acessibilidade (skill `legal`) | ciclo de segurança limpo nos dois lugares; serviços conferidos; a lista de prontidão fechada com evidência | Leis 4, 7, 8; `seguranca-san`; `legal`; `references/prontidao-operacional.md` |
| 7 | **Lançamento** | Nesta ordem: obrigações legais conferidas e documentos publicados; varredura final (rodada dupla); entrega de manutenção | documentos publicados; veredito **completo** na varredura; lista de reenvio entregue ao dono | Lei 10; skill `legal`; `references/varredura-final.md` |

**As leis não são as estações.** A numeração das leis é catálogo de obrigações e serve de citação estável; a ordem de construção é a da tabela. A Lei 9 (git desde o commit zero) é das primeiras coisas a acontecer; a Lei 2 (modularização) nunca termina.

## Fecha antes de avançar

Esta é a regra que sustenta tudo o mais, e ela vale igual para estação e para lei.

**Fechado é reverificado com evidência, nunca declarado.** Uma estação ou uma lei fecha quando a segunda passada confirmou o estado corrigido — commit, URL que responde, execução de CI verde, migration aplicada. "Deve estar certo agora" não é verificação.

**Nada abre com o anterior aberto.** Antes da primeira ação de qualquer estação, a sessão escreve três linhas: qual estação abre; o que fechou a anterior, com a evidência e onde se confere; o que esta vai olhar. Trabalho parecido com a estação seguinte não é a estação seguinte — mexer em segurança durante a Construção é Construção; a estação só muda com o fechamento declarado. Para o que verifica o que está no ar (estação 6 e varredura final), abrir exige antes as **três condições de "Antes de começar"** de `references/varredura-final.md` — commit servido, migrations, nada só no disco; faltando uma, não abre (lição nº 14).

**Bloqueio trava a esteira inteira.** Item que depende de ação do dono — push, migration, deploy, arquivo que a ferramenta recusa —, modelo indisponível, ou aditivo recusado mantém a estação **aberta** e para tudo. Não existe "sigo na próxima enquanto isso", nem "essa não depende daquela", nem trabalhar em paralelo para aproveitar o tempo. **Pedir na hora, nunca acumular**: aparecendo algo que só o dono resolve, interromper e pedir imediatamente, com a ação exata e o conteúdo pronto. O risco real não é a esteira parar — é a pendência ser esquecida três leis atrás.

**A única exceção é a auditoria de projeto que já existe:** pendência levantada ali é registrada e não trava — o objetivo é mapear, não reconstruir. A partir da estação em que o projeto retoma a construção, a regra volta integralmente.

**Fechado fica fechado.** Ao seguir, não reler nem refazer o anterior — voltar por conta própria desfaz decisão já tomada, inclusive exceção discutida e aprovada. Reabre-se por uma causa só: algo posterior mexeu no que o anterior definiu (a Lei 7 grava limites no `CONSTRAINTS.md`, que a Lei 1 definiu — mexeu ali, a Lei 1 reabre). Reabrir é explícito — qual reabriu, o que causou, o que mudou — e revisa só o ponto afetado.

**Como saber o que está aberto:** a seção de pendências do `CLAUDE.md` lista o que bloqueia; `docs/pendencias.md` lista o resto. Fechar é remover dali; reabrir é devolver com o motivo.

## A estação 5 fecha no ar, e a 6 começa nele

Código que roda na máquina de quem escreveu não é software entregue. A Construção fecha no **primeiro deploy real**: ambiente real, variáveis completas, migrations aplicadas, CI verde no commit que subiu, fluxo principal exercitado **lá**. Endereço temporário serve; máquina de desenvolvimento exposta, não.

**Deploy é produção de verdade, não ensaio** — apontando para o ambiente real dos provedores, inclusive pagamento. Subir em sandbox para trocar depois é testar uma coisa e lançar outra: identificador, formato de webhook, assinatura e erro mudam entre ambientes.

**A única coisa que a estação 5 não libera é a divulgação.** Subir não é lançar; antes da estação 7 não há anúncio, link enviado nem cadastro aberto a terceiros. Sem convite não há dado de pessoa entrando, e é isso que mantém o projeto fora de problema legal enquanto os documentos não existem. Qualquer exceção é decisão do dono, não da sessão. Uma consequência a declarar uma vez: domínio novo com HTTPS aparece em log público de certificado em minutos — motivo para a 6 começar imediatamente, não para adiar o deploy.

**A estação 6 roda em dois lugares:** no local e no domínio real, pelo navegador integrado. O que só o ar mostra: cabeçalho que o servidor real aplica, certificado, redirecionamento, cookie com as flags de verdade, resposta do provedor de pagamento real. E confere o estado dos serviços que sustentam o projeto — a pergunta é sempre *o que está no ar é o que eu acho que está?* — pela lista da Passada 4 de `references/varredura-final.md`. **Conector do serviço vem antes do navegador** (resposta estruturada vira evidência; o que cada conector alcança está em `references/automacao-plataformas.md`); serviço sem login segue a regra da Passada 4 — *não verificável daqui*, nunca conforme. **Painel de serviço é leitura, conector inclusive** — mudar DNS, deploy, variável ou permissão cai na lista curta.

**A prontidão operacional é a segunda metade da estação 6**, e é o que separa um sistema no ar de um sistema que alguém consegue operar. Os sete itens da tabela acima, cada um com comando, limiar e a evidência que o fecha, estão em **`references/prontidao-operacional.md`**; a lista fecha a estação junto com o ciclo de segurança. O procedimento de incidente e a acessibilidade são conferidos nesta estação também (skill `legal`, estação 6).

## Trocar de superfície de trabalho

O mesmo projeto é tocado do editor, da sessão na nuvem e do painel. Duas cópias editadas em paralelo divergem, e a que perde é a que tinha trabalho não commitado.

- **O repositório é a verdade.** Toda pasta — disco, pen drive, ambiente de nuvem — é cópia de trabalho.
- **Sincronizar ao abrir, publicar ao fechar.** Trabalho não commitado é trabalho que não existe (lição nº 31). Comando destrutivo montado para outra pessoa rodar traz o `git status` e o commit junto, porque quem escreve não sabe o que está pendente na máquina de quem roda.
- **Trocar de superfície só em fronteira de estação** — é onde o estado já está escrito no `CLAUDE.md`. No meio de uma estação, metade do contexto ainda está na conversa.

## Deploy automático: o agente publica

Com deploy automático, **push na branch principal é publicação** em todo serviço que o projeto usa. A porta é o **CI verde — não uma pessoa**: aprovação humana do deploy a cada publicação é atrito que não compra segurança (a revisão de merge da Lei 9, havendo mais de uma pessoa, é outra coisa: revisa código, não libera deploy), porque quem aprova dez merges por dia aprova o décimo sem olhar; verificação que roda sozinha não cansa.

O que isso exige:

- **Publicar só com a verificação verde.** É a porta inteira.
- **O caminho de dinheiro coberto por teste que roda nesse CI.** É a condição que substitui a aprovação manual — cobrança, estorno, webhook e conciliação sem teste automático significam deploy automático deles sem nada olhando. O motivo, uma vez: erro de código volta com redeploy; erro de dinheiro não — quarenta pessoas cobradas duas vezes continuam cobradas depois de consertar o código.
- **Saber reverter antes de precisar** — como, e em quanto tempo, respondido antes do primeiro deploy automático e escrito no `RUNBOOK.md`.
- **Variável de ambiente não sobe junto, e a ordem tem duas metades:** a nova existe **antes** do código que a usa; a antiga só sai **depois** que o código que a usava saiu do ar (lição nº 27).

O que o agente faz sozinho em GitHub, Supabase, Cloudflare e Northflank — comando, conector ou API, e o que precisa existir antes — e a lista do que o dono configura **uma vez** para nunca mais ser chamado está em **`references/automacao-plataformas.md`**. Tarefa entregue ao dono sem ter passado por essa lista é tarefa mal entregue.

## Modelo e esforço por estação

| Estação | Modelo | Esforço | Ter em mãos antes |
|---|---|---|---|
| 1 Escopo | Opus | alto | a ideia, e disposição para responder pergunta por pergunta |
| 2 Fronteiras | Sonnet; Opus se houver dúvida real entre estrutura e projeto | médio | o spec fechado |
| 3 Fundação | Sonnet | médio | acesso ao repositório e às contas |
| 4 Contratos | Opus | alto | o spec, e o `API.md` do Checkout se o projeto cobra |
| 5 Construção | Sonnet; Opus nas partes difíceis | médio a alto | contratos fechados, ambiente rodando, acesso à hospedagem |
| 6 Prontidão | Opus | alto | o sistema rodando local, e acesso ao que está no ar |
| 7 Lançamento | Sonnet nos documentos; **Fable na varredura final** | médio; alto na varredura | inventário preenchido, razão social e CNPJ, documentos publicados antes de a varredura começar |

**A troca é manual, e por isso é obrigação avisar.** Ao fechar uma estação, dizer qual modelo e esforço a próxima exige, e parar se o atual não for esse. **A tabela é o padrão; a sessão julga o caso concreto** — avalia a tarefa que está de fato na frente dela e recomenda, com motivo, em duas ou três linhas; a decisão é do dono. Sinais para modelo mais forte: muitos arquivos que precisam ficar coerentes ao mesmo tempo; erro caro ou difícil de detectar; decisão irreversível; **duas tentativas erradas na mesma tarefa** (o sinal mais confiável). Sinais para mais leve: tarefa mecânica verificável na hora; escopo pequeno; limite semanal apertado numa tarefa não crítica. Julgar a tarefa, não a própria capacidade — alegar incapacidade sem evidência é palpite; recomendar sempre o mais caro anula a tabela.

**Fable é reservado** para dois usos, e fora deles não é recomendado: a varredura final e a aceleração de um trecho já decidido. O motivo é orçamentário — no plano Max ele pode consumir metade do limite semanal, e ela precisa existir na hora da varredura. O protocolo da aceleração está em `references/aceleracao.md`. **Fable indisponível** na varredura — por limite, ou por sinalização das salvaguardas, que é esperada em estação que fala de hash, chave e webhook — substitui-se por Opus alto e registra-se a substituição; a passada vale. **Proibido reescrever o pedido para escapar da sinalização** — é contornar guardrail, e guardrail não se contorna.

## Varredura final

Antes de declarar concluído, rodar **`references/varredura-final.md`** com Fable, duas vezes: local e no que está no ar. Ler o arquivo antes de começar, não durante. O veredito tem duas formas — **completo** ou **falta** — e "completo com ressalvas" não existe.

## O que chega ao dono é decisão, não problema

Parar e avisar não é empurrar o problema. O que chega ao dono tem as quatro: **a causa, não o sintoma**; **duas ou três saídas com trade-off e uma recomendada**; **o que já foi verificado e o que não foi**; **o que acontece se nada for feito**.

**Simples não é superficial.** A solução mais simples que *funciona* é a menor que resolve a causa; a que faz o sintoma sumir sem tocar na causa volta com outro nome. Sinais de remendo: condição especial para o caso relatado; conserto do dado depois de gravado errado; funciona porque o caminho defeituoso deixou de ser percorrido; não explica por que aconteceu. Encontrando um, dizer na hora, com a alternativa que trata a causa e o que custa a mais. Remendo aceito vira exceção no `CONSTRAINTS.md`.

**Pergunta sem trabalho feito é trabalho transferido.** Perguntar cedo é obrigação quando a informação só o dono tem — o que quer, o que decidiu, quanto aceita gastar, qual risco topa. Nunca para o que a sessão descobriria lendo, medindo, testando ou consultando a documentação.

## Como relatar ao dono

Relatório é **curto, direto e separado por mudança**: uma linha cada, no formato `<o que estava errado> → <o que foi feito>`. Sem explicação — se o dono pedir, vem a necessária sobre o conjunto, não o passo a passo. No fim, sempre, **o que só o dono faz**, com URL ou caminho exato (os cinco campos de `references/aceleracao.md`), ou "nada". **Ferramenta que recusou por falta de permissão entra ali com o caminho para liberar**, nunca como "sem acesso" (`references/automacao-plataformas.md`, "Faltando permissão"). Vale para fechar tarefa, estação e corrida; a varredura final mantém o veredito por item, porque ali a evidência é o produto. Token gasto em explicação não pedida é token que falta na varredura.

## Ao encontrar o projeto fora da lei

Achar violação não termina em relatório. Termina em projeto corrigido e reverificado.

**1. Aditivo, aplicado na hora sem perguntar.** Criar o que falta (`CONSTRAINTS.md`, `docs/erros/`, `.env.example`, linha no inventário, seção no README) e **corrigir documento que deixou de ser verdade** — a direção é sempre alinhar o texto ao que o sistema faz; mudar o sistema para caber no texto é mudança de funcionalidade, caminho estrutural. Documento falso é pior que ausente: ausência faz perguntar, texto errado faz agir errado com confiança. E a regra dura que vale para todo documento: **nunca escrever que algo existe antes de existir** — o que não existe entra como pendência, com o nome de pendência (lição nº 2).

**1b. Aditivo que a ferramenta recusa** — `.github/workflows/` é o caso comum, protegido porque workflow roda com a credencial do repositório. Nunca contornar; entregar o conteúdo pronto com o caminho exato; registrar como pendência; o ciclo pausa até o dono aplicar.

**2. Estrutural** — mover, renomear, apagar, mudar import, deploy, build, e qualquer mudança que altere comportamento, contrato ou dado existente. **É liberado sem autorização caso a caso quando a sessão demonstra que não quebrou nada**, e as três condições valem juntas: verificação que roda e passa (teste, build, fluxo exercitado — não leitura); ciclo completo da skill `revisar` sobre a mudança e o que ela arrasta; reversível em um commit próprio. Cumpridas, aplicar e relatar depois — o que mudou, o que foi verificado, como reverter. "Não quebra" é evidência, não opinião: quebrar inclui tela que renderiza mas parou de salvar, webhook que parou de chegar, página que dá 404 só no ar.

**3. Lista curta que pede permissão sempre**, por mais limpa que esteja a verificação: caminho de dinheiro (cobrança, estorno, webhook, split, conciliação); autenticação, sessão, chave, segredo, permissão; migration destrutiva ou reescrita de dado existente; contrato que outro projeto consome; remoção de funcionalidade em uso; mudança verificável só em produção. Nesses, listar o que seria mudado e o que pode quebrar junto, e esperar. Nela o erro não aparece como tela quebrada — aparece como dinheiro no lugar errado, dado apagado ou porta aberta.

**4. Escrever a regra dentro do projeto**, na casa que já existe — nunca em arquivo novo: regra, veto, limite, exceção → `CONSTRAINTS.md`; como rodar → `README.md`; por que → spec ou ADR em `docs/`; o erro → `docs/erros/`; o índice → `CLAUDE.md`.

**5. Rodar a lei de novo sobre o estado corrigido**, uma vez, relendo o que mudou.

**6. Conforme é cumprir ou não cumprir com exceção registrada e justificada no `CONSTRAINTS.md`.** Exceção escrita é conformidade; exceção esquecida não é. Parte das violações é decisão deliberada do dono, e forçar 100% cego destrói decisão boa.

**7. Não conformando depois da segunda passada, o ciclo pausa** — dizer o que falta e por quê, esperar a ordem, executar, verificar, seguir até fechar. **Não existe estado final "não conforme"**: todo ciclo termina corrigido ou com exceção registrada. Nenhum projeto da San & Co. opera fora de conformidade — a saída rápida, quando existe, é registrar a exceção, não ignorar a violação.

## Fecho da esteira: a entrega de manutenção

**Só a sessão de manutenção do plugin edita as skills.** Sessão de projeto contribui com uma coisa: lição de erro no `docs/erros/` dele, marcada como de ecossistema quando atravessa projeto (skill `depurar`). Não edita skill, não escreve dentro do plugin, não abre proposta de lição, não promete promoção. A régua que mede todos os projetos, editada em paralelo, para de medir.

A estação 7 fecha na entrega: terminada a varredura, a sessão declara o projeto concluído e diz que estes arquivos precisam ser **reenviados na conversa de manutenção do plugin**:

| Reenviar | Por quê |
|---|---|
| `docs/erros/` inteira | as lições; as de ecossistema viram catálogo compartilhado |
| `CONSTRAINTS.md` | limites que outros projetos vão esbarrar |
| `CLAUDE.md` | as pendências que nunca fecharam mostram onde a esteira não coube |
| contrato alterado (`API.md` e equivalentes) | contrato de estrutura que mudou desatualiza quem consome |
| spec da estação 1 | só se o escopo revelou pergunta que as fases não fazem |

Junto, **três linhas escritas na hora**: qual lei foi violada mais de uma vez, qual estação fechou com exceção, qual regra faltou. A promoção acontece na manutenção, por decisão do dono; até lá a lição vive só no projeto, e isso é aceito, não pendência.

## Depois do lançamento: a esteira roda de novo

A estação 7 fecha uma versão, não o produto.

**Guardar — `docs/proximas-versoes.md`.** Toda vez que alguém disser "fica para depois", a ideia entra ali na mesma sessão, em cinco linhas e nenhuma é o "como": **o que**; **por que** (a linha que apodrece primeiro — meses depois ninguém lembra do problema, só da solução); **de onde veio**, com data; **o que toca**; **quando vale a pena** — a condição que torna urgente, sem a qual o arquivo vira lista de desejos. Ideia, nunca decisão: entrada ali não autoriza construir nada.

**Entre versões — estado de coleta.** É estado, não estação: sem gate, dura o que o dono quiser. A sessão recebe, **compila em vez de empilhar** (ideia que toca o mesmo problema entra na entrada existente), e mantém o projeto vivo. Não constrói, não desenha solução, não abre a estação 1, não repete "vamos começar?". **Bug, falha de segurança, documento que virou mentira e obrigação legal não são ideias** — vão para a correção na hora. Quem abre versão nova é o dono; a sessão pode avisar uma vez, em uma linha, quando a condição de alguma entrada virou verdade.

**Reabrir — proporcional ao delta.** Estação 1 sempre (lê o banco inteiro agrupando por parte do sistema — três ideias no mesmo módulo são uma versão — e produz spec novo); 2 se cria capacidade nova ou mexe no banco; 3 como auditoria rápida; 4 se muda contrato, dado ou migration; 5 sempre, fechando com deploy; 6 sempre — atualização é onde regressão nasce; 7 se muda o que os documentos legais dizem. "É só um campo" é a frase que antecede a maioria das regressões. Item implementado sai do arquivo — o registro é o spec da versão.

## `CLAUDE.md`: a porta de entrada

Antes de qualquer tarefa, conferir se existe na raiz. **Não existindo, criar nesta sessão, dentro do repositório**, com conteúdo lido do projeto real — nunca de longe, nunca de modelo preenchido no chute. Existindo, conferir se continua verdadeiro; ponteiro quebrado é corrigido na hora.

**Cabe numa tela** — passando de umas quarenta linhas, virou conteúdo, e conteúdo ali é a pior duplicação possível, porque é lido inteiro em toda conversa. É índice: **nada que já esteja em outro documento é repetido nele**, com uma exceção autorizada — as pendências que bloqueiam a esteira, em uma linha cada, porque quem abre precisa tropeçar nelas primeiro.

```markdown
# <nome do projeto>

Projeto da San & Co. Segue as leis do plugin `san-co`.

## Antes de propor ou escrever qualquer coisa, leia
- `CONSTRAINTS.md` — o que este projeto NÃO faz, e os limites assumidos
- `docs/specs/<arquivo>` — por que existe, e o veredito dos contrapontos
- `docs/funcional.md` — o que o sistema faz, tela por tela
- `docs/erros/` — o que já deu errado aqui; não repita
- `docs/pendencias.md` — o trabalho que falta, e o que só o dono faz
- `RUNBOOK.md` — como operar, reverter e restaurar
- `README.md` — como rodar e testar

## Classificação
Porte: <…> · Dado: <…> · Vida útil: <…> → rigor <nível>

## Estado na esteira
Estação atual: <n — nome>, aberta em <data>.
Fechadas:
- 1 Escopo — <o que fechou> · evidência: <commit, arquivo, URL>
- <uma linha por estação fechada, sempre com onde se confere>
Falta para fechar a atual: <lista curta, ou "nada">
Próxima estação: <n — nome>, pede <modelo> com esforço <nível>

## Mapa de caminhos
- Entrada da aplicação: <…> · rotas: <…> · regras e integrações: <…>
- Dados e migrations: <…> · variáveis: `.env.example`
- Componentes e tokens visuais: <…>
- Integração com o Checkout (ou outra estrutura): <…>
- Testes: <…>

## Conformidade
Violação segue o ciclo da skill `leis`. Não existe estado final fora de
conformidade: ou corrige, ou vira exceção registrada no `CONSTRAINTS.md`.

## Pendências que bloqueiam a esteira
- <lista, ou "nenhuma">
```

**"Estado na esteira"** responde, sem reconstruir a história, em que estação o projeto está, o que fechou cada anterior e onde se confere, e o que falta — atualizado no fechamento de cada estação e em nenhuma outra hora. **"Mapa de caminhos"** troca uma varredura da pasta por uma linha lida: ler o mapa antes de procurar, corrigir o mapa quando ele falhar, caminhos sempre relativos à raiz (absoluto de ontem é ponteiro morto amanhã), e apontar onde as coisas moram — não o que fazem, porque comportamento envelhece a cada commit.

## A pasta-mãe: todos os projetos lado a lado

Um por subpasta. O ganho é que **contrato de estrutura passa a ser verificável** — abrir o `API.md` do Checkout e ver quem consome na mesma sessão. Três condições: **não é monorepo** (cada projeto com o próprio `.git`, `CLAUDE.md`, `CONSTRAINTS.md`, testes; nenhum `git init` na mãe, nenhum import atravessando projeto — vizinhos, não partes); **a sessão declara em qual projeto está antes de encostar em arquivo**, ler outro é o motivo da pasta, escrever em outro exige ordem; **a pasta-mãe é cópia de trabalho** — a casa é o repositório remoto.

Na raiz vive **`SAN-CO.md`**: uma linha por projeto — nome, pasta, o que é, estrutura ou projeto, onde roda, estação. Índice que aponta para cada `CLAUDE.md` e não repete nada; atualizado pela sessão que fecha uma estação, no momento do fechamento.

---

## Lei 0 — Proporcionalidade

O rigor escala com a classificação (porte, sensibilidade, vida útil). Experimento pessoal sem dado sensível não precisa de CI com cobertura — mas cumpre a Lei 3 e tem escopo negativo escrito. **Nenhum projeto pula segurança de credenciais.**

Projeto no **topo da escala** — multi-inquilino, dado de terceiro, dinheiro, vida longa — tem obrigações verificáveis, não intenções: teste e verificações automáticas de segurança rodando sozinhos a cada push (roteiro manual é complemento, nunca substituto); revisão em ciclos antes de subir; escopo negativo dentro do repositório. Nenhuma delas se dispensa por proporcionalidade; cada dispensa usada no pé da escala fica escrita no `CONSTRAINTS.md`.

## Lei 1 — Estrutura de pastas

```
projeto/
├── .github/workflows/   # CI e verificações de segurança (Lei 0)
├── docs/
│   ├── specs/                  # escopo validado (Lei 10)
│   ├── erros/                  # um arquivo por erro vivido (Lei 10)
│   ├── funcional.md            # o que o sistema faz (Lei 10)
│   ├── inventario-de-dados.md  # que dado, de quem, para quê (Lei 10)
│   ├── pendencias.md           # o que falta, e o que só o dono faz (Lei 10)
│   ├── proximas-versoes.md     # ideias para a próxima volta (Lei 10)
│   └── ...                     # ADRs
├── src/
│   ├── ui/          # componentes — nascem aqui, uma vez
│   ├── tokens/      # cor, tipografia, espaçamento
│   └── constantes/  # texto repetido e constante de negócio
├── infra/           # IaC, configs de deploy
├── scripts/         # automação, não lógica de negócio
├── tests/           # executáveis por um comando só
├── .env.example
├── CLAUDE.md        # porta de entrada
├── CONSTRAINTS.md   # o que não se faz, e os limites
├── RUNBOOK.md       # como operar, reverter, restaurar (Lei 10)
└── README.md
```

`apps/` e `packages/` só em monorepo com mais de um app — nunca por antecipação. Regra dura: nenhuma lógica de negócio em `scripts/` ou `infra/`; nenhum segredo commitado em pasta nenhuma, nem em branch descartável. O que cada documento da raiz guarda e como se distinguem é da Lei 10.

## Lei 2 — Modularização

Cada módulo tem uma responsabilidade descritível em uma frase. Domínio não importa de infraestrutura — a dependência vai de fora para dentro. Nada de abstração para "caso um dia precise". Reuso vem depois de duplicação intencional **para lógica que pode divergir**; o que precisa continuar idêntico — componente, token, texto, constante de negócio — nasce em um lugar só desde o primeiro uso (skill `construir`, "Elemento repetido").

## Lei 3 — Segredos e credenciais

Credenciais em variável de ambiente ou gerenciador de segredos — nunca hardcoded, nunca em `docs/`, nunca em print versionado. `.env` no `.gitignore`; `.env.example` documenta as chaves com valores fictícios. Segredo diferente por ambiente. Segredo que vazou, mesmo suspeita, é revogado. Segredo com caractere especial de shell é guardado codificado em base64 ou hex (lição nº 26).

Senha de usuário nunca em texto puro, nunca MD5/SHA1. Hash lento, nesta ordem (OWASP): **Argon2id**; **scrypt** quando Argon2id não estiver disponível; PBKDF2 só sob exigência de FIPS-140; bcrypt apenas em sistema legado. Parâmetros, custo de memória, teto de simultaneidade, assincronia, salt, comparação segura e a decisão entre biblioteca e primitiva crua estão em **`seguranca-san/references/senha-e-kdf.md`** — ler antes de escrever a primeira linha de autenticação.

## Lei 4 — Segurança mínima

Todo projeto com qualquer usuário além de você passa pela skill **`seguranca-san`**, que é a autoridade sobre segurança. Esta lei é só o gatilho.

## Lei 5 — Frontend

Responsivo por padrão. Acessibilidade não é opcional nem em projeto pequeno — e no Brasil é obrigação legal para site privado (skill `legal`): HTML semântico, navegação inteira por teclado, contraste, rótulo em todo campo, foco visível, texto alternativo, nada informado só por cor. Uma fonte de verdade por dado. Sem dependência pesada para o que HTML e CSS nativos resolvem. Elemento visual nasce em um lugar só (skill `construir`). O que cada site tem — `<head>`, tipografia, imagens, formulários, estados, páginas de erro, formato brasileiro — é a lista de `construir/references/desenvolvimento-web.md`.

## Lei 6 — Backend e dados

Toda API com contrato explícito antes de várias partes dependerem dela. Migrations versionadas, nunca editadas depois de aplicadas — corrige-se com migration nova; coluna acrescentada depois da primeira ida a produção exige alteração explícita no corpo executável (lição nº 22). Backup automático do que não pode ser perdido, **restaurado ao menos uma vez em teste** — nunca restaurado é backup hipotético. RLS ou equivalente com múltiplos perfis no mesmo banco. Aplicação e banco na mesma região (skill `classificar`).

**Nunca alterar schema por conexão direta com `DATABASE_URL`.** Mudança de schema passa pelo editor da plataforma e vira migration versionada. Exceções: DML da aplicação em runtime; CLI ou pipeline aplicando migration já versionada; backup e restauração; ferramenta somente-leitura; ambiente local; hotfix de emergência com migration retroativa obrigatória.

## Lei 7 — Escalabilidade consciente

Escrever o limite assumido no `CONSTRAINTS.md` ("atende até X"), com número medido quando houver. Só investir em fila, cache distribuído ou réplica com evidência real. Identificar o gargalo mais provável e escrever o que fazer quando for atingido. Operação cara em memória tem teto de simultaneidade no código, não só de taxa (lição nº 21).

## Lei 8 — Observabilidade e operação

Todo projeto que roda sem supervisão tem log de erro visível. Projeto com usuário externo tem: alerta **externo** de "caiu" que chega ao celular; captura de exceção com contexto da requisição; monitor de tarefa agendada que avisa quando ela **não rodou**; retenção de log finita; e alerta de orçamento em toda conta paga. O que instalar, o que alerta e o que não alerta, e como testar derrubando o serviço de propósito, está em `references/prontidao-operacional.md`.

## Lei 9 — Versionamento

Git desde o commit zero, mesmo em projeto pessoal. Commits atômicos explicando o porquê. Nada direto em produção sem passar pelo CI, e, havendo mais de uma pessoa, revisão antes do merge.

## Lei 10 — Documentação viva

Cada documento tem um dono e uma pergunta que responde. **"por onde começo?"** → `CLAUDE.md`. **"por que existe?"** → `docs/specs/AAAA-MM-DD-<projeto>.md`, o escopo validado das Fases 0 a 3.5, escrito uma vez. **"posso construir isso?"** → `CONSTRAINTS.md`: escopo negativo com o porquê de cada item, limites da Lei 7, exceções aceitas, dispensas usadas — diz *não construa*. **"o que fica para depois?"** → `docs/proximas-versoes.md` — diz *ainda não*, e é o oposto do anterior; item desejado mora só aqui. **"o que o sistema faz?"** → `docs/funcional.md`, o único documento de definição que muda durante o projeto, reescrito na mesma tarefa em que o comportamento muda. **"o que falta?"** → `docs/pendencias.md`, trabalho desta versão, com a seção "Só o dono faz". **"como rodo?"** → `README.md`: o que é, como rodar, variáveis (nomes, não valores), como testar com um comando. **"como opero?"** → `RUNBOOK.md`: como operar, reverter, restaurar e responder a incidente — o sumário exato e o teste pela segunda pessoa estão no item 6 de `references/prontidao-operacional.md`. **"isso já deu errado?"** → `docs/erros/`. **"de onde vem cada prova do site?"** → `docs/provas.md`, só em site que exibe depoimento ou número (`construir/references/tipo-institucional.md`). **"que dado de pessoa existe aqui?"** → `docs/inventario-de-dados.md`, atualizado na mesma tarefa que cria o dado — é dele que saem os documentos legais, e ele **é** o registro de operações que a LGPD exige (skill `legal`).

**Tudo isso vive no repositório, não numa conversa nem em ferramenta externa.** Quem clona — pessoa ou agente — não vê o que está fora, e é exatamente essa pessoa que precisa ser impedida de construir o que foi vetado (lição nº 5).
