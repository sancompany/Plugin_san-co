# Loja, catálogo e venda de ingresso — o que este tipo tem além da referência-mãe

Referência por tipo da estação 5, para o site que vende: a rede de supermercados com três lojas, o Trimundi9 vendendo ingresso. O comum a qualquer site é apontado por número em `desenvolvimento-web.md`. Pagamento é a skill `checkout`; arrependimento, NFS-e e Decreto 7.962 são a skill `legal` (`obrigacoes-brasil.md`, itens 5 e 6). Os percentuais são do Baymard Institute, que mede em teste de usabilidade e em benchmark de mais de 150 lojas, salvo indicação.

**Regra que atravessa tudo:** a evidência que fecha é um pedido real, pago com Pix de valor baixo, do celular, sem cadastro, chegando ao painel e ao e-mail — e depois estornado. Loja sem pedido de teste é vitrine.

---

## 1. Página de produto

**Por que é esquecido:** nasce como ficha de cadastro: foto, nome, preço, botão. 62% das lojas mobile têm página de produto "medíocre ou pior" em 2026.

**O que existe**, nesta ordem no celular: galeria; nome; preço à vista com parcelamento por extenso ("ou 3× de R$ 33,33 sem juros") — o Decreto 5.903, art. 3, exige à vista, número e valor das parcelas, juros e total a prazo; variação em botão, não `<select>` (57% erram), com estoque **por variação**, a esgotada visível e desabilitada; data de entrega por CEP (item 5) ao lado do botão único "Adicionar ao carrinho"; descrição em destaques escaneáveis (78% não estruturam); especificação em `<table>`; avaliações. Fotos: 56% dos usuários vão à galeria antes de ler; mínimo três, uma "em escala" (na mão, com pessoa — 42% tentam estimar tamanho pela foto), zoom real, miniaturas visíveis no celular (76% não têm). Supermercado: preço por unidade de medida (R$/kg, R$/L) junto do preço — Lei 10.962, art. 2º-A; 81% não mostram. Avaliação: distribuição por estrelas clicável (43% não têm), escondida abaixo de cinco, negativa respondida. Link de troca e devolução no corpo (60% procuram ali).

**Como conferir:** a 360 px, sem rolar, ler preço, parcela e botão; trocar variação e ver foto, preço e estoque mudarem juntos.

**Exagero:** vídeo 360°; realidade aumentada; avaliação importada de terceiro.

## 2. Catálogo, busca e filtro

**Por que é esquecido:** com trinta produtos tudo cabe numa página; com trezentos, é corredor sem placa.

**O que existe:** categoria é o que a pessoa pensa antes de entrar (hortifrúti, bebidas); filtro é o que decide depois. Os cinco filtros essenciais — preço, nota, cor, tamanho, marca; 57% das lojas não têm todos — mais os do segmento (supermercado: sem lactose, sem glúten, oferta; ingresso: data, setor, lote), só de atributo que aparece na lista. Ordenação: preço nos dois sentidos, nota, mais vendidos (52% não têm), novidades; padrão "mais vendidos", com o rótulo fora do `<select>`. Lista: desktop 50 a 150 por carga, celular 15 a 30, botão "Carregar mais" com lazy loading (item 11), nunca scroll infinito; voltar do produto cai no mesmo ponto. Item da lista: foto em fundo consistente, nome, preço com parcela, nota. Busca normaliza acento e caixa no servidor (`unaccent` no Postgres ou coluna normalizada) e tolera erro de grafia (69% não sugerem correção); sem resultado, dizer claro que não achou, sugerir grafia, categorias próximas e mais vendidos, sem piada (Nielsen Norman); termo preservado no campo; filtro na URL.

**Como conferir:** "açucar" e "acucar" devolvendo o mesmo; "xyzw" devolvendo página útil; filtrar, recarregar e o filtro continuar; abrir produto da página 3 e voltar à página 3.

**Exagero:** busca com IA; motor externo antes de mil produtos; faceta com contagem em tempo real.

## 3. Carrinho

**Por que é esquecido:** é uma lista de linhas, então parece pronto. O abandono médio é 70%, e as causas moram aqui e no checkout.

