# Verificações automáticas de segurança — o que rodar, onde, e como

As três classes em que a leitura é cega — dependência vulnerável, segredo no histórico, configuração efetiva de produção — só são cobertas por ferramenta. Este arquivo traz o comando de cada uma, onde ela entra na esteira, e o que conta como evidência.

**Regra que atravessa tudo:** ferramenta que depende de alguém lembrar de rodar não roda. O que dá para automatizar vai para o CI; o que só existe em produção entra na estação 6 e na varredura final, com a saída anexada.

---

## Onde cada uma entra na esteira

| Verificação | Onde é ligada | Onde roda depois |
|---|---|---|
| Dependência vulnerável | estação 3, junto com o CI | todo push + agendamento semanal |
| Segredo no histórico | estação 3 | todo push, histórico inteiro |
| Análise estática | estação 3 (projeto com backend próprio) | todo push |
| Cabeçalho, cookie e TLS | estação 6 | estação 6 e Passada 1 da varredura |
| Origem alcançável por fora | estação 6 | estação 6 e Passada 5 da varredura |

Ligar as três primeiras é trabalho de **estação 3**, não de estação 6. Ligadas tarde, elas descobrem na véspera do lançamento o que descobririam na primeira semana.

---

## 1. Dependência vulnerável

O auditor do próprio gerenciador de pacotes resolve, e falha o build no que importa:

```bash
npm audit --audit-level=high     # Node
pip-audit                        # Python
```

Ligar também o alerta automático do repositório (Dependabot no GitHub), que abre aviso sozinho quando uma vulnerabilidade nova sai — inclusive em projeto parado.

**O agendamento semanal não é excesso.** Vulnerabilidade é publicada sem o seu código mudar; sem execução periódica, um projeto que ninguém toca há dois meses tem dois meses de exposição não vista.

## 2. Segredo no histórico

`gitleaks` varre o histórico inteiro, não só os arquivos de hoje:

```bash
gitleaks detect --source . --redact --exit-code 1
```

`--redact` impede que o próprio log da verificação imprima o segredo encontrado — sem isso, o achado vaza no log do CI, que costuma ser mais visível que o commit original.

Ligar junto a **proteção de push** do GitHub, que barra a credencial antes de ela entrar. Barrar na entrada vale mais que encontrar depois: segredo que chegou ao histórico precisa ser **revogado**, não apagado — reescrever histórico não alcança clone, fork nem cache de quem já baixou.

## 3. Análise estática

Regras prontas pegam padrão perigoso repetido que passa na leitura:

```bash
semgrep scan --config p/owasp-top-ten --config p/secrets --error
```

## 4. Cabeçalho, cookie e TLS (só em produção)

```bash
curl -sSI https://<dominio-de-producao>
```

O que precisa estar na resposta: `Strict-Transport-Security`, `Content-Security-Policy` (ou `-Report-Only` na primeira semana de relatório, como manda `construir/references/desenvolvimento-web.md`, item 12 — a bloqueante é conferida na varredura final), `X-Content-Type-Options: nosniff`, `Referrer-Policy`, proteção contra enquadramento (`frame-ancestors` na CSP ou `X-Frame-Options`), e cookie de sessão com `Secure`, `HttpOnly` e `SameSite`. Conferir também que `http://` redireciona para `https://`.

Avaliador público de configuração serve de segunda opinião, nunca de fonte única — ele não conhece as exceções do seu projeto.

## 5. Origem alcançável por fora (só em produção)

```bash
curl -sSI https://<endereco-direto-da-hospedagem>
```

Respondendo o mesmo que o domínio, a proteção que vive no domínio está contornável (skill `seguranca-san`, armadilha 1 do Access).

---

## O workflow para colar

Caminho: `.github/workflows/seguranca.yml`. **Arquivo em `.github/workflows/` é escrito à mão pelo dono** — ferramenta remota não escreve ali (skill `leis`, aditivo que a ferramenta recusa).

Este é um ponto de partida: conferir a versão de cada ação e do gitleaks contra a documentação atual antes de colar, como manda a regra de consultar a fonte da skill `construir`.

```yaml
name: Segurança

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 9 * * 1'   # toda segunda, 06:00 em Brasília

permissions:
  contents: read

jobs:
  dependencias:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: npm
      - run: npm ci
      - run: npm audit --audit-level=high

  segredos:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0        # sem isso, varre só o último commit
      - name: Instalar gitleaks
        run: |
          VERSAO=8.28.0         # conferir a atual antes de colar
          curl -sSL "https://github.com/gitleaks/gitleaks/releases/download/v${VERSAO}/gitleaks_${VERSAO}_linux_x64.tar.gz" \
            | tar -xz gitleaks
      - run: ./gitleaks detect --source . --redact --exit-code 1

  estatica:
    runs-on: ubuntu-latest
    container: semgrep/semgrep
    steps:
      - uses: actions/checkout@v4
      - run: semgrep scan --config p/owasp-top-ten --config p/secrets --error
```

Detalhes que costumam ser perdidos ao adaptar: **`fetch-depth: 0`** — sem ele o checkout traz um commit só e a varredura de segredo perde exatamente o que ela existe para achar; e a ação de gitleaks distribuída no marketplace pede licença para repositório de organização, motivo de o binário ser baixado direto aqui.

---

## O que conta como evidência

Saída da ferramenta, colada ou anexada. **"Rodei e passou" não fecha item nenhum** — é a mesma regra da varredura final, e existe porque afirmação sem saída é indistinguível de comando que nem chegou a rodar.

Achado que não será corrigido agora vira exceção no `CONSTRAINTS.md`, com o motivo e o prazo. Silêncio, não.

## O que não fazer

**Scanner ativo contra produção enquanto ela processa dinheiro real.** Varredura automatizada cria cobrança, cadastro e bloqueio de verdade, e apaga a fronteira entre teste e incidente. Precisando desse tipo de teste, é contra instância local — e só em sistema que é seu, nunca contra serviço de terceiro, mesmo integrado ao projeto.
