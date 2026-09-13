---
name: revisar
description: Revisa uma mudança em correção, segurança, simplicidade e legibilidade antes de ela entrar. Use antes de commit, merge ou deploy, ou quando o usuário pedir revisão de código.
---

# Revisar — San & Co.

Revisar o **diff**, não o arquivo inteiro. Ler o código que a mudança toca antes de opinar sobre ela: crítica baseada em trecho isolado erra o alvo.

## Os quatro eixos

**1. Correção.** A mudança faz o que diz? Procurar: caso de borda não tratado (lista vazia, valor nulo, zero, string vazia), condição invertida, erro engolido por `catch` silencioso, `await` faltando, e comparação de valor monetário em ponto flutuante. Para cada defeito encontrado, descrever o cenário concreto que quebra — entrada específica levando a resultado errado. Achado sem cenário é palpite.

**2. Segurança.** Entrada validada na fronteira? Autorização checada no servidor e não só escondida no frontend? Segredo fora do código? Log sem dado sensível? Se a mudança toca pagamento, senha, documento ou dado de cliente, usar a skill `seguranca-san` — ali estão as regras específicas, e nenhuma delas é opcional.

**3. Simplicidade.** O que dá para deletar? Procurar: abstração com um único uso, dependência nova para o que a biblioteca padrão resolve, configuração para valor que nunca muda, flexibilidade que ninguém pediu, e código morto deixado "por garantia". Se existe caminho mais curto que funciona igual, apontar qual.

**4. Legibilidade e padrões.** Nome que diz o que a coisa é. Função que cabe na cabeça. Módulo com uma responsabilidade. Aderência às Leis de construção (skill `leis`) — estrutura de pastas, fronteira entre domínio e infraestrutura, migration versionada.

## Varredura em ciclos — uma passada não basta

Uma leitura só encontra o óbvio. E toda correção pode introduzir erro novo. Então a revisão roda em **ciclos**, não em passada única.

**Um ciclo** = as quatro varreduras, cada uma procurando uma coisa só: correção, depois segurança, depois simplicidade, depois legibilidade e padrões. Varredura que procura tudo ao mesmo tempo não acha nada direito.

**Regra de repetição**: encontrou achado em qualquer varredura do ciclo → corrigir → **rodar o ciclo inteiro de novo**, do começo. Não basta reconferir o trecho corrigido: a correção muda o código, e o que estava certo pode ter deixado de estar.

**Critério de parada**: parar quando um ciclo completo passar **sem nenhum achado novo**. Não é "parar depois de três ciclos" — é parar quando o código sobreviver a um ciclo limpo.

**Teto de escalada**: se depois de três ciclos completos ainda aparecer achado novo a cada volta, parar de varrer e dizer isso ao usuário. Achado que não para de surgir não é bug a mais — é sinal de que o desenho está errado, e mais varredura não conserta desenho. Nesse ponto o certo é rever a abordagem, não seguir remendando.

**Regra inegociável**: nunca deixar de relatar um achado para conseguir fechar o ciclo. A pressão de "terminar" cria exatamente esse incentivo, e ceder a ele transforma a revisão em teatro. Ciclo que fecha porque o achado foi engolido é pior que nenhuma revisão, porque gera confiança falsa.

Ao terminar, dizer quantos ciclos rodaram e o que cada um encontrou. Isso mostra se o código estava razoável ou se está sendo remendado.

## Escopo da revisão

Comentar apenas o que a mudança introduz ou toca. Não pedir refatoração de código vizinho que já estava lá e não faz parte do problema — isso é outro trabalho, e misturar os dois trava o merge.

## Formato do retorno

Ordenar por gravidade: o que quebra em produção primeiro, depois o que é risco de segurança, depois simplificação, por último estilo. Para cada item: onde está, o que acontece de errado, e o que fazer. Uma linha por item quando possível.

Se nada relevante foi encontrado, dizer isso em uma frase — não inventar achado para parecer diligente. Revisão que sempre encontra algo vira ruído e deixa de ser lida.

## Antes de aprovar

Checar: os segredos continuam fora do repositório, a migration (se houver) é nova e não editada, existe pelo menos um teste cobrindo o caminho crítico que mudou, o README continua verdadeiro depois da mudança, e **toda referência que a mudança tocou continua existindo** — arquivo, skill, seção citada. Ponteiro envelhece calado: preferir apontar por função ("o documento canônico na raiz") a apontar por caminho ou número de seção.
