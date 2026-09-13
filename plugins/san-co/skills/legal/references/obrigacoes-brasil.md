# Obrigações legais de um sistema brasileiro pequeno — além dos Termos e da Política

O que a lei exige de um sistema que vende assinatura online, trata dado pessoal e é operado por ME no Simples — e que costuma ser esquecido porque exige **código ou procedimento**, não só texto. Cada item diz em que estação entra, o que exige, o prazo, e o que **não** é obrigatório para esse porte, porque evitar excesso é tão útil quanto listar.

Data-base: setembro de 2026. Prazo e norma envelhecem — conferir na fonte antes de decidir, como manda a skill `construir`.

---

## A premissa: agente de tratamento de pequeno porte

ME, EPP e startup têm regime flexibilizado pela Resolução CD/ANPD nº 2/2022, **desde que não façam tratamento de alto risco**. É autoenquadramento — não existe cadastro na ANPD; a única formalidade é declarar a condição ao comunicar incidente. O que ela flexibiliza: encarregado, forma do registro, política de segurança, e **prazos em dobro** para responder titular, comunicar incidente e responder à ANPD. O que ela **não** dispensa: bases legais, direitos do titular, segurança, comunicação de incidente, transferência internacional.

Perde o regime quem faz tratamento em larga escala **ou** que afete significativamente direitos, combinado com dado sensível, de criança ou idoso, decisão automatizada relevante ou vigilância. Um cofre de senhas trata "dado de autenticação em sistemas": enquanto o volume for pequeno, continua pequeno porte — mas todo vazamento dele será comunicável (item 2).

---

## 1. Direitos do titular — código na estação 5

**Obrigação:** atender, gratuitamente e a qualquer momento, os direitos do art. 18 da LGPD — confirmação, acesso, correção, anonimização ou eliminação do desnecessário, portabilidade, eliminação do tratado por consentimento, informação sobre compartilhamento, e revogação do consentimento por procedimento **gratuito e facilitado**.

**Prazos:** confirmação e acesso em formato simplificado, **imediatamente**; declaração completa em **15 dias** — **30 para pequeno porte**. Os demais direitos ainda não têm prazo regulamentado pela ANPD (agenda 2025-2026, sem resolução publicada); usar os mesmos 15/30 dias como padrão razoável.

**O que exige do produto:**

- **Exportar os dados da conta** em formato eletrônico (JSON ou CSV baixável resolve acesso e portabilidade juntos; não há formato obrigatório).
- **Excluir a conta** com apagamento efetivo — não só marcação — do que foi tratado por consentimento, preservando apenas o que tem guarda legal (fiscal; registro de acesso do Marco Civil, item B), e registrando o que foi retido e por quê.
- **Revogar consentimento com um clique** onde a base for consentimento (marketing, por exemplo) — mesma facilidade que foi dada para consentir.
- **Um canal identificado** para requerimento do titular (e-mail dedicado ou formulário), publicado de forma clara no site — é a contrapartida de não ter encarregado.
- **Registrar cada requerimento** com data de entrada e de resposta: é a prova de prazo.
- Verificar a identidade do requerente antes de entregar dado — a própria sessão autenticada é o caminho simples.
- A lista de **com quem os dados são compartilhados** precisa existir de fato: é o inventário de subprocessadores (banco, hospedagem, e-mail, pagamento), exposto na política e mantido no registro do item 4.

## 2. Incidente com dado pessoal — procedimento pronto na estação 6

**Obrigação:** comunicar à ANPD **e** aos titulares todo incidente que possa acarretar risco ou dano relevante (LGPD art. 48; Resolução CD/ANPD nº 15/2024). É relevante quando afeta direitos **e** envolve dado sensível, de criança ou idoso, **financeiro**, **de autenticação em sistemas**, sob sigilo, ou em larga escala. Para checkout e cofre, assumir que **todo incidente de confidencialidade será comunicável**.

**Prazos:** à ANPD, **3 dias úteis** do conhecimento — **6 para pequeno porte**; aos titulares, o mesmo; complementação do que faltava, **20 dias úteis**. Pode-se comunicar preliminarmente e completar.

**O que consta na comunicação à ANPD:** natureza dos dados; número de titulares afetados; medidas de segurança antes e depois; riscos; motivo de eventual demora; mitigação; data do incidente e do conhecimento; identificação do controlador **com a declaração de pequeno porte**; identificação do operador; descrição e causa raiz. **Aos titulares:** o mesmo, em linguagem simples, direta e individualizada — e-mail serve; se individual for inviável, aviso no site por **no mínimo três meses**. Envio pelo peticionamento eletrônico da ANPD, com conta gov.br, assinado por encarregado ou representante com procuração.

**Registro interno obrigatório mesmo quando não se comunica** (art. 10): todo incidente fica registrado por **no mínimo cinco anos**, com data do conhecimento, circunstâncias, natureza dos dados, número de titulares, avaliação de risco, medidas, forma da comunicação **ou os motivos de não ter comunicado**.