**O que existe:** carrinho persistente sem login — id opaco em cookie longo, itens no servidor, fundido à conta quando ela existir; quantidade em botões `−`/`+` com campo editável (61% usam `<select>` ou campo solto), total atualizando na hora, sem "Atualizar"; quantidade 0 remove; "Desfazer" por alguns segundos; resumo sempre visível — subtotal, frete por CEP **no carrinho**, desconto, total — porque 40% abandonam por custo que apareceu depois; "faltam R$ 23 para frete grátis" quando existe; cupom atrás de "Tem um cupom?" — aberto, manda a pessoa ao Google e ela não volta. Minicarrinho: `<dialog>` lateral (mãe, item 2) ao adicionar, com item, total, "Continuar" e "Finalizar".

**Como conferir:** adicionar, fechar o navegador, reabrir amanhã e o carrinho estar lá; remover e desfazer; CEP no carrinho mudando o total; cupom inválido com erro ao lado do campo.

**Exagero:** "salvar para depois"; carrinho compartilhável; e-mail de abandono antes de cem pedidos por mês.

## 4. Checkout como o Baymard mede

**Por que é esquecido:** o processamento é do `checkout`, então "está resolvido" — mas o abandono é no formulário antes do link. O checkout médio tem 11 a 15 campos; 8 bastam.

**O que existe:** compra sem cadastro como **botão** com a palavra "sem cadastro", acima de "Entrar" (24% já abandonaram por conta obrigatória; 47% escondem a opção); conta oferecida **depois**, na confirmação, com um clique (84% não fazem). Campos: nome completo num campo só (89% separam; 42% dos usuários erram), e-mail, CPF (nota fiscal e Pix), telefone (o `checkout` exige em cartão), CEP antes do endereço com ViaCEP preenchendo rua, bairro, cidade e UF editáveis (item 5), número, complemento, referência. Resumo do pedido visível, em `<details>` no topo do celular; erro por campo e `autocomplete` (mãe, item 9). Aqui é escolha de método; processamento é lá: Pix com QR **e** copia-e-cola com "Copiar", contagem regressiva e o que acontece ao expirar; cartão com parcelas por extenso e total de cada opção; boleto só sem reserva com prazo (o `checkout` o desliga com `expiraEm`). Nenhum campo de cartão no projeto (`checkout`).

**Como conferir:** contar os campos de um pedido de um item — acima de dez, justificar cada um; completar em aba anônima sem criar conta; CEP preenchendo cidade; Pix expirando e a tela dizendo o que fazer.

**Exagero:** login social; vários endereços salvos antes de cliente recorrente; compra em um clique.

## 5. Entrega e retirada

**Por que é esquecido:** 20% abandonam por entrega lenta, e 41% das lojas dizem "3 a 5 dias úteis" em vez de uma data.

**O que existe:** CEP no produto e no carrinho respondendo custo **e data** ("Chega quinta, 17/09"), calculada com o corte de despacho real da loja. ViaCEP: `GET https://viacep.com.br/ws/{cep}/json/` devolve `logradouro`, `bairro`, `localidade`, `uf`, `ibge`, `ddd`; CEP inexistente devolve `{"erro": "true"}`; malformado, 400. Gratuito e sem SLA: chamar do servidor com limite de 3 s e cair no manual. Cotação: Melhor Envio (CEP origem e destino, cm e kg, OAuth2, sandbox, várias transportadoras numa chamada; guardar a cotação no pedido) ou API dos Correios (Preço e Prazo exigem contrato). Todas as formas no mesmo seletor: envio, retirada com loja e horário, entrega própria com janela ("sábado, 9h–12h") — 50% escondem retirada fora dele. Endereço brasileiro: número com "sem número", complemento visível e opcional (o Baymard manda esconder "linha 2"; aqui bloco e apartamento são reais), referência opcional. Três lojas: o CEP decide a loja que atende e o estoque mostrado (item 9).

**Como conferir:** CEP de outra capital com data diferente; CEP inexistente caindo em digitação manual; retirada mostrando endereço e horário; entrega própria na janela certa no painel.

**Exagero:** rastreio em mapa; roteirização; peso cúbico antes de vender item grande.

## 6. Estoque e reserva

**Por que é esquecido:** dois compradores nunca colidem no teste, e o Pix chega dez minutos depois do esgotado.

