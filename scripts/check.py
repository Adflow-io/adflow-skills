#!/usr/bin/env python3
"""Checks manifests, skill frontmatter and relative markdown links. Exits 1 on errors."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
LOCAL_PATH = re.compile(r"(?:/Users/|/home/|[A-Z]:\\)\w[^\s`)]*")
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
MAX_SKILL_LINES = 300
TRIGGER = re.compile(r"\b(gebruik (bij|voor|als|wanneer)|use (for|when|this|it)|trigger)", re.I)
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
    manifest_data = json.loads(manifest.read_text())
    if manifest_data.get("name") != plugin["name"]:
        errors.append(f"{rel(manifest)}: name wijkt af van marketplace.json ({plugin['name']})")
    if "version" in manifest_data:
        errors.append(f"{rel(manifest)}: geen version gebruiken, anders krijgen gebruikers wijzigingen pas na een bump")

    for skill in sorted(source.glob("skills/*/")):
        skill_md = skill / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{rel(skill)}: SKILL.md ontbreekt")
            continue
        text = skill_md.read_text()
        fields = frontmatter(text)
        if fields is None:
            errors.append(f"{rel(skill_md)}: frontmatter ontbreekt of is niet afgesloten met ---")
            continue
        if len(skill.name) > 64 or not SKILL_NAME.fullmatch(skill.name):
            errors.append(f"{rel(skill)}: mapnaam mag alleen kleine letters, cijfers en streepjes bevatten (max 64)")
        if fields.get("name") != skill.name:
            errors.append(f"{rel(skill_md)}: name moet '{skill.name}' zijn (de mapnaam), is '{fields.get('name')}'")
        description = fields.get("description", "")
        if not description:
            errors.append(f"{rel(skill_md)}: description ontbreekt")
        elif description[0] in ">|":
            errors.append(f"{rel(skill_md)}: zet de description op één regel")
        elif len(description) > 1024:
            errors.append(f"{rel(skill_md)}: description is {len(description)} tekens, maximaal 1024")
        elif description[0] not in "\"'" and (": " in description or " #" in description):
            errors.append(f"{rel(skill_md)}: description bevat ': ' of ' #'; zet hem tussen dubbele aanhalingstekens, anders is het geen geldige YAML en kan Adbase de skill niet lezen")
        elif not TRIGGER.search(description):
            warnings.append(f"{rel(skill_md)}: description zegt niet wanneer de skill gebruikt wordt; voeg 'Gebruik bij \"...\"' toe met woorden die een gebruiker typt")
        lines = text.count("\n") + 1
        if lines > MAX_SKILL_LINES:
            errors.append(f"{rel(skill_md)}: {lines} regels, maximaal {MAX_SKILL_LINES}; verplaats uitleg naar references/")

for md in sorted(ROOT.rglob("*.md")):
    if ".git" in md.parts:
        continue
    text = md.read_text()
    for target in LINK.findall(re.sub(r"`[^`\n]*`", "", text)):  # links in code are examples
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        if not (md.parent / target.split("#")[0]).exists():
            errors.append(f"{rel(md)}: kapotte link naar {target}")
    for path in LOCAL_PATH.findall(text):
        errors.append(f"{rel(md)}: pad op een eigen computer ({path}); gebruik een relatieve link")
    for name in WIKILINK.findall(text):
        warnings.append(f"{rel(md)}: [[{name}]] verwijst naar een notitie die niet in de repo staat")

for line in warnings:
    print(f"waarschuwing: {line}")
for line in errors:
    print(f"fout: {line}")
print(f"{len(errors)} fouten, {len(warnings)} waarschuwingen")
sys.exit(1 if errors else 0)
