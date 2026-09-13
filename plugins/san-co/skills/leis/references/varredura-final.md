# Varredura final — a lista completa

A passada de conclusão do projeto, rodada **duas vezes**: na versão local e no que está efetivamente no ar. Ela é a **segunda metade da estação 7**: roda depois de os documentos legais estarem escritos e publicados, e antes da entrega de manutenção. Quem roda decide, ao final, se o projeto fechou ou se falta algo — e esse veredito é o que **fecha** a estação 7.

Esta lista existe para que a varredura não dependa de memória nem de disposição. Item que não está aqui pode ser verificado; item que está aqui **não pode ser pulado**.

## Antes de começar: a varredura está olhando a versão certa?

Conferir, nesta ordem, e **não começar** enquanto os três não baterem:

1. o commit que a hospedagem está servindo é o mesmo da branch principal;
2. todas as migrations foram aplicadas no banco de produção;
3. nada relevante existe só no disco de alguém — trabalho não commitado, arquivo não enviado.

Divergindo em qualquer ponto, a varredura **não roda**: diz o que falta e para. Passada sobre versão desatualizada devolve um relatório limpo de um sistema que ninguém examinou, e alguém acredita nele (lição nº 14).

## Como se usa

**Cada item recebe um veredito com evidência**, nunca uma impressão:

- **conforme** — e ao lado, *como* foi verificado (o comando que rodou, a tela que foi aberta, a resposta que voltou);
- **divergência** — está lá, mas diferente do que deveria;
- **falta** — não existe;
- **não verificável daqui** — e por quê. Isso **não é conforme**: é pendência, e aparece no veredito final.

**Proibido:**

- "parece ok", "deve estar certo", "provavelmente funciona" — sem evidência, o item é **falta**;
- amostragem — "verifiquei três telas, as outras seguem o mesmo padrão" não vale. Ou todas, ou o que não foi aberto entra como não verificado;
- marcar conforme por ter lido o código. Ler prova intenção; só executar prova comportamento;
- pular passada por ela "não se aplicar" sem escrever em uma linha por que não se aplica.

**Onde cada passada roda:** 0 a 3, 6 e 7 rodam nas duas rodadas (local e produção); **3b, 4 e 5 só existem em produção**. Divergência entre as duas rodadas é achado por si só — é justamente o que a rodada dupla existe para pegar.

---

## Passada 0 — Direção: o projeto ainda é o que se propôs a ser?

- Cada item do escopo validado (`docs/specs/`) existe e funciona? O que não existe é **falta**, não "ficou para depois" — a menos que tenha descido formalmente para `CONSTRAINTS.md` ou `docs/proximas-versoes.md`.
- **Vazamento ao contrário:** existe algo construído que não está no spec nem no `CONSTRAINTS.md`? Funcionalidade órfã é superfície de ataque e custo de manutenção que ninguém decidiu assumir.
- Nada que o `CONSTRAINTS.md` veta foi construído.
- Os limites declarados da Lei 7 ("atende até X") ainda batem com o que o sistema faz hoje.
- O veredito dos contrapontos continua verdadeiro: o problema que justificou o projeto ainda existe, e a solução ainda é essa.

## Passada 1 — Mercado: isso está no padrão de hoje?

Esta passada é **pesquisa, não opinião** — consultar fonte externa antes de julgar.

- **Os fluxos principais** (os três a cinco que o usuário vai repetir) comparados com o que produtos da mesma categoria fazem hoje: onde fica a ação principal, o que acontece depois de salvar, como se recupera acesso, como um erro de pagamento é comunicado. O que é padrão o usuário já espera, e a ausência é sentida como defeito mesmo quando nada quebrou.
- **O que o mercado trata como básico** e aqui não existe: busca, filtro, ordenação, paginação, confirmação antes de ação destrutiva, desfazer, feedback de carregamento, recibo ou comprovante, histórico.
- **Versões e suporte:** runtime e dependências principais em versão ainda suportada; nenhuma com vulnerabilidade conhecida; nada abandonado pelo autor.
- **Recomendações de segurança mudaram** desde que a decisão foi tomada? Conferir os parâmetros contra a fonte oficial de hoje, não contra o que foi escrito meses atrás (lições 10 e 13).
- **Higiene de plataforma que hoje é obrigatória:** HTTPS em tudo, redirecionamento de HTTP, HSTS, cookie com `Secure`, `HttpOnly` e `SameSite`, cabeçalhos de segurança, senha com KDF atual, segundo fator onde a skill `seguranca-san` o exige (área administrativa, conta que move dinheiro).

**Divergir do padrão de mercado é permitido — esquecer dele, não.** Divergência deliberada vira linha no `CONSTRAINTS.md` com o motivo. Divergência descoberta aqui e sem motivo é falta.

## Passada 2 — Frontend: é produto ou protótipo?