**O que existe:** reserva ao iniciar o pagamento, não ao adicionar ao carrinho — `UPDATE ... SET reservado = reservado + n WHERE disponivel - reservado >= n`, sem `SELECT` antes; expiração igual à da cobrança (`calendario.expiracao` em segundos na API Pix do Banco Central, padrão 86.400; ingresso e oferta, 15 a 30 minutos via `expiraEm` do `checkout`), liberada por tarefa agendada monitorada (prontidão 2). Estoque zero temporário continua comprável com prazo estendido e aviso junto ao botão (68% bloqueiam; 30% abandonam ao ver "esgotado"). Ingresso não sobrevende: "Pix confirmou depois de esgotar" é decidido **antes** — estorno automático pelo `checkout` com e-mail, ou honrar de uma reserva técnica de 1% a 2% — e escrito no `CONSTRAINTS.md`.

**Como conferir:** dois navegadores comprando a última unidade, um recebe erro claro; reserva expirada volta no tempo dito; Pix pago após expirar segue o caminho decidido, com e-mail.

**Exagero:** fila virtual; estoque por WebSocket; reserva no carrinho.

## 7. Pedido e pós-compra

**Por que é esquecido:** a venda "acabou" no webhook. Para o cliente, começou.

**O que existe:** número curto e legível (`SC-2026-00184`), distinto do id opaco da URL (`checkout`, regra 1); página de status sem login pelo link do e-mail, com linha do tempo — recebido, pagamento confirmado, em separação, enviado ou pronto para retirada, entregue —, itens, endereço, rastreio com link da transportadora, nota fiscal em PDF (`legal`, item 6). Um e-mail por estado (mãe, item 11), com instrução de Pix pendente no primeiro e endereço e horário no "pronto para retirar"; assunto é o fato: "Pedido SC-2026-00184 enviado". Cancelamento e arrependimento na própria página de status com estorno pelo `checkout` (`legal`, item 5); devolução por formulário com protocolo.

**Como conferir:** pedido de teste percorrendo os cinco estados e os e-mails chegando no celular; link de status em aba anônima; cancelar pela tela e o estorno aparecer na Asaas.

**Exagero:** SMS e WhatsApp por estado; app de rastreio; pedir avaliação antes da entrega.

## 8. Ingresso

**Por que é esquecido:** parece produto sem frete. É produto com lei própria, lote, nome e porta.

**O que existe:** lote com quantidade, preço e data de virada, o próximo visível ("Lote 2 a partir de 20/09 — R$ 80"); ingresso nominal com transferência pela tela e registro; QR único carregando `id` e assinatura (HMAC ou Ed25519 com chave do servidor) para o leitor validar **offline** — confere a assinatura, marca o `id` numa lista local, sincroniza quando a rede volta; reemissão invalida o anterior. Meia-entrada (Lei 12.933): estudante com CIE, jovem de 15 a 29 do CadÚnico, pessoa com deficiência e acompanhante, idoso (Estatuto, art. 23, ao menos 50%); **40% dos ingressos de cada evento** (art. 1º, § 10) — contador que fecha a opção na cota, e o site mostra quantos há e avisa quando acabam (art. 2º, § 1º); comprovação é na porta, e o ingresso diz "meia — apresente o documento". Taxa de conveniência é lícita se "acessível e clara" (STJ, REsp 1.632.928, 2024): linha própria na página do evento e no resumo, nunca só no total.

**Como conferir:** comprar meia até a cota e a opção fechar; validar um QR em modo avião, duas vezes, a segunda recusando; transferir e o QR antigo parar de valer.

**Exagero:** mapa de assentos sem lugar marcado; catraca integrada; app nativo de porta — PWA com câmera resolve.

## 9. Painel do lojista

**Por que é esquecido:** é "admin", fica para depois, e o primeiro pedido é lido no banco.

**O que existe**, atrás de Cloudflare Access (`seguranca-san`): pedidos do dia por status com ação de um clique (separando, enviado com rastreio, pronto para retirada, entregue, cancelar com estorno); produto com variação, foto, estoque, preço e parcelas; ajuste de estoque com motivo; cupom com regra (valor ou percentual, mínimo, validade, uso único por CPF); relatório do dia — pedidos, receita, ticket médio, Pix pendente — que é a prontidão 7 respondida. Multi-loja: `estoque(produto_id, loja_id, quantidade)`, preço por loja só se houver diferença real, pedido ligado à loja que atende. Tabelas com filtro e paginação (`tipo-saas.md`, item 5); os estados, mãe, item 10.

