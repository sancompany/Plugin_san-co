# Sessão de manutenção do plugin san-co

Este repositório é **o plugin `san-co` e o marketplace que o distribui**. O que entra na `main` chega a todas as sessões de nuvem da San & Co. na próxima vez que alguém abrir uma. Trate cada mudança com esse peso.

## Onde mexer

- **Conteúdo das skills**: `plugins/san-co/skills/<skill>/SKILL.md` e `plugins/san-co/skills/<skill>/references/`.
- **Descrição do plugin**: `plugins/san-co/.claude-plugin/plugin.json`.
- **Catálogo**: `.claude-plugin/marketplace.json` — só muda se um plugin novo entrar.

Componentes moram na raiz do plugin. Dentro de `.claude-plugin/` só vai o `plugin.json`.

## Regras da casa

1. **Mudou algo em `plugins/san-co/`, sobe o `version`** do `plugin.json` no mesmo commit. É o campo que faz a atualização chegar em quem já instalou. A CI recusa o pull request que esquecer.
2. **Descrição curta na skill, conteúdo longo em `references/`.** A descrição entra no contexto a cada mensagem; a reference só é lida quando serve.
3. **Sem duplicação.** Cada assunto mora em exatamente uma skill; as outras apontam para ela. Lição do catálogo é citada por número, nunca reescrita.
4. **Um escritor só.** A esteira depende de não existirem duas versões da mesma regra. Sessão de projeto propõe por issue ou pull request; quem publica é o mantenedor.
5. **Antes de commitar**, rode as conferências:
   ```bash
   python3 scripts/validar.py
   ./scripts/conferir-versao.sh origin/main
   ```

## Ao terminar

Anote a linha no `CHANGELOG.md`. Depois do merge na `main`, a versão é marcada com `git tag v<version>` e a CI publica a release com o `san-co.plugin` do Cowork anexado — ver `docs/atualizar.md`.
