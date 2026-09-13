# Site institucional e landing page — o que este tipo tem além da referência-mãe

Referência por tipo da estação 5, para página pública sem login cujo trabalho é apresentar e converter: o sancocore.com.br, o site do Mostraí, a landing de um serviço. O que é comum a qualquer site é apontado por número em `desenvolvimento-web.md`. Acessibilidade é a Lei 5; cookies, termos e CNPJ no rodapé são a skill `legal`; analytics é prontidão 7.

**Regra que atravessa tudo:** aqui a evidência que fecha é o lead chegando — enviado de um celular real, caindo na caixa certa, com resposta automática de volta. Site bonito sem lead testado é protótipo.

---

## 1. Anatomia da página que converte

**Por que é esquecido:** a home nasce como capa — foto, slogan, três ícones — e ninguém responde "o que esta página quer que a pessoa faça?".

**O que existe:** acima da dobra, três coisas: uma frase que diz o que é e para quem, um único botão de ação, uma prova. A Nielsen Norman mediu em 2018 57% do tempo de leitura na primeira tela e 17% na segunda: a primeira decide, mas precisa sinalizar que há mais (texto cortando na borda, nunca seta "role"). Abaixo, nesta ordem: o problema que o cliente reconhece; o que se faz, em até três blocos; prova social (item 4); preço ou faixa (item 2); o mesmo CTA; rodapé. Comprimento segue o conteúdo: a pessoa rola quando há motivo. Landing de campanha tem **uma** ação e nenhum menu; home institucional tem menu (mãe, item 1) e um único CTA repetido no topo, no meio e no fim. O botão nomeia o resultado ("Pedir orçamento"), nunca "Enviar".

**Como conferir:** a 360 px, sem rolar, ler em voz alta o que é, para quem e o que fazer; mais de um botão de ação distinto, justificar no `CONSTRAINTS.md`.

**Exagero:** carrossel no topo; vídeo de fundo; teste A/B antes de cem leads por mês.

## 2. Estrutura mínima de páginas

**Por que é esquecido:** o template traz doze páginas e todas vão ao ar com texto de exemplo — ou o oposto, uma página só, tudo em âncora.

**O que existe:** home; "Serviços" (página por serviço só com conteúdo próprio: o que faz, para quem, o que entrega, faixa de preço); "Sobre" com pessoa, cidade e história curta; "Contato" com todos os canais (item 5); preço quando existe preço — a NN/g mostra comprador B2B indo ao concorrente quando o site esconde valor, e faixa ou "a partir de" resolve quando o exato depende de escopo — só onde a contratação não acontece no site; página que vende online segue o Decreto 7.962 (`legal`, `obrigacoes-brasil.md`, item 5: preço sem "a partir de"); Política e Termos (skill `legal`). Tudo na lista de telas do `docs/funcional.md` (mãe, item 1). O que **não** precisa existir: blog sem calendário (dois posts de 2024 envelhecem o site inteiro), "Clientes" com três logos, "Trabalhe conosco", FAQ com perguntas que ninguém fez.

**Como conferir:** cada página do mapa responde uma pergunta que alguém faria antes de contratar; a que não responde sai.

**Exagero:** mais de sete páginas no primeiro lançamento; versão em inglês sem cliente estrangeiro.

## 3. Copy em português para leitura em F

**Por que é esquecido:** o texto é escrito para ser lido inteiro, e ninguém lê inteiro. O eyetracking da NN/g mostra leitura em F — duas passadas horizontais no topo, uma vertical pela esquerda.

**O que existe:** título que diz o que é e para quem, na língua do cliente ("Sites e sistemas para pequenas empresas de Belo Horizonte"); os dois primeiros parágrafos carregam o essencial; cada subtítulo começa pelas duas palavras que mais informam; a primeira frase fala do cliente, não de "nós". Sem jargão de agência ("soluções", "sinergia") e sem superlativo que a CONAR pode mandar comprovar ("o melhor").

