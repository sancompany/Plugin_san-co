# Mudanças

O `version` do `plugins/san-co/.claude-plugin/plugin.json` é a fonte da verdade; esta lista é a leitura humana dela.

## 1.2.2 — primeira publicação neste repositório

Conteúdo do plugin idêntico ao que já circulava como `san-co.plugin`. O que entrou junto:

- `.claude-plugin/marketplace.json` na raiz: o repositório passa a ser também o marketplace, instalável por `sancompany/Plugin_san-co`.
- `docs/`: instalação na nuvem, no terminal e no Cowork; ciclo de publicação; desenho de acessos.
- `exemplos/projeto-claude-settings.json`: o arquivo que faz um projeto nascer com o plugin.
- `scripts/`: empacotamento do `.plugin` do Cowork e as conferências de estrutura e de versão.
- CI que recusa plugin quebrado ou versão não subida, e release que anexa o `.plugin` na tag.
