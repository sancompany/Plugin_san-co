# Lições aprendidas — San & Co.

Erros já cometidos em projetos da San & Co., com a regra que cada um gerou. **Ler antes de construir algo novo e antes de investigar erro novo.** Projeto novo herda estas lições sem precisar repetir o erro para aprendê-las.

Este catálogo é do **ecossistema**, não de um projeto. Erro que só faz sentido dentro de um código específico vive no `docs/erros/` daquele projeto. O teste para decidir: *outro projeto, com outra stack, cometeria esse mesmo erro?* Sim → aqui. Não → lá.

**Os números são estáveis e nunca são reaproveitados** — o plugin inteiro cita lições por número. Lição nova entra no fim.

## Onde procurar

- **Duplicação e estrutura:** 1, 5, 6, 8, 24, 25
- **Frontend:** 1, 16, 18
- **Documento mentindo ou envelhecido:** 2, 7, 17
- **Caminho de dinheiro:** 3, 4, 9, 18, 19, 20
- **Segurança e parâmetro:** 10, 11, 12, 13, 26, 28, 29
- **Acesso e barreira:** 15, 30
- **Capacidade e carga:** 21, 23
- **Dados e migração:** 22
- **Plataforma e configuração:** 17, 26, 27, 33
- **Processo, esteira e verificação:** 14, 31, 32

---

# As primeiras quinze — em ordem de descoberta

## 1. Elemento visual duplicado arquivo por arquivo

**Sintoma:** o código cresceu muito mais que o esperado, e alterar um botão exigia encostar em várias telas.
**Causa raiz:** cada arquivo definiu o próprio botão em vez de importar um só. A regra "duplique antes de abstrair" foi aplicada a elemento visual, quando ela vale para lógica que pode divergir.
**Regra que evita:** componente, token (cor, fonte, espaçamento), mensagem repetida e constante de negócio nascem em um lugar só, desde o primeiro uso. Teste: se isso mudar, quantos arquivos preciso encostar? Mais de um = já está dessincronizando.
**Onde vive:** skill `construir`, seção "Elemento repetido"; Lei 5.

## 2. Documento afirmando algo que ainda não existe

**Sintoma:** o `CLAUDE.md` dizia que o CI existia e rodava. Não existia — o `ci.yml` tinha sido recusado pela ferramenta.
**Causa raiz:** o documento foi escrito descrevendo a intenção, não o estado verificado. A reverificação pegou; sem ela, teria passado.
**Regra que evita:** nunca escrever que algo existe antes de existir. O que ainda não existe entra como pendência, com o nome de pendência. Mentira na porta de entrada é pior que ausência, porque o próximo agente confia e não verifica.
**Onde vive:** skill `leis`, ciclo de conformidade.

## 3. Conciliação que não alcança um dos tipos de cobrança

**Sintoma:** a rota de conciliação consultava por `pedidoId`, mas cobrança de assinatura é gravada por `planoId` — recorrência ficava sem rede de segurança nenhuma.
**Causa raiz:** a conciliação foi desenhada para o caso principal e o segundo tipo entrou depois sem revisitar a cobertura.
**Regra que evita:** ao criar mecanismo de recuperação (conciliação, retry, reprocessamento), listar **todos** os tipos que ele precisa alcançar antes de considerá-lo pronto. Cobertura parcial em mecanismo de segurança é pior que ausência declarada, porque gera confiança falsa.
**Onde vive:** skill `checkout`, conciliação.

## 4. Fila de reenvio em memória num serviço que reinicia

**Sintoma:** webhook de pagamento confirmado se perde, e o pagamento segue válido — some só o aviso.
**Causa raiz:** a fila de retry vive na memória do processo. Reinício por deploy, queda ou despertar de hospedagem que dorme apaga o que estava na fila.
**Regra que evita:** estado que não pode ser perdido não mora só em memória. Não dando para persistir agora, a conciliação periódica deixa de ser opcional e vira parte do desenho — declarada, não subentendida.
**Onde vive:** skill `checkout`, "Conciliação diária não é opcional".

## 5. Escopo negativo escrito fora do repositório

