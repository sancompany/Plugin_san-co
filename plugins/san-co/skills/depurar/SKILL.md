---
name: depurar
description: Encontra a causa raiz de um erro em vez de tratar o sintoma. Use quando algo quebrar, um teste falhar, o build parar, um deploy der errado, ou o comportamento não bater com o esperado.
---

# Depurar — causa raiz, não sintoma

Um relato descreve um **sintoma**. O trabalho é achar a causa. Nunca sair editando código na base do palpite, e nunca repetir o mesmo comando em loop esperando resultado diferente.

## Antes da investigação: isso é incidente?

É **incidente** quando está em produção e alguém está sendo prejudicado agora — pagamento cobrado sem entrega, dado sendo perdido ou corrompido, serviço fora do ar, ou informação de uma pessoa visível para outra. Nesse caso a investigação **não vem primeiro**.

Ordem no incidente:

1. **Conter.** Parar o sangramento — desativar o fluxo quebrado, voltar para a versão anterior, ou bloquear novas entradas. Estancar antes de entender é aceitável aqui; é o único caso em que é.
2. **Delimitar.** Quem foi afetado e desde quando. Listar concretamente: quais pagamentos, quais registros, quais pessoas. Sem essa lista não há como reparar depois.
3. **Reparar o que já aconteceu.** Reconciliar na mão o que ficou pendente — entregar o que foi pago, restaurar o que sumiu. Isso é separado de corrigir o código, e costuma ser mais urgente.
4. **Comunicar**, quando houver terceiro afetado.
5. **Só então** seguir a investigação abaixo.

Não sendo incidente, ir direto para a sequência.

## Sequência

**1. Reproduzir de forma confiável.** Sem reprodução, não há correção verificável — só coincidência. Anotar os passos exatos, a entrada exata e o ambiente (local, produção, navegador). Se não reproduz, o primeiro trabalho é descobrir o que difere entre onde funciona e onde falha.

**2. Ler o erro de verdade.** A mensagem completa, o stack trace inteiro, e a primeira linha que aponta para código seu — não a última. Em produção, olhar o log real do serviço antes de teorizar.

**3. Localizar por bisseção.** Cortar o espaço do problema pela metade a cada passo: a falha está no cliente ou no servidor? Antes ou depois da chamada externa? Com esse dado ou com qualquer dado? Cada teste elimina metade das hipóteses.

**4. Checar todos os chamadores antes de editar.** Antes de mexer numa função, procurar quem mais a chama. Se três lugares dependem dela, corrigir só o caminho do relato deixa os outros dois quebrados.

**5. Corrigir na raiz.** Uma guarda na função compartilhada, não uma guarda em cada chamador. Se a correção precisa ser repetida em vários lugares, provavelmente está no lugar errado.

**6. Deixar uma guarda.** Um teste pequeno ou um `assert` que falha se o bug voltar. Bug corrigido sem guarda volta.

## Armadilhas comuns no contexto San & Co.

- **Serviço que estava dormindo**: hospedagem que suspende por inatividade faz a primeira requisição demorar e estourar timeout. O Northflank não dorme, mas serviço legado em outra plataforma pode — antes de caçar bug na aplicação, confirmar onde ele roda e se estava de pé.
- **Região errada**: lentidão sem ponto lento, intermitente e difícil de reproduzir, costuma ser distância entre aplicação e banco, não código. Medir a viagem antes de otimizar consulta.
- **Integração entre projeto e estrutura**: quando o Checkout não enxerga um pedido, checar na ordem — a chave de autenticação do projeto, o endereço cadastrado da API, e só então a lógica.
- **Webhook que "não chega"**: verificar se o provedor realmente disparou antes de investigar o receptor. Log do lado de quem envia primeiro.
- **Variável de ambiente**: erro que só aparece em produção e não local é variável de ambiente faltando ou diferente, até prova em contrário.
- **Configuração declarada não é configuração aplicada**: o arquivo diz a intenção, a resposta diz o efeito. Código local funcionando e publicado não, comparar **os cabeçalhos da resposta**, não o conteúdo dos arquivos — e verificar sempre pelo caminho público, nunca lendo a configuração (lição nº 17).
- **O ambiente do teste faz parte do teste**: endereço de origem, cookie já presente e relógio do lugar de onde se testa são variáveis do experimento, não constantes. Antes de declarar quebrado o que está do outro lado, conferir o que este lado está de fato mandando (lição nº 32).

## Dois catálogos, audiências diferentes

**`references/licoes-aprendidas.md` (neste plugin)** — erros já cometidos em qualquer projeto da San & Co., com a regra que cada um gerou. Ler antes de investigar erro novo.

**`docs/erros/` (no repositório do projeto)** — o que só faz sentido dentro daquele código. O teste para a marca de ecossistema e o caminho até o catálogo estão na seção abaixo; **só a sessão de manutenção do plugin edita skills** — a governança inteira está na skill `leis`, "Fecho da esteira".

## Registrar em `docs/erros/`

Todo erro que custou tempo vira um arquivo em `docs/erros/AAAA-MM-DD-<resumo>.md` no projeto, commitado junto com a correção. Erro corrigido e não registrado volta — em outro arquivo, em outro projeto, meses depois, sem ninguém lembrar que já tinha acontecido.

Cada registro tem cinco linhas, não mais:

- **Sintoma** — o que apareceu para quem usou.
- **Causa raiz** — o que realmente estava errado, não onde apareceu.
- **Correção** — o que foi mudado.
- **Guarda** — o teste ou verificação que impede a volta.
- **Como evitar na origem** — a regra que teria evitado isso ser escrito. Esta é a linha mais valiosa das cinco.

Uma sexta linha entra **só quando o erro atravessa projeto** — o teste é *outro projeto, com outra stack, cometeria o mesmo erro?*: `**Ecossistema:** sim — <por quê>`. É a marca que leva a entrada à manutenção do plugin no fecho do projeto; a sessão do projeto não decide em qual skill a regra vai morar. Sem a marca, a lição fica aqui, e tudo bem.

Registrar também erro que não foi de código: decisão de arquitetura que deu errado, duplicação que dessincronizou, dependência que quebrou, configuração que faltou em produção.

Quando um erro se repetir apesar de estar registrado, o problema não é o erro — é que a regra da linha "como evitar na origem" não está sendo aplicada. Nesse caso, promover a regra **dentro do projeto** — `CONSTRAINTS.md` se virou limite ou veto, `CLAUDE.md` se é instrução de entrada — e marcar a entrada como de ecossistema.

## Quando parar e perguntar

Depois de duas ou três tentativas sem avanço, ou quando a investigação começar a abrir frentes não relacionadas: parar, explicar o que foi tentado, o que foi descartado e com que evidência, e perguntar como seguir. Insistir no mesmo caminho que já falhou duas vezes gasta tempo e contexto sem gerar informação nova.
