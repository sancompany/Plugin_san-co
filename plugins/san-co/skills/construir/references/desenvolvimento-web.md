# Desenvolvimento web — o que todo site ou app da San & Co. tem

Referência-mãe da estação 5; as referências por tipo (`tipo-institucional.md`, `tipo-saas.md`, `tipo-ecommerce.md`, `tipo-pwa.md`) apontam para cá, e um projeto pode ser de mais de um tipo — loja com painel do lojista lê a de e-commerce e a de SaaS. Cada item diz por que é esquecido, o que existe, como conferir e o que é exagero para uma pessoa (Lei 0). Não repete o que mora em outro lugar: acessibilidade é a Lei 5; Core Web Vitals, SPF/DKIM e analytics são a prontidão; legal, segurança e pagamento são as skills de mesmo nome.

**Regra que atravessa tudo:** item fecha com evidência — a tag no HTML servido, o cabeçalho que voltou, a tela no celular. "Está no template" não fecha nada.

---

## 1. Mapa de páginas antes de tela

**Por que é esquecido:** a primeira tela nasce no editor, a segunda copia a primeira, e URL e menu viram consequência em vez de decisão.

**O que existe:** a lista de telas do `docs/funcional.md` (seção 3) com a URL de cada uma, quem acessa e de onde se chega — fechada na estação 4, antes do primeiro componente. URL minúscula, com hífen, sem extensão nem parâmetro para conteúdo (`/servicos/consultoria`); identificador público opaco. Menu com até sete itens; em mobile, até quatro ficam visíveis e só acima disso entra o botão "Menu" — com a palavra, não só o ícone: navegação escondida corta a descoberta quase pela metade (Nielsen Norman). Breadcrumb só a partir de três níveis, começando em "Início", item atual sem link.

**Como conferir:** cada URL da lista responde 200 e nenhuma no ar está fora dela; menu por teclado a 360 px.

**Exagero:** mega-menu; busca interna em site de dez páginas.

## 2. Design system de uma pessoa

**Por que é esquecido:** o primeiro botão é escrito onde surgiu, o segundo é copiado, e a primeira troca de cor encosta em oito arquivos (lição nº 1).

**O que existe:** um único arquivo de tokens (`src/tokens/tokens.css`, a pasta da Lei 1) com custom properties, nenhum valor solto fora dele. Tipografia em escala de razão fixa (1,2 ou 1,25 sobre 1 rem); espaçamento em múltiplos de 4 px; cor com papel semântico (`--cor-acao`, `--cor-erro`), nunca `--azul-3`; raio e sombra em dois degraus. Grade fluida (`max-width`, `padding` lateral, `grid` com `gap`) e três breakpoints em `em`. Componentes nascem nesta ordem, porque cada um usa o anterior: botão, campo, link, cartão, cabeçalho e rodapé, `<dialog>` nativo, tabela, aviso. Tema escuro só se pedido.

**Como conferir:** `grep -rE "#[0-9a-fA-F]{3,6}|[0-9]+px" src/ --include=*.css` fora de `src/tokens/` devolve vazio; mudar `--cor-acao` muda todo botão.

**Exagero:** Storybook; biblioteca de componentes publicada; tokens em JSON com pipeline.

## 3. Tipografia web

**Por que é esquecido:** a fonte chega do Google Fonts em seis pesos, e o texto salta a cada carregamento.

**O que existe:** primeira opção é a pilha do sistema (`system-ui, sans-serif`): zero download, zero salto. Webfont só se a marca exige: só WOFF2, self-hosted, no máximo dois arquivos (variável se há vários pesos), subset latino, `font-display: swap` com fallback ajustado por `size-adjust`, `preload` só da fonte do corpo. Corpo em 1 rem (16 px) no mínimo — também em campo de formulário, senão o Safari do iPhone dá zoom ao focar; linha de 45 a 75 caracteres (`max-width: 65ch`); `line-height` 1,5.

**Como conferir:** aba Network filtrada por fonte; texto visível na primeira pintura com rede lenta simulada.

**Exagero:** mais de dois pesos; fonte de ícone (usar SVG); tamanho por breakpoint além de `clamp()` no título.

## 4. O `<head>` completo

**Por que é esquecido:** o `<head>` de exemplo do framework vai ao ar com título "Vite App" e sem imagem de compartilhamento.

