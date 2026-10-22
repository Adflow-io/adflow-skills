# Adflow skills

Skills van Adflow, verpakt als private Claude-marketplace. De skills zelf (`SKILL.md`) zijn ook bruikbaar in andere agents.

| Plugin | Wat |
|---|---|
| [`adflow`](plugins/adflow/README.md) | De verbinding met Adflow (MCP). Nodig voor de andere plugins |
| [`adflow-ads`](plugins/adflow-ads/README.md) | Skills voor ads (static en video), van concept-slot tot briefing en copy |

## Installeren (eenmalig)

Je hebt een GitHub-account nodig met toegang tot deze repo.

1. Open Claude (desktop of claude.ai) → **Customize** → **Add marketplace**.
2. Koppel je GitHub-account en geef de Claude GitHub App toegang tot `Adflow-io/adflow-skills`.
3. Vul `Adflow-io/adflow-skills` in, zet **Sync automatically** aan en installeer `adflow` en `adflow-ads`.
4. De Adflow-verbinding (MCP) zit in de plugin `adflow`: log de eerste keer in met je Adflow-account (in Claude Code via `/mcp`). Heb je Adflow ook als connector in claude.ai, zet die dan uit, anders heb je hem dubbel.
5. Zet de connectors voor Google Drive en (voor winners) Meta Ads aan in claude.ai.

Daarna heb je de plugins in Chat, Cowork en Claude Code (daar heten ze `adflow@synced` en `adflow-ads@synced`). Wijzigingen die in `main`
komen, worden vanzelf bijgewerkt.

## Een skill aanpassen

1. Open het bestand op GitHub, bijvoorbeeld `plugins/adflow-ads/skills/meta-copy/SKILL.md`, en klik op het potlood
   (of druk op `.` voor de editor met meerdere bestanden).
2. Kies **Create a new branch and start a pull request** en beschrijf wat je verandert en waarom.
3. De check controleert de frontmatter en de links. Na goedkeuring en merge heeft iedereen de nieuwe versie.

Elke `SKILL.md` begint met frontmatter met `name` (gelijk aan de mapnaam) en een `description`. Claude gebruikt de
`description` om te kiezen wanneer de skill wordt gebruikt, dus schrijf die zorgvuldig.

## Indeling

```
.claude-plugin/marketplace.json   lijst van plugins in deze marketplace
plugins/<plugin>/                 één map per plugin, met eigen .claude-plugin/plugin.json
scripts/check.py                  de check die op elke pull request draait
```

Geen klantdata in deze repo. Klantkennis staat in Adflow, de handleidingen per merk in Drive.
