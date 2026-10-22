# Adflow skills

De Claude-plugin `adflow`: de verbinding met Adflow plus de skills waarmee we ads maken, van concept-slot tot briefing
en copy. Verspreid als private marketplace. De skills zelf (`SKILL.md`) zijn ook bruikbaar in andere agents.

Skills roep je aan als `adflow:<skill>`, bijvoorbeeld `adflow:slots`. Overzicht en pijplijn:
[plugins/adflow/README.md](plugins/adflow/README.md).

## De plugin gebruiken (eenmalig instellen)

Je hebt een GitHub-account nodig dat lid is van `Adflow-io`.

1. Open Claude (desktop of claude.ai) → **Customize** → **Add marketplace**.
2. Koppel je GitHub-account en geef de Claude GitHub App toegang tot `Adflow-io/adflow-skills`.
3. Vul precies `Adflow-io/adflow-skills` in, zet **Sync automatically** aan en installeer `adflow`.
4. Log de eerste keer in bij Adflow met je eigen Adflow-account (in Claude Code via `/mcp`, server
   `plugin:adflow:mcp`). Heb je Adflow ook als connector in claude.ai, zet die dan uit, anders heb je hem dubbel.
5. Zet de connectors voor Google Drive en (voor winners) Meta Ads aan in claude.ai.

Daarna heb je de plugin in Chat, Cowork en Claude Code. Wat in `main` komt, wordt vanzelf bijgewerkt.

**Lukt het toevoegen niet** ("Repository niet toegankelijk")? Controleer of je de uitnodiging voor `Adflow-io` hebt
geaccepteerd en of in Claude (Settings → Connectors → GitHub) hetzelfde GitHub-account gekoppeld is. Verbreek de
koppeling en koppel opnieuw als je twijfelt.

## Skills aanpassen met Claude Code

Je past skills aan door Claude Code te vragen wat je wilt veranderen. Claude volgt de regels in
[AGENTS.md](AGENTS.md): eigen branch, checks, pull request. Nicky keurt goed, daarna heeft iedereen de nieuwe versie.

### Eenmalig instellen

```bash
brew install gh
gh auth login
gh auth setup-git
gh repo clone Adflow-io/adflow-skills ~/Projects/adflow-skills
```

### Zo werk je

1. Open Claude Code in de map `adflow-skills` (desktop: Code-tab → map kiezen; terminal: `cd ~/Projects/adflow-skills`
   en `claude`).
2. Zeg wat je wilt, zo concreet mogelijk. Bijvoorbeeld:
   - *"`meta-copy` schrijft te lange headlines. Maximaal 40 tekens, en geef 3 opties in plaats van 1."*
   - *"Maak een nieuwe skill `tiktok-copy`, gebaseerd op `meta-copy`, voor TikTok-captions."*
   - *"`video-voorzet` moet ook altijd een CTA-richting geven."*
3. Claude maakt een branch, past de skill aan en draait de checks. Lees wat hij veranderde.
4. Test de skill voor een echt merk: open een nieuwe sessie met `claude --plugin-dir ./plugins/adflow` en roep de
   skill aan, of stel een vraag die hem zou moeten activeren.
5. Tevreden? Vraag Claude om een pull request te openen. Zet erin wat je testte.
6. Nicky kijkt mee en merget. Binnen een paar minuten heeft iedereen de nieuwe versie.

Wil je opnieuw beginnen of een wijziging weggooien? Zeg dat tegen Claude ("gooi deze branch weg en begin opnieuw
vanaf main").

### Spelregels

- **Eén onderwerp per pull request.** Klein en makkelijk na te kijken.
- **Geen klantdata in de repo**: geen klantnamen, reviews, winners, cijfers of briefs, ook niet als voorbeeld.
  Klantkennis staat in Adflow, de handleidingen per merk in Drive.
- **Merkspecifieke regels horen in de Drive-handleiding van het merk**, niet in een skill.
- **De `description` bepaalt wanneer Claude een skill gebruikt.** Pas je die aan, test dan of Claude de skill nog
  kiest bij een gewone vraag.
- **Hernoemen of verwijderen alleen in overleg.** Gebruikers en andere skills gebruiken de naam.
- **Geen gekopieerde tekst** uit cursussen, boeken of swipe files. Eigen woorden, met bronvermelding.

Alle regels voor de agent staan in [AGENTS.md](AGENTS.md).

## Indeling

```
AGENTS.md                         regels voor agents (CLAUDE.md verwijst ernaar)
.claude-plugin/marketplace.json   de marketplace
plugins/adflow/
  .claude-plugin/plugin.json      naam en beschrijving van de plugin
  .mcp.json                       de verbinding met Adflow
  skills/<naam>/SKILL.md          de skills
  references/                     frameworks die meerdere skills delen
scripts/check.py                  de check die op elke pull request draait
```