**O que existe**, num único layout: `<html lang="pt-BR">`; `charset="utf-8"`; `viewport` `width=device-width, initial-scale=1`; `<title>` no padrão `Página · Nome do site` (na home só o nome), único — o Google não fixa tamanho, mas trunca e reescreve título repetitivo; `description` própria; `canonical` absoluta e autorreferente; `og:title`, `og:description`, `og:url` e `og:image` em URL absoluta, 1200×630, com uma imagem padrão para as páginas sem a sua; `twitter:card` `summary_large_image`; os três ícones que bastam hoje (Evil Martians): `favicon.ico` 32×32, `icon.svg`, `apple-touch-icon.png` 180×180; `manifest.webmanifest` com `icon-192.png` e `icon-512.png`; `theme-color`.

**Como conferir:** `curl -s https://dominio.com.br/rota | grep -E "<title>|canonical|og:image"` no HTML servido; a URL num validador de compartilhamento; ícones e manifest respondendo 200.

**Exagero:** `og:image` gerada por página; dezenas de tamanhos de ícone; `keywords`.

## 5. SEO técnico básico

**Por que é esquecido:** não quebra nada, e o efeito aparece semanas depois no Search Console.

**O que existe:** `sitemap.xml` com URL absoluta e `lastmod` verdadeiro (o Google ignora `priority` e `changefreq`); `robots.txt` com `Sitemap:`. `noindex` (meta ou cabeçalho `X-Robots-Tag`) em tudo que não é público — área logada, página de sucesso, preview — sem bloquear essa página no `robots.txt`, senão o Google nunca lê o `noindex`. URL que muda ganha 301 (`_redirects` no Pages: `/antiga /nova 301`; sem código o padrão é 302). JSON-LD `Organization` na home com `name`, `url`, `logo` (mínimo 112×112), `sameAs`, `contactPoint`, e `WebSite`. Sobre JavaScript, o Google em 2026 renderiza tudo com Chromium atualizado e em março tirou da documentação o conselho de testar com JS desligado — mas a renderização entra em fila, e crawlers de IA em geral não executam JS: o que precisa ser encontrado vem no HTML do servidor.

**Como conferir:** `curl -sI https://dominio.com.br/antiga | grep -i location`; Teste de Resultados Avançados no JSON-LD; inspeção de URL no Search Console numa pública e numa privada.

**Exagero:** dados estruturados além do que o tipo do projeto pede; ferramenta paga de SEO.

## 6. Páginas que ninguém desenha

**Por que é esquecido:** não são "funcionalidade", e o usuário as encontra num dia ruim.

**O que existe:** `404.html` na raiz (no Pages, sem ele toda rota devolve a home com 200); 500 como HTML estático que não depende da aplicação; manutenção com previsão de volta e 503 com `Retry-After`; "sem permissão" que diz o que fazer; sucesso e erro de formulário como estado da página ou página própria com `noindex`; offline só com service worker (`tipo-pwa.md`). Todas no layout do site, com caminho de volta e sem código interno.

**Como conferir:** abrir `/nao-existe`, forçar um 500, entrar em rota administrativa deslogado, enviar formulário com o servidor derrubado.

**Exagero:** ilustração por erro; busca dentro da 404.

## 7. Formato brasileiro

**Por que é esquecido:** o exemplo da documentação é americano e o servidor está em UTC.

**O que existe:** `Intl` em vez de biblioteca — `Intl.NumberFormat("pt-BR", {style: "currency", currency: "BRL"})`; `Intl.DateTimeFormat("pt-BR", {dateStyle: "short", timeZone: "America/Sao_Paulo"})`; `Intl.Collator("pt-BR").compare` para ordenar com acento. Fuso numa constante, passado explicitamente. Dinheiro em centavos inteiros. Máscara é apresentação; validação roda no servidor: CPF e CNPJ por módulo 11 rejeitando sequência repetida; **CNPJ é alfanumérico desde julho de 2026** (raiz e ordem aceitam letras, os verificadores seguem numéricos, cada caractere vale o código ASCII menos 48) — validador só numérico rejeita empresa nova; CEP `00000-000`; telefone guardado em E.164. `inputmode="numeric"` em CPF e CEP, `"tel"`, `"email"`, `"decimal"`. Validadores em `src/br/`, importados.

**Como conferir:** autoteste com CPF válido, inválido e repetido; CNPJ com letra; data às 23h de Brasília contra o banco em UTC; "Ágata" antes de "Bruno".

**Exagero:** biblioteca de máscara; segundo idioma antes de existir usuário que precise.

## 8. Imagens e mídia

**Por que é esquecido:** a foto de 4 MB fica bonita no monitor e vira o LCP e a conta de egresso (prontidão 4 e 5).

