# App web com conta, painel e assinatura — o que este tipo tem além da referência-mãe

Referência por tipo da estação 5, para o produto em que a pessoa entra, vê dado seu e paga por mês: o painel do San Checkout, um app financeiro, qualquer área de cliente. O comum a qualquer site é apontado por número em `desenvolvimento-web.md`. Segurança é a `seguranca-san`; cobrança, a `checkout`; direito do titular e arrependimento, a `legal`.

**Regra que atravessa tudo:** a evidência que fecha é uma conta nova, num celular real, indo do cadastro à exclusão sem que ninguém do lado de cá intervenha.

---

## 1. Conta de ponta a ponta

**Por que é esquecido:** o login é a primeira tela e a última terminada — recuperar acesso, trocar e-mail e excluir conta ficam para "depois".

**O que existe:** cadastro com e-mail e senha, nada mais; o resto vem na primeira sessão (item 3). `type="email"`, `autocomplete="username"`, `new-password` e `current-password`, botão "mostrar senha", senha pedida uma vez (web.dev). Mínimo de 8 caracteres sem regra de composição; senha vazada (HaveIBeenPwned) é do plano Pro. **Padrão San & Co.:** senha como método principal e "entrar por link" na mesma tela (`signInWithOtp` com `shouldCreateUser: false`); passkey vai para `docs/proximas-versoes.md` — no Supabase ainda é experimental — e, quando entrar, é oferecida depois de um login com senha, nunca no cadastro (web.dev). Confirmação de e-mail vem ligada; o link vale uma hora e só pode ser repedido após 60 segundos — a tela diz isso. O SMTP embutido manda dois e-mails por hora: SMTP próprio antes do primeiro usuário (mãe, item 11). Turnstile via `captchaToken` no cadastro, login e recuperação (mãe, item 9). Recuperação: `resetPasswordForEmail` com `redirectTo`, resposta idêntica exista a conta ou não; depois, a pessoa volta para onde estava — 34% dos sites erram esse destino (Baymard). Troca de e-mail com "Secure email change": link nos dois endereços, os dois clicados, explicado antes. Exclusão é botão na área de conta, pede a senha e roda no servidor com `auth.admin.deleteUser`, que derruba `auth.sessions` e, com `profiles` em `on delete cascade`, o dado do produto; o que fica é regra da `legal`.

**Como conferir:** os seis fluxos numa conta descartável no celular, cada e-mail aberto; após excluir, a tabela não tem a linha.

**Exagero:** login social antes de cliente pedir; símbolo obrigatório na senha; telefone e CPF no cadastro.

## 2. Sessão

**Por que é esquecido:** o Supabase renova a sessão sozinho; ninguém decide quanto ela dura nem o que acontece com o formulário aberto quando acaba.

**O que existe:** JWT de uma hora (o padrão, que a documentação manda manter) e refresh token de uso único; a sessão persiste enquanto renovada, então "lembrar de mim" é o padrão e a caixa não existe. Limite de duração e expiração por inatividade são do plano Pro; sem Pro, a sessão longa vai para o `CONSTRAINTS.md`. "Sair de todos os dispositivos" é `signOut({ scope: 'global' })`, o padrão do JS; "sair só aqui" é `local`. O access token revogado vale até o `exp` — por isso rota que lê ou move dado sensível confere a sessão no servidor a cada requisição, não só o JWT; é o teste "sair e usar a aba antiga" da `seguranca-san`, e a aba antiga não pode continuar mostrando nada sensível. Sessão expirada no meio de um formulário: o digitado fica, um `<dialog>` de reautenticação abre por cima e o envio segue — a WCAG 2.2.6 exige avisar sobre inatividade que perde dado, a menos que ele seja preservado por mais de 20 horas.

**Como conferir:** sair "de todos" num navegador e o outro cair na renovação seguinte; expirar a sessão com um formulário preenchido sem perder nada.

