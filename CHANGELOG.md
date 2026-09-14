# Mudanças

O `version` do `plugins/san-co/.claude-plugin/plugin.json` é a fonte da verdade; esta lista é a leitura humana dela.

## 1.3.0 — o fim de linha de automacao-plataformas.md virou estado real

`leis/references/automacao-plataformas.md` já descrevia, como alvo, um dono que configura GitHub, Supabase, Cloudflare e Northflank uma vez para o agente nunca mais pedir. Na San & Co. isso aconteceu — as quatro credenciais estão ativas no ambiente de sessão.

- Parágrafo novo logo na abertura da referência, declarando isso: criar repositório, provisionar banco, fazer deploy e configurar domínio são fluxo normal da estação, sessão testa e lança sem pedido separado. A **lista curta** (dinheiro, segredo/autenticação, migration destrutiva, contrato de terceiro, remoção em uso, mudança só-em-produção) continua pedindo permissão do mesmo jeito — isto não muda o que já era regra na skill `leis`, só confirma que o alcance técnico chegou.
- Linha da Cloudflare corrigida: o mecanismo em uso é a **Global API Key** (`CLOUDFLARE_EMAIL` + `CLOUDFLARE_API_KEY`), não o token com escopo (`CLOUDFLARE_API_TOKEN`) que o texto assumia — header diferente, sem `GET /user/tokens/verify` para testar, e sem lista de permissão para configurar porque a Global Key não tem escopo. Uma linha em "Armadilhas" sobre isso.
- Regra nova, o segundo parágrafo: **a credencial alcança a conta inteira; a sessão não.** Nenhuma das quatro tem escopo por projeto, então quem separa é a sessão, não a chave — escrever, criar ou apagar é só no projeto desta sessão; qualquer outro repositório, banco, zona ou serviço que a credencial alcançar é só leitura. Mesma lógica do isolamento de banco da skill `classificar`, um nível acima: lá é o código nunca lendo o banco alheio; aqui é a sessão nunca escrevendo fora do projeto que está construindo.

## 1.2.3 — plugin de plataforma não é plugin de processo

- README do plugin: "único plugin ativo" → "único plugin de processo ativo", com a exceção escrita — plugin de plataforma (como o oficial da Northflank, `northflank/skills`) entrega comando, não regra de trabalho, e não disputa autoridade sobre a esteira.
- `leis/references/automacao-plataformas.md`: a linha da Northflank sobre conectar ao Claude Code, antes só "não há MCP oficial", agora traz os dois comandos de instalação do plugin de skills e o pré-requisito do CLI logado.

## Correção da documentação de instalação na nuvem

Sem mudança no plugin (segue 1.2.2). O que mudou foi o que os documentos afirmavam:

- **O `.claude/settings.json` do projeto não instala o plugin numa sessão de nuvem.** Ele registra o marketplace e marca o plugin como habilitado; a sessão abre sem as skills. Testado em container de sessão de nuvem, Claude Code 2.1.270.
- **O que instala é o script de setup do ambiente**, com `claude plugin marketplace add` e `claude plugin install` — é o que roda antes de o Claude Code subir. Testado: as nove skills carregam num projeto sem nenhum `.claude/`.
- `exemplos/setup-ambiente-nuvem.sh` novo; `docs/instalar-nuvem.md`, `docs/atualizar.md`, `README.md` e `exemplos/LEIA-ME.md` corrigidos.

## 1.2.2 — primeira publicação neste repositório

Conteúdo do plugin idêntico ao que já circulava como `san-co.plugin`. O que entrou junto:

- `.claude-plugin/marketplace.json` na raiz: o repositório passa a ser também o marketplace, instalável por `sancompany/Plugin_san-co`.
- `docs/`: instalação na nuvem, no terminal e no Cowork; ciclo de publicação; desenho de acessos.
- `exemplos/projeto-claude-settings.json`: o arquivo que faz um projeto nascer com o plugin.
- `scripts/`: empacotamento do `.plugin` do Cowork e as conferências de estrutura e de versão.
- CI que recusa plugin quebrado ou versão não subida, e release que anexa o `.plugin` na tag.
