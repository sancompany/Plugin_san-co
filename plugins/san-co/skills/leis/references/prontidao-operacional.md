# Prontidão operacional — a segunda metade da estação 6

Um sistema no ar não é um sistema que alguém consegue operar. Esta lista é o que separa os dois, e ela fecha a estação 6 junto com o ciclo de segurança. Cada item tem o que fazer, como conferir, e o que é exagero para um projeto operado por uma pessoa.

**Regra que atravessa tudo:** item fecha com evidência — o cabeçalho que voltou, o alerta que chegou no celular, o número que a consulta devolveu. "Configurei" não fecha nada.

---

## 1. E-mail transacional chega

**Por que é esquecido:** o provedor devolve `200` e ninguém vê o Gmail jogando "redefinir senha" em spam. Nada quebra do lado do sistema. E desde o fim de 2025 o Google **rejeita** remetente não autenticado — deixou de ser recomendação.

**O que existe no DNS do domínio remetente:**

```
seudominio.com.                TXT  "v=spf1 include:<do provedor> ~all"   ; UM registro só; até 10 lookups
<seletor>._domainkey.seudominio.com.   ; DKIM — nome e valor vêm do provedor; chave de 2048 bits
_dmarc.seudominio.com.         TXT  "v=DMARC1; p=none; rua=mailto:dmarc@seudominio.com"
```

Mais o **Return-Path alinhado** (Postmark: CNAME de bounces; SES: MAIL FROM customizado) — sem isso o SPF passa mas não alinha, e o DMARC fica dependendo só do DKIM. Dois registros SPF na raiz é erro permanente; `include` acima de dez também.

**Como conferir:** mandar um e-mail real do sistema para uma conta Gmail, abrir "Mostrar original", e em `Authentication-Results` ler `spf=pass`, `dkim=pass header.d=seudominio.com`, `dmarc=pass`. Depois, cadastrar o domínio no Google Postmaster Tools. Com volume baixo os gráficos ficam vazios — não é bug seu.

**Não é exagero:** e-mail de marketing precisa de descadastro em um clique (`List-Unsubscribe` e `List-Unsubscribe-Post`) e processamento em até dois dias; transacional não precisa de descadastro, mas precisa da mesma autenticação. **Exagero:** `p=reject` no primeiro dia, BIMI, IP dedicado.

## 2. Alguém descobre o erro antes do cliente

**Por que é esquecido:** o erro que importa acontece daqui a três semanas, às duas da manhã, num webhook. Sem sinal externo, o cliente é o monitor.

**O mínimo para uma pessoa:**

| Camada | O que | Por quê |
|---|---|---|
| Exceção com contexto | captura de erro com a requisição (Sentry ou equivalente) | é o "grep" dos 500 com o que estava acontecendo |
| Uptime **externo** | monitor de fora com alerta no celular | quem cai não consegue se auto-monitorar |
| Tarefa agendada | ping ao fim de cada job crítico num serviço de "dead man's switch"; alerta quando o ping **não chega** | painel não mostra o job que não rodou |
| Log | o do próprio painel da hospedagem, com retenção finita | suficiente em serviço único |

**O que alerta (acorda alguém):** serviço fora por duas checagens seguidas; taxa de 5xx acima de X% por N minutos; job crítico (backup, cobrança, e-mail) não rodou; certificado a vencer; disco acima de 85%. **O que não alerta:** exceção individual (vai para o rastreador, não para o celular); CPU ou memória pontual; deploy concluído; aviso; qualquer coisa já ignorada três vezes. Alerta é para sintoma **urgente, acionável e visível ao usuário** — o resto é log.

**Como conferir:** derrubar o serviço de propósito e cronometrar até o alerta chegar no celular. Forçar uma exceção e vê-la no rastreador com a requisição. Comentar o ping do job e ver o alerta de ausência disparar. Se qualquer um dos três não acontecer, o item está aberto.

**Exagero:** stack completa de métricas e tracing distribuído — o gatilho para isso é vários serviços interligados ou mais de uma pessoa.

## 3. O backup restaura

**Por que é esquecido:** "tem backup" é uma caixa marcada no painel. "Consegue restaurar" exige ter feito uma vez — e certos defeitos só aparecem no restore.

**A regra:** três cópias, duas mídias, uma fora do provedor principal, **uma imutável** (que nem o dono da conta apaga por engano), e zero erro verificado por restauração de verdade. Plano gratuito de banco gerenciado costuma **não ter backup automático**, e backup de banco **não inclui arquivos em storage** — os dois precisam de cobertura própria.

**O ensaio de restauração**, mensal e depois de qualquer mudança de versão, extensão ou ferramenta:

```bash
pg_dump --format=custom --no-owner --no-privileges --file="backup_$(date -u +%Y%m%dT%H%M%SZ).dump" "$DATABASE_URL"
# baixar o dump DO storage externo (não da cópia local) e subir um banco descartável
docker run -d --name ensaio -e POSTGRES_PASSWORD=x -p 55432:5432 postgres:16
pg_restore --dbname="postgres://postgres:x@localhost:55432/postgres" --exit-on-error --jobs=4 backup_*.dump
# validar: contagem das tabelas críticas, e a idade do dado mais recente
psql "postgres://postgres:x@localhost:55432/postgres" -c "select count(*) from <tabela>;" -c "select now() - max(created_at) from <eventos>;"
docker rm -f ensaio
```

`--exit-on-error` importa: o padrão do `pg_restore` é continuar em erro, em silêncio. O tempo que levou é o seu RTO real; a idade do dado mais recente é o seu RPO real — e são esses dois números, medidos, que o `CONSTRAINTS.md` declara.

