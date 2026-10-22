# Ads Machine

Skills en referenties voor het maken van Meta-ads (static en video), van concept-slot tot launch.

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
| S1 | `ad-slots` |
| S2 | `static-format`, `video-format` |
| S4 | `static-voorzet`, `video-voorzet` (met `power-hooks`, `hook-levers`, `ad-body`, `copy-levers`) |
| S6 | `video-brief` (editor en creator), `designer-brief` (static), `video-broll` |
| Naamgeving | `ad-naming` |
| Ad copy en copy templates | `ad-copy` |

## Wijzigingen in 0.2.0

- Alle verwijzingen naar lokale klantmappen (`clients/<klant>/...`) vervangen door bronnen in Adflow en Drive.
- Nieuw: `references/bronnen.md`, de skill `ad-copy` en generieke voorbeelden bij `video-brief` en `ad-copy`.
- `video-brief` en `ad-naming` herschreven rond de briefing handleiding: naamgeving met conceptnummer en variantcodes,
  briefdiepte per concepttype, brief in het conceptdocument in Adflow.
- `designer-brief` volgt een Designer-handleiding als die bestaat.

## Installeren

Zie de [README van de repo](../../README.md). De skills hebben de connectors voor Adflow, Google Drive en (voor
winners) de Meta Ads MCP nodig.

## Open punten

1. **Ontbrekende regels.** Skills en referenties verwijzen met `[[...]]` naar notities uit Louis' lokale geheugen die
   niet in de repo staan: `feedback-token-confirm-timing`, `feedback-persona-friend-test`,
   `feedback-full-script-before-brief`, `feedback-voorzetjes-first`, `feedback-variation-keep-angle`,
   `feedback-name-product-once`, `feedback-cta-not-fixed`, `feedback-no-client-data-in-refs`,
   `reference-briefing-format` en `feedback-script-framework`. Zodra ze beschikbaar zijn, horen ze in de skills.
2. **Nog niet gecontroleerd met een echte run.** De aangepaste skills zijn niet end-to-end getest tegen Adflow en Drive.
3. **Format-fit en hookbank per klant.** De skills verwijzen naar Adflow-documenten "Format fit — <merk>" en
   "Hooks — <merk>". Die bestaan nog niet.
4. **Designer-handleiding.** Er is nog geen `<Merk> – Designer briefing handleiding`; `designer-brief` valt terug op
   `references/designer-brief-static.md`.
5. **Verwijzingen naar bronvideo's** in `references/` wijzen naar transcripts die bewust niet in de repo staan.
6. **Niet meegenomen** (bewust): swipe-bestanden (herkomst en licentie nakijken), transcripts van externe video's,
   klantmappen, ruwe data, zips.