**Como conferir:** ler só o título e as duas primeiras palavras de cada subtítulo e ver se dá para explicar o serviço; `grep -riE "soluç|sinergi|inovad|melhor do|líder" src/` devolve vazio ou cada ocorrência tem prova.

**Exagero:** copywriter antes do terceiro cliente; manual de tom de voz.

## 4. Prova social honesta

**Por que é esquecido:** o depoimento chega por WhatsApp, vira citação com iniciais, e ninguém guarda a mensagem.

**O que existe:** depoimento com nome completo, contexto e o que foi feito ("emissão de nota caiu de 40 para 5 minutos" vale mais que "excelente profissional"); logo só com autorização; número só se for verdadeiro hoje e recontável. A regra é o Código do CONAR, porque site é publicidade: o art. 27 exige que alegação sobre fato seja comprovável quando pedida, e o Anexo Q exige que testemunhal de consumidor reflita experiência real, tenha autorização por escrito, seja de uso contemporâneo e fique documentado pelo anunciante. Por baixo, o CDC art. 37 trata como enganosa a informação capaz de induzir a erro — "garantia de resultado" é a alegação que mais cobra. No repositório, `docs/provas.md`: cada depoimento com data e forma de autorização (print, e-mail), cada número com o que o comprova. A NN/g avisa que prova escassa vira prova contra: um depoimento bem contado supera uma seção magra.

**Como conferir:** cada depoimento e número do site tem linha no `docs/provas.md` com evidência; nenhuma citação com só iniciais.

**Exagero:** widget de avaliações; contador animado; selo "verificado" criado pela própria empresa.

## 5. CTA, formulário e o destino do lead

**Por que é esquecido:** o formulário funciona e o e-mail cai numa caixa que ninguém abre. A auditoria da HBR em 2.241 empresas achou 23% que nunca responderam e média de 42 horas; responder em até uma hora dava sete vezes mais chance de qualificar o contato.

**O que existe:** três a cinco campos (NN/g): nome, e-mail **ou** WhatsApp (a pessoa escolhe), o que precisa em texto livre; nunca CPF, faixa de orçamento nem "como nos conheceu" no primeiro contato. Construção e Turnstile: mãe, item 9. A página de contato mostra também e-mail e WhatsApp em texto — a NN/g documenta rejeição a site que só oferece formulário — e diz o prazo ("Respondemos em até um dia útil") e cumpre. Depois de enviar: estado de sucesso com `noindex` (mãe, item 6) que repete o prazo e oferece o WhatsApp para urgência; resposta automática em até um minuto, do endereço monitorado (mãe, item 11); o lead vai para **dois** lugares — o e-mail de quem responde e uma linha em planilha ou tabela, porque a planilha responde "quantos leads este mês". No Pages é uma Function (item 9).

**Como conferir:** enviar do celular, cronometrar a resposta automática, achar a linha na planilha, ver a notificação no celular de quem responde. Sem os quatro, aberto.

**Exagero:** CRM antes de trinta leads por mês; formulário em etapas; agendamento embutido na primeira versão.

## 6. WhatsApp como canal

**Por que é esquecido:** o botão verde entra por plugin, cobre o CTA no celular, e o link abre sem mensagem — a conversa começa com "oi".

**O que existe:** link no formato oficial `https://wa.me/5531999999999?text=…` — número internacional só com dígitos (sem `+`, zeros, parênteses ou hífen: o `+` falha no WhatsApp Web, o `00` falha no Android) e mensagem pré-preenchida com `encodeURIComponent` dizendo de onde veio e o que quer, uma por página. Botão flutuante só se o formulário não for o CTA principal: canto inferior direito, `aria-label`, `padding-bottom` no rodapé para não cobrir botão nem texto legal — overlays concorrentes (chat, cookie, barra fixa) são a reclamação mais comum da NN/g em mobile. Número comercial (WhatsApp Business), nunca o pessoal. Abuso: janela que abre sozinha, "1 mensagem nova" falsa, disparo sem opt-in — o WhatsApp bane o número.

