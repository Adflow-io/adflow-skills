#!/usr/bin/env python3
"""Checks manifests, skill frontmatter and relative markdown links. Exits 1 on errors."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
errors, warnings = [], []


def rel(path):
    return path.relative_to(ROOT)


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip()
    return fields


marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
for plugin in marketplace["plugins"]:
    source = ROOT / plugin["source"]
    manifest = source / ".claude-plugin/plugin.json"
    if not manifest.is_file():
        errors.append(f"marketplace.json: {plugin['name']} heeft geen {rel(manifest)}")
        continue
    if json.loads(manifest.read_text()).get("name") != plugin["name"]:
        errors.append(f"{rel(manifest)}: name wijkt af van marketplace.json ({plugin['name']})")

    for skill in sorted(source.glob("skills/*/")):
        skill_md = skill / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{rel(skill)}: SKILL.md ontbreekt")
            continue
        fields = frontmatter(skill_md.read_text())
        if fields is None:
            errors.append(f"{rel(skill_md)}: frontmatter ontbreekt of is niet afgesloten met ---")
            continue
        if fields.get("name") != skill.name:
            errors.append(f"{rel(skill_md)}: name moet '{skill.name}' zijn (de mapnaam), is '{fields.get('name')}'")
        if not fields.get("description"):
            errors.append(f"{rel(skill_md)}: description ontbreekt")

for md in sorted(ROOT.rglob("*.md")):
    if ".git" in md.parts:
        continue
    text = md.read_text()
    for target in LINK.findall(text):
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        if not (md.parent / target.split("#")[0]).exists():
            errors.append(f"{rel(md)}: kapotte link naar {target}")
    for name in WIKILINK.findall(text):
        warnings.append(f"{rel(md)}: [[{name}]] verwijst naar een notitie die niet in de repo staat")

for line in warnings:
    print(f"waarschuwing: {line}")
for line in errors:
    print(f"fout: {line}")
print(f"{len(errors)} fouten, {len(warnings)} waarschuwingen")
sys.exit(1 if errors else 0)