- **Tokens em um lugar só:** cor, tipografia, espaçamento, raio, sombra. Procurar valor mágico solto — hexadecimal repetido, `px` fixo espalhado, margem escolhida no olho. Cada um deles é uma divergência futura.
- **Nenhum componente repetido:** botão, campo, card, modal, cabeçalho, rodapé definidos uma vez e importados (lição 1). Teste: mudar um deles exige encostar em quantos arquivos?
- **Responsivo de verdade** em telas estreita, média e larga: sem rolagem horizontal, sem texto cortado, sem sobreposição, sem botão fora do alcance do polegar.
- **Todos os estados de cada tela**, não só o feliz: os seis de `construir/references/desenvolvimento-web.md`, item 10 (mais "desatualizado" em PWA), e em cada um o texto mais longo que o dado real produz. Tela que só tem o estado de sucesso está pela metade, e é a origem mais comum de "ficou meia-boca".
- **Formulários:** rótulo visível, foco visível, erro por campo e não só no topo, botão travado enquanto envia, e **nada do que foi digitado se perde quando dá erro**.
- **Acessibilidade básica:** contraste suficiente, navegação inteira por teclado, imagem com texto alternativo, hierarquia de títulos correta, área de toque adequada.
- **Hierarquia visual consistente:** peso, espaçamento e alinhamento seguindo a mesma régua na tela toda.
- **Percepção de velocidade:** imagem no tamanho certo e com dimensão declarada, fonte com alternativa, nada de salto de layout enquanto carrega.
- **Texto real:** nenhum *lorem ipsum*, nenhum "TODO", nenhum nome de teste, nenhum valor de exemplo, nenhuma tela escondida de desenvolvimento acessível por URL.
- **A lista "O que fecha"** de `construir/references/desenvolvimento-web.md` e da referência do tipo (`tipo-*.md`) continua verdadeira no que está no ar — a estação 5 fechou com ela na versão local; aqui cada evidência é refeita contra o domínio real (`curl` do `<head>`, cabeçalho de cache, CSP, páginas de erro, formulário de verdade).

## Passada 3 — Backend e dados

- **Caminho crítico coberto por teste**, e o teste roda no CI — verde **no commit que está em produção**, não em outro.
- Validação em toda fronteira de confiança; erro tratado; nunca rastro de pilha ou mensagem interna chegando ao usuário.
- **Identificador em rota pública é opaco**, nunca sequencial (lição 9).
- Operação cara é assíncrona (lição 12); parâmetro de primitiva de segurança explícito no código e conferido contra a recomendação atual (lições 10 e 13).
- **Caminho de dinheiro:** operação idempotente, retry não cobra duas vezes, transação onde precisa, valor conferido no servidor e nunca aceito do cliente; toda desistência silenciosa distingue "não configurado" de "não carregado" e registra qual foi (lição 20).
- **Estado que não pode se perder não mora só em memória** (lição 4). Morando, a conciliação periódica existe e está declarada.
- **Mecanismo de recuperação alcança todos os tipos** que precisa alcançar — conciliação, retry, reprocessamento (lição 3).
- Migrations aplicadas, nenhuma pendente, e o caminho de volta conhecido.
- Consultas que crescem com o uso têm índice; nenhuma consulta em laço.
- Log tem o suficiente para investigar e **nenhum segredo nem dado pessoal**.
- **Saída das verificações automáticas anexada**, não afirmada: auditoria de dependência sem achado alto ou crítico em aberto, varredura de segredo limpa **no histórico inteiro**, análise estática sem achado pendente. Sem a saída, o item é falta (skill `seguranca-san`).

## Passada 3b — Prontidão operacional (só em produção)

Os sete itens de `references/prontidao-operacional.md`, cada um com a evidência listada em "O que fecha a estação" daquele arquivo — a estação 6 já fechou com eles; aqui se confere que **continuam** verdadeiros no que está no ar (o backup ainda restaura, o alerta ainda chega). Item sem evidência é falta.

## Passada 4 — Serviços (só em produção)

Para cada serviço que sustenta o projeto, pelo painel real:

- **Repositório:** a branch principal é o commit que está no ar; verificação automática verde nesse commit; nada existindo só no disco de alguém.
- **Hospedagem:** último deploy sem erro; variáveis de ambiente todas presentes (nomes, nunca valores); plano e região corretos; o que acontece quando o processo reinicia.
- **DNS e CDN:** domínio e subdomínios resolvendo; certificado válido e renovando sozinho; redirecionamento entre raiz e `www`; cache não servindo versão antiga.
- **Banco:** backup ativo, limites do plano longe de estourar, conexões dentro do teto, política de acesso fechada.
- **Terceiros:** chave de produção (não de teste), webhook apontando para a URL de produção, limite de requisições conhecido, comportamento de falha entendido.
- **Comercial:** quem paga cada serviço, quando vence, e o que acontece com o projeto se um pagamento falhar.
- **Área administrativa:** havendo painel de administrador, a política do Cloudflare Access **existe agora** — conferida nesta passada, não na instalação (lição nº 15) —, cobre o caminho certo (e **não** as rotas de integração, sob pena de derrubar webhook), e a lista de quem entra tem só quem precisa: sem endereço de quem saiu, sem "qualquer um autenticado". Regras em `seguranca-san`.