**Exagero:** lista de sessões com dispositivo e cidade; expiração em minutos fora de área de dinheiro.

## 3. Primeira sessão

**Por que é esquecido:** quem construiu nunca viu a conta vazia, e o tour de balões parece resolver.

**O que existe:** nada de tutorial — a NN/g mediu que tour não é lembrado nem melhora a tarefa; ajuda no contexto vence. A primeira tela pede só o que falta (nome, empresa) e leva à ação central; cada tela vazia segue as três regras da NN/g: diz o que aconteceu ("Nenhum cliente ainda"), ensina em uma frase, oferece o botão da primeira ação. Checklist de três a cinco passos no painel, riscado conforme feito, some ao terminar. Dado de exemplo só como opção explícita, nunca pré-carregado — exemplo que parece real vira dado falso (mãe, item 10).

**Como conferir:** conta recém-criada chega ao primeiro registro sem ninguém explicar; cada tela vazia aberta.

**Exagero:** tour com overlay; vídeo de boas-vindas; sequência de e-mails.

## 4. Navegação do painel

**Por que é esquecido:** cada funcionalidade nova ganha um item de menu; em seis meses são catorze.

**O que existe:** barra lateral com cinco ou mais seções, menu no topo abaixo disso — a NN/g mede 80% do olhar na metade esquerda e recomenda as duas convenções. Até sete itens e breadcrumb a partir de três níveis (mãe, item 1), agrupados por tarefa, não por tabela. Conta, cobrança e sair no menu do avatar, canto superior direito, sempre. Busca global só quando há vários tipos de registro procurados pelo nome; antes, o filtro da lista (item 5).

**Como conferir:** a 360 px, conta, cobrança e sair em dois toques; contar os itens.

**Exagero:** menu só de ícones; favoritos; atalhos de teclado.

## 5. Tabelas e listas

**Por que é esquecido:** com vinte linhas de teste tudo cabe; com dois mil do cliente, não.

**O que existe**, pelas quatro tarefas da NN/g: primeira coluna é o identificador legível, não o id; colunas por importância; cabeçalho fixo; ordenação por coluna; filtro visível; edição de linha em painel lateral, não modal, para as outras linhas seguirem à vista; seleção em lote com "selecionar todos" e ações acima da tabela. Ordenação, filtro e página na URL (`?status=ativo&ordem=-criado_em&pagina=2`): recarregar, compartilhar e voltar preservam o estado. Página de 20 com "ver tudo" até uns cem itens; scroll infinito não, porque a tarefa é achar e comparar (NN/g). CSV com `;` e BOM UTF-8, senão o Excel em português junta tudo numa coluna e troca os acentos; a exportação respeita o filtro. No celular, primeira coluna fixa e coluna cortada na borda como sinal de rolagem (NN/g). Os estados: mãe, item 10.

**Como conferir:** conta com 500 registros gerados; URL com filtro colada noutra aba; CSV no Excel; tabela a 360 px.

**Exagero:** colunas configuráveis; edição em célula; XLSX.

## 6. Formulários de criar e editar

**Por que é esquecido:** o "salvar" funciona e ninguém decide o clique errado em "excluir" nem o autosave que salvou metade.

**O que existe:** criar e editar no mesmo componente, em tela ou painel lateral; modal só até três campos. "Salvar" explícito é o padrão; autosave só em formulário longo em que o botão sai da dobra, com estado escrito ("Salvando…", "Salvo às 14:32") e nunca em senha, e-mail, cobrança ou permissão (GitLab). Destruição: preferir desfazer — a linha some, "Cliente excluído · Desfazer" fica alguns segundos, a exclusão roda depois; confirmação só para o que não tem volta, com botões que dizem o que fazem ("Excluir cliente" / "Manter"), porque confirmação em tudo vira clique automático (NN/g). Validação: mãe, item 9.

**Como conferir:** salvar com rede derrubada sem perder nada; desfazer uma exclusão.