**Sintoma:** o que o projeto deliberadamente não faz estava documentado, bem documentado — e invisível para quem clonava o repositório.
**Causa raiz:** confundiu-se "está escrito" com "está onde precisa ser lido". A função do escopo negativo é impedir que alguém construa o que foi vetado, e esse alguém só enxerga o repositório.
**Regra que evita:** `CONSTRAINTS.md` e spec vivem dentro do repositório. Documento de decisão que mora só em conversa ou em ferramenta externa não existe para quem chega depois — cada vez mais, quem chega depois é um agente de IA.
**Onde vive:** Lei 10, "Tudo isso vive no repositório".

## 6. Nomes diferentes para artefatos diferentes, sem dizer qual é qual

**Sintoma:** três menções — "escopo negativo", `CONSTRAINTS.md`, "escopo validado em arquivo próprio" — sem relação declarada entre elas. Dava para criar três arquivos para duas coisas, ou nenhum por não saber qual era o certo.
**Causa raiz:** cada regra foi escrita isoladamente, e nenhuma disse como se relacionava com as outras.
**Regra que evita:** ao nomear um artefato, dizer o que ele guarda e como se distingue dos vizinhos. Mapa de pergunta → documento resolve melhor que definição: "posso construir isso?" → `CONSTRAINTS.md`; "por que existe?" → spec.
**Onde vive:** Lei 1.

## 7. Ponteiro para documento ou skill que deixou de existir

**Sintoma:** uma regra mandava consultar uma skill para entender um arquivo obrigatório. A skill tinha sido desativada; o arquivo continuava exigido e a explicação sumira.
**Causa raiz:** referência cruzada criada quando o alvo existia, nunca reverificada depois que o ambiente mudou.
**Regra que evita:** referência a arquivo, skill ou seção numerada de documento externo envelhece. Preferir apontar por função ("o documento canônico na raiz do repositório") a apontar por número de seção ou caminho de disco, e revalidar as referências ao revisar.
**Onde vive:** skill `revisar`, checklist "Antes de aprovar"; `varredura-final.md`, Passada 6.

## 8. Regra de segurança escrita em dois lugares

**Sintoma:** a mesma checagem de segurança aparecia em duas skills, com redações diferentes.
**Causa raiz:** conveniência — parecia útil o leitor encontrar a regra sem abrir outro documento.
**Regra que evita:** cada assunto tem exatamente uma autoridade; as demais apontam para ela. Regra escrita em dois lugares diverge no primeiro dia em que só um dos dois é atualizado, e aí ninguém sabe qual vale.
**Onde vive:** Lei 4 delega para `seguranca-san`; README do plugin.

## 9. Id sequencial em rota pública

**Sintoma:** rota que o comprador precisa acessar antes de qualquer login, recebendo o id da tabela.
**Causa raiz:** o id do banco foi reaproveitado como identificador externo.
**Regra que evita:** identificador que trafega em URL pública é opaco e imprevisível — UUID, hash ou token. Id sequencial permite varrer `1, 2, 3` e ler o dado de todos os registros. Não precisa trocar o banco: uma coluna a mais com token opaco resolve.
**Onde vive:** skill `checkout`, regras inegociáveis.

## 10. Parâmetro padrão de primitiva de segurança abaixo do recomendado

**Sintoma:** nenhum. O código roda, o hash é gerado, nada falha — e a proteção é mais fraca do que se acredita.
**Causa raiz:** o valor padrão de um KDF, cifra ou gerador foi escrito quando a recomendação era outra, e bibliotecas mantêm o default por compatibilidade. O caso concreto: `crypto.scrypt` do Node usa N=2^14, enquanto o mínimo recomendado hoje é N=2^17 — oito vezes menos trabalho que o necessário.
**Regra que evita:** ao usar primitiva de segurança, **nunca aceitar o parâmetro padrão sem conferir contra a recomendação atual**, e deixar o valor escrito explicitamente no código, não implícito. Falha silenciosa não aparece em teste nem em revisão de comportamento — só em auditoria de parâmetro.
**Onde vive:** Lei 3.

## 11. Trocar dependência por implementação própria sem contar o custo

**Sintoma:** remover uma biblioteca para eliminar risco de supply-chain, e herdar responsabilidades que ela cumpria em silêncio.
**Causa raiz:** o ganho (menos dependência) é visível e o custo (o que a biblioteca fazia por você) não. No caso do hash de senha: geração de salt por senha, armazenamento de salt e parâmetros junto do hash, e comparação em tempo constante — tudo embutido no formato do Argon2/bcrypt, tudo seu se usar o KDF cru.
**Regra que evita:** antes de remover dependência, listar o que ela fazia além da função óbvia. Menos dependência é bom; formato de segurança feito à mão para economizar uma dependência costuma ser pior que a dependência.
**Onde vive:** Lei 3; skill `construir`, degrau 3 da escada (o inverso do degrau: remover dependência também tem custo).