**O que existe:** `<picture>` com AVIF, WebP e `<img>` JPEG de segurança; `srcset` com descritores de largura e `sizes` real; `width` e `height` em toda imagem (o navegador reserva o espaço); `loading="lazy"` abaixo da dobra; a imagem principal **sem** lazy e com `fetchpriority="high"` — em uma ou duas por página, senão a prioridade deixa de valer. Logo e ícone em SVG. Vídeo com `preload="none"` e pôster; autoplay só mudo, curto e respeitando `prefers-reduced-motion`. Otimização no build (`sharp`), nunca à mão.

**Como conferir:** Lighthouse sem aviso de formato nem de dimensão; nenhuma imagem acima de 300 KB na aba Network; `alt` em todas (Lei 5).

**Exagero:** CDN de imagem paga para vinte fotos; mais de três larguras no `srcset`.

## 9. Formulários

**Por que é esquecido:** o caminho feliz funciona no primeiro dia; erro, duplo clique e autofill errado aparecem no cliente.

**O que existe:** `<label for>` visível em todo campo (placeholder não é rótulo); `autocomplete` com os valores da especificação — `name`, `email`, `tel`, `postal-code`, `address-level2` (cidade), `address-level1` (estado), `new-password`, `current-password`, `one-time-code`; validação nativa (`required`, `type`, `pattern`) com `:user-invalid`, repetida no servidor; erro por campo, ao lado dele, via `aria-describedby`, dizendo o que fazer; botão desabilitado com "Enviando…" durante a requisição; em erro, o digitado permanece. Anti-bot: Cloudflare Turnstile em modo gerenciado, gratuito — `<div class="cf-turnstile" data-sitekey="…">` dentro do `<form>`, campo `cf-turnstile-response` validado no servidor em `POST https://challenges.cloudflare.com/turnstile/v0/siteverify` com `secret` e `response`; o token vale cinco minutos, uma vez. Modo invisível exige citar o adendo de privacidade do Turnstile na política (skill `legal`).

**Como conferir:** autofill caindo no campo certo; erro por campo com texto preservado; duplo clique gerando uma requisição; token vazio recusado pelo servidor.

**Exagero:** biblioteca de formulário para três campos; reCAPTCHA visível.

## 10. Os estados de cada tela

**Por que é esquecido:** com dado de teste a lista nunca está vazia, nunca demora, nunca falha.

**O que existe**, em toda tela que mostra dado: vazio (o que é isso e a primeira ação, com botão); carregando (nada abaixo de 1 s; skeleton com a forma do conteúdo até 10 s em página inteira, spinner em módulo, barra de progresso acima disso ou em upload — Nielsen Norman); erro (o que houve, o que fazer, tentar de novo; placeholder nunca vira dado falso, lição nº 18); sucesso (confirmação e caminho seguinte); sem permissão (item 6); lista longa (paginação; o tamanho da página é da referência do tipo). Os seis entram no spec da tela antes do código.

**Como conferir:** conta nova sem dado; rede lenta; API devolvendo 500; conta com 500 registros — tela por tela, sem amostragem.

**Exagero:** animação entre estados; scroll infinito.

## 11. E-mail transacional

**Por que é esquecido:** é a última coisa construída, com o template do provedor e remetente `noreply@`. Autenticação do domínio é prontidão 1.

**O que existe:** template base (`src/emails/base.html`) com logo, corpo, um botão e rodapé com razão social, CNPJ e endereço (skill `legal`); texto puro gerado junto, link em linha própria; remetente com nome e endereço monitorado, nunca `noreply`; assunto de até uns 50 caracteres dizendo o fato ("Pedido 1234 confirmado"); data e hora absolutas no fuso de Brasília, nunca "hoje"; um assunto por e-mail; transacional e marketing em subdomínios separados. Lista dos e-mails no `docs/funcional.md`.

**Como conferir:** cada e-mail da lista disparado de verdade e aberto no celular; texto puro legível; botão levando à página certa, logado ou não.

**Exagero:** editor visual; personalização além do nome; MJML para cinco e-mails.

## 12. Segurança de construção

**Por que é esquecido:** é assunto da estação 6, então nada é feito na 5 — e refazer o carregamento de script depois custa dez vezes mais. O ciclo é da skill `seguranca-san`; aqui só o que é decisão de construção.

