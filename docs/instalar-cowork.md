# Instalar no Cowork

O Cowork não usa marketplace: ele instala **um arquivo `.plugin`**, que é a pasta `plugins/san-co/` compactada.

## Pegar o arquivo

Na página de **Releases** deste repositório, baixe o `san-co.plugin` da versão mais recente. Cada versão publicada leva o arquivo anexado, gerado pela própria CI a partir da pasta que está no repositório — é literalmente a mesma pasta que o Claude Code instala pelo marketplace.

Se preferir gerar na sua máquina, com o repositório clonado:

```bash
./scripts/empacotar-plugin.sh
# escreve dist/san-co.plugin
```

## Instalar

No Cowork, instalar plugin a partir do arquivo e apontar para o `san-co.plugin` baixado. Versão nova é o mesmo caminho, com o arquivo novo.

## A regra que não muda

**Cada superfície instala a sua cópia; nenhuma herda da outra.** O que você instalou no Cowork não aparece na sessão de código, e o contrário também não. Publicou versão nova:

- **Sessões de nuvem**: nada a fazer, a próxima sessão já entra atualizada.
- **Claude Code no terminal**: `/plugin marketplace update san-co` (ou auto-update ligado).
- **Cowork**: baixar o `.plugin` novo e instalar.

Só uma superfície atualizada é o mesmo projeto medido por duas réguas diferentes.