**Exagero:** histórico de versões; rascunho automático em todo formulário.

## 7. Papéis e convite

**Por que é esquecido:** o primeiro cliente é uma pessoa só; o segundo tem sócio e contadora.

**O que existe:** três papéis: dono (cobrança, excluir a organização, transferir posse), administrador (convidar, remover, tudo do produto), membro (usa). A tela esconde; o servidor decide (`seguranca-san`), por RLS lendo `app_metadata` ou a tabela de membros (item 12). Papel no JWT entra por Custom Access Token Hook e só muda quando o token é reemitido — até uma hora; remoção imediata é apagar a linha de membro que a política consulta. Convite: linha em `convites` com token opaco e validade de sete dias, e-mail com um botão (mãe, item 11); quem não tem conta recebe `auth.admin.inviteUserByEmail` do servidor — chave de serviço, nunca no navegador — e cria a senha ao aceitar.

**Como conferir:** membro na URL de cobrança recebe "sem permissão"; convite aceito de um celular sem conta; convite vencido recusado.

**Exagero:** papéis personalizados; permissão por registro; SSO.

## 8. Conta e cobrança

**Por que é esquecido:** cobrança nasce como link de pagamento e a tela "meu plano" nunca é feita; o cliente descobre o valor no extrato.

**O que existe:** tela "Plano e cobrança" com o que o portal da Stripe entrega: plano e valor, próximo vencimento, forma de pagamento (cartão ou Pix, sem dado do cartão — `checkout`), histórico com status e a nota de cada cobrança (obrigação da `legal`), trocar plano, trocar cartão, cancelar. No San Checkout, trocar cartão segue a regra do `checkout` (não existe troca; é renovação) e o projeto decide o cancelamento. Cancelar é botão na mesma tela, efeito no fim do período pago, confirmação por e-mail, sem ligação nem chat; arrependimento em sete dias é da `legal`. Cobrança recusada: aviso fixo no topo do painel com o link de renovação e e-mail no mesmo dia (item 9).

**Como conferir:** assinar, ver a nota, trocar cartão, cancelar e reativar numa conta de teste; de novo na Passada 5.

**Exagero:** cupom; upgrade proporcional no meio do mês; portal de cobrança fora do painel.

## 9. Notificações

**Por que é esquecido:** cada evento vira e-mail, e em um mês o cliente manda o remetente para a lixeira.

**O que existe:** e-mail só para o que exige ação com a pessoa fora do app ou o que a lei e o Checkout exigem: confirmação da contratação com o contrato e a nota de cada cobrança (`legal`; `checkout`, "responsabilidade do projeto"), cobrança recusada, convite, e segurança (senha ou e-mail alterado, com "não fui eu"). O resto é in-app: sino com contador e lista com data absoluta (mãe, item 7). O que exige ação é intrusivo; o passivo fica no canto; erro crítico nunca em toast que some — a NN/g viu usuário esperar cinco minutos por um aviso que sumiu em cinco segundos. Preferências: um interruptor por categoria, com segurança e cobrança sempre ligadas.

**Como conferir:** disparar cada evento e ver onde chega; desligar uma categoria, a de cobrança continua.

**Exagero:** digest semanal; push; SMS; WhatsApp.

## 10. Painel do dono

**Por que é esquecido:** o dono opera pelo Studio e uma linha editada à mão apaga uma assinatura.

**O que existe:** rota `/admin` própria, atrás do Cloudflare Access e com segundo fator (`seguranca-san`); no Supabase, o segundo fator vira política restritiva exigindo `aal2` no JWT das tabelas administrativas. O dono vê: usuários (e-mail, papel, último login), assinaturas com estado e última cobrança (as duas metades da `checkout`), pendências de conciliação, link para os erros (prontidão 2). Impersonar: somente leitura, faixa fixa "Vendo como fulano", cada requisição na trilha com os dois ids (item 11).

