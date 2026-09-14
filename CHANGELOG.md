# Mudanças

O `version` do `plugins/san-co/.claude-plugin/plugin.json` é a fonte da verdade; esta lista é a leitura humana dela.

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
