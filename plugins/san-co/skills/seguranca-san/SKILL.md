---
name: seguranca-san
description: Checagem de segurança para o que a San & Co. constrói — pagamento, cofre de senhas e documentos, área administrativa e dado de cliente de terceiro. Use ao mexer em cobrança, checkout, autenticação, senha, documento, integração com Asaas, ou antes de expor qualquer coisa à internet.
---

# Checagem de segurança — San & Co.

Autoridade sobre segurança no ecossistema (Lei 4). **Alcance:** vale integralmente para todo projeto com usuário além de você; projeto sem usuário externo cumpre só os itens de credencial e segredo, com a dispensa do resto escrita no `CONSTRAINTS.md`. Nada aqui se simplifica em nome de brevidade.

## Sempre, em qualquer projeto

- Segredos e senha de usuário: a **Lei 3** vale integralmente, e o detalhe de KDF, parâmetro, memória e comparação segura está em `references/senha-e-kdf.md`.
- Validação de entrada em toda fronteira de confiança — formulário, endpoint, upload, parâmetro de URL. Nunca confiar em dado vindo do cliente. **Teto de tamanho por campo mora no validador**, não em cada controlador: validar formato não valida tamanho (lição nº 24).
- Autenticação e autorização checadas separadamente no servidor, em toda rota sensível. Esconder o botão não é controle de acesso. **Segundo fator** na área administrativa e em conta que move dinheiro; nas demais, oferecido quando o porte justificar.
- Log sem senha, token, cartão ou documento em texto puro.
- Rate limiting em login e recuperação de senha — e em **toda rota pública que faz trabalho** (toca banco, disco ou rede), mesmo devolvendo só um `ok`; a lista de rotas limitadas se confere contra a lista de rotas montadas (lição nº 23).
- **Propriedade de segurança que depende de variável de ambiente é propriedade não garantida.** Dando para fechar em código, fecha em código; tratadores de erro e de 404 são os últimos registrados (lição nº 28).
- As verificações que a leitura não alcança — dependência vulnerável, segredo no histórico, configuração efetiva de produção — rodam por ferramenta, no CI, desde a estação 3. Comandos, workflow para colar e onde cada uma entra: **`references/verificacoes-automaticas.md`**.

## Área administrativa: Cloudflare Access na frente, sempre

**Porta de operação tem entrada própria e proteção própria** — nunca escondida dentro de um fluxo de produto, dependendo de uma tela renderizar ou de um registro falso existir (lição nº 30).

Todo projeto com login de administrador põe a entrada administrativa atrás do Cloudflare Access, **além** do login próprio da aplicação. São duas camadas porque falham por motivos diferentes: rota esquecida ou sessão com problema não derrubam o Access; Access mal configurado ainda encontra o login atrás. Access nunca substitui o login do projeto. A decisão de consumi-lo é da estação 2 (skill `classificar`); a política está aplicada **antes do deploy** que fecha a estação 5; a verificação é da estação 6 e de toda varredura final.

**As quatro armadilhas que anulam o Access:**

1. **Origem alcançável por fora.** O Access só protege o que passa pelo Cloudflare; o endereço direto da hospedagem respondendo é a barreira inteira contornada. Fechar a origem — túnel, regra que só aceite tráfego do Cloudflare, ou segredo exigido na origem — é parte da tarefa. Testar pelo endereço direto faz parte da verificação.
2. **Política no domínio inteiro.** Derruba o que é máquina — o webhook de pagamento passa a receber a tela de login. Política por caminho: área administrativa dentro, rota pública e de integração fora; máquina usa token de serviço.
3. **A política cai sozinha e ninguém percebe.** É configuração externa ao repositório: DNS repontado, proxy desligado, serviço recriado a derrubam sem tocar em código — e isso não gera erro, log nem teste vermelho. A verificação em janela anônima é **recorrente**, e caindo, achar o que derrubou **antes** de recriar (lição nº 15).
4. **Lista de quem entra frouxa.** Regra por pessoa, só quem precisa; revisar em toda varredura final.

