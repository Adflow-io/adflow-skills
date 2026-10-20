# Ads Machine

Skills en referenties voor het maken van Meta-ads (static en video), van concept-slot tot briefing.
Eerste versie (v0.1.0): de bestaande skills en referenties, overgenomen uit de lokale Ads Machine van Louis.
Nog niet bijgewerkt (zie "Open punten").

## Uitgangspunten

- **Eén bron per soort informatie.** Deze repo bevat alleen de werkwijze. Klantkennis staat in Adflow
  (dimensies, brand guidelines, briefings, research) en de merkspecifieke handleidingen staan in Google Drive
  (`<Merk> – Briefing handleiding`, `– Ad copy handleiding Meta`, `– Launch handleiding Meta`).
- **De Drive-handleidingen zijn leidend** voor alles wat per merk verschilt (naamgeving, concepttypes, tekstregels,
  soort brief). De skills zijn de generieke motor eronder.
- **Live cijfers worden opgehaald, niet opgeslagen** (Adflow of Meta).
- **Geen klantdata in deze repo.** Geen reviews, comments, winners of briefings per klant.

## Indeling

```
.claude-plugin/    plugin.json en marketplace.json
skills/            de skills (ad-slots, static-format, video-format, static-voorzet, video-voorzet,
                   designer-brief, video-brief, ad-naming, ad-body, power-hooks, hook-levers, copy-levers, video-broll)
references/        klant-agnostische frameworks (pijplijn, hooks, scripts, formats, naamconventie)
```

De pijplijn staat in `references/ad-pipeline.md`: S1 slots, S2 format, S3 arc (video), S4 voorzet,
S5 script (video), S6 brief, E feedback.

## Installeren

Nog niet getest. Bedoeld als Claude plugin: voeg de repo toe als marketplace en installeer `ads-machine`.

## Open punten (v0.1.0)

1. **Ontbrekende regels.** Skills en referenties verwijzen naar notities uit Louis' lokale geheugen die niet in de
   repo staan: `feedback-token-confirm-timing`, `feedback-persona-friend-test`, `feedback-full-script-before-brief`,
   `feedback-voorzetjes-first`, `feedback-variation-keep-angle`, `feedback-name-product-once`, `feedback-cta-not-fixed`,
   `feedback-no-client-data-in-refs`, `reference-briefing-format` en `feedback-script-framework`.
2. **Lokale klantmappen.** Skills lezen nog `clients/<klant>/...` en `brand.md`. Dat moet worden omgezet naar Adflow
   en de Drive-handleidingen.
3. **Briefing-skills lopen achter** op de Drive-handleidingen: de brief leeft in Adflow, de variantcode staat in de
   brief, naamgeving en briefdiepte verschillen per merk en concepttype.
4. **Globale installatie.** `designer-brief`, `hook-levers` en `power-hooks` verwijzen naar `~/.claude/skills/...`.
5. **Vijf kapotte verwijzingen in `references/`**: vier naar transcripts van externe video's (`videos/...`) en één
   naar een klantvoorbeeld (`deal-ad-examples.md`). Beide zijn bewust niet meegenomen; de verwijzingen moeten nog weg.
6. **Niet meegenomen** (bewust): swipe-bestanden (herkomst en licentie nakijken), transcripts van externe video's,
   klantmappen, ruwe data, zips.