Serviço que exige login e não está logado: abrir o navegador na página de login e pedir ao dono que entre; até lá o item é **não verificável daqui**.

## Passada 5 — Produção de verdade (só em produção)

- Percorrer os fluxos principais **no domínio real**, ponta a ponta, do começo ao fim, incluindo o caminho de dinheiro com um valor real pequeno.
- **Erro forçado:** derrubar ou atrasar o terceiro e ver o que o usuário recebe. Silêncio, tela branca ou giro infinito é falta.
- Primeira visita real: primeiro carregamento, despertar de serviço adormecido, cache vazio.
- **A porta dos fundos:** o endereço direto da hospedagem, fora do domínio, não entrega o que a barreira protege; e o painel administrativo em janela anônima mostra a barreira antes da aplicação.
- **Vendendo recorrência:** o ciclo completo de assinatura no ar — assinar, pausar, retomar, cancelar — e a cobrança seguinte chegando como deveria. Cobrança única testada não prova assinatura (lição nº 3).
- Dois navegadores diferentes e **um celular de verdade**, não só o emulador.
- Ler o log e os alertas **depois** de tudo isso: a varredura acabou de gerar tráfego, e o que apareceu ali é evidência.

## Passada 6 — Legal e documentação

- Termos de Uso e Política de Privacidade acessíveis na URL pública, e **dizendo o que o sistema realmente faz** — conferidos contra o inventário de dados.
- **As obrigações que exigem código existem e funcionam** (`legal/references/obrigacoes-brasil.md`): exportar dados; excluir conta de verdade; revogar consentimento; canal do titular publicado; botão de arrependimento com estorno; log de acesso com seis meses; razão social, CNPJ e endereço em destaque; nota fiscal por cobrança; procedimento de incidente no `RUNBOOK.md` com conta gov.br testada. Cada um verificado **executando**, não lendo.
- Inventário completo: cada dado coletado tem linha, inclusive os que entraram no fim.
- `CLAUDE.md` verdadeiro: cada arquivo citado existe, a classificação ainda bate, a lista de pendências está correta. `RUNBOOK.md` existe e foi testado por outra pessoa.
- `README.md` roda do zero seguindo o que está escrito; `.env.example` tem todas as chaves; `CONSTRAINTS.md` atualizado.
- **Nenhum documento afirmando o que não existe** (lição 2) e **nenhum ponteiro para arquivo ou skill que sumiu** (lição 7).

## Passada 7 — O vão entre as estações

O que não pertence a estação nenhuma e por isso costuma escapar:

- Decisão tomada em conversa e nunca escrita em documento algum.
- Pendência registrada numa estação e nunca fechada — inclusive as que foram "resolvidas" sem ninguém reverificar.
- Exceção aceita no `CONSTRAINTS.md` que virou permanente sem nunca ser revisitada.
- Comentário `limite:` no código sem dono nem caminho de saída.
- Ideia cortada durante a construção que nunca chegou ao `docs/proximas-versoes.md`.
- Arquivo criado por uma estação e abandonado pela seguinte; pasta vazia; configuração de algo que não existe mais.
- Teste marcado como pulado, comentado ou sempre verde.
- Dependência instalada e não usada; variável de ambiente declarada e não lida; rota que ninguém chama.

---

## O veredito

Quem roda a varredura decide, e a decisão tem **duas formas apenas**:

**Completo** — quando todo item tem veredito conforme, com evidência, **em cada rodada em que a passada dele roda** (as passadas 3b, 4 e 5 só têm rodada de produção). Só então o projeto está na versão 100% de produção.

**Falta** — a lista do que falta, ordenada por risco, cada item dizendo onde foi encontrado e o que precisa acontecer.

**"Completo com ressalvas" não existe.** Ressalva é falta. Item não verificado é falta. Item que depende de decisão do dono é falta até a decisão ser tomada e registrada.

**Faltando, o caminho é o ciclo de conformidade de sempre:** conserta → verifica → ainda faltando, para e avisa → espera a ordem → prossegue → verifica → conforme. E então a varredura **roda de novo na parte afetada e em todas as passadas que aquela mudança toca** — não o documento inteiro de novo, mas nunca só o item isolado, porque correção também quebra vizinho.

Não existe estado final fora de conformidade. Ou o projeto está conforme, ou a falta está registrada como exceção aceita no `CONSTRAINTS.md`, com o motivo e assumida pelo dono.