## 12. Operação cara feita de forma síncrona num servidor

**Sintoma:** requisições sem relação nenhuma com a operação pesada ficam lentas ou dão timeout, de forma intermitente e difícil de reproduzir.
**Causa raiz:** uma chamada síncrona e cara segurou o event loop. O caso concreto: `scryptSync` com custo alto bloqueia por quase um segundo, e em Node isso para **tudo** que estava em voo — inclusive confirmação de pagamento que não tem relação com o login que disparou o hash.
**Regra que evita:** em caminho servido por requisição, toda operação cara é assíncrona. A versão `Sync` de qualquer API existe para script e inicialização, não para servidor. Suspeitar sempre que lentidão aparecer em endpoints que não deveriam ter relação entre si.
**Onde vive:** Lei 3.

## 13. Limite padrão da plataforma barrando o parâmetro seguro

**Sintoma:** a configuração recomendada pela norma lança exceção em execução.
**Causa raiz:** a plataforma tem um teto próprio, pensado para outro uso. O caso concreto: `crypto.scrypt` do Node tem `maxmem` padrão de 32 MiB, e o parâmetro mínimo recomendado (N=2^17, r=8) precisa de ~128 MiB — falha até `maxmem` ser aumentado explicitamente.
**Regra que evita:** falha assim é armadilha dupla — a tentação é baixar o parâmetro de segurança até "funcionar", e aí a proteção cai sem aviso. Ao ver uma recomendação de segurança falhar por limite de plataforma, **aumentar o limite, nunca reduzir a segurança**, e registrar a decisão. Vale conferir também o custo real: a 2^17 são ~128 MiB **por hash simultâneo**, o que é limite de capacidade e entra no `CONSTRAINTS.md`.
**Onde vive:** Lei 3; Lei 7.

## 14. Estação aberta antes de a anterior fechar, verificando versão desatualizada

**Sintoma:** a sessão passou a verificar prontidão e segurança de um sistema que ainda estava em construção. O relatório saiu limpo — sobre uma versão que não era a atual: o deploy não tinha sido feito, a segunda leva de migrations não tinha rodado, e o código nem tinha subido para o repositório.
**Causa raiz:** trabalho parecido com a estação seguinte foi confundido com a estação seguinte. Ninguém declarou o fechamento da anterior, e a abertura da nova não exigiu prova de nada.
**Regra que evita:** antes da primeira ação de qualquer estação, declarar qual abre, **o que fechou a anterior com evidência verificável** (commit, URL que responde, execução de CI verde, migration aplicada), e o que esta vai olhar. Nas estações que examinam o que está no ar, conferir antes que o commit servido em produção é o da branch principal — diferindo, a estação não abre. Item do fechamento que depende de ação do dono mantém a estação aberta; não se adianta a próxima enquanto isso.
**Onde vive:** skill `leis`, "Fecha antes de avançar".


## 15. Proteção que foi configurada e deixou de valer sozinha

**Sintoma:** a barreira de acesso na frente da área administrativa simplesmente não estava mais lá — confirmado de fora, em produção, com o serviço no ar. Ninguém tinha ido no painel desativar.

**Causa raiz:** proteção de acesso não é estado do projeto, é estado de uma configuração externa — e configuração externa cai por motivos que não passam pelo repositório: DNS repontado, proxy desligado, política editada, domínio trocado, serviço recriado. O projeto continua exatamente igual enquanto a proteção some.

**Regra que evita:** o que protege **é verificado de fora, periodicamente, e não uma vez na instalação**. Item da estação 6 e da varredura final: abrir a URL protegida em janela anônima e confirmar que a barreira responde antes da aplicação. E, tendo caído, **descobrir o que a derrubou antes de recriar** — proteção que cai sozinha uma vez cai de novo, e recriar sem achar a causa é tratar sintoma.

**Onde vive:** skill `seguranca-san`, "Área administrativa"; `varredura-final.md`, Passadas 4 e 5.



---

# Frente e plataforma

## 16. Reset agressivo de CSS apaga comportamento nativo

