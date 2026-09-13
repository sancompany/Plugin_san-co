# San & Co.

Os padrões e o ciclo de trabalho da San & Co., empacotados como skills. Desenhado para ser o **único plugin ativo** — cobre da ideia ao lançamento, e do lançamento à versão seguinte, sem depender de pacotes genéricos.

## Skills

| Skill | Quando dispara |
|---|---|
| `novo-projeto` | "tenho uma ideia", "quero criar um app/site/sistema", começar ou escopar um projeto |
| `classificar` | estrutura compartilhada ou projeto; banco compartilhado ou separado; onde roda |
| `leis` | abrir ou fechar uma estação, montar estrutura de pastas, revisar contra os padrões, subir para produção |
| `construir` | abrir a construção de um site ou app, escrever código, adicionar funcionalidade, refatorar, escolher biblioteca |
| `depurar` | algo quebrou, teste falhou, build parou, comportamento fora do esperado |
| `revisar` | antes de commit, merge ou deploy |
| `checkout` | o projeto precisa receber pagamento, cobrar assinatura ou estornar |
| `seguranca-san` | cobrança, autenticação, senha, documento, área administrativa ou dado de cliente |
| `legal` | dado novo, terceiro novo, conta de usuário, cobrança a consumidor, ir ao ar |

## O ciclo

Sete estações, em ordem de criação: **escopo → fronteiras → fundação → contratos → construção → prontidão → lançamento.** Estação não fecha, esteira não anda. A tabela completa vive na skill `leis` e é a única fonte. A esteira foi desenhada para projeto nascendo do zero; projeto que já existe entra pela auditoria.

As leis (0 a 10) são o que se verifica em cada estação, não as estações em si — numeração estável para citação, ordem de construção pela tabela.

## Quem edita este plugin

**Um escritor só** — a sessão de manutenção. Sessão de projeto contribui com lição de erro no `docs/erros/` dela e, no fecho, entrega a lista de reenvio. A governança inteira está na skill `leis`, "Fecho da esteira". É convenção, não trava técnica; funciona porque está escrito onde as sessões leem.

## Onde ele fica instalado

**Cada superfície instala a sua cópia; nenhuma herda da outra.** No Cowork, o arquivo `.plugin`. No Claude Code (CLI e extensão do VS Code), só por **marketplace** — sessão de código não enxerga o que foi instalado no Cowork.

O marketplace é uma pasta (ou repositório) com `.claude-plugin/marketplace.json` na raiz e o plugin numa subpasta:

```
claude-plugins/
├── .claude-plugin/marketplace.json   # name, owner, plugins[{name, source, description}]
└── plugins/san-co/                   # este plugin inteiro
```

Instalar: `/plugin marketplace add <caminho ou owner/repo>` e depois `/plugin install san-co@san-co`. Para um projeto já nascer com ele, `.claude/settings.json` com `extraKnownMarketplaces` e `enabledPlugins` — o marketplace se adiciona sozinho ao confiar na pasta.

**A cópia do Cowork e a do marketplace são a mesma pasta empacotada de dois jeitos.** Publicou versão nova, atualiza as duas; só uma atualizada é o mesmo projeto medido por duas réguas diferentes.

**Versão** em `.claude-plugin/plugin.json`, semântica: correção pequena ou ajuste de texto sobe o último número (1.1.0 → 1.1.1); regra ou referência nova sobe o do meio (1.2.0); mudança que altera a esteira sobe o primeiro.

## Como o plugin é organizado

**Descrições curtas de propósito** — elas entram no contexto a cada mensagem. **Conteúdo longo vive em `references/`**, carregado só quando serve: as listas da varredura final, da prontidão operacional, da definição funcional, da aceleração e da automação das plataformas (`leis`); o mapa do que todo site tem e as referências por tipo — institucional, SaaS, e-commerce, PWA (`construir`); o catálogo de lições (`depurar`); as verificações automáticas e a derivação de senha (`seguranca-san`); as plataformas (`classificar`); as obrigações legais brasileiras e o conteúdo dos documentos (`legal`).

**Sem duplicação.** Cada assunto mora em exatamente uma skill; as outras apontam. Lição do catálogo é citada por número, nunca reescrita.

**Contexto real do ecossistema.** As skills já conhecem o San Checkout, as plataformas em uso, as armadilhas que já custaram caro, e as obrigações legais de quem vende assinatura no Brasil.
