# Instalar no Claude Code da nuvem

Vale para **claude.ai/code**, o app de celular, o Desktop, o `claude --cloud` do terminal, as rotinas e o Claude Tag — todos rodam o mesmo tipo de sessão em máquina descartável.

## A regra que manda aqui

A sessão de nuvem **nasce do zero toda vez**: VM nova, clone novo, `~/.claude` vazio. E o carregamento de plugin acontece **no start da sessão**, antes de qualquer coisa que rode dentro dela. Disso sai a única regra que importa:

> **O plugin tem que estar instalado antes de a sessão começar. O que instala depois só vale na sessão seguinte — e não existe sessão seguinte na mesma VM.**

O lugar que roda antes do Claude Code subir é o **script de setup do ambiente de nuvem**. É lá que o plugin entra.

## O que **não** basta (e por que)

Declarar o plugin no `.claude/settings.json` do projeto **registra o marketplace e marca o plugin como habilitado, mas não o instala.** A sessão abre sem as skills.

Isto foi testado num container de sessão de nuvem, Claude Code 2.1.270, com o arquivo correto e commitado:

```
$ cat .claude/settings.json      # extraKnownMarketplaces + enabledPlugins, corretos
$ claude -p "liste as skills do plugin san-co"
NENHUMA
$ claude plugin list
No plugins installed.
```

Se uma sessão sua disser que não encontra `san-co:leis`, `san-co:construir` e as outras, **ela está certa e não é culpa dela** — é isto aqui. O arquivo continua valendo (ver "O que o arquivo do projeto ainda faz"), só não é suficiente sozinho.

## O que funciona: duas linhas no script do ambiente