**Sintoma:** `<dialog>` renderizando sem o estilo que o torna um diálogo; e, na mesma leva, o anel de foco sumido de toda a interface.
**Causa raiz:** reset universal apaga o estilo padrão dos elementos nativos que dependem dele, e `outline: none` foi escrito sem substituto. Nenhum dos dois aparece na leitura do código — o que falta não está escrito em lugar nenhum.
**Regra que evita:** depois de um reset, conferir **com a tela renderizada e navegando por teclado**, não lendo o CSS. `outline: none` só entra acompanhado do substituto, na mesma edição; querendo tirar o anel só do clique, o seletor é `:focus-visible`, não `:focus`.
**Onde vive:** skill `construir`, "Elemento repetido" e verificação; `varredura-final.md`, Passada 2.

## 17. Configuração declarada não é configuração aplicada

**Sintoma:** duas vezes na mesma semana. O `noindex` estava no arquivo de configuração e não na resposta da web; o HTML novo era servido com o script velho, porque a política de cache era outra.
**Causa raiz:** confundiu-se o que o arquivo pede com o que a plataforma faz. Host estático normaliza caminho, aplica cache por padrão de rota e pode aceitar a regra e ignorá-la em silêncio.
**Regra que evita:** **verificar pelo caminho público, nunca pelo arquivo de configuração.** Uma requisição que mostre os cabeçalhos de resposta resolve em segundos o que dedução não resolve — e é ela, não o arquivo, que diz o que está valendo. Regra de borda casa o caminho que o servidor **entrega**, não o nome do arquivo no repositório.
**Onde vive:** skill `depurar`, armadilhas; `varredura-final.md`, Passadas 4 e 5.

## 18. Ausência de valor virou zero na tela de dinheiro

**Sintoma:** total exibido como `0,00` quando a API não devolveu o valor. Três dos quatro valores da tela estavam protegidos; o quarto não.
**Causa raiz:** o placeholder `0,00` estava escrito na marcação e sobreviveu à falha de carregamento — o que sobra na tela quando o preenchimento não acontece é invisível na leitura do código.
**Regra que evita:** ao defender um valor exibido, defender **todos os irmãos na mesma passada** — três de quatro protegidos é sinal de que o quarto foi esquecido, não de que é seguro. Em tela de dinheiro, ausência nunca vira zero: ou o dado aparece, ou a tela deixa de oferecer a ação. E o estado de erro **apaga o placeholder**.
**Onde vive:** skill `construir`, "Verificação" (placeholder); `varredura-final.md`, Passada 2.

---

# Backend, dados e capacidade

## 19. Conjunto fechado de terceiro enumerado pela metade

**Sintoma:** projeto novo entrou e obrigou a mexer no motor de pagamento que se achava pronto — palavra em inglês na tela do comprador, pedido pendente para sempre. O sistema conhecia 4 de 7 ciclos e 5 de 13 status.
**Causa raiz:** enumerou-se a lista de valores que tinham aparecido até então, não a definição do terceiro. Cada projeto novo forçava uma atualização que parecia requisito novo e era dívida antiga.
**Regra que evita:** onde o terceiro define um conjunto fechado, o projeto conhece o **conjunto inteiro**, lido na documentação dele — nunca o pedaço em uso hoje. Valor fora do conjunto é recusado nomeando os aceitos, não repassado adiante.
**Onde vive:** skill `construir`, "Consultar a documentação".

## 20. Desistência silenciosa no caminho de dinheiro

**Sintoma:** nenhum. Pagamentos confirmavam no banco e o contratante nunca era avisado.
**Causa raiz:** uma consulta sem o join trouxe a relação vazia, e um `if (!x) return;` tratou isso como "não configurado". Bug de consulta virou comportamento normal.
**Regra que evita:** em caminho que move dinheiro, **desistência silenciosa precisa distinguir "não configurado" de "não carregado"** e registrar qual dos dois foi. Saída muda por caminho de erro sem deixar rastro é indistinguível de sucesso.
**Onde vive:** skill `seguranca-san`, pagamento; `varredura-final.md`, Passada 3, caminho de dinheiro.

## 21. Limite de taxa não é limite de simultaneidade

**Sintoma:** o serviço caiu. Duas operações caras dispararam ao mesmo tempo e estouraram a memória da instância.
**Causa raiz:** existia teto de requisições por minuto e não existia teto de quantas cabem **ao mesmo tempo**. As duas coisas parecem a mesma até o dia em que não são.
**Regra que evita:** operação cara em memória (derivação de chave, geração de documento, redimensionamento, importação) precisa de **teto de simultaneidade no código**. A pergunta é *quantas destas cabem juntas nesta máquina?* — e nenhum limite por minuto responde isso.
**Onde vive:** Lei 3; Lei 7 (o teto vira limite declarado).

