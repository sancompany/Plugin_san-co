# Publicar uma versão

Quem publica: **o dono do repositório**. Quem usa, não publica — ver [acessos.md](acessos.md).

## O ciclo, inteiro

1. **Editar** o que muda dentro de `plugins/san-co/` (skill, reference, README do plugin).
2. **Subir o `version`** em `plugins/san-co/.claude-plugin/plugin.json`. Não é burocracia: é o campo que faz a atualização chegar em quem já tem o plugin instalado. Sem ele, quem instalou fica parado na versão antiga para sempre.
   - correção pequena ou ajuste de texto → último número (`1.2.2` → `1.2.3`)
   - regra ou reference nova → número do meio (`1.3.0`)
   - mudança que altera a esteira → primeiro número (`2.0.0`)
3. **Anotar** a linha no [CHANGELOG.md](../CHANGELOG.md).
4. **Commitar e subir** para `main` (pela branch e pull request, ver abaixo).
5. **Marcar a versão** para gerar o `.plugin` do Cowork, de um jeito ou de outro:
   ```bash
   git tag v1.2.3
   git push origin v1.2.3
   ```
   Ou, sem sair do navegador: **Actions → publicar → Run workflow**, deixando o campo de versão em branco. O workflow lê o `version` do `plugin.json`, cria a tag e publica a release com o `san-co.plugin` anexado. Sessão de nuvem publica por aqui: o proxy do GitHub nas sessões só deixa subir branch, não tag.

## O que acontece depois, em cada superfície

| Superfície | Como a versão chega | Quando |
|---|---|---|
| **Sessões de nuvem** (claude.ai/code, app, Claude Tag, rotinas) | o script de setup do ambiente instalou o plugin; o ambiente guarda um snapshot do disco e as sessões seguintes partem dele | na próxima sessão **depois que o snapshot for refeito** — editar o script de setup (a linha `# san-co <versão>`) força isso na hora; senão, sozinho em ~7 dias |
| **Claude Code no terminal / VS Code** | `/plugin marketplace update san-co`, ou auto-update ligado no marketplace | quando a pessoa atualiza, ou na sessão seguinte se o auto-update estiver ligado |
| **Cowork** | baixar o `san-co.plugin` da release e instalar | à mão, sempre |

**Publicou versão e quer que entre hoje:** edite o campo **Setup script** do ambiente em claude.ai/code — mudar a linha do comentário com a versão já basta. É o único gesto manual do ciclo, é do mantenedor, e vale para todo mundo daquele ambiente de uma vez.

O detalhe de por que é assim — e por que o `.claude/settings.json` do projeto não instala sozinho na nuvem — está em [instalar-nuvem.md](instalar-nuvem.md).

## A CI confere

Todo pull request passa por `.github/workflows/validar.yml`, que recusa:

- `marketplace.json` ou `plugin.json` fora do formato;
- skill sem `SKILL.md`, ou `SKILL.md` sem `description` no frontmatter;
- `version` do `plugin.json` que **não subiu** quando algo em `plugins/san-co/` mudou;
- `version` que andou para trás.

É a trava técnica do passo 2. O resto da governança — um escritor só, lição de erro voltando pela sessão de projeto — continua sendo convenção, escrita na skill `leis`.

## Sem pular a fila

Publicar direto na `main` com `git push` não deve ser possível: a `main` é protegida ([acessos.md](acessos.md)). O caminho é branch → pull request → CI verde → merge. Para o dono do repositório isso custa dois minutos; o que ele compra é nunca publicar uma versão quebrada para todas as sessões de uma vez, que é exatamente o que a instalação automática torna possível.