Em [claude.ai/code](https://claude.ai/code), no seletor de ambiente → engrenagem do ambiente → campo **Setup script**:

```bash
claude plugin marketplace add sancompany/Plugin_san-co
claude plugin install san-co@san-co
```

Está pronto em [`exemplos/setup-ambiente-nuvem.sh`](../exemplos/setup-ambiente-nuvem.sh), com as duas linhas idempotentes.

Testado no mesmo container, rodando os dois comandos antes da sessão, num projeto **sem nenhum `.claude/`**:

```
$ claude -p "liste as skills do plugin san-co"
checkout, classificar, construir, depurar, legal, leis, novo-projeto,
revisar, seguranca-san
```

As nove skills, em qualquer projeto daquele ambiente, sem arquivo nenhum no repositório. **Uma configuração por pessoa, e não uma por projeto** — que é melhor do que o desenho anterior prometia.

## A versão que chega, e como forçar a atualização

O ambiente guarda um **snapshot do disco depois que o script de setup roda**, e as sessões seguintes partem dele **sem rodar o script de novo**. Ou seja: a versão do plugin congela no snapshot. O snapshot é refeito quando o script de setup muda, quando a lista de domínios do ambiente muda, ou sozinho depois de uns sete dias.

Para uma esteira que publica com frequência, isso dá o gesto que o mantenedor controla: **publicou versão e quer que entre já, edite o script de setup.** Basta mudar o comentário da versão — é por isso que o exemplo tem uma linha `# san-co 1.2.2` no topo. Editar o campo já refaz o snapshot, e a sessão seguinte de todo mundo entra com a versão nova.

Duas coisas que ajudam, e que valem só a partir da **próxima** sessão (o Claude Code carrega plugin no start; o que instala depois fica para o próximo start):

- um **SessionStart hook** no `.claude/settings.json` do projeto rodando `claude plugin install san-co@san-co` — o comando com o nome do marketplace junto sempre puxa o catálogo antes de instalar;
- o auto-update de marketplace, que no terminal é um botão, e aqui não tem interface.

Por isso o gesto de editar o script continua sendo o caminho determinístico.

## Quando a sessão já está aberta e sem o plugin

Dentro da sessão, peça para rodar:

```bash
claude plugin marketplace add sancompany/Plugin_san-co
claude plugin install san-co@san-co
```

Depois disso, `/reload-plugins` digitado direto na caixa da sessão costuma carregar as skills na hora. Se não carregar, **abra uma sessão nova** — a instalação já está no disco daquela VM e a sessão seguinte abre com tudo. Para não repetir isso, ponha as duas linhas no script do ambiente.

## O que o arquivo do projeto ainda faz

Continua valendo a pena commitar isto no `.claude/settings.json` do projeto ([`exemplos/projeto-claude-settings.json`](../exemplos/projeto-claude-settings.json)):

```json
{
  "extraKnownMarketplaces": {
    "san-co": { "source": { "source": "github", "repo": "sancompany/Plugin_san-co" } }
  },
  "enabledPlugins": { "san-co@san-co": true }
}
```

Ele faz três coisas reais: registra o marketplace sem ninguém digitar comando, deixa o plugin habilitado quando ele existe, e é o que faz o Claude Code **do terminal e do VS Code** herdar tudo ao confiar na pasta ([instalar-terminal.md](instalar-terminal.md)). O que ele **não** faz é instalar na nuvem.

## O caminho sem repositório e sem script: a conta claude.ai

Skill e plugin ligados na **conta claude.ai** (barra lateral → **Customize**) são baixados sozinhos em toda sessão de nuvem e do Cowork, a cada sessão, sem marketplace e sem cache — é o mecanismo dos *synced plugins*, que vivem em `~/.claude/plugins/synced/`. Se o `san-co` puder ser ligado por aí na sua conta, é o desenho mais limpo dos três: nada no ambiente, nada no projeto, e sempre a versão corrente.

Não consegui testar isso daqui — depende do que a sua conta oferece nessa tela. Se a opção existir, vale experimentar antes do script de setup; se não existir, o script de setup é o caminho.

## Rede

O clone do marketplace sai pelo GitHub. O nível **Confiável** (`Trusted`), padrão do ambiente Default, já libera `github.com`, `api.github.com` e `codeload.github.com` — nada a configurar. Em ambiente **Personalizado**, marque "incluir também a lista padrão" ou acrescente esses domínios. Sem rede, o plugin não instala.

## Se este repositório for privado

**Hoje ele é público, então nada aqui se aplica** — o clone dispensa credencial. Esta seção existe para o dia em que alguém pensar em fechar o repositório.

A sessão de nuvem fala com o GitHub por um proxy cuja credencial só alcança **os repositórios anexados à sessão**. O repositório do plugin não é o do projeto, então o clone do marketplace privado volta 403.

1. **Repositório público.** Não há segredo no plugin — são padrões de trabalho. Público, o clone funciona em qualquer superfície. Leitura pública não dá escrita a ninguém.
2. **Token de leitura no ambiente.** *Fine-grained token* com **Contents: Read-only** só neste repositório, guardado como variável do ambiente, e no script de setup, antes das duas linhas:
   ```bash
   git config --global \
     url."https://x-access-token:${SANCO_PLUGIN_TOKEN}@github.com/sancompany/Plugin_san-co".insteadOf \
     "https://github.com/sancompany/Plugin_san-co"
   ```
   Com a ressalva: **quem usa o ambiente consegue ler as variáveis dele**.
3. **Copiar as skills para dentro de cada projeto** (`.claude/skills/`). Funciona — skill commitada sempre carrega — e é exatamente o que a esteira não quer: nove cópias para atualizar à mão a cada versão.

A recomendação é a **1**. Quem pode o quê está em [acessos.md](acessos.md).

## O que não existe na sessão de nuvem

- **`/plugin`** e a sua interface: são do terminal. Aqui tudo passa pelo script do ambiente ou pelo `claude plugin` no Bash.
- **Plugin habilitado só no `~/.claude/settings.json` da sua máquina**: fica na sua máquina.
- **Servidores LSP de plugin**: a nuvem não os inicia. O `san-co` não usa LSP.

## Resumo para colar no chat de um colega

> Abra claude.ai/code, escolha o ambiente, engrenagem, campo **Setup script**, e ponha estas duas linhas:
> ```
> claude plugin marketplace add sancompany/Plugin_san-co
> claude plugin install san-co@san-co
> ```
> A partir da próxima sessão, todo projeto daquele ambiente abre com as nove skills `san-co:*`. Só o `.claude/settings.json` no projeto **não** instala na nuvem — ele serve ao Claude Code do terminal.
