# PWA — o que o app instalável tem além da referência-mãe

Referência por tipo da estação 5, para o app que uma pessoa (ou poucas) abre pelo ícone todo dia no celular e precisa que funcione em rede ruim: o dashboard pessoal da SAN & CO., a Fairy. O que é comum a qualquer site — `<head>`, manifest básico, `theme-color`, viewport, imagens, os seis estados de cada tela, orçamento de performance — está em `desenvolvimento-web.md` e é apontado por número. Acessibilidade é a Lei 5; segurança é a skill `seguranca-san`.

**Regra que atravessa tudo:** a evidência que fecha é o app instalado num Android e num iPhone reais, aberto pelo ícone, em modo avião, mostrando dado do último acesso com carimbo de hora. Instalável no DevTools sem isso é protótipo.

---

## 1. Quando PWA vale — e quando é site responsivo ou app nativo

**Por que é esquecido:** "PWA" entra no escopo como adjetivo, sem ninguém dizer qual capacidade paga o custo do service worker.

**O que existe:** a decisão no `CONSTRAINTS.md`, por quatro critérios. **Uso diário pelo ícone** — menos de uma vez por semana é site responsivo. **Offline** — precisa mostrar algo sem rede, é PWA. **Notificação** — Android faz push no navegador; iOS só com o app na Tela de Início, desde o 16.4. **Câmera e arquivo** — `<input capture>` e Web Share cobrem quase tudo; Bluetooth, NFC, tarefa em segundo plano de verdade ou loja é nativo. Desde o iOS 26 qualquer site adicionado à Tela de Início abre por padrão como web app, com ou sem manifest (WebKit, Safari 26.0); continua fora no iOS: Background Sync, Web Share Target, `shortcuts`, `beforeinstallprompt`. Para um usuário, sem loja e sem revisão da Apple, PWA é o padrão da San & Co. para app de uso diário.

**Como conferir:** os quatro critérios respondidos por escrito; três "não" tiram o service worker do escopo.

**Exagero:** nativo ou Capacitor para app de um usuário; PWA para site institucional.

## 2. Manifest completo para instalar

**Por que é esquecido:** o manifest da mãe (item 4) já existe com dois ícones, e ninguém volta nele.

**O que existe**, em `manifest.webmanifest`: o que o Chrome exige para o prompt — `name` ou `short_name`, `icons` com 192 e 512, `start_url`, `display: "standalone"` (ou `minimal-ui`), `prefer_related_applications` ausente ou `false` — mais o que faz o app se comportar: `id` fixo (`"/"`), porque sem ele a identidade é o `start_url`, e mudá-lo depois cria um segundo app; `start_url` com rastreio (`"/?origem=pwa"`) para a prontidão 7 distinguir abertura pelo ícone; `short_name` de até uns 12 caracteres; `theme_color` e `background_color` — o esquema escuro fica na `<meta name="theme-color" media="(prefers-color-scheme: dark)">`, o manifest não tem media; dois ícones separados, `purpose: "any"` sem margem e `purpose: "maskable"` de 512 com a marca dentro do círculo de raio 40%, nunca `"any maskable"` no mesmo arquivo; `screenshots` para a instalação rica: ao menos uma, entre 320 e 3.840 px, lado maior até 2,3× o menor, `form_factor: "narrow"` (celular) ou `"wide"` (desktop), mesma proporção dentro de cada grupo, até oito, com `sizes` e `type`; `description` de até uns 300 caracteres; `shortcuts` com duas ou três ações (`name`, `url`, ícone 96×96) — Android e desktop mostram no toque longo, iOS ignora.

**Como conferir:** DevTools → Application → Manifest sem erro em Installability; "Show only the minimum safe area for maskable icons" marcado e a marca inteira dentro; a captura no diálogo de instalação do Android.

**Exagero:** dez tamanhos de ícone; `related_applications`; `display_override`.

## 3. Instalação: o botão próprio e a instrução do iOS

**Por que é esquecido:** o Chrome mostra o mini-infobar uma vez, a pessoa dispensa, e o app nunca é instalado.