**O que precisa existir antes, senão seis dias úteis não dão:**

1. **Log de acesso a dado** que permita responder "quais registros, de quem, e quando" — sem ele não se preenche a comunicação.
2. **Modelo de e-mail de notificação** ao titular já redigido, e meio de disparo para os afetados.
3. **Conta gov.br** do responsável criada e testada no peticionamento da ANPD; procuração assinada se não houver encarregado.
4. **Runbook de incidente de uma página** no `RUNBOOK.md`: quem decide, como isolar, como contar afetados, quem escreve — a ANPD publicou guia de segurança com checklist para pequeno porte que serve de base.
5. **A tabela de registro de incidentes** com os campos que o art. 10 da Res. 15/2024 exige — descrição do incidente, dados e titulares afetados, medidas técnicas em uso, riscos, medidas de mitigação, datas do incidente e da ciência, e se houve comunicação — guardada por cinco anos.

## 3. Encarregado — não obrigatório, com contrapartida

Pequeno porte é **dispensado de indicar encarregado** (Res. 2/2022 art. 11; Res. 18/2024 art. 3 §3), com uma contrapartida: **disponibilizar canal de comunicação com o titular**, publicado de forma clara, para titulares e para a ANPD. Indicando mesmo assim — recomendável quando o produto é sensível —, é ato formal escrito, identidade e contato publicados em local de destaque no site, e assume-se receber reclamações e orientar.

## 4. Registro de operações — obrigatório, em forma simplificada

Controlador e operador **mantêm registro das operações de tratamento** (LGPD art. 37) — vale para todos; para pequeno porte, em forma simplificada (Res. 2/2022 art. 9). A ANPD publicou modelo em planilha, de uso facultativo. É documento interno, exibido se pedido; não achei prazo de guarda nem exigência de envio.

**O que é na prática:** uma linha por atividade (cadastro, cobrança, suporte, marketing, o cofre) com dado tratado, finalidade, base legal, origem, compartilhamento (operadores nacionais e estrangeiros), retenção e medida de segurança. **É o mesmo artefato do `docs/inventario-de-dados.md`** — mantido na tarefa em que entra campo ou fornecedor novo, ele já é o registro.

**Não obrigatório:** relatório de impacto (RIPD) como regra geral — a ANPD só pode determinar, e ainda não regulamentou.

## 5. Venda online ao consumidor — Decreto 7.962/2013, na estação 7

Aplica-se a consumidor pessoa física e a pessoa jurídica destinatária final — plano pequeno vendido a empresa, tratar como consumidor por segurança.

**No site, em destaque:** nome empresarial e **CNPJ**; **endereço físico e eletrônico**; características do serviço; preço com **toda despesa adicional discriminada**; condições integrais da oferta; restrições à fruição (os limites do plano). Concretamente: rodapé com razão social, CNPJ, endereço e e-mail; página de preço sem "a partir de".

**Antes de fechar:** sumário do contrato com as cláusulas que limitam direitos (renovação automática, cancelamento, reajuste); ferramenta para **rever e corrigir** antes de confirmar; **confirmação imediata** do recebimento da aceitação, com o contrato ou link estável para ele (PDF ou HTML que se conserva); segurança de pagamento e dado.

**Atendimento:** serviço eletrônico eficaz, **confirmação imediata do recebimento** de cada demanda, resposta em **até cinco dias** — ticket numerado com auto-resposta e fila com esse prazo.

**Arrependimento (CDC art. 49):** sete dias da contratação, reembolso integral, exercido **pela mesma ferramenta usada para contratar** (botão dentro do sistema, não só e-mail), e o fornecedor **comunica imediatamente o meio de pagamento** para estorno — na prática, estorno pelo provedor no mesmo fluxo. Para serviço digital não há exceção na lei; há decisões afastando o reembolso quando o consumo é imediato e o consumidor foi avisado de forma destacada, mas sem orientação consolidada — o caminho seguro é **honrar os sete dias com reembolso integral no primeiro ciclo**. Renovação posterior não reabre o prazo; cancelar precisa continuar tão fácil quanto contratar.

**Não se aplica:** a Lei do SAC (Decreto 11.034/2022) — só alcança serviço regulado pelo Executivo federal (telecom, banco, plano de saúde). SaaS privado está fora: sem obrigação de telefone gratuito nem atendimento 24 horas.

## 6. Nota fiscal de serviço — uma por cobrança

ME e EPP emitem documento fiscal em toda prestação. A partir de **1º de novembro de 2026**, obrigatoriamente pela **NFS-e Nacional** (Resolução CGSN nº 191/2026), independente do município, por web ou **API**. Para assinatura recorrente: **uma nota por cobrança**, com CPF ou CNPJ do tomador. Com dezenas de assinantes, emissão manual não escala — integração com a API do Emissor Nacional é trabalho de código, não de contabilidade. Pergunta para o contador antes de fechar preço: em qual item da LC 116 e em qual anexo do Simples cai a atividade, porque a alíquota muda a conta.

## 7. Cookies — banner só se houver cookie não necessário

