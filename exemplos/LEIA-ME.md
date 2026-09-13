# Trechos prontos

## `projeto-claude-settings.json`

O `.claude/settings.json` de um projeto que nasce com o plugin `san-co`. Copie para o repositório **do projeto**:

```bash
mkdir -p .claude
curl -fsSL https://raw.githubusercontent.com/sancompany/Plugin_san-co/main/exemplos/projeto-claude-settings.json \
  -o .claude/settings.json
git add .claude/settings.json && git commit -m "Ativa o plugin san-co nas sessões de código"
```

O `curl` acima só funciona com o repositório público; com ele privado, copie o conteúdo do arquivo à mão.

**Se o projeto já tem `.claude/settings.json`**, não substitua: acrescente as chaves `extraKnownMarketplaces` e `enabledPlugins` ao objeto existente.

Vale para as duas superfícies de código ao mesmo tempo — a sessão de nuvem instala sozinha no início de cada sessão, e o Claude Code do terminal adiciona o marketplace assim que a pessoa confia na pasta. O porquê está em [`docs/instalar-nuvem.md`](../docs/instalar-nuvem.md).
