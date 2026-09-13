# Instalar no Claude Code da nuvem

Vale para **claude.ai/code**, o app de celular, o Desktop, o `claude --cloud` do terminal, as rotinas e o Claude Tag — todos rodam o mesmo tipo de sessão em máquina descartável.

## Por que aqui é diferente

A sessão de nuvem **nasce do zero toda vez**: uma VM nova, um clone novo do repositório, e nada do que está instalado na sua máquina. Por isso:

- **`/plugin` não existe na sessão de nuvem.** Não dá para instalar à mão lá dentro.
- **O que está no repositório, está na sessão.** `CLAUDE.md`, `.claude/settings.json`, `.claude/skills/` — tudo que foi commitado chega.
- **Plugin declarado no `.claude/settings.json` do projeto é instalado no início da sessão**, direto do marketplace, com acesso de rede ao GitHub.

Essas três coisas juntas dão de graça o que a esteira precisa: **a sessão de nuvem sempre abre com a última versão publicada do `san-co`.** Não existe "atualizar" na nuvem — existe abrir sessão. Publicou versão nova aqui, a próxima sessão de qualquer projeto já entra com ela.

## O que fazer — uma vez por projeto

### 1. Declarar o marketplace e o plugin

No repositório **do projeto** (não neste), crie ou edite `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "san-co": {
      "source": {
        "source": "github",
        "repo": "sancompany/Plugin_san-co"
      }
    }
  },
  "enabledPlugins": {
    "san-co@san-co": true
  }
}
```

O arquivo pronto está em [`exemplos/projeto-claude-settings.json`](../exemplos/projeto-claude-settings.json).

Se o projeto já tem um `.claude/settings.json`, **acrescente as duas chaves** ao objeto que já existe em vez de substituir o arquivo.

### 2. Commitar e subir

```bash
git add .claude/settings.json
git commit -m "Ativa o plugin san-co nas sessões de código"
git push
```

O plugin é instalado a partir do que está **no branch que a sessão clona**. Enquanto o commit não estiver no branch, a sessão não vê.

### 3. Conferir numa sessão nova

Abra uma sessão de nuvem no projeto e peça:

> Quais skills do plugin san-co estão disponíveis?

Ou rode `/context` e procure as skills `san-co:leis`, `san-co:construir`, `san-co:novo-projeto` e as demais. Se elas aparecem, acabou — nada mais a fazer, nem agora nem nas próximas versões.

## Rede: o que o ambiente precisa liberar

A sessão clona o marketplace do GitHub no início. O nível de acesso de rede **Confiável** (`Trusted`), que é o padrão do ambiente Default, já inclui `github.com`, `api.github.com`, `codeload.github.com` e `raw.githubusercontent.com` — não há nada a configurar.

Se o ambiente usa acesso **Personalizado** (`Custom`) com lista própria de domínios, marque **"incluir também a lista padrão"** ou acrescente esses domínios. Com a rede desligada, o plugin não instala.

## Se este repositório for privado

A sessão de nuvem fala com o GitHub por um proxy que usa credencial **restrita aos repositórios anexados à sessão**. O repositório do plugin não é o repositório do projeto, então o clone do marketplace privado pode voltar 403.

Três saídas, da mais simples para a mais trabalhosa:

1. **Repositório público.** O plugin não tem segredo dentro — são padrões de trabalho, não chaves nem código de produção. Público, o clone dispensa credencial e tudo funciona em qualquer superfície, sem exceção. Continua sendo você quem publica: leitura pública não dá permissão de escrita a ninguém.
2. **Token de leitura no ambiente.** Crie um *fine-grained token* com **Contents: Read-only** só neste repositório, guarde como variável de ambiente do ambiente de nuvem (`SANCO_PLUGIN_TOKEN`) e ponha no **script de setup** do ambiente:
   ```bash
   git config --global \
     url."https://x-access-token:${SANCO_PLUGIN_TOKEN}@github.com/sancompany/Plugin_san-co".insteadOf \
     "https://github.com/sancompany/Plugin_san-co"
   ```
   Vale lembrar: **quem usa o ambiente consegue ler as variáveis dele**. Um token só de leitura, só deste repositório, é o menor estrago possível — mas é um token exposto ao time.
3. **Copiar as skills para dentro de cada projeto** (`.claude/skills/`). Funciona, e é exatamente o que a esteira não quer: nove cópias para atualizar à mão a cada versão. Só faz sentido como remendo temporário.

A recomendação é a **1**. O detalhamento de quem pode o quê está em [acessos.md](acessos.md).

## O que não vem junto

- **`/plugin`, `/plugin install`, `/plugin marketplace`**: comandos de terminal, não existem na sessão de nuvem. Toda a configuração é pelo arquivo commitado.
- **Plugin habilitado só no `~/.claude/settings.json` da sua máquina**: fica na sua máquina. Tem que estar no `.claude/settings.json` do repositório.
- **Servidores LSP de plugins**: a nuvem não os inicia. O `san-co` não usa LSP, então não muda nada aqui.

## Resumo para colar no chat de um colega

> No repositório do projeto, crie `.claude/settings.json` com `extraKnownMarketplaces` apontando para `sancompany/Plugin_san-co` e `enabledPlugins` com `"san-co@san-co": true`. Commita e sobe. A partir da próxima sessão de nuvem o plugin entra sozinho, sempre na última versão. O arquivo pronto está em `exemplos/projeto-claude-settings.json` do repositório do plugin.
