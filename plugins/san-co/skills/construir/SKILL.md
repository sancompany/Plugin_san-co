---
name: construir
description: Implementa mudanças em fatias pequenas e verificáveis, sempre pela solução mais simples que funciona, e carrega o mapa do que todo site ou app precisa ter — por tipo (institucional, SaaS, e-commerce, PWA). Use ao escrever código, adicionar funcionalidade, refatorar, escolher entre bibliotecas e abordagens, ou ao abrir a construção de um site ou app.
---

# Construir — San & Co.

## Antes de escrever qualquer linha

Informar sempre ao usuário o **caminho completo do arquivo** na árvore de pastas a partir da raiz do projeto, e **quais arquivos ele precisa reenviar** para releitura antes de qualquer alteração. Nunca alterar um arquivo com base em conteúdo possivelmente truncado de uma saída anterior — reler primeiro.

Fechar a funcionalidade em discussão antes de escrever ou atualizar código. Código antes da decisão fechada é retrabalho garantido.

Se a mudança toca algo que **outros projetos consomem** (Checkout, contrato de integração, qualquer peça de estrutura), usar a skill `classificar` antes de editar — lá estão as regras de compatibilidade. Mudança silenciosa em estrutura quebra projeto em produção sem aviso.

**Consultar os dois catálogos de erro antes de começar.** O da skill `depurar` (`references/licoes-aprendidas.md`) traz o que já deu errado em qualquer projeto da San & Co. e a regra que cada caso gerou — projeto novo herda isso sem repetir o erro. O `docs/erros/` do projeto, quando existir, traz o que é específico deste código. Repetir erro já registrado é a falha mais evitável que existe, e a mais comum, porque ninguém lembra do que quebrou há três meses.

## Consultar a documentação antes, não depois

Memória de API é hipótese, não fonte. Biblioteca muda assinatura, plataforma muda teto, norma de segurança muda parâmetro recomendado — e nada disso avisa: o código roda, o teste passa, e só uma auditoria descobre que estava errado. Duas das lições do catálogo (nº 10 e nº 13) são exatamente isso — parâmetro padrão defasado e limite de plataforma barrando o valor seguro — e as duas seriam evitadas por uma leitura de documentação antes de escrever.

**Consultar a fonte oficial, online, quando:**

- é o primeiro uso desta biblioteca, API ou recurso de plataforma **neste projeto**;
- há parâmetro de segurança, de custo ou de capacidade envolvido (KDF, cifra, timeout, limite de memória, tamanho de pool, cota);
- a decisão é entre duas bibliotecas ou duas abordagens — comparar contra o que cada uma documenta hoje, não contra a lembrança de como era;
- a mensagem de erro cita depreciação, ou o comportamento observado não bate com o esperado;
- o terceiro define um **conjunto fechado** que o projeto vai enumerar (status, ciclo, moeda, tipo de documento) — ler a definição inteira, nunca a lista de valores que apareceram até agora, e recusar valor fora dela nomeando os aceitos (lição nº 19);
- o **runtime é fixado à mão** em algum lugar (CI, imagem, plataforma) — a exigência de versão também é declarada no manifesto do projeto, senão o único lugar que aponta a versão certa é o que quebrou (lição nº 33);
- o serviço é de terceiro e o contrato é dele (Asaas, Supabase, Northflank, Cloudflare, provedor de e-mail, GitHub Actions).

**O que ler:** a documentação oficial da **versão que está instalada** — conferir a versão no `package.json` e no lockfile antes, porque doc da versão errada é pior que nenhuma. Junto dela, o changelog ou as notas de migração entre a versão documentada e a instalada. Blog, vídeo e resposta de fórum servem para entender um conceito, nunca para decidir um parâmetro.

**A consulta serve para encurtar o código, não só para confirmá-lo.** Recurso nativo que resolve sozinho o que se ia escrever à mão é o degrau 4 da escada abaixo, e normalmente só a documentação revela que ele existe. Ler a página inteira da função que está sendo usada, não só o exemplo — é lá que aparecem a opção que elimina vinte linhas e a armadilha que custa uma madrugada.

**O que fazer com o que foi lido:** quando a decisão depende da documentação, registrar no código ou no spec **o que foi lido, de qual versão e quando** — uma linha basta. Sem isso, quem passa por ali depois não sabe se o valor foi pensado ou chutado, e recomeça a pesquisa do zero.

