#!/usr/bin/env bash
# Empacota plugins/san-co/ no arquivo .plugin que o Cowork instala.
# Uso: ./scripts/empacotar-plugin.sh [diretorio-de-saida]
set -euo pipefail

raiz="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
origem="$raiz/plugins/san-co"
saida="${1:-$raiz/dist}"

[ -f "$origem/.claude-plugin/plugin.json" ] || {
  echo "erro: $origem/.claude-plugin/plugin.json não encontrado" >&2
  exit 1
}

versao="$(grep -o '"version"[[:space:]]*:[[:space:]]*"[^"]*"' "$origem/.claude-plugin/plugin.json" | head -1 | sed 's/.*"\([^"]*\)"$/\1/')"
[ -n "$versao" ] || { echo "erro: version não encontrada no plugin.json" >&2; exit 1; }

mkdir -p "$saida"
destino="$saida/san-co.plugin"
rm -f "$destino"

# O .plugin é um zip com o conteúdo do plugin na raiz do arquivo.
( cd "$origem" && zip -r -q -X "$destino" . -x '.DS_Store' -x '__MACOSX/*' )

echo "san-co $versao -> $destino"
