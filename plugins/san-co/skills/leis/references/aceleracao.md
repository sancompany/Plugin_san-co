# Modo aceleração — encadear estações e devolver só o trabalho humano

Modo de trabalho para quando existe prazo que não se move e um bloco longo disponível. A sessão atravessa as estações **uma atrás da outra, sem parar para conversar**, faz tudo que as ferramentas alcançam, e devolve no fim uma lista única do que só o dono pode fazer.

Não é um atalho pelas leis. É a esteira inteira, rodada sem intervalo.

## Quando ligar, e quando não

Ligar exige as quatro condições juntas — as mesmas que autorizam usar Fable para acelerar:

1. as decisões estão fechadas (escopo resolvido, contratos definidos, `docs/funcional.md` completo);
2. o trecho tem começo e fim claros;
3. existe verificação no fim (teste, ciclo de revisão, deploy que responde);
4. há um bloco longo e sem interrupção.

**Faltando a primeira, não acelerar.** Correr com escopo aberto produz muito trabalho rápido numa direção que depois é descartada — e gastou da bolsa do Fable para isso.

## O que muda e o que não muda

**Não muda nenhuma lei.** As estações continuam em ordem; cada uma fecha com evidência; a lista curta continua pedindo permissão; conformidade continua obrigatória.

**Muda uma regra de ritmo, de propósito:** fora do modo, pendência se pede na hora; aqui ela é acumulada na fila e entregue de uma vez, porque o único benefício do modo é o dono não precisar acompanhar. **E muda o silêncio.** Fora dos motivos de parada abaixo, a sessão não interrompe para confirmar, não pede opinião sobre escolha que ela pode fundamentar sozinha, e não relata progresso a cada passo. Ela encadeia e documenta.

## Antes de chamar de trabalho humano, tentar pelas ferramentas

A regra que faz o modo valer: **só é trabalho humano o que nenhuma ferramenta alcança.** Antes de mandar um item para a fila do dono, tentar, nesta ordem:

1. **conector do serviço** — deploy, banco, log, migration;
2. **navegador integrado**, com o dono já logado — painel que não tem conector: DNS, política de acesso, configuração de conta;
3. **shell e repositório** — commit, push, build, teste, script.

Só depois disso o item vira pendência. "Precisa de você" dito sem ter tentado é o modo aceleração se transformando em lista de tarefas para o dono, que é exatamente o oposto do que ele existe para fazer. O que cada ferramenta alcança em cada plataforma, com o comando exato, está em `automacao-plataformas.md` — conferir lá antes de escrever "só o dono".

## O que interrompe a corrida

Cinco motivos, e só eles:

1. **Item da lista curta** da skill `leis`.
2. **Decisão que depende de informação que só o dono tem** — preço, texto de marca, quem entra na lista de acesso, o que aceita gastar, qual risco topa.
3. **Ação que nenhuma ferramenta alcança** — aprovar segundo fator, colar arquivo em `.github/workflows/`, pagar plano, confirmar e-mail de domínio, ligar um serviço na conta. **Permissão faltando entra aqui com o caminho para liberar** (`automacao-plataformas.md`, "Faltando permissão"), não como impossibilidade.
4. **Duas tentativas erradas na mesma tarefa.** Evidência observável, não intuição: a terceira tentativa quase sempre repete a segunda.
5. **Verificação que falha e cuja correção cairia na lista curta.**

Nenhum outro motivo interrompe. Dúvida de gosto resolve-se pela referência de mercado e segue; escolha técnica reversível resolve-se pela escada da simplicidade e segue, com a decisão registrada.

## A fila do dono

Durante a corrida, cada item que parou vai para a seção **"Só o dono faz"** do `docs/pendencias.md` do projeto, com cinco campos:

- **o que fazer**, em uma frase de ação;
- **onde** — URL exata ou caminho completo do arquivo;
- **por que é necessário** — uma linha;
- **o que está bloqueado por isso** — qual estação ou qual verificação não fecha sem;
- **quanto leva**, estimado em minutos.

Ordenada pelo que desbloqueia mais, não pelo que apareceu primeiro. Entregue **de uma vez, no fim**, nunca pingada durante a corrida — pingar destrói o único benefício do modo, que é o dono não precisar acompanhar.

Item que o dono resolve durante a corrida, se ele estiver por perto, sai da fila e a estação correspondente é reaberta e fechada na hora.

## A regra de ouro

**O que não pôde ser feito nunca é escrito como feito** (lição nº 2). Estação que dependeu de item da fila fica **aberta** — não "concluída com pendência". O relatório final separa o que fechou do que está esperando.

## Como a corrida termina

Um relatório, uma mensagem, no formato de "Como relatar ao dono" (skill `leis`):

1. **Estações fechadas**, cada uma com a evidência (commit, URL que responde, execução de CI, migration aplicada).
2. **Estações abertas**, cada uma com exatamente o que falta.
3. **A fila do dono**, ordenada.
4. **O que muda quando cada item for feito** — para ele decidir a ordem sabendo o efeito.
5. **O que foi decidido sozinho e por quê** — as escolhas técnicas reversíveis tomadas durante a corrida, para ele revisar depois se quiser.

## Sobre o modelo

Corrida longa é o segundo uso reservado do Fable, e é para isso que ele existe aqui. Mas a **varredura final também é dele**, e é o uso insubstituível: apertando o limite semanal, a corrida cede a vez. Acelerar até a estação 6 e chegar sem Fable na varredura é ter corrido para parar na porta.

Sinalização das salvaguardas durante a corrida não interrompe nada: a resposta vem no modelo alternativo, registra-se a substituição e segue (skill `leis`).