## 22. `create table if not exists` não cria coluna nova

**Sintoma:** campo voltando `null` da API sem motivo claro, explicado como "linha antiga" quando era coluna inexistente.
**Causa raiz:** o arquivo de schema era idempotente e foi rodado de novo. Numa tabela que já existe, ele não faz nada — e a coluna acrescentada no corpo dele nunca foi criada.
**Regra que evita:** coluna acrescentada **depois** da primeira ida a produção exige alteração explícita no corpo executável, nunca em comentário nem dentro do `create table`.
**Onde vive:** Lei 6.

## 23. Rota que "não faz nada" mas toca o banco

**Sintoma:** rota de saúde pública, sem limite, consultando o banco a cada chamada — amplificação de carga com um laço de terminal.
**Causa raiz:** a rota não parecia uma rota de verdade, então ficou fora da lista de limites.
**Regra que evita:** a pergunta não é "esta rota cria alguma coisa?", é **"esta rota faz trabalho?"**. Rota pública que toca banco, disco ou rede externa entra na lista de limites, mesmo devolvendo só `{status:'ok'}`. E a lista de rotas limitadas se confere contra a lista de rotas montadas, não de memória.
**Onde vive:** skill `seguranca-san`, "Sempre".

## 24. Validar formato não valida tamanho

**Sintoma:** campo de texto livre aceitando entrada muito maior que o previsto, porque o único teto era o do corpo da requisição.
**Causa raiz:** o limite do parser parecia cobrir tudo, e fez o teto por campo parecer redundante.
**Regra que evita:** teto por campo mora **no validador**, não em cada controlador — seis arquivos chamando os mesmos validadores é regra que um dia vale em cinco.
**Onde vive:** skill `seguranca-san`, "Sempre"; Lei 2.

## 25. Middleware com estado reaproveitado entre montagens

**Sintoma:** contador de limite compartilhado entre rotas que deveriam ter baldes separados. Só aparece sob carga.
**Causa raiz:** a mesma instância do middleware foi montada em lugares diferentes. Middleware com estado interno não é valor reutilizável — é instância.
**Regra que evita:** cada montagem cria a sua. Reaproveitar a instância compartilha o estado, e o sintoma é invisível em teste isolado.
**Onde vive:** skill `construir`, "Nada de abstração não pedida".

---

# Segredo, acesso e configuração

## 26. Caractere especial de shell dentro de um segredo

**Sintoma:** rota de segurança respondendo **rápido demais**. O valor guardado tinha `$`, e a plataforma expandiu como shell — parte do segredo foi apagada em silêncio.
**Causa raiz:** o formato padrão de hash de senha (`alg$param$sal$hash`) tem cifrão por construção, e várias plataformas expandem shell no valor da variável. A colisão é previsível.
**Regra que evita:** segredo com caractere especial (`$`, crase, contrabarra, aspas) é **codificado em base64 ou hex antes de guardar** e decodificado dentro do processo. E rota de segurança que responde rápido demais é sinal tão forte quanto rota que responde errado.
**Onde vive:** Lei 3.

## 27. Ordem errada ao trocar uma variável de ambiente

**Sintoma:** o serviço parou. A variável foi renomeada no painel enquanto o código que usava o nome antigo ainda estava rodando.
**Causa raiz:** tratou-se como um passo o que são dois, com ordem obrigatória entre eles.
**Regra que evita:** **a variável nova existe antes do código que a usa; a antiga só sai depois que o código que a usava saiu do ar.** Trocar tudo de uma vez só é seguro quando o código aceita os dois nomes — e aceitar o antigo às vezes é justamente o que a mudança veio eliminar. Sem transição, a ordem não é preferência, é requisito.
**Onde vive:** skill `leis`, "Deploy automático".

## 28. Propriedade de segurança dependendo de variável de ambiente

**Sintoma:** rastro de pilha chegando ao usuário em produção, porque a variável de ambiente que decide isso não era a esperada.
**Causa raiz:** o comportamento "mostra o erro completo fora de produção" é padrão dos frameworks, e confiou-se que o ambiente estaria configurado certo.
**Regra que evita:** **propriedade de segurança que depende de configuração de ambiente é propriedade não garantida.** Dando para fechar em código, fecha em código — aí o valor da variável deixa de importar. E tratador de erro e de 404 são os **últimos** registrados, sempre, porque a ordem de registro é o que decide se são alcançados.
**Onde vive:** skill `seguranca-san`, "Sempre".