**Como conferir:** `/admin` em janela anônima mostra o Access; impersonação tentando salvar é recusada e fica na trilha.

**Exagero:** gráfico em tempo real; edição de qualquer tabela pelo painel.

## 11. Trilha de auditoria

**Por que é esquecido:** "quem mudou o preço?" só é perguntado depois.

**O que existe:** tabela `auditoria` só de inserção — sem política de `update` nem `delete`, nem para o dono — com os campos do EnterpriseReady: `user_id` (e o id do administrador na impersonação), `org_id`, `evento` no padrão `objeto.acao` (`cliente.excluido`), `tabela`, `registro_id`, antes e depois em JSONB só dos campos que mudaram, IP, `criado_em` em UTC. Entra: criar, editar e excluir registro de negócio, papel, convite, login, cobrança e tudo do administrador; não entra: leitura, senha, token, cartão. O dono vê a trilha da sua organização, filtrável e exportável (item 5); retenção de um ano para eventos de negócio; as linhas de `login` são o log de acesso do Marco Civil (`legal`), seguem os seis meses dele e são apagadas depois.

**Como conferir:** editar um registro e achar a linha com antes e depois; `delete from auditoria` como dono devolve zero linhas.

**Exagero:** hash encadeado; SIEM; trilha de leitura.

## 12. Multi-inquilino no Supabase

**Por que é esquecido:** a política protege o `select` do navegador, e o primeiro endpoint com a chave de serviço devolve a organização inteira. O resto é Lei 6.

**O que existe:** `org_id not null` em toda tabela de negócio, com índice — coluna de política sem índice vira varredura sequencial. Política de leitura e escrita (`using` e `with check`) por pertencimento, com o helper embrulhado em `select` para rodar uma vez por consulta: `org_id in (select org_id from membros where user_id = (select auth.uid()))`, ou o claim de `app_metadata` do item 7 — nunca `user_metadata`, que o usuário edita. O erro clássico: `service_role` ignora RLS, e o `.eq('org_id', …)` esquecido numa rota devolve tudo. Regra: o servidor repassa o JWT do usuário em tudo que é em nome de alguém; `service_role` só nas rotas do item 10. Teste de isolamento no CI: duas organizações, um usuário em cada, `set local role authenticated; set local request.jwt.claim.sub = '<id>'`, e asserções de que A lê só o seu, não insere com `org_id` de B nem atualiza linha de B.

**Como conferir:** o teste verde no CI do commit em produção; Security Advisor sem tabela sem RLS; `grep -r service_role src/` com cada ocorrência numa rota do item 10.

**Exagero:** schema por inquilino; banco por cliente; chave de criptografia por organização.

---

## O que fecha este tipo

Os doze itens com evidência, além dos catorze da mãe: a conta descartável do cadastro à exclusão; o logout global e o formulário que sobrevive à sessão; o primeiro registro sem ajuda; conta, cobrança e sair em dois toques; a URL com filtro e o CSV no Excel; o desfazer; o membro barrado e o convite aceito; assinar, nota, cartão e cancelar; cada notificação no lugar certo; `/admin` atrás do Access e a impersonação na trilha; a auditoria com antes e depois; o teste de isolamento verde no CI. As Passadas 2 e 5 reconferem no ar.

Item sem evidência é item aberto, e estação com item aberto não fecha.

Fontes consultadas, para reconferir quando algo parecer velho: docs do Supabase Auth (sessões, senhas, passwordless, passkeys, sign-out, rate limits, SMTP, captcha, MFA, custom claims, RLS, checklist de produção); web.dev (sign-in form, passkeys); Nielsen Norman Group (onboarding, empty states, data tables, mobile tables, pagination, infinite scrolling, confirmation dialogs, notifications, horizontal attention); Baymard (sign-in flows); GitLab Pajamas (saving and feedback); Stripe (customer portal); EnterpriseReady (audit log); WCAG 2.2.6.
