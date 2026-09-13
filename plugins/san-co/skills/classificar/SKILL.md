---
name: classificar
description: Decide se algo é estrutura compartilhada da San & Co. ou projeto próprio, e aplica a política de isolamento de banco. Use quando surgir dúvida sobre onde uma capacidade mora, se um banco deve ser compartilhado ou separado, ou se algo deve ser reaproveitado entre projetos.
---

# Estrutura vs. projeto

## Os quatro testes

Aplicar **os quatro**. Apontando todos na mesma direção, ela decide; discordando entre si, vale a regra de desempate abaixo.

1. **Desligamento** — se isso parar de existir hoje, quantos projetos param junto? Mais de um → estrutura.
2. **Público** — tem usuário final próprio (alguém que abre, compra, usa)? Sim → projeto. Se os únicos "usuários" são outros sistemas → estrutura.
3. **Entrega** — se esse projeto fosse entregue ou vendido a um cliente amanhã, isso iria junto? Se **não pode** ir junto porque outros dependem → estrutura.
4. **Pedido de mudança** — quem pede alteração? Um projeto só → projeto. Vários → estrutura.

Se dois testes discordarem, tratar como **projeto** até existir um segundo consumidor **real e em funcionamento** — não planejado, não prometido, não "vai precisar depois". Consumidor previsto não conta: é assim que tudo vira estrutura por antecipação, que é a engenharia especulativa proibida pelas Leis. Promover projeto → estrutura depois é barato; desmontar estrutura que nunca teve dois consumidores é desperdício puro.

## O que é estrutura hoje

San Checkout (motor de pagamento), domínio `sancocore.com.br` e DNS no Cloudflare, **Cloudflare Access como porta das áreas administrativas**, e-mail Google Workspace com alias por projeto, Google Drive, contas de infraestrutura (Cloudflare, Northflank, Supabase, GitHub), emissão de nota fiscal via Asaas, o **contratante de teste** do Checkout (bancada e implementação de referência — skill `checkout`), e a identidade visual San & Co.

Todo o resto — o que tem público e razão de existir próprios — é projeto.

**Como usar cada plataforma está em `references/plataformas-san-co.md`** — o que cada uma serve, o que dorme, o que não tem backup, a regra de aplicação e banco na mesma região, e a ordem de migração do que ainda roda em hospedagem descontinuada. Ler antes de responder "onde isso roda": quase toda decisão de hospedagem que dá errado depois foi tomada por hábito, não por número.

**Projeto com login de administrador consome o Access, não constrói proteção própria de entrada.** A decisão e o registro são desta estação; as regras de como aplicar, as quatro armadilhas que anulam a camada e onde ela é verificada estão na skill `seguranca-san`.

## Regras de fronteira

- **Estrutura não conhece regra de negócio de projeto.** O Checkout sabe o que é "pedido", não o que é ingresso ou cesta de compras. Toda vez que a estrutura precisar de um `if` específico de um projeto, a fronteira foi rompida: o específico volta para o projeto.
- **Projeto nunca acessa banco de outro projeto nem da estrutura diretamente.** Comunicação sempre por API com contrato explícito e chave de autenticação própria por projeto.
- **Cadastro de projeto na estrutura é manual** — URL da API, chave e `walletId` inseridos à mão no banco da estrutura, nunca por endpoint público.
- **Namespace por projeto dentro de cada recurso compartilhado** — uma pasta raiz por projeto no Drive, um alias de e-mail por projeto, uma credencial por projeto. Nunca a mesma chave mestra distribuída, para que revogar um projeto não derrube os outros.
- **Comunicação é do dono do assunto** — e-mail de confirmação de pagamento sai do Checkout; e-mail de produto sai do projeto.

## Mudar estrutura sem quebrar projeto

Estrutura tem consumidores que não estão na sua frente. Antes de alterar qualquer peça de estrutura (Checkout, contrato de integração, formato de resposta, alias de e-mail):

- **Ler o contrato existente primeiro** — o documento de integração, o formato que os projetos já consomem hoje. Nunca alterar de memória.
- **Mudança é aditiva por padrão.** Campo novo, endpoint novo, parâmetro opcional: pode. Renomear campo, remover campo, mudar tipo, mudar significado de valor existente, tornar obrigatório o que era opcional: isso quebra consumidor.
- **Quebra de contrato exige avisar e versionar.** Listar quais projetos consomem aquilo, manter o comportamento antigo funcionando enquanto eles migram, e só então remover.
- **Na dúvida sobre quem consome**, não alterar: descobrir primeiro. Um projeto quebrado em produção por mudança silenciosa na estrutura é o modo de falha mais caro deste modelo.

O mesmo vale ao contrário: projeto nunca depende de comportamento não documentado da estrutura. Se funciona por acaso, vai quebrar.

## Política de dado: isolar sempre

Cada projeto e cada peça de estrutura tem **seu próprio banco / projeto Supabase**. Estrutura compartilhada sim; banco compartilhado não. Decisão fechada, sem exceção.

Motivos, quando alguém propuser centralizar:

- **Entrega e venda** — projeto que divide banco com o resto não pode ser entregue a um cliente sem desmontar o banco inteiro.
- **Raio de dano** — migration errada, credencial vazada ou query pesada num banco único atinge todos os projetos de uma vez.
- **Mistura de responsabilidade** — dado de cliente de terceiro no mesmo banco de dado pessoal é risco que economia nenhuma compensa.

**Custo assumido conscientemente**: mais instâncias para administrar quando vários projetos estiverem no ar. Mitigação: instância paga só quando o projeto entra em produção.

**Dado cruzado entre projetos** resolve-se por leitura via API autenticada, nunca por acesso direto ao banco alheio. Se virar frequente, criar uma peça de estrutura de consolidação — não furar o isolamento.

## Aplicar em projeto novo

Para cada capacidade que o projeto precisa (pagamento, e-mail, arquivo, domínio), checar se já existe como estrutura: existindo, **consumir**, não reconstruir. Para pagamento, usar a skill `checkout` — o motor já está em produção e nenhum projeto constrói cobrança própria. Se não existe e só esse projeto precisa, nasce dentro do projeto. Quando um segundo projeto pedir a mesma coisa, aí sim promover a estrutura, com contrato e chave por projeto.