**Como conferir:** o link abre com a mensagem preenchida no celular, no WhatsApp Web e no desktop; a 360 px o botão não cobre CTA, banner de cookies nem rodapé.

**Exagero:** API oficial do WhatsApp para uma pessoa; chatbot; catálogo no app duplicando o site.

## 7. SEO local e de negócio

**Por que é esquecido:** o cliente pesquisa "site para clínica em BH", não o nome da empresa, e o Google mostra o Perfil da Empresa antes do site.

**O que existe:** Google Business Profile com nome igual ao da fachada (cidade ou palavra-chave no nome viola as diretrizes), categoria mínima, endereço real ou — para quem atende a domicílio — endereço oculto e área de até umas duas horas de deslocamento, telefone e site. NAP — nome, endereço, telefone — idêntico caractere a caractere no perfil, no rodapé, no JSON-LD e na política. JSON-LD `LocalBusiness` na página de contato com `name`, `address` completo, `telephone`, `url`, `openingHoursSpecification` e `geo`; `Organization` na home é a mãe, item 5. Título e `description` por página são a mãe, item 4; aqui o título carrega serviço e cidade quando o negócio é local. Página por cidade ou serviço só com conteúdo real e diferente: a política de spam do Google chama de "doorway" as páginas por região que levam ao mesmo lugar.

**Como conferir:** Teste de Resultados Avançados sem erro; `grep` do telefone e do endereço em `src/` devolvendo uma grafia só; nome da empresa em janela anônima mostrando perfil e site juntos.

**Exagero:** dez páginas de cidade; diretório pago; ferramenta de rank.

## 8. Rastreamento com consentimento

**Por que é esquecido:** o GA4 entra pelo snippet padrão, o pixel do Meta junto, e o cookie está no navegador antes de qualquer pergunta.

**O que existe:** primeiro a decisão — o que medir é prontidão 7, e medição própria em tabela não usa cookie de terceiro nem pede banner (skill `legal`, guia da ANPD). Entrando GA4, Ads ou pixel, entra o banner nos termos da ANPD, e o Consent Mode faz as tags do Google obedecê-lo: antes de carregar a tag, `gtag('consent','default',{ad_storage:'denied', ad_user_data:'denied', ad_personalization:'denied', analytics_storage:'denied'})`; ao aceitar, `gtag('consent','update',{…:'granted'})`; `wait_for_update: 500` se o banner carrega assíncrono. Os quatro sinais são exigência do Google desde março de 2024 só para tráfego do EEE; no Brasil quem obriga é a LGPD — o padrão negado atende os dois. Pixel do Meta segue a mesma lógica com a API dele.

**Como conferir:** janela anônima sem clicar no banner: Application sem `_ga`, Network sem `google-analytics.com`; após aceitar, os dois aparecem; após recusar, continua limpo.

**Exagero:** Tag Manager para uma tag; plataforma de consentimento paga; mapa de calor.

## 9. Hospedagem estática no Cloudflare Pages

**Por que é esquecido:** o deploy funciona pelo `pages.dev`, e domínio, preview e formulário ficam para "depois".

**O que existe:** projeto ligado ao repositório, build e diretório de saída no painel, `main` como produção. `_headers` e `_redirects` na pasta de saída (até 100 regras de cabeçalho e 2.000 redirecionamentos; 301 e cache são a mãe, itens 5 e 13). Domínio customizado com a zona no Cloudflare (o apex exige a zona; subdomínio aceita CNAME externo); Redirect Rule de `https://www.*` para `https://${1}` com 301; Bulk Redirect de `<projeto>.pages.dev` para o domínio. Preview: todo push fora de `main` vira `<branch>.<projeto>.pages.dev`, já com `X-Robots-Tag: noindex`, e com Cloudflare Access (Settings → General) quando mostra cliente antes da hora. Formulário sem servidor: `functions/api/contato.js` exportando `onRequestPost(context)`, lendo `await context.request.formData()`, validando o Turnstile (mãe, item 9), mandando o e-mail pela API do provedor com a chave em variável de ambiente, e redirecionando para a página de sucesso; conta na cota gratuita do Workers, 100 mil chamadas por dia. O que custa uma tarde: `_headers` **não** se aplica à resposta de Function — CSP e afins nela vão no código.