**Proporcionalidade (Lei 0).** Não é pesquisa por linha escrita: uso trivial de algo que o projeto já usa não precisa de consulta, e o gatilho é a lista acima. Documentação fora do ar ou inacessível também não trava a esteira — seguir com o que se sabe, marcar no código com `nao-conferido:` — marcador próprio, porque `limite:` é reservado para simplificação deliberada com teto e caminho de upgrade — dizendo o valor, contra qual versão ele deveria ser conferido, e a data. Conferir depois, e apagar a marca.

## O mapa do que todo site tem

Princípio não substitui lista. O que um site ou app precisa ter para ser produto — e não protótipo — está em **`references/desenvolvimento-web.md`**: catorze itens (lista de telas e URL, design system de uma pessoa, tipografia, `<head>`, SEO técnico, as páginas que ninguém desenha, formato brasileiro, imagens, formulários, estados, e-mail, segurança de construção, performance e ambiente de build), cada um com o que existe, como conferir e o que é exagero. Sobre ela, **uma referência por tipo**, escolhida pela classificação da estação 1: `references/tipo-institucional.md` (página pública que apresenta e converte), `references/tipo-saas.md` (conta, painel, assinatura), `references/tipo-ecommerce.md` (loja, catálogo, ingresso), `references/tipo-pwa.md` (app instalável, offline, celular). Projeto de dois tipos lê as duas.

**Ler a mãe e a do tipo ao abrir a estação 5, antes do primeiro componente** — é onde se decide o que nasce em um lugar só, o orçamento de performance e a CSP, coisas que custam dez vezes mais depois. A seção "O que fecha" de cada uma é a lista que fecha a estação 5 junto com o deploy; a Passada 2 da varredura final reconfere no ar.

## Referência de mercado antes de desenhar comportamento

Antes de construir um fluxo que já existe no mundo — login, recuperação de acesso, carrinho, pagamento, filtro, upload, tabela com paginação —, **olhar como dois ou três produtos conhecidos resolvem**. Não para copiar tela: para não reinventar pior o que o usuário já sabe usar.

O ganho é duplo e concreto. Primeiro, o que é padrão o usuário espera sem pensar, e a ausência dele é sentida como defeito mesmo quando nada quebrou. Segundo, produto maduro já tropeçou nos casos de borda que ainda não te ocorreram — o que acontece com duplo clique no botão de pagar, o que aparece quando a lista está vazia pela primeira vez, o que o sistema faz quando o e-mail já existe.

O que se traz da referência é **o comportamento e a sequência**, nunca o código nem a arte. Divergir do padrão é permitido — divergência deliberada vira linha no `CONSTRAINTS.md` com o motivo. Divergir sem perceber é o que a Passada 1 da varredura final encontra no fim, quando refazer custa dez vezes mais. Os fluxos mais comuns já estão comparados nas referências por tipo — ler antes de pesquisar de novo.

## A escada da simplicidade

Parar no primeiro degrau que resolve:

1. **Isso precisa existir?** Necessidade especulativa = não construir, e dizer isso em uma linha.
2. **Já existe neste projeto?** Um helper, tipo ou padrão que já mora aqui → reusar. Reimplementar o que está dois arquivos ao lado é o erro mais comum.
3. **A biblioteca padrão resolve?** Usar. E o inverso vale igual: antes de **remover** uma dependência para reimplementar à mão, listar o que ela fazia além da função óbvia — em segurança isso costuma ser salt por item, formato de armazenamento e comparação em tempo constante, tudo embutido e tudo seu se sair.
4. **Um recurso nativo da plataforma cobre?** `<input type="date">` antes de biblioteca de calendário, CSS antes de JS, constraint no banco antes de código na aplicação.
5. **Uma dependência já instalada resolve?** Usar. Nunca adicionar dependência nova para o que meia dúzia de linhas faz.
6. **Dá em uma linha?** Uma linha.
7. **Só então**: o mínimo de código que funciona.

A escada encurta a solução, nunca a leitura. Entender o problema inteiro primeiro — todos os arquivos que a mudança toca, o fluxo real de ponta a ponta — e só depois escolher o degrau. Diff pequeno no lugar errado não é economia, é um segundo bug.

