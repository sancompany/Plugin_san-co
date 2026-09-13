#!/usr/bin/env python3
"""Confere a estrutura do marketplace e do plugin san-co.

Uso: python3 scripts/validar.py
Sai com 0 se tudo passou, 1 se algo está errado.
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
erros: list[str] = []
avisos: list[str] = []


def erro(msg: str) -> None:
    erros.append(msg)


def ler_json(caminho: Path):
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except FileNotFoundError:
        erro(f"{caminho.relative_to(RAIZ)}: não encontrado")
    except json.JSONDecodeError as e:
        erro(f"{caminho.relative_to(RAIZ)}: JSON inválido — {e}")
    return None


def frontmatter(caminho: Path) -> dict | None:
    texto = caminho.read_text(encoding="utf-8")
    if not texto.startswith("---"):
        return None
    fim = texto.find("\n---", 3)
    if fim == -1:
        return None
    campos: dict[str, str] = {}
    chave = None
    for linha in texto[3:fim].splitlines():
        if not linha.strip():
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", linha)
        if m:
            chave = m.group(1)
            campos[chave] = m.group(2).strip()
        elif chave and linha.startswith((" ", "\t")):
            campos[chave] += " " + linha.strip()
    return campos


def validar_marketplace() -> list[Path]:
    dados = ler_json(RAIZ / ".claude-plugin" / "marketplace.json")
    if dados is None:
        return []
    for campo in ("name", "owner", "plugins"):
        if campo not in dados:
            erro(f"marketplace.json: falta o campo obrigatório '{campo}'")
    nome = dados.get("name", "")
    if nome and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", nome):
        erro(f"marketplace.json: name '{nome}' não está em kebab-case")
    if not isinstance(dados.get("owner"), dict) or "name" not in dados.get("owner", {}):
        erro("marketplace.json: owner precisa ser um objeto com 'name'")

    caminhos: list[Path] = []
    entradas = dados.get("plugins")
    if not isinstance(entradas, list) or not entradas:
        erro("marketplace.json: 'plugins' precisa ser uma lista não vazia")
        return []
    for i, entrada in enumerate(entradas):
        onde = f"marketplace.json: plugins[{i}]"
        if not isinstance(entrada, dict):
            erro(f"{onde}: precisa ser um objeto")
            continue
        for campo in ("name", "source"):
            if campo not in entrada:
                erro(f"{onde}: falta o campo obrigatório '{campo}'")
        origem = entrada.get("source")
        if isinstance(origem, str) and origem.startswith("./"):
            pasta = RAIZ / origem[2:]
            if not pasta.is_dir():
                erro(f"{onde}: source '{origem}' não existe no repositório")
            else:
                caminhos.append(pasta)
        elif isinstance(origem, str):
            avisos.append(f"{onde}: source '{origem}' não é caminho relativo; não dá para conferir aqui")
    return caminhos


def validar_plugin(pasta: Path) -> None:
    rel = pasta.relative_to(RAIZ)
    manifesto = pasta / ".claude-plugin" / "plugin.json"
    dados = ler_json(manifesto)
    if dados is not None:
        if "name" not in dados:
            erro(f"{rel}/.claude-plugin/plugin.json: falta 'name'")
        versao = dados.get("version")
        if versao is None:
            erro(
                f"{rel}/.claude-plugin/plugin.json: falta 'version' — é ela que faz a "
                "atualização chegar em quem já instalou"
            )
        elif not re.fullmatch(r"\d+\.\d+\.\d+([-+].+)?", str(versao)):
            erro(f"{rel}/.claude-plugin/plugin.json: version '{versao}' não é semântica (x.y.z)")
        if not str(dados.get("description", "")).strip():
            erro(f"{rel}/.claude-plugin/plugin.json: 'description' vazia ou ausente")

    # Componentes moram na raiz do plugin, nunca dentro de .claude-plugin/
    for indevido in ("skills", "commands", "agents", "hooks"):
        if (pasta / ".claude-plugin" / indevido).exists():
            erro(f"{rel}/.claude-plugin/{indevido}/: componente no lugar errado, mova para {rel}/{indevido}/")

    skills = pasta / "skills"
    if not skills.is_dir():
        erro(f"{rel}/skills/: não encontrado")
        return
    pastas = sorted(p for p in skills.iterdir() if p.is_dir())
    if not pastas:
        erro(f"{rel}/skills/: nenhuma skill")
    for skill in pastas:
        arquivo = skill / "SKILL.md"
        if not arquivo.is_file():
            erro(f"{rel}/skills/{skill.name}/: falta SKILL.md")
            continue
        campos = frontmatter(arquivo)
        if campos is None:
            erro(f"{rel}/skills/{skill.name}/SKILL.md: sem frontmatter YAML delimitado por ---")
            continue
        if not campos.get("description", "").strip():
            erro(f"{rel}/skills/{skill.name}/SKILL.md: frontmatter sem 'description'")
        nome = campos.get("name", "").strip()
        if nome and nome != skill.name:
            erro(f"{rel}/skills/{skill.name}/SKILL.md: name '{nome}' difere do nome da pasta")
        # Toda reference citada precisa existir em algum lugar do plugin
        texto = arquivo.read_text(encoding="utf-8")
        citacoes = set(re.findall(r"(?:([A-Za-z0-9_-]+)/)?references/([A-Za-z0-9._-]+\.md)", texto))
        for dona, citada in citacoes:
            alvo = skills / dona / "references" / citada if dona else skill / "references" / citada
            if alvo.is_file():
                continue
            # citação curta pode apontar para a reference de outra skill
            if not dona and any((s / "references" / citada).is_file() for s in pastas):
                continue
            prefixo = f"{dona}/" if dona else ""
            erro(f"{rel}/skills/{skill.name}/SKILL.md: cita {prefixo}references/{citada}, que não existe")


def main() -> int:
    pastas = validar_marketplace()
    for pasta in pastas:
        validar_plugin(pasta)

    for aviso in avisos:
        print(f"aviso: {aviso}")
    if erros:
        print()
        for e in erros:
            print(f"ERRO: {e}")
        print(f"\n{len(erros)} problema(s). Nada publicado.")
        return 1
    plural = "s" if len(pastas) != 1 else ""
    print(f"OK — marketplace e {len(pastas)} plugin{plural} conferidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