**O que existe:** Chrome no Android e no desktop dispara `beforeinstallprompt` quando o item 2 bate (desde o Chrome 108/112 o service worker não é exigido para instalar pelo menu; o prompt automático ainda pesa engajamento — visitas nos últimos 14 dias). O padrão: `event.preventDefault()`, guardar o evento, mostrar um botão "Instalar" em Configurações ou num aviso discreto após a segunda visita, chamar `evento.prompt()` no clique, esconder em `appinstalled`. Nunca antes do primeiro dado. No iOS não há evento nem prompt: com `navigator.standalone !== true` em iPhone, mostrar uma vez a instrução com o ícone de compartilhar — "Toque em Compartilhar, depois em Adicionar à Tela de Início". Dentro do app, `(display-mode: standalone)` esconde botão e instrução.

**Como conferir:** instalar de verdade num Android e num iPhone; o ícone abre no `start_url` sem barra de endereço; `matchMedia("(display-mode: standalone)").matches` verdadeiro.

**Exagero:** modal de instalação no primeiro acesso; biblioteca só para o banner do iOS.

## 4. Service worker por tipo de recurso

**Por que é esquecido:** o exemplo copiado faz `CacheFirst` de tudo, e a correção urgente de sexta nunca chega ao celular.

**O que existe:** Workbox, com `sw.js` gerado no build. Uma estratégia por tipo: **precache** do shell — HTML de entrada, CSS e JS com hash, fontes, ícones — via `precacheAndRoute(self.__WB_MANIFEST)`, que grava revisão por arquivo e limpa o velho; **`CacheFirst`** só para o que tem hash no nome (mãe, item 13); **`StaleWhileRevalidate`** para imagem e o resto estático, com `ExpirationPlugin({maxEntries: 60, maxAgeSeconds: 30 * 24 * 3600})`; **`NetworkFirst`** com `networkTimeoutSeconds: 3` para dado de leitura da API, para o app abrir com o último dado quando a rede demora; **nenhuma rota** para o que é autenticado e muda — sessão, `POST`, pagamento (skill `checkout`), dado de terceiro. Página offline via `setCatchHandler` devolvendo o `offline.html` precacheado (mãe, item 6). `sw.js` na raiz, com `Cache-Control: no-cache` no `_headers` do Pages.

**O erro clássico** — versão velha para sempre: HTML sem revisão ou em `CacheFirst`, `sw.js` com cache longo, ou nenhum tratamento do estado *waiting* — o SW novo instala mas só assume quando todas as abas fecham, e em app instalado isso leva dias. O padrão do Workbox: no app, `workbox-window` com o evento `waiting` mostrando a faixa "Nova versão disponível — recarregar"; no clique, `wb.messageSkipWaiting()` e, em `controlling`, `location.reload()`; no `sw.js`, o `message` que chama `self.skipWaiting()`. Nunca `skipWaiting()` automático no `install`: a página velha pede um chunk que o SW novo já apagou.

**Como conferir:** Application → Service Workers com "Offline" marcado, o app abre com dado; deploy de uma mudança de texto e a faixa no celular sem fechar o app; na aba Network, a API autenticada nunca com `(ServiceWorker)` na coluna Size.

**Exagero:** service worker escrito à mão; cache de vídeo; navigation preload antes de medir.

## 5. Offline de verdade

**Por que é esquecido:** "funciona offline" vira "não mostra erro 500 offline". Sem rede, a tela precisa ser útil.

**O que existe:** cada tela com dado tem um sétimo estado além dos seis da mãe (item 10): **desatualizado** — o dado do último acesso com carimbo "atualizado às 14h32" e o aviso fixo "sem conexão, mostrando dados de …". Escrita sem rede vai para uma fila em IndexedDB (`fila_acoes`: id, tipo, corpo, criado_em, tentativas) e a tela confirma "salvo, envia quando voltar a rede"; a fila é drenada ao abrir o app, no evento `online` e a cada leitura bem-sucedida. `workbox-background-sync` faz isso no Chrome, mas Safari não tem Background Sync — drenar ao abrir é a regra. Conflito: com um usuário, a última escrita vence e o servidor guarda `atualizado_em` para descartar resposta mais velha que a fila; com mais de um, 409 e a tela mostra as duas versões. `navigator.onLine` só dá dica (MDN: "inerentemente não confiável" — rede local sem internet é "online"); a verdade é a requisição falhar ou o `NetworkFirst` cair no cache, e é isso que liga o aviso.

**Como conferir:** modo avião, abrir pelo ícone, ver dado com carimbo; criar um registro, sair do modo avião, ver no banco o `criado_em` de quando foi digitado; derrubar só o servidor com Wi-Fi ligado e ver o mesmo aviso.

**Exagero:** CRDT; sincronizar tudo; interface de conflito antes de existir dois usuários.