**Como conferir:** a pessoa da loja, sem quem construiu, dá baixa num pedido e ajusta um estoque; o relatório de ontem bate com a Asaas.

**Exagero:** BI; permissão por papel antes de dois operadores; leitor de código de barras.

## 10. Conteúdo e SEO de produto

**Por que é esquecido:** a loja vive em `?id=42`, e o Google indexa a variação errada.

**O que existe** além da mãe (itens 4 e 5): URL estável por produto (`/produto/arroz-tio-joao-5kg`), slug em coluna própria, 301 se mudar; variação por parâmetro (`?tamanho=m`) com uma única canonical no produto base, como o Google pede; categoria indexável com texto próprio; imagem com nome descritivo e `alt`. JSON-LD `Product` com `name`, `image` (mais de uma), `description`, `sku`, `brand`, e `offers` do tipo `Offer` com `price`, `priceCurrency: "BRL"`, `availability`, `itemCondition`, `url`, mais `shippingDetails` e `hasMerchantReturnPolicy` quando forem verdade; `ProductGroup` com `hasVariant` só quando a variação tem preço ou foto própria; `aggregateRating` só com avaliação real. Carrinho, checkout, sucesso e painel com `noindex`.

**Como conferir:** Teste de Resultados Avançados numa URL de produto sem aviso; `curl` da página com variação mostrando a canonical do produto base.

**Exagero:** Merchant Center antes de cinquenta produtos; feed de Shopping; markup de `Review` próprio.

## 11. Desempenho da lista de produtos

**Por que é esquecido:** a lista carrega a foto original de cada produto, e 30 produtos viram 30 MB.

**O que existe** além da mãe (itens 8 e 13): miniatura gerada no tamanho da grade — duas larguras (`400w`, `800w`) em `srcset` com `sizes` real, com `width` e `height`; `loading="lazy"` abaixo das quatro primeiras; `aspect-ratio` no `<a>` da grade; paginação real no servidor (`?pagina=3` responde HTML da página 3, e "Carregar mais" só anexa por cima), com índice na coluna de ordenação; consulta sem `SELECT *` e sem N+1 para preço e estoque.

**Como conferir:** Network na categoria maior: nenhuma miniatura acima de 60 KB, página abaixo de 1,5 MB; `?pagina=3` com JavaScript desligado; `EXPLAIN` da lista sem `Seq Scan` em produtos.

**Exagero:** CDN de imagem paga; virtualização de lista; pré-carregar a página seguinte.

---

## O que fecha este tipo

Os onze itens com evidência: a variação trocando tudo junto a 360 px; "açucar" e "xyzw" na busca; o carrinho sobrevivendo à noite; a compra sem cadastro com o CEP preenchendo endereço; a data de entrega mudando com o CEP; a colisão na última unidade e o Pix tardio no caminho escrito; os e-mails no celular; o QR em modo avião e a cota de meia fechando; a pessoa da loja dando baixa sozinha; o Teste de Resultados Avançados limpo; a categoria maior abaixo de 1,5 MB. Tudo termina no estorno do pedido de teste, conferido na Asaas — e os seis passos do `checkout` rodam de novo na estação 6 e na Passada 5.

Item sem evidência é item aberto, e estação com item aberto não fecha.

Fontes consultadas, para reconferir quando algo parecer velho: Baymard Institute (abandono de carrinho, campos do checkout, guest checkout, carrinho, benchmark de página de produto 2026, imagens, avaliações, produto sem estoque, frete e data de entrega, retirada, filtros e ordenações, produtos por carga, busca e página sem resultado); Nielsen Norman Group; Google Search Central (Merchant listing, Product variants); Banco Central (OpenAPI da API Pix); ViaCEP (testado); Correios (portal de desenvolvedores); Melhor Envio; Lei 12.933/2013; Estatuto do Idoso, art. 23; STJ, REsp 1.632.928; Decreto 5.903/2006, art. 3; Lei 10.962/2004, art. 2º-A.
