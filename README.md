# Adflow skills

Skills van Adflow, verpakt als private Claude-marketplace. De skills zelf (`SKILL.md`) zijn ook bruikbaar in andere agents.

| Plugin | Wat |
|---|---|
| [`ads-machine`](plugins/ads-machine/README.md) | Skills en referenties voor Meta-ads (static en video), van concept-slot tot launch |

## Installeren (eenmalig)

Je hebt een GitHub-account nodig met toegang tot deze repo.

1. Open Claude (desktop of claude.ai) → **Customize** → **Add marketplace**.
2. Koppel je GitHub-account en geef de Claude GitHub App toegang tot `Adflow-io/skills`.
3. Vul `Adflow-io/skills` in, zet **Sync automatically** aan en installeer `ads-machine`.
4. Zet de connectors aan die de skills nodig hebben: Adflow, Google Drive en (voor winners) Meta Ads.

Daarna heb je de plugin in Chat, Cowork en Claude Code (daar heet hij `ads-machine@synced`). Wijzigingen die in `main`
komen, worden vanzelf bijgewerkt.

## Een skill aanpassen

1. Open het bestand op GitHub, bijvoorbeeld `plugins/ads-machine/skills/ad-copy/SKILL.md`, en klik op het potlood
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