## 6. Dado local

**Por que é esquecido:** `localStorage` resolve no primeiro dia e ninguém lê a política de evicção.

**O que existe:** `localStorage` só para preferência pequena (tema, último filtro) — 5 MiB, síncrono, string; dado de verdade em IndexedDB por uma camada fina (`idb`) com versão de esquema. A cota é grande (Chrome e Safari 17+, até 60% do disco por origem), mas o navegador apaga tudo da origem de uma vez, por LRU, e o Safari apaga o dado escrito por script depois de **sete dias sem interação** — exceto para app na Tela de Início. Por isso `navigator.storage.persist()` num gesto do usuário na primeira gravação importante, nunca no carregamento (Chrome concede em silêncio para app instalado ou com engajamento; Firefox pergunta). O que **não** fica no dispositivo: token de longa duração fora de cookie `HttpOnly`, chave de API, segredo, dado pessoal de terceiro além do que a tela offline precisa — o celular é perdido, emprestado, sem senha (skill `seguranca-san`; inventário na skill `legal`).

**Como conferir:** `await navigator.storage.persisted()` verdadeiro no app instalado; Application → Storage → "Clear site data" e o app se recupera do servidor sem tela branca; `grep -r "localStorage.setItem" src/` com cada chave justificada.

**Exagero:** SQLite em WASM; criptografia no cliente fora de cofre de senhas e documentos — lá ela é obrigatória (`seguranca-san`, "Cofre").

## 7. Notificação push

**Por que é esquecido:** o pedido de permissão vai no carregamento, o usuário nega, e não há segunda chance.

**O que existe:** Android recebe push no navegador; iOS só com o app na Tela de Início (16.4+) e `display: "standalone"`, e a permissão precisa vir de um toque — o iOS ignora pedido sem gesto. A permissão é pedida quando a pessoa liga algo que precisa dela ("Avisar quando o pagamento cair"), com uma tela própria antes do diálogo do sistema; nunca no primeiro acesso. Servidor: par VAPID gerado uma vez (`npx web-push generate-vapid-keys`), pública no app, privada no cofre; `setVapidDetails("mailto:…", pub, priv)`; `sendNotification(subscription, payload, {TTL})`; assinatura por usuário no banco; 404 ou 410 do serviço de push apaga a assinatura. Desde o iOS 18.4 existe Declarative Web Push — JSON com `"web_push": 8030`, `notification.title` e `navigate` — que dispensa o SW para exibir; enviar nesse formato serve os dois mundos. Merece push: evento externo que ela esperaria ver na hora (pagamento confirmado, prazo hoje). Não merece: "você não abre há três dias".

**Como conferir:** push chegando no iPhone e no Android com o app fechado; permissão negada não gerando novo pedido; assinatura expirada removida do banco.

**Exagero:** serviço pago de push para um usuário; push de marketing.

## 8. Ergonomia de celular

**Por que é esquecido:** é construído no desktop com a janela estreita; polegar, barra e teclado só aparecem no aparelho.

**O que existe:** área de toque de 44×44 pt (Apple) ou 48 dp (Material) na ação principal — o mínimo da WCAG 2.5.8 é 24 px e não basta para uso diário; ação principal e navegação embaixo, ao alcance do polegar, em barra de até cinco itens; `viewport-fit=cover` na meta viewport com `padding-bottom: env(safe-area-inset-bottom)` na barra inferior e `-top` no cabeçalho, senão o conteúdo fica atrás do indicador de gesto; `100dvh`, nunca `100vh`, que mede com a barra do navegador recolhida; `interactive-widget=resizes-content` para o teclado não cobrir o campo, com `scrollIntoView` no foco como reserva; `user-scalable=no` nunca (Lei 5); voltar do sistema fecha modal e volta de tela, não sai do app — cada tela é uma entrada no histórico e o modal é `<dialog>` com entrada própria; hover nunca é o único sinal; animação atrás de `prefers-reduced-motion`; campo em 16 px (mãe, item 3).

**Como conferir:** no iPhone e no Android reais, tela por tela: nada atrás da barra inferior; campo visível com teclado aberto; voltar do sistema em toda tela e modal.

**Exagero:** gesto de arrastar próprio; gaveta lateral; animação de transição entre telas.

## 9. Desempenho em celular médio

**Por que é esquecido:** o orçamento da mãe (item 13) foi medido no desktop, e o celular de R$ 1.000 leva quatro vezes mais para rodar o mesmo JavaScript.