**Como conferir:** existe tarefa automática fazendo dump para storage fora do provedor, monitorada pelo item 2; existe registro do último ensaio com data, duração e resultado, com menos de trinta dias.

**Exagero:** restauração ponto-a-ponto paga para projeto que aceita perder um dia.

## 4. Desempenho medido no celular de verdade

**Por que é esquecido:** na máquina de quem desenvolve, com cache quente e fibra, tudo é rápido. O que conta é o percentil 75 no celular do cliente.

| Métrica | Bom | Ruim |
|---|---|---|
| LCP (carregamento) | ≤ 2,5 s | > 4 s |
| INP (resposta à interação) | ≤ 200 ms | > 500 ms |
| CLS (estabilidade visual) | ≤ 0,1 | > 0,25 |

**Como medir:** em campo, pelo PageSpeed Insights ou pelo Search Console — que ficam vazios em site novo; ou com medição própria desde a primeira visita (biblioteca `web-vitals` mandando os três valores para uma tabela, e o p75 por rota numa consulta). Em laboratório, para não regredir: Lighthouse CI com orçamento no pipeline. Laboratório evita regressão; campo diz a verdade.

**O que fazer com o número:** se o p75 está em "bom" nas três, parar — não otimizar. LCP ruim costuma ser imagem principal sem dimensão ou servidor lento; CLS, imagem e fonte sem dimensão declarada; INP, JavaScript pesado no manipulador.

**Exagero:** perseguir nota 100 no Lighthouse — é laboratório, não campo.

## 5. A conta não surpreende

**Por que é esquecido:** a fatura chega trinta dias depois do erro, e o que escala não é o que se pensou: egresso (imagem de 4 MB servida em vez de 200 KB), invocações por unidade, ingestão de log que por padrão nunca expira, armazenamento que só cresce.

**Antes de subir:** alerta de orçamento em **cada** conta paga, com valor igual ao dobro do esperado; teto duro decidido conscientemente onde existe (e anotado no `RUNBOOK.md`); retenção de log definida, nunca infinita; `Cache-Control` em toda resposta que pode ser cacheada; imagens otimizadas; asset grande em storage com egresso zero. Dado de cobrança das plataformas atrasa até dois dias — **alerta não é freio**.

**Como conferir:** abrir cada painel de cobrança e ver o alerta configurado. Dez minutos por mês revisando a fatura por serviço.

## 6. Outra pessoa consegue operar

**Por que é esquecido:** quem construiu tem tudo na cabeça, até o dia em que o cartão do registrador expira e o domínio cai.

O `RUNBOOK.md`, versionado ao lado do código, responde nesta ordem: inventário de contas — uma linha cada, com dono, e-mail de login, onde está a senha e o segundo fator, **data de renovação e cartão que paga**; onde estão os segredos e como rotacionar cada um (o ponteiro para o cofre, nunca o segredo); deploy e reversão com os comandos exatos; restauração de backup (o ensaio do item 3, colado); alerta → significado → primeira ação; **incidente com dado pessoal** — quem decide, como isolar, como contar afetados, quem escreve, e os prazos da ANPD (skill `legal`, `references/obrigacoes-brasil.md`); dependências externas e o que quebra se cada uma cair; contatos, inclusive a pessoa número dois; como desligar tudo com segurança.

**Como conferir:** a pessoa número dois, com o runbook e sem falar com quem construiu, faz um deploy trivial, reverte, e acha a data de vencimento do domínio. Onde ela travar, o runbook está incompleto. Uma vez por semestre basta.

**Exagero:** plano de continuidade formal.

## 7. A métrica de sucesso responde "quantos ontem?"

**Por que é esquecido:** o sistema está "no ar" tecnicamente, e ninguém definiu o que "funcionando" significa para o negócio. A estação 1 exigiu uma métrica; sem esta seção, ela nunca é instrumentada.

**O que existe antes de considerar pronto:**

- **Uma métrica principal**, precursora da receita e não a receita em si — definida na estação 1.
- **Cinco a dez eventos** que indicam valor, nomeados por convenção **antes** da primeira linha de instrumentação (`categoria:objeto_acao`, verbo no presente, propriedades `objeto_adjetivo`) — listados na seção 9 do `docs/funcional.md`.
- **Os eventos críticos emitidos no servidor**, não só no navegador: cadastro, ação central, pagamento confirmado (pelo webhook). Navegador tem bloqueador e JavaScript que falha.
- **Uso interno filtrado**, para o dono testando não contaminar.
- Uma tabela `eventos(usuario_id, nome, propriedades, criado_em)` e três consultas salvas atendem quase todo projeto de uma pessoa.

**Como conferir:** abrir o painel ou rodar a consulta e responder, com número: quantos se cadastraram ontem, quantos fizeram a ação central, quantos pagaram. Qualquer "não sei" é item aberto.

**Exagero:** gravação de sessão, experimentação A/B, data warehouse.

---

## O que fecha a estação

Os sete itens com evidência: os três `pass` no cabeçalho do Gmail; o alerta cronometrado no celular; o registro datado do ensaio de restauração; o p75 das três métricas; o alerta de orçamento em cada conta; o teste da pessoa número dois; os três números de ontem. Item sem evidência é item aberto, e estação com item aberto não fecha.

Fontes consultadas ao escrever esta lista, para reconferir quando um número parecer velho: diretrizes de remetente do Google e do Yahoo; o livro de SRE do Google (monitoramento e plantão); web.dev (Core Web Vitals e limiares); documentação de backup do Supabase; regra 3-2-1-1-0 da Veeam; documentação de orçamento de Vercel, Supabase e Google Cloud; guias de analytics de produto da Amplitude e do PostHog.
