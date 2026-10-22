# Bronnen: waar staat welke informatie

De skills lezen geen lokale klantmappen meer. Elke soort informatie heeft één bron. Haal de informatie op via de
connectors, per merk. Zet nooit merk-ID's of klantgegevens vast in een skill.

| Wat | Bron | Hoe ophalen |
|---|---|---|
| Merk, toon, do's en don'ts, verplichte elementen | Adflow-document "Brand guidelines — <merk>" | `search_workspace_items` (type Document), dan `get_document` |
| Persona's, angles, producten, offers, creators, awareness, talen | Adflow-dims | `list_dimensions`, `list_dimension_values` |
| Concepten, briefs, status | Adflow-concepten | `search_concepts`, `get_concept` |
| Research (reviews, comments, bewijs per dimensie) | Adflow-documenten met tag research | `search_workspace_items`, dan `get_document`. De ruwe CSV's staan in de Drive-klantmap |
| Winners en performance | Live, nooit uit een bestand | Adflow (`get_top_ads`, `get_dimension_performance`, `analyze_ad_performance`) of de Meta Ads MCP |
| Ad copy die al bestaat | Adflow Copy library | `list_ad_copy_sets` |
| Hoe we briefen, copy schrijven en launchen voor dit merk | Drive-handleidingen, zie hieronder | Drive `search_files`, dan `read_file_content` |
| Format-fit en hookbank van de klant | Adflow-documenten "Format fit — <merk>" en "Hooks — <merk>" als ze bestaan | Zoals research. Bestaan ze niet, zeg dat dan en ga door zonder |
| Voorbeeldbriefs | De sectie Referentiebriefs in de briefing handleiding van het merk | Zoek de brief op titel in Adflow |

## De Drive-handleidingen

Per merk staan er handleidingen in de Drive-map van het merk. De titel volgt dit patroon:

- `<Merk> – Briefing handleiding`, of gesplitst: `<Merk> – Editor briefing handleiding` en
  `<Merk> – Creator briefing handleiding`
- `<Merk> – Ad copy handleiding Meta`
- `<Merk> – Launch handleiding Meta`

Zoek ze op met `title contains '<Merk>'` en `title contains 'handleiding'`. **De handleiding is leidend** voor alles
wat per merk verschilt: naamgeving, concepttypes, soort brief, tekstregels, launchplek. De skills bevatten alleen de
generieke werkwijze.

Bestaat er voor een merk nog geen handleiding? Zeg dat. Gebruik dan de generieke voorbeelden in de skill als
vertrekpunt, en stel voor om de handleiding eerst op te zetten.

## Wat er niet meer is

- `clients/<klant>/brand.md`, `dimensions/`, `winners.md`, `reviews.md`, `comments.md`: vervangen door de bronnen hierboven.
- `clients/<klant>/ads/` met opgeslagen briefings: briefings leven in Adflow.
- Een lokale token-woordenlijst: de tokens zijn de waardes van de dims in Adflow.
