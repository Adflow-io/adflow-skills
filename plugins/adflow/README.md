# Adflow

De verbinding met Adflow plus skills en referenties voor het maken van ads (static en video), van concept-slot tot
launch. Skills roep je aan als `adflow:<skill>`, bijvoorbeeld `adflow:slots`. Platformspecifieke skills beginnen met het platform, zoals
`meta-copy`.

## Uitgangspunten

- **Eén bron per soort informatie.** Deze repo bevat alleen de werkwijze. De rest leeft elders en wordt per merk
  opgehaald via connectors. Zie [references/bronnen.md](references/bronnen.md).
  - Klantkennis (brand guidelines, dims, concepten, briefs, research, Copy library): **Adflow**
  - Hoe we per merk briefen, copy schrijven en launchen: **Drive-handleidingen**
    (`<Merk> – Briefing handleiding`, `– Ad copy handleiding Meta`, `– Launch handleiding Meta`)
  - Winners en performance: **live** uit Adflow of Meta, nooit uit een bestand
- **De Drive-handleidingen zijn leidend** voor alles wat per merk verschilt. De skills zijn de generieke motor eronder
  en bevatten alleen generieke voorbeelden als vertrekpunt voor een nieuw merk.
- **Geen klantdata in deze repo.** Geen reviews, comments, winners of briefings per klant.

## Indeling

```
.claude-plugin/    plugin.json
skills/            de skills
references/        klant-agnostische frameworks (pijplijn, hooks, scripts, formats, naamconventie, bronnen)
```

De pijplijn staat in [references/ad-pipeline.md](references/ad-pipeline.md): S1 slots, S2 format, S3 arc (video),
S4 voorzet, S5 script (video), S6 brief, daarna ad copy en launch, en feedback uit de cijfers.

| Stap | Skill |
|---|---|
| S0 (begin hier) | `start` (wat wil je, op basis waarvan, wat is er al; stuurt door naar de juiste stap) |
| Vóór S1 (research) | `review-research` (reviews en ad comments omzetten in klantwoorden, twijfels en persona's; bijwerken met nieuwe reviews) |
| S1 | `slots` |
| S2 | `static-format`, `video-format` |
| S4 | `static-voorzet`, `video-voorzet` (met `power-hooks`, `hook-levers`, `body`, `copy-levers`) |
| Tussen S5 en S6 | `concept` (conceptdocument: hypothese, bewijs, dims, ad copy, launchplek) |
| S6 | `video-brief` (editor en creator), `designer-brief` (static), `broll-shotlist` |
| Na S6 (video) | `video-montage` (Claude monteert de varianten zelf uit footage in Adflow) |
| Na S6 (static) | `static-qa` (laatste check van een opgeleverde static vóór die naar de klant gaat) |
| Naamgeving | `naming` |
| Ad copy en Copy library | `meta-copy` |
| Vóór launch (Meta) | `adset-plan` (adset plan per pillar: welke nieuwe adsets, in welke campagne, met welke naam en looptijd), daarna `meta-adsets` (de adsets uit het plan als lege, gepauzeerde concepten aanmaken) |
| Na launch (Meta) | `meta-partnership-ads` (creators uit het concept als partner koppelen aan de gelanceerde ads) |

## Wijzigingen in 0.2.0

- Alle verwijzingen naar lokale klantmappen (`clients/<klant>/...`) vervangen door bronnen in Adflow en Drive.
- Nieuw: `references/bronnen.md`, de skill `meta-copy` en generieke voorbeelden bij `video-brief` en `meta-copy`.
- `video-brief` en `naming` herschreven rond de briefing handleiding: naamgeving met conceptnummer en variantcodes,
  briefdiepte per concepttype, brief als eigen brief onder het concept in Adflow.
- `designer-brief` volgt een Designer-handleiding als die bestaat.

## Installeren

Zie de [README van de repo](../../README.md). De verbinding met Adflow zit in de plugin als MCP-server
(`https://app.adflow.io/api/v1/mcp`, zie `.mcp.json`). Na het installeren log je één keer in met je eigen
Adflow-account (in Claude Code via `/mcp`, server `plugin:adflow:mcp`). Heb je Adflow ook als connector in claude.ai,
zet die dan uit, anders heb je hem dubbel. Google Drive en (voor winners) de Meta Ads MCP zijn connectors in claude.ai.

## Open punten

1. **Nog niet gecontroleerd met een echte run.** De aangepaste skills zijn niet end-to-end getest tegen Adflow en Drive.
2. **Format-fit en hookbank per klant.** De skills verwijzen naar Adflow-documenten "Format fit — <merk>" en
   "Hooks — <merk>". Die bestaan nog niet.
3. **Designer-handleiding.** Er is nog geen `<Merk> – Designer briefing handleiding`; `designer-brief` valt terug op
   `references/designer-brief-static.md`.
4. **Verwijzingen naar bronvideo's** in `references/` wijzen naar transcripts die bewust niet in de repo staan.
5. **Niet meegenomen** (bewust): swipe-bestanden (herkomst en licentie nakijken), transcripts van externe video's,
   klantmappen, ruwe data, zips.
