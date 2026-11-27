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
| Ad copy die al bestaat | Adflow Copy library | Zoeken in de Copy library (op naam, dims of concept) |
| Hoe we briefen en copy schrijven voor dit merk | Drive-handleidingen, zie hieronder | Drive `search_files`, dan `read_file_content` |
| Hoe we launchen voor dit merk: namen van campagne, adset en copy, talen en regio's, landingspagina per taal, vertaalinstructies | De AI-instructies van het merk in Adflow | Komen mee met elke zoekopdracht in Adflow voor dat merk. Staat er niets over launchen in, zeg dat en stel voor om het daar eerst vast te leggen |
| Format-fit en hookbank van de klant | Adflow-documenten "Format fit — <merk>" en "Hooks — <merk>" als ze bestaan | Zoals research. Bestaan ze niet, zeg dat dan en ga door zonder |
| Voorbeeldbriefs | De sectie Referentiebriefs in de briefing handleiding van het merk | Zoek de brief op titel in Adflow |

## De Drive-handleidingen

Per merk staan er handleidingen in de Drive-map van het merk. De titel volgt dit patroon:

- `<Merk> – Briefing handleiding`, of gesplitst: `<Merk> – Editor briefing handleiding` en
  `<Merk> – Creator briefing handleiding`
- `<Merk> – Ad copy handleiding Meta`

Zoek ze op met `title contains '<Merk>'` en `title contains 'handleiding'`. **De handleiding is leidend** voor alles
wat per merk verschilt bij briefen en copy: naamgeving, concepttypes, soort brief, tekstregels. Alles over launchen
staat in de AI-instructies van het merk in Adflow, niet in Drive. De skills bevatten alleen de
generieke werkwijze.

Bestaat er voor een merk nog geen handleiding? Zeg dat. Gebruik dan de generieke voorbeelden in de skill als
vertrekpunt, en stel voor om de handleiding eerst op te zetten.

## Wat er niet meer is

- `clients/<klant>/brand.md`, `dimensions/`, `winners.md`, `reviews.md`, `comments.md`: vervangen door de bronnen hierboven.
- `clients/<klant>/ads/` met opgeslagen briefings: briefings leven in Adflow.
- Een lokale token-woordenlijst: de tokens zijn de waardes van de dims in Adflow.