**O que existe:** orçamento menor para o que carrega na abertura — cerca de 200 KB de JS comprimido, o resto por rota; teste no DevTools → Performance com o preset calibrado "Mid-tier mobile" (sem ele, CPU 4× slowdown) e rede "Slow 4G"; ícone e avatar com `srcset` `1x`/`2x`, foto por largura (mãe, item 8); shell renderizado do precache antes de qualquer dado.

**Como conferir:** abertura pelo ícone com dado em cache abaixo de 2 s no preset calibrado; INP da prontidão 4 no celular real.

**Exagero:** SSR só por performance em app de um usuário; virtualização de lista com menos de 500 itens.

## 10. Atualização e versionamento do app

**Por que é esquecido:** o deploy sobe, o SW novo fica esperando, e o usuário reporta bug já corrigido.

**O que existe:** versão vinda do build (`APP_VERSION`), visível em Configurações e no log de erro (prontidão 2); a faixa do item 4 é como o usuário sabe que atualizou, com o changelog em uma linha ("Novo: exportar em CSV") tirado da mensagem do commit ou do spec da versão (`docs/specs/`); migração do IndexedDB no `upgrade` do `openDB`, uma função por versão, idempotente; dado que não migra é descartado com aviso, nunca corrompido em silêncio. Ícone e nome: no Android o WebAPK atualiza quando o app é aberto; no iOS só reinstalando — decidir antes do primeiro usuário.

**Como conferir:** subir versão com esquema novo, abrir com o banco velho e ver o dado sobreviver; a versão nova em Configurações.

**Exagero:** atualização forçada; migração com rollback.

## 11. Integração com o sistema

**Por que é esquecido:** cada capacidade entra porque existe, não porque alguém pediu.

**O que existe**, só quando um fluxo pede: Web Share — `navigator.share({title, url, files})` atrás de `navigator.canShare`, com "copiar link" de reserva; câmera — `<input type="file" accept="image/*" capture="environment">`, sem `getUserMedia` (o desktop ignora o `capture` e abre o seletor); arquivo — `showSaveFilePicker` só no Chromium e o iOS não tem File System Access público, então exportar é `<a download>` de um Blob; `shortcuts` do item 2; `navigator.setAppBadge(n)` no ícone (iOS 16.4+ instalado) e `clearAppBadge()` ao abrir. Web Share Target (só Android com WebAPK) e protocolo próprio (só desktop) ficam fora.

**Como conferir:** cada integração testada num iPhone e num Android, com a reserva testada no desktop.

**Exagero:** Contact Picker; Wake Lock; File Handling; Bluetooth.

---

## O que fecha este tipo

Os onze itens com evidência, além da mãe: os quatro critérios no `CONSTRAINTS.md`; o Manifest sem erro no DevTools; o app instalado num Android e num iPhone reais; a faixa de nova versão após um deploy; a API autenticada nunca vindo do service worker; o dado com carimbo em modo avião e a fila drenada ao voltar; `persisted()` verdadeiro; o push nos dois aparelhos com o app fechado; as telas conferidas contra barra inferior, teclado e botão voltar; a abertura abaixo de 2 s no preset calibrado; a migração rodando sobre o banco velho; cada integração com a reserva de desktop.

Sobre instalabilidade: **o Lighthouse não tem mais categoria PWA** — saiu na 12.0.0 (abril de 2024) depois de o Chrome afrouxar os critérios. O que substitui: a seção Installability do painel Application → Manifest no DevTools, que lista o erro exato; o `curl` do manifest e dos ícones com 200 e `Content-Type` certo; e a instalação real nos dois aparelhos, a única prova que vale para o iOS.

Item sem evidência é item aberto, e estação com item aberto não fecha.

Fontes consultadas, para reconferir quando algo parecer velho: web.dev/learn/pwa (instalação, manifest, atualização, integração com o SO); Chrome for Developers (critérios de instalação revisados, instalação rica, `id` do manifest, ícones maskable, Workbox, DevTools para PWA, throttling calibrado, Lighthouse 12); MDN (`beforeinstallprompt`, cotas e evicção, `navigator.onLine`, meta viewport, `capture`); WebKit (Web Push no iOS 16.4, badging, Declarative Web Push no 18.4, armazenamento no Safari 17, Safari 26.0); Apple HIG (44 pt); WCAG 2.2 (2.5.8); biblioteca `web-push`; caniuse (Background Sync).