Não sendo possível aplicar o Access, é limite declarado no `CONSTRAINTS.md` com a compensação escrita — segundo fator obrigatório, restrição por IP, rate limiting agressivo na rota administrativa.

## Pagamento e cobrança (Checkout, Asaas)

Para integrar um projeto ao San Checkout, usar a skill `checkout`. As regras abaixo valem para qualquer coisa que toque dinheiro.

- **Desistência silenciosa distingue "não configurado" de "não carregado"**, e registra qual foi — saída muda por caminho de erro é indistinguível de sucesso (lição nº 20).
- Nunca armazenar número de cartão ou CVV; apenas o token do provedor. Cartão salvo pede reconfirmação de CVV antes de pagar.
- Nunca confiar em preço ou valor vindo pela URL ou pelo cliente — o valor real é puxado da API do projeto pelo identificador do pedido.
- `walletId` de contratante e endereço da API são cadastrados manualmente no banco, nunca por endpoint público — risco direto de desvio de dinheiro.
- Cada projeto contratante tem sua própria chave; chave compartilhada faz revogar um derrubar todos.
- Webhook valida a origem antes de aceitar mudança de estado de pagamento.
- Cancelamento e estorno só pelo projeto, nunca pelo pagador diretamente.

## Cofre de senhas e documentos pessoais

- Zero-knowledge: conteúdo cifrado no dispositivo antes de qualquer sincronização; a chave nunca sai dele. Nem o provedor de nuvem lê.
- Senha mestra nunca armazenada — usada em memória para derivar a chave e descartada. KDF pela Lei 3, com o desvio do navegador descrito em `references/senha-e-kdf.md`.
- Nenhum dado do cofre em texto puro fora da sessão desbloqueada; documento vai para a nuvem já cifrado — Drive pessoal não cifra do lado do cliente, o app cifra antes do upload.
- Auto-lock por inatividade; limpeza da área de transferência depois de copiar senha.
- Kit de recuperação offline gerado na configuração inicial e guardado fisicamente fora do dispositivo. Sem ele, perder a senha mestra é perder o cofre — é o design funcionando.
- Restauração do backup testada logo após configurar.

## Dado de cliente de terceiro

- Banco isolado por projeto, sem exceção.
- Coletar o mínimo — dado que não existe não vaza.
- Desde o desenho, como esse dado sairia do sistema se o cliente pedisse ou se o projeto fosse encerrado (skill `legal`).

## Teste no navegador — checar o que roda, não o que está escrito

Ler o código encontra o erro que está lá; abrir a página encontra o que só aparece rodando. Com o navegador integrado, na página no ar ou rodando local:

- **Console e rede:** algum segredo, token ou chave aparece no que o navegador recebe? Chave que chega ao cliente é pública, mesmo que o nome diga o contrário.
- **Controle de acesso pela URL:** abrir direto a rota administrativa ou a de outro usuário. Se abrir, a proteção estava só no botão.
- **Formulário sem o cliente:** enviar valor que o front-end recusaria — preço negativo, campo obrigatório vazio, texto onde espera número. O servidor recusa sozinho.
- **Sessão:** sair e usar a aba antiga. Nada sensível continua acessível.
- **Erro exposto:** forçar um erro. Rastro de pilha, nome de tabela ou versão de biblioteca na tela é informação para quem ataca.
- **Pagamento:** alterar o valor no navegador e confirmar que a cobrança é recusada.

Em **ciclos**, como a skill `revisar` define: achou, corrigiu, testa tudo de novo do começo — a correção pode abrir outra porta. Nunca omitir achado para fechar o ciclo.

## Pergunta final, antes de expor à internet

Se isso vazasse hoje, qual é o pior dado exposto, e quem seria prejudicado além de você?