## 29. Comparação segura que não é segura sozinha

**Sintoma:** um autoteste falhou mostrando que a comparação de credencial em tempo constante devolvia verdadeiro para dois valores vazios.
**Causa raiz:** a normalização com valor padrão vazio, escrita do jeito mais comum, transformou "credencial ausente" em "credencial confere".
**Regra que evita:** função que promete comparação segura **cumpre a promessa sozinha** — não delega ao chamador a parte que a torna segura. E quando um autoteste falha, a primeira hipótese é que o código esteja errado, não a asserção.
**Onde vive:** Lei 3.

## 30. Acesso administrativo pendurado em fluxo de produto

**Sintoma:** o dono perdeu o acesso ao painel porque uma validação nova recusou um valor que a porta improvisada dependia de aceitar.
**Causa raiz:** a entrada do administrador estava escondida dentro de um fluxo de pagamento — dependia de uma tela renderizar, de um pedido falso existir e de uma validação não mudar. Bastou uma das três mudar.
**Regra que evita:** **porta de operação tem entrada própria e proteção própria**, nunca obscuridade dentro de um fluxo de produto. E validação nova é mudança de contrato com quem chama, mesmo quando o diff toca um arquivo só: apertar o que é aceito quebra quem dependia do que era aceito antes.
**Onde vive:** skill `seguranca-san`, "Área administrativa".

---

# Processo e ferramenta

## 31. Reescrita de histórico apagou trabalho não commitado

**Sintoma:** trabalho pendente na árvore desapareceu ao reescrever o histórico do repositório.
**Causa raiz:** o comando foi rodado com a árvore suja. Cópia da pasta ajuda a recuperar; commit evita perder.
**Regra que evita:** antes de qualquer operação que reescreva histórico, commitar tudo, conferir que a árvore está limpa, e reescrever de preferência num clone fresco. **Quem monta um comando destrutivo para outra pessoa rodar assume esse passo junto** — a instrução traz o commit e a conferência, não só o aviso de fazer backup, porque quem escreve o comando não sabe o que está pendente na máquina de quem vai rodar.
**Onde vive:** skill `leis`, "Trocar de superfície de trabalho".

## 32. O ambiente do teste faz parte do teste

**Sintoma:** um limite de taxa parecia quebrado; era o proxy trocando de endereço a cada requisição. Na mesma semana, uma política de acesso "passou" na verificação porque o navegador já tinha o cookie de sessão.
**Causa raiz:** tratou-se como constante o que era variável do experimento — endereço de origem, cookie já presente, relógio do ambiente.
**Regra que evita:** antes de declarar quebrado o que está do outro lado, conferir o que **este** lado está de fato mandando. Verificação de limite fixa a origem; verificação de barreira de acesso roda em janela anônima. Verificação feita de dentro de CI, contêiner, VPN ou proxy carrega as condições desse lugar junto.
**Onde vive:** skill `depurar`, armadilhas; `seguranca-san`, "Área administrativa" (janela anônima); `varredura-final.md`, Passada 5.

## 33. Faixa aberta de dependência com runtime fixado à mão

**Sintoma:** o CI quebrou sozinho, sem ninguém mexer no código. Uma dependência avançou dentro da faixa permitida e passou a exigir runtime mais novo que o fixado na configuração.
**Causa raiz:** a versão do runtime estava declarada só no lugar que a executa, e não no manifesto do projeto. O pacote anda; o ambiente fixo fica para trás em silêncio até quebrar.
**Regra que evita:** onde o runtime é fixado por escolha explícita, **declarar a exigência no manifesto do projeto** — senão o único lugar que aponta a versão certa é aquele que quebrou.
**Onde vive:** skill `construir`, "Consultar a documentação".

---

## Como uma lição chega aqui

No mesmo formato — sintoma, causa raiz, regra que evita, onde a regra passou a viver. A quarta linha é obrigatória: lição que não virou regra em nenhuma skill não foi aprendida, só anotada. Quem escreve é a sessão de manutenção do plugin, a partir dos `docs/erros/` que o dono traz no fecho de cada projeto (skill `leis`, "Fecho da esteira"). Não há promoção automática.
