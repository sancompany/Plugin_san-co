# Instalar no Claude Code do terminal e do VS Code

Aqui o `/plugin` existe, e a instalação é feita uma vez por máquina — ou uma vez por projeto, se for pelo arquivo de configuração.

## Caminho curto: pelo comando

Dentro de uma sessão do Claude Code:

```
/plugin marketplace add sancompany/Plugin_san-co
/plugin install san-co@san-co
```

O instalador pergunta o **escopo**:

| Escopo | O que significa | Quando usar |
|---|---|---|
| **User** | você, em todos os projetos | é o normal para quem trabalha em vários projetos San & Co. |
| **Project** | todo mundo que abre este repositório (grava no `.claude/settings.json`) | quando o projeto é da San & Co. e todo colaborador deve herdar |
| **Local** | você, só neste repositório | teste |

Conferir: `/plugin list` mostra o instalado; as skills aparecem como `san-co:leis`, `san-co:construir`, `san-co:novo-projeto` e assim por diante.

Fora da sessão, pela linha de comando:

```bash
claude plugin marketplace add sancompany/Plugin_san-co
claude plugin install san-co@san-co
```

## Caminho recomendado: pelo arquivo do projeto

É o mesmo arquivo que faz o plugin funcionar nas sessões de nuvem — **um arquivo só resolve as duas superfícies**. No repositório do projeto, `.claude/settings.json`:

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

Quem clonar o projeto ganha o marketplace assim que **confiar na pasta** — o Claude Code pergunta isso na primeira abertura. Se o plugin não carregar sozinho depois disso, o próprio Claude Code mostra o `claude plugin install san-co@san-co` a rodar; é um comando, uma vez.

## Atualizar

```
/plugin marketplace update san-co
```

Isso puxa o catálogo e atualiza o plugin instalado **quando o `version` do `plugin.json` mudou** — por isso a regra de sempre subir a versão a cada publicação ([atualizar.md](atualizar.md)). Se a atualização pedir, rode `/reload-plugins` para valer na sessão aberta; senão ela entra na próxima.

### Deixar automático

`/plugin` → aba **Marketplaces** → escolher `san-co` → **Enable auto-update**.

Com isso o Claude Code passa a atualizar o marketplace e o plugin sozinho depois que a sessão começa (com atraso aleatório de até dez minutos, para não mexer na sessão que acabou de carregar). Quando alguma versão nova entra, aparece o aviso para rodar `/reload-plugins` — ou ela vale na próxima abertura.

Marketplace de terceiro nasce com auto-update **desligado**; é uma escolha por máquina, feita uma vez.

## Se este repositório for privado

O `git` da sua máquina precisa saber se autenticar no GitHub. Basta uma vez:

```bash
gh auth login
gh auth setup-git
```

Com isso o clone e as atualizações em segundo plano funcionam pelo mesmo credencial que você já usa no dia a dia. Sem isso, o `/plugin marketplace add` falha com erro de autenticação.

## Desinstalar

```
/plugin uninstall san-co@san-co
/plugin marketplace remove san-co
```

Remover o marketplace desinstala o que veio dele.
