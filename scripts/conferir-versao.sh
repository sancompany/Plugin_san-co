#!/usr/bin/env bash
# Confere que o version do plugin.json subiu quando algo em plugins/san-co/ mudou.
# Uso: ./scripts/conferir-versao.sh <ref-base>     (ex.: origin/main)
set -euo pipefail

base="${1:-origin/main}"
manifesto="plugins/san-co/.claude-plugin/plugin.json"

if ! git rev-parse --verify --quiet "$base" >/dev/null; then
  echo "aviso: base '$base' não existe aqui; nada a comparar."
  exit 0
fi

mudou="$(git diff --name-only "$base"...HEAD -- plugins/san-co/ || true)"
if [ -z "$mudou" ]; then
  echo "OK — nada mudou em plugins/san-co/; version não precisa subir."
  exit 0
fi

ler_versao() { python3 -c "import json,sys; print(json.load(sys.stdin).get('version',''))"; }

nova="$(ler_versao < "$manifesto")"
antiga="$(git show "$base:$manifesto" 2>/dev/null | ler_versao || true)"

if [ -z "$antiga" ]; then
  echo "OK — não havia version na base; publicando $nova."
  exit 0
fi

if [ "$nova" = "$antiga" ]; then
  cat >&2 <<MSG
ERRO: plugins/san-co/ mudou e o version continua $antiga.

  $(echo "$mudou" | sed 's/^/  /')

Suba o version em $manifesto. É ele que faz a atualização
chegar em quem já tem o plugin instalado — sem bump, quem instalou fica na versão antiga.

  correção pequena ou ajuste de texto -> último número
  regra ou reference nova             -> número do meio
  mudança que altera a esteira        -> primeiro número
MSG
  exit 1
fi

maior="$(printf '%s\n%s\n' "$antiga" "$nova" | sort -V | tail -1)"
if [ "$maior" != "$nova" ]; then
  echo "ERRO: version andou para trás: $antiga -> $nova." >&2
  exit 1
fi

echo "OK — version $antiga -> $nova."
