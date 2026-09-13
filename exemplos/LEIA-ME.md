# Trechos prontos

## `setup-ambiente-nuvem.sh`

As duas linhas que instalam o plugin nas **sessões de nuvem**. Vão no campo **Setup script** do ambiente em [claude.ai/code](https://claude.ai/code) (seletor de ambiente → engrenagem), porque é o único lugar que roda antes de o Claude Code subir. Uma vez por pessoa; vale para todo projeto daquele ambiente.

Só o `.claude/settings.json` abaixo **não** resolve a nuvem — ver [`docs/instalar-nuvem.md`](../docs/instalar-nuvem.md).

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

Serve ao Claude Code **do terminal e do VS Code**: o marketplace é adicionado assim que a pessoa confia na pasta, e o plugin já entra habilitado. Na nuvem ele registra e habilita, mas não instala — quem instala lá é o script de setup do ambiente.
