#!/usr/bin/env bash
# Script de setup do ambiente de nuvem do Claude Code.
# Cole o conteúdo em claude.ai/code -> ambiente -> engrenagem -> "Setup script".
#
# Roda antes de o Claude Code subir, que é a única hora em que dá para instalar
# plugin para a sessão que vai começar.
#
# san-co 1.2.2   <- mude esta linha ao publicar versão nova: editar o script
#                   refaz o snapshot do ambiente e a próxima sessão de todo
#                   mundo entra com a versão nova.
set -euo pipefail

claude plugin marketplace add sancompany/Plugin_san-co \
  || claude plugin marketplace update san-co

claude plugin install san-co@san-co

claude plugin list