Guia orientativo da ANPD (2022): cookie **necessário** — sessão, autenticação, CSRF — não pede consentimento, e pedir é inadequado. Cookie **não necessário** — analytics com perfil, marketing, terceiros — pede consentimento livre, informado e inequívoco: primeira camada com **rejeitar tão destacado quanto aceitar**; segunda camada por categoria, **desativada por padrão**; nada pré-marcado; nada por rolagem; revogação tão fácil quanto a concessão. **App autenticado sem analytics de terceiro nem pixel de marketing não precisa de banner** — só do aviso na política. É o caso mais barato e mais defensável, e a medição própria do item 7 da prontidão operacional cabe nele.

## 8. Acessibilidade — obrigação legal para site privado

A Lei Brasileira de Inclusão (art. 63) obriga acessibilidade em site de empresa com sede no país, "conforme as melhores práticas e diretrizes adotadas internacionalmente"; o Decreto 9.405/2018 confirma que vale **também para ME, EPP e MEI**, com fiscalização orientadora e dupla visita antes de autuar. Padrão de referência exigível: **WCAG 2.2, nível AA**. Não há multa administrativa própria hoje; o risco é ação civil pública e ação individual.

**Mínimo defensável, e é o que a Lei 5 exige:** HTML semântico, navegação inteira por teclado, contraste AA, rótulo em todo campo, foco visível, texto alternativo, nada informado só por cor, erro de formulário descrito em texto. Verificador automático (axe, Lighthouse) no CI resolve a maior parte.

---

## Bônus — o que quase ninguém sabe que é obrigatório

**A. Transferência internacional (Res. CD/ANPD nº 19/2024).** Banco, hospedagem, e-mail ou backup fora do Brasil é exportação de dado, e exige mecanismo válido: cláusulas-padrão da ANPD sem alteração (prazo de adequação encerrado em 23/08/2025) ou decisão de adequação — só existe uma, a União Europeia (2026). **Estados Unidos não tem adequação.** **Sem dispensa para pequeno porte.** Ação concreta: hospedar em região brasileira quando o provedor oferece — que é a regra de região da skill `classificar` por outro motivo —, ou conferir se o contrato do provedor incorpora as cláusulas-padrão literalmente; e listar cada transferência no registro do item 4 e na política.

**B. Marco Civil, art. 15.** Provedor de aplicação constituído como pessoa jurídica com fins econômicos **guarda registro de acesso — data, hora e IP de cada uso — por seis meses**, sob sigilo. É uma tabela de log de login com retenção mínima de seis meses e máxima razoável (o art. 16 veda guardar mais que o necessário). E o art. 7, X: direito à exclusão definitiva ao fim da relação, exceto guarda legal — que reforça o "excluir conta" do item 1.

**C. Estatuto Digital da Criança (Lei 15.211/2025, vigente desde março de 2026).** Aplica-se a serviço direcionado ou com provável acesso por menor. Produto para adulto, com termos 18+, sem apelo a criança e sem conteúdo aberto, fica fora na leitura razoável — mas a avaliação é concreta: documentar a análise em uma linha no registro do item 4. Não obrigatório: verificação de idade robusta, controle parental.

**D. Para calibrar prioridade:** LGPD art. 52 — advertência, multa até 2% do faturamento limitada a R$ 50 milhões por infração, bloqueio ou eliminação de dado; a dosimetria considera porte e boa-fé, e comunicar incidente no prazo conta a favor.

---

## Resumo por estação

| Estação | O que entra |
|---|---|
| 4 Contratos | inventário de dados **é** o registro de operações; lista de subprocessadores; região do banco decide transferência internacional |
| 5 Construção | exportar dados; excluir conta de verdade; revogar consentimento com um clique; canal do titular; registro de requerimentos; botão de arrependimento com estorno; log de acesso de seis meses; confirmação de contratação por e-mail; ticket com auto-resposta; NFS-e por cobrança (a partir de 11/2026) |
| 6 Prontidão | runbook de incidente; conta gov.br testada; modelo de e-mail de notificação; tabela de incidentes; acessibilidade verificada |
| 7 Lançamento | CNPJ, endereço e canal no rodapé; sumário pré-contrato; Termos e Política publicados; banner de cookies só se houver cookie não necessário |

**O que não encontrei e não devo inventar:** regulamento ANPD de direitos do titular e portabilidade (não publicado); orientação consolidada sobre arrependimento em serviço digital; prazo municipal de emissão de nota para assinatura; versão do guia de cookies posterior a 2022.

Fontes: LGPD (Lei 13.709/2018); Resoluções CD/ANPD nº 2/2022, 15/2024, 18/2024, 19/2024; guia de segurança para pequeno porte e guia de cookies da ANPD; Decreto 7.962/2013; CDC art. 49; Decreto 11.034/2022; Resolução CGSN nº 191/2026; LBI (Lei 13.146/2015) e Decreto 9.405/2018; Marco Civil (Lei 12.965/2014); Lei 15.211/2025.
