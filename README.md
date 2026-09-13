# Plugin_san-co — marketplace da San & Co.

Repositório oficial do plugin **`san-co`**: os padrões e o ciclo de trabalho da San & Co. empacotados como skills do Claude Code.

Este repositório é ao mesmo tempo **o plugin** e **o marketplace** que o distribui. Uma fonte só, um lugar só para atualizar.

```
Plugin_san-co/
├── .claude-plugin/marketplace.json   # o catálogo: aponta para plugins/san-co
├── plugins/san-co/                   # o plugin inteiro (skills, references, plugin.json)
├── docs/                             # instalação, atualização, acessos
├── exemplos/                         # trechos prontos para copiar
└── scripts/empacotar-plugin.sh       # gera o san-co.plugin do Cowork
```

## Instalar

| Onde | Como | Documento |
|---|---|---|
| **Claude Code na nuvem** (claude.ai/code, app, Claude Tag) | `.claude/settings.json` no repositório do projeto — instala sozinho a cada sessão | [docs/instalar-nuvem.md](docs/instalar-nuvem.md) |
| **Claude Code no terminal / VS Code** | `/plugin marketplace add sancompany/Plugin_san-co` e `/plugin install san-co@san-co` | [docs/instalar-terminal.md](docs/instalar-terminal.md) |
| **Cowork** | arquivo `san-co.plugin` da última release | [docs/instalar-cowork.md](docs/instalar-cowork.md) |

O caminho mais curto, para um projeto já nascer com o plugin em **qualquer** superfície de código, é copiar [`exemplos/projeto-claude-settings.json`](exemplos/projeto-claude-settings.json) para o `.claude/settings.json` do projeto e commitar.

## Atualizar

Quem lança versão: ver [docs/atualizar.md](docs/atualizar.md). Regra que não se negocia: **subiu conteúdo em `plugins/san-co/`, sobe o `version` no `plugin.json`** — é o `version` que faz a atualização chegar em quem já tem o plugin instalado. A CI recusa o pull request que esquecer.

Quem só usa: não faz nada nas sessões de nuvem (cada sessão já nasce com a última versão); no terminal, `/plugin marketplace update san-co`.

## Acessos

A equipe entra com **leitura**; o lançamento de versão fica com o dono do repositório. O desenho completo — permissão no GitHub, proteção da branch `main`, o que cada papel pode — está em [docs/acessos.md](docs/acessos.md).

## O que o plugin contém

Nove skills (`novo-projeto`, `classificar`, `leis`, `construir`, `depurar`, `revisar`, `checkout`, `seguranca-san`, `legal`), a esteira de sete estações e as onze leis. A descrição de cada uma e o desenho interno estão no [README do plugin](plugins/san-co/README.md).