**O que existe:** CSP desde o primeiro deploy, em `Content-Security-Policy-Report-Only`, no `_headers` do Pages ou no servidor — a base do web.dev: `script-src 'nonce-…' 'strict-dynamic'; object-src 'none'; base-uri 'none'` (site estático usa hash em vez de nonce), mais `frame-ancestors 'none'`; lista de domínios é o modelo que o Google considera contornável. Isso obriga a decidir cedo que não há `onclick` inline nem `eval`. HTML de usuário nunca entra por `innerHTML`: `textContent` para texto; DOMPurify e sanitização no servidor quando precisa ser HTML — `setHTML()` nativo ainda não é Baseline. `target="_blank"` já implica `noopener`; `noreferrer` só para não enviar o `Referer`. Variável que chega ao navegador é pública.

**Como conferir:** `curl -sI https://dominio.com.br | grep -i content-security`; console sem violação no site inteiro; `grep -r innerHTML src/` com cada ocorrência justificada.

**Exagero:** CSP bloqueante antes de uma semana de relatório limpo.

## 13. Performance na construção

**Por que é esquecido:** o limiar é medido na estação 6, quando o bundle já tem 900 KB por causa do primeiro `npm install`.

**O que existe:** orçamento no `CONSTRAINTS.md` antes do primeiro componente — ordem de grandeza da série Performance Inequality Gap: cerca de 350 KB de JavaScript comprimido e 150 KB de HTML, CSS e fontes. Antes de instalar dependência, a escada da skill `construir`: `<dialog>`, `<details>`, `popover`, `:has()` e container queries são Baseline e substituem biblioteca. CSS e JS com hash no nome e `Cache-Control: public, max-age=31536000, immutable` (no Pages, `_headers` em `/assets/*`); HTML com `no-cache`. CSS crítico inline só se o Lighthouse apontar FCP ruim — a maioria não precisa (web.dev). Script de terceiro só com `defer`, justificado numa linha.

**Como conferir:** tamanho do build contra o orçamento; `curl -sI …/assets/app.abc123.js | grep -i cache-control`; Lighthouse local antes de cada merge, sem perseguir 100.

**Exagero:** code splitting em site de cinco páginas; service worker fora de `tipo-pwa.md`.

## 14. Ambiente de desenvolvimento e build

**Por que é esquecido:** funciona na máquina de quem construiu, e a pessoa número dois (prontidão 6) descobre que "rodar" são onze comandos de memória.

**O que existe:** `.editorconfig` na raiz (`indent_style`, `end_of_line = lf`, `charset = utf-8`); lint e formatter no CI — Biome quando é só JS/TS, ESLint e Prettier quando há plugin que só existe lá; runtime fixado no manifesto **e** no `.nvmrc` (lição nº 33); um comando para rodar, um para verificar (`npm run check`: lint, formato, tipos, testes) e um para build, os três no `README.md`; `.env.example` e `.gitignore` pela Lei 3; variável pública com o prefixo da plataforma.

**Como conferir:** clone em pasta limpa rodando os três comandos só pelo `README.md`; chaves do `.env.example` e do `.env` batendo num `diff`; CI vermelho com um `console.log` esquecido.

**Exagero:** monorepo; Docker para app estático; matriz de CI com três versões de Node.

---

## O que fecha a estação 5

Os catorze itens com evidência, na versão local: a lista de telas batendo com as rotas; o `grep` de valor solto vazio; no máximo dois arquivos de fonte; o `curl` do `<head>`; `noindex` e 301 conferidos; as páginas que ninguém desenha abertas (as cinco do item 6; a offline só em PWA); o autoteste brasileiro passando; a imagem principal com `fetchpriority`; os quatro testes de formulário; os seis estados de cada tela; cada e-mail no celular; a CSP em report-only sem violação; o build dentro do orçamento; o clone limpo rodando pelo `README.md`. A Passada 2 reconfere tudo no ar.

Item sem evidência é item aberto, e estação com item aberto não fecha.

Fontes consultadas, para reconferir quando algo parecer velho: Google Search Central (JavaScript SEO, sitemaps, `noindex`, canonical, título, Organization); web.dev (fontes, LCP, imagens, cache HTTP, CSS crítico, formulários, CSP estrita, Baseline 2026); MDN (`autocomplete`, `Intl`, `noopener`, Sanitizer API); Nielsen Norman Group (menus escondidos, breadcrumbs, skeleton screens, erros); docs do Cloudflare Turnstile e Pages; Evil Martians ("How to Favicon", 2026); Postmark; Receita Federal (CNPJ alfanumérico); Performance Inequality Gap, de Alex Russell.
