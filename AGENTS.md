# AGENTS.md

Regels voor AI-agents (Claude Code, Codex, Cursor) die in deze repo skills aanpassen. Marketeers sturen de agent aan;
de agent houdt zich aan deze regels, ook als de vraag anders klinkt. Twijfel je, vraag het de gebruiker in plaats van te
gokken.

## Wat deze repo is

Eén Claude-plugin, `adflow`, verspreid als private marketplace. Alles wat in `main` komt, staat binnen een paar minuten
bij iedereen die de plugin heeft, ook bij klanten later. Een fout in `main` is dus meteen een fout bij iedereen.

```
.claude-plugin/marketplace.json    de marketplace (niet aanpassen zonder Nicky)
plugins/adflow/
  .claude-plugin/plugin.json       naam en beschrijving van de plugin (niet aanpassen zonder Nicky)
  .mcp.json                        de verbinding met Adflow (niet aanpassen zonder Nicky)
  skills/<naam>/SKILL.md           één map per skill; hier werk je
  skills/<naam>/*.md               voorbeelden of hulpbestanden die alleen bij die skill horen
  references/*.md                  frameworks die meerdere skills delen
scripts/check.py                   de check die op elke pull request draait
```

Skills roep je aan als `adflow:<naam>`, bijvoorbeeld `adflow:slots`.

## Werkwijze (verplicht)

1. **Begin altijd vanaf een verse `main`:** `git switch main && git pull`.
2. **Maak een branch** met een korte naam die zegt wat er verandert: `git switch -c skill/meta-copy-headlines`.
   Werk nooit direct op `main` en push nooit naar `main`.
3. **Eén onderwerp per pull request.** Eén skill aanpassen, of één nieuwe skill. Geen opruimacties erbij.
4. **Lees eerst** de skill die je aanpast, de referenties waar hij naar linkt en de skills die naar hem verwijzen
   (`grep -rn "<naam>" plugins/`).
5. **Draai de checks** en los elke fout op voordat je commit:
   ```bash
   python3 scripts/check.py
   claude plugin validate .
   ```
6. **Test de skill** in een echte sessie met de lokale versie van de plugin (zie *Testen*). Zet in de pull request
   wat je hebt getest en wat eruit kwam.
7. **Commit en open een pull request:** `git push -u origin HEAD` en `gh pr create --fill`, of met een titel en
   beschrijving volgens het template. Merge nooit je eigen pull request; Nicky keurt goed.

## Een skill schrijven

### Naam en map
- De mapnaam is de skillnaam: kleine letters, cijfers en streepjes, maximaal 64 tekens (`static-voorzet`).
- `name:` in de frontmatter is precies gelijk aan de mapnaam.
- Geen `adflow-` of `ad-` ervoor: de plugin zet al `adflow:` voor de naam.
- Platformspecifiek? Begin met het platform: `meta-copy`, `tiktok-copy`. Werkt het voor elk platform, dan geen
  platform in de naam.

### Frontmatter
```yaml
---
name: meta-copy
description: Schrijf de Meta ad copy (primary text, headline, description) voor een concept volgens de ad copy handleiding van het merk. Gebruik bij "schrijf de copy", "maak de ad copy", of als een concept klaar is voor launch.
---
```
- `description` staat op **één regel** en is maximaal 1024 tekens.
- De `description` bepaalt wanneer Claude de skill kiest. Zet erin **wat** de skill doet, **wanneer** je hem gebruikt
  (met woorden die een gebruiker echt typt) en **wat niet** (verwijs naar de skill die dat wel doet).
- Geen andere velden toevoegen zonder overleg.

### Inhoud
- Schrijf in het Nederlands. Vaktermen die het team in het Engels gebruikt (hook, angle, persona, awareness, b-roll)
  blijven Engels.
- Begin met één alinea: wat levert deze skill op en voor welke stap in de pijplijn
  ([references/ad-pipeline.md](plugins/adflow/references/ad-pipeline.md)).
- Daarna de stappen in volgorde, als genummerde lijst. Concreet en uitvoerbaar, geen achtergrondverhaal.
- Sluit af met de vorm van de output (een tabel, een lijst, een brief) en wat de gebruiker daarna doet.
- Houd `SKILL.md` onder de 300 regels. Langere uitleg of een framework dat meerdere skills gebruiken hoort in
  `references/`; voorbeelden die alleen bij deze skill horen in de map van de skill (`voorbeelden.md`).
- Verwijs naar bestanden met een **relatieve markdown-link**, vanuit een skill bijvoorbeeld
  `[hook-levers](../../references/hook-levers.md)`.
  Nooit een pad op je eigen computer (`/Users/...`), nooit links met dubbele blokhaken naar notities buiten de repo.
- Verwijs naar een andere skill met zijn naam tussen backticks: `` `power-hooks` ``.

### Bronnen: wat wel en niet in de repo hoort
- **Geen klantdata.** Geen klantnamen, reviews, comments, winners, cijfers, briefs, scripts of screenshots van een
  klant. Ook niet als voorbeeld. Gebruik verzonnen, generieke voorbeelden.
- **Klantkennis staat in Adflow**, de handleidingen per merk in Google Drive. De skill zegt waar hij die ophaalt
  (zie [references/bronnen.md](plugins/adflow/references/bronnen.md)), niet wat erin staat.
- **Merkspecifieke regels horen in de Drive-handleiding van dat merk**, niet in een skill. Een skill is de werkwijze
  voor alle merken.
- Noem gegevens uit Adflow naar wat ze zijn (dims, concepten, Copy library), niet naar de technische naam van een
  tool. Toolnamen kunnen veranderen.
- **Geen gekopieerde tekst** uit cursussen, boeken, swipe files of betaalde bronnen. Vat samen in eigen woorden en
  noem de bron.

## Hernoemen of verwijderen

Gebruikers roepen skills aan bij naam, en andere skills verwijzen ernaar. Daarom:
- Hernoem of verwijder alleen als de gebruiker daar expliciet om vraagt.
- Zoek alle verwijzingen (`grep -rn "<oude-naam>" plugins/ README.md`) en werk ze in dezelfde pull request bij.
- Zet in de pull request **"Hernoemd: oud → nieuw"** of **"Verwijderd: naam"**, zodat het team het weet.

## Testen

Laad de plugin uit je eigen map in plaats van de geïnstalleerde versie:

```bash
claude --plugin-dir ./plugins/adflow
```

Roep de skill aan (`/adflow:<naam>`) of stel een vraag die hem zou moeten activeren, voor een echt merk in Adflow.
Controleer:
- Kiest Claude de skill bij een normale vraag? Zo niet, scherp de `description` aan.
- Volgt de output de stappen en de vorm uit de skill?
- Haalt hij de juiste bronnen op uit Adflow en Drive, zonder iets te verzinnen?

Zet geen klantoutput uit de test in de repo of in de pull request; beschrijf alleen wat je controleerde.

## Wat een agent nooit doet

- Pushen naar `main`, force-pushen, of de geschiedenis herschrijven.
- `.claude-plugin/`, `plugins/adflow/.mcp.json`, `scripts/` of `.github/` aanpassen zonder dat Nicky erom vraagt.
- Een `version` toevoegen aan `plugin.json`: zonder versie komt elke merge vanzelf bij gebruikers aan.
- Wachtwoorden, tokens of API-keys in een bestand zetten.
- Een check uitzetten of omzeilen om een pull request groen te krijgen.