**Como conferir:** `curl -sI` em `www.` e em `<projeto>.pages.dev` devolvendo 301 para o domínio; `curl -sI https://<branch>.<projeto>.pages.dev | grep -i x-robots`; formulário com a chave do provedor removida devolvendo erro tratado.

**Exagero:** Worker separado para um formulário; KV ou D1 para lead que cabe numa planilha; staging além do preview.

## 10. Desempenho específico de landing

**Por que é esquecido:** a home institucional tem o pior LCP do projeto por ser a mais "visual": foto de 3 MB, YouTube, mapa e chat antes do primeiro texto.

**O que existe:** a imagem hero é a única com `fetchpriority="high"` (mãe, item 8), cortada para celular e tela larga (`<picture>` com `media`), abaixo de 200 KB; texto do hero em HTML, nunca na imagem. Terceiro embarcado só sob interação, com facade: YouTube via `lite-youtube-embed` ou pôster próprio que injeta o `<iframe>` no clique (o web.dev mede cerca de 500 KB por embed); mapa como imagem estática linkando para o Google Maps; chat só depois do primeiro clique. Todo `<iframe>` com `width`, `height` e `loading="lazy"`. Limiares são prontidão 4.

**Como conferir:** Network na home com filtro de terceiros vazio até a primeira interação; LCP apontando para a imagem hero, não para um `<iframe>`.

**Exagero:** animação de entrada por seção; parallax; fonte extra só para o título.

## 11. Manutenção pós-lançamento

**Por que é esquecido:** site institucional não tem deploy semanal, e ninguém recebe alerta quando o preço do site deixa de ser o cobrado.

**O que existe:** lista do que envelhece no `RUNBOOK.md`, revisada a cada trimestre: preço; equipe; depoimento (o cliente ainda existe e ainda autoriza); números; horário e endereço (site, perfil do Google e JSON-LD juntos); ano do rodapé gerado no build, nunca digitado; links externos; portfólio com projeto fora do ar; política contra o inventário (skill `legal`). Certificado, DNS e uptime são prontidão 2 e Passada 4.

**Como conferir:** a lista existe com data da última revisão abaixo de noventa dias; `grep -E "20[0-9]{2}" src/` devolve só datas que são conteúdo.

**Exagero:** CMS para site que muda quatro vezes por ano; monitor de conteúdo.

---

## O que fecha a estação 5 neste tipo

Os onze itens com evidência, somados aos catorze da mãe: a leitura a 360 px sem rolar; o mapa enxuto; o `grep` de jargão vazio; o `docs/provas.md` completo; o lead de celular na caixa, na planilha e com resposta cronometrada; o `wa.me` nos três clientes; o `LocalBusiness` sem erro e o NAP numa grafia só; a janela anônima sem cookie antes do aceite; os três `curl` do Pages; a Network sem terceiro antes da interação; a lista de envelhecimento datada. A Passada 2 reconfere no ar.

Item sem evidência é item aberto, e estação com item aberto não fecha.

Fontes consultadas, para reconferir quando algo parecer velho: Nielsen Norman Group (Scrolling and Attention, Fold Manifesto, F-Pattern, Contact Us Pages, Show Price, Overlay Overload, Social Proof); Harvard Business Review, "The Short Life of Online Sales Leads"; Código do CONAR (art. 27 e Anexo Q) e CDC art. 37; Google Search Central (`LocalBusiness`, título, spam); diretrizes do Google Business Profile; Consent Mode e política de consentimento da UE do Google; docs do Cloudflare Pages e Redirect Rules; web.dev (embeds) e Lighthouse (facades); FAQ do WhatsApp (click to chat).
