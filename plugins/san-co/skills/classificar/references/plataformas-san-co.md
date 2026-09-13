# As plataformas da San & Co. — como cada uma é usada

Como cada plataforma entra num projeto, e o que decidir antes de usá-la. **Não é inventário**: quantos projetos existem, em que conta e em que região cada um está é coisa que muda toda semana e se confere no painel, não aqui.

**Número envelhece.** Cota, preço e limite mudam sem aviso — decisão que depende de um número confere na fonte oficial antes, como manda a skill `construir`. O que está aqui é a forma de usar e o que já custou caro descobrir.

---

## Northflank — onde roda serviço com processo vivo

Plataforma oficial de hospedagem da San & Co. Usada quando o projeto tem servidor próprio: rota que responde, webhook que chega, tarefa agendada.

- **Criar o serviço já na região sul-americana.** Região não se troca depois sem recriar o serviço, e a razão de a plataforma ser esta é justamente ficar perto do banco. Região errada na criação anula o motivo da escolha.
- **Compute sempre ligado no plano gratuito** — não dorme, e portanto não existe aqui a armadilha de primeira requisição lenta depois de inatividade.
- **O plano gratuito é sandbox com teto**, não plano ilimitado: número pequeno de serviços, um banco e algumas tarefas agendadas. Projeto que passar do teto sai do gratuito, e isso é decisão registrada, não surpresa no dia.
- **Deploy automático a partir da branch principal** — push é publicação; as condições estão na skill `leis`, "Deploy automático".
- **Front-end que só fala com o banco não precisa de serviço aqui.** Página estática vai para o Cloudflare, de graça, e sem processo para manter de pé.

**Render está descontinuado no ecossistema.** Não se cria serviço novo lá. O que ainda estiver rodando lá é legado em migração — ver a seção final deste arquivo.

## Supabase — banco de dados do projeto

Um projeto Supabase por projeto da San & Co., pela política de isolar sempre.

- **O plano gratuito tem teto de projetos ativos** e **pausa por inatividade**. Requisição periódica evita a pausa, mas é remendo: projeto que precisa estar de pé precisa de plano que o mantenha de pé.
- **Plano gratuito não tem backup automático.** Isso decide sozinho onde dado de pagamento e dado de pessoa podem morar: sem backup, a Lei 6 fica em exceção registrada no `CONSTRAINTS.md` até deixar de ser verdade.
- **Edge Function não tem processo vivo.** Fila em memória, contador de limite em memória e sincronização "no boot e a cada 24h" não existem ali: a função é invocada, responde e deixa de existir. Mover para lá é reescrever esses mecanismos, não movê-los (lição nº 4).

## Cloudflare — domínio, DNS e porta

- Domínio, DNS e proxy de todos os projetos, e página estática servida sem custo, com deploy automático — push é publicação.
- **Access é a porta de toda área administrativa** — regras na skill `seguranca-san`.

## GitHub — a casa de cada projeto

Repositório é a **casa**; pasta em disco, pen drive e cópia em área de trabalho são cópias de trabalho.

- Minutos de execução automática em repositório privado são limitados no gratuito — o que roda a cada push e o que roda por agendamento está definido em `seguranca-san/references/verificacoes-automaticas.md`.
- Ligar a proteção que **barra o push com credencial** (`seguranca-san/references/verificacoes-automaticas.md`).

## Asaas — o dinheiro

Provedor por trás do San Checkout; as regras de integração são da skill `checkout`. O que vale aqui: **dado de cartão nunca passa pelo Checkout nem pelo projeto**, e é isso que mantém os dois fora do escopo de PCI-DSS.

---

## Regra de região: aplicação e banco juntos

Aplicação numa região e banco em outra pagam a viagem **em toda consulta**. Uma requisição que faz cinco consultas em sequência paga cinco vezes, e o sintoma é um sistema lento sem nenhum ponto lento — não aparece no código, não aparece em teste local, e ninguém acha.

**Aplicação e banco na mesma região, ou o mais perto possível.** Não dando, a distância vira limite declarado no `CONSTRAINTS.md` **com o número medido**, nunca estimado: uma requisição real cronometrada encerra a discussão.

E o público também conta: projeto para usuário brasileiro roda no Brasil. Usuário paga a distância uma vez por página; a aplicação paga por consulta.

## Migração do legado: o que ainda está no Render

**Northflank é oficial; Render está descontinuado.** Serviço novo nasce no Northflank, na região sul-americana. O que resta no Render é legado, e sai — mas sair tem ordem, e ela não começa pela hospedagem.

1. **Tirar o estado da memória antes de mover.** Fila de reenvio, contadores de limite e sincronização periódica saem para tabela no banco com tarefa agendada, **ainda onde o serviço está hoje**. Isso conserta a lição nº 4 sozinho e desacopla a migração do risco: serviço que não depende de processo vivo troca de casa sem perder nada no caminho. Serviço que depende perde o que estava na memória no instante em que muda.
2. **Subir o novo com o antigo de pé.** Os dois respondendo, o novo verificado contra o mesmo contrato, e só então o tráfego apontado. Nunca desligar os dois lados no mesmo dia.
3. **Um serviço por vez.**
4. **Conferir a região do novo antes de apontar tráfego** — a migração existe por causa da distância; destino na região errada repete o problema com outro nome.
5. **Nunca durante uma reta final.** Trocar runtime de serviço que processa dinheiro cai na lista curta da skill `leis`.
6. **Desligar o antigo só depois** de o novo ter passado por um ciclo completo — incluindo um webhook real chegando e uma cobrança real conciliando. Serviço antigo desligado cedo demais leva junto o caminho de volta.

**Uma ressalva que vale escrever:** camada gratuita de qualquer provedor tem recurso limitado e termos que mudam. Para serviço que processa dinheiro, o plano gratuito serve para começar, não para ser a casa definitiva — e o dia em que deixar de servir é decisão registrada, não deriva.
