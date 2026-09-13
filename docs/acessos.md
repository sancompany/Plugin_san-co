# Acessos: quem lê, quem publica

O desenho é um só: **o time lê, o dono publica.** Instalação automática significa que o que entra na `main` entra em todas as sessões de nuvem da próxima vez que alguém abrir uma — então quem pode escrever aqui pode mudar como toda a empresa constrói. Esse poder fica com uma pessoa.

## Permissão no GitHub

Em **Settings → Collaborators and teams** do repositório:

| Papel | Permissão do GitHub | Pode |
|---|---|---|
| Time (todo mundo que usa o plugin) | **Read** | clonar, instalar, abrir issue, abrir pull request a partir de fork |
| Mantenedor (quem publica) | **Admin** ou **Maintain** | fazer merge na `main`, marcar versão, publicar release |

**Read basta para usar.** O Claude Code só clona o repositório para ler o catálogo e a pasta do plugin — nunca escreve nele. Ninguém precisa de Write para instalar, atualizar ou rodar as skills.

Se o time já está num GitHub Team, dê **Read** ao time inteiro de uma vez em vez de pessoa por pessoa; quem entra na empresa passa a herdar o acesso sem ninguém lembrar de conceder.

## Proteger a `main`

Em **Settings → Rules → Rulesets** (ou **Branches → Branch protection rules**), para `main`:

- **Restringir quem pode fazer push**: só o mantenedor. Isso já impede publicação acidental de quem tem Write por outro motivo.
- **Exigir pull request antes do merge.**
- **Exigir os status checks**: o job `validar` do workflow de CI. Pull request com plugin quebrado ou sem bump de versão não entra.
- **Bloquear force push e deleção** da `main`.

Com isso, a única porta para as sessões do time é: pull request → CI verde → merge feito pelo mantenedor.

## Público ou privado?

**Privado** é o padrão de reflexo, e aqui ele custa caro numa superfície específica: a sessão de nuvem fala com o GitHub por um proxy cuja credencial só alcança **os repositórios anexados à sessão**. O repositório do plugin não é o repositório do projeto, então o clone do marketplace pode voltar 403 e o plugin não instalar — que é justamente o automatismo que se quer ter.

**Público** resolve isso sem abrir nada: leitura pública **não** dá escrita a ninguém. Quem publica continua sendo só quem tem Maintain e passa pela `main` protegida. O que fica visível é o conteúdo do plugin — padrões de trabalho, a esteira, as leis, as obrigações legais. Não há chave, segredo, dado de cliente nem código de produção aí dentro.

Antes de tornar público, uma varredura de dois minutos:

```bash
grep -rniE "senha|token|secret|api[_-]?key|sk-|BEGIN .*PRIVATE KEY" plugins/san-co/
```

O que aparecer tem que ser **menção a conceito** (a reference de derivação de senha, por exemplo), nunca valor real. Confirmado isso, público é a escolha melhor.

Se ainda assim precisar ficar privado, o caminho para a nuvem continuar automática é o token de leitura no script de setup do ambiente, descrito em [instalar-nuvem.md](instalar-nuvem.md#se-este-repositório-for-privado) — com a ressalva que está lá: **quem usa o ambiente consegue ler as variáveis dele**.

## Como o time contribui sem publicar

Com **Read**, ninguém do time faz push direto — e não precisa. A skill `leis` já define o fluxo no "Fecho da esteira": a sessão de projeto registra a lição em `docs/erros/` dela e entrega a lista de reenvio no fecho. O mantenedor traz para cá.

Quando alguém quiser propor texto, o caminho é **issue** (Read já permite) ou **pull request a partir de fork**. A decisão de publicar segue sendo de um escritor só — a esteira depende disso para não ter duas versões da mesma regra.