## Como entregar

- **Fatias verticais pequenas**, cada uma testável, nunca um "big bang" de código.
- **Nada de abstração não pedida**: interface com uma implementação, factory para um produto, config para valor que nunca muda — tudo isso sai.
- **Middleware com estado interno é instância, não valor reutilizável.** Cada montagem cria a sua; reaproveitar a mesma compartilha o contador entre rotas que deveriam ser independentes, e isso só aparece sob carga (lição nº 25).

## Elemento repetido: definir uma vez, desde o primeiro uso

A regra "duplicar antes de abstrair" vale para **lógica que pode divergir** — dois fluxos parecidos hoje que amanhã seguem caminhos diferentes. Ela **não vale** para o que precisa continuar idêntico em todo lugar:

- Componente de interface repetido (botão, campo, card, modal, cabeçalho, rodapé).
- Token visual (cor, fonte, espaçamento, raio de borda, sombra).
- Texto que aparece em mais de uma tela (rótulo, mensagem de erro, aviso legal).
- Constante de negócio (taxa, prazo, limite, formato de código).

Esses nascem em **um único lugar** e são importados — nunca copiados. Antes de escrever um botão, uma cor ou uma mensagem, procurar se já existe. Se não existe e vai aparecer em mais de um arquivo, criar já no lugar compartilhado (`src/ui/`, `src/tokens/`, `src/constantes/`), não no arquivo onde surgiu a necessidade.

O teste: **se esse valor mudar, em quantos arquivos eu preciso encostar?** Mais de um = está duplicado e vai dessincronizar. Um botão copiado em oito telas não é código a mais; é oito botões que vão ficar diferentes entre si na primeira alteração, e ninguém vai lembrar dos oito.

Encontrando duplicação desse tipo em código existente: avisar, dizer quantos arquivos estão afetados, e propor a extração como passo próprio — não misturar com a funcionalidade em andamento.
- **Deletar vence adicionar.** Óbvio vence esperto: esperto é o que alguém decifra às 3 da manhã.
- Ao corrigir bug, corrigir na **raiz** — uma guarda na função compartilhada é um diff menor que uma guarda em cada chamador, e não deixa os chamadores irmãos quebrados.
- Marcar simplificação deliberada que corta um canto real com um comentário `limite:` nomeando o teto e o caminho de upgrade — por exemplo `// limite: trava global, virar trava por conta se a vazão apertar`. Isso deixa a dívida visível no código em vez de virar surpresa depois.

## Verificação

Lógica não trivial (uma condição, um laço, um parser, caminho de dinheiro ou de segurança) deixa **uma** checagem executável: um autoteste com `assert` ou um teste pequeno. Sem framework, sem fixture, sem suíte por função. One-liner trivial não precisa de teste — YAGNI vale para teste também.

Nunca simplificar para fora: validação de entrada em fronteira de confiança, tratamento de erro que evita perda de dado, medida de segurança, acessibilidade básica, e qualquer coisa explicitamente pedida.

**O que a leitura do código não mostra, e por isso se confere com a tela renderizada:** depois de um reset agressivo de CSS, o estilo padrão de elementos nativos (`dialog`, `details`, controles de formulário) e o anel de foco somem sem deixar rastro no texto — o que falta não está escrito em lugar nenhum. `outline: none` só entra acompanhado do substituto, na mesma edição, e querendo tirar o anel só do clique o seletor é `:focus-visible` (lição nº 16). Conferir navegando **por teclado**, não lendo.

**Placeholder na marcação vira dado falso quando o carregamento falha.** Valor que começa como `0,00` ou `--` no HTML sobrevive ao erro e é exibido como se fosse real. Estado de erro apaga o placeholder; em tela de dinheiro, ausência nunca vira zero — ou o dado aparece, ou a tela deixa de oferecer a ação. E ao proteger um valor exibido, proteger **todos os irmãos na mesma passada** (lição nº 18).

## Fechamento

Commit e branch seguem a Lei 9 (skill `leis`).

Ao terminar, o relatório de "Como relatar ao dono" (skill `leis`): uma linha por mudança, `<errado> → <feito>`, mais o que ficou de fora e quando adicionar, e o que só o dono faz. Se a explicação ficar maior que o código, apagar a explicação.
