# Bronnen: waar staat welke informatie

Skills noemen geen toolnamen, want die veranderen. Kijk per connector (Adflow MCP, Drive, Meta Ads) welke tools er zijn
voor de taak en lees hun beschrijving voordat je ze gebruikt.

De skills lezen geen lokale klantmappen meer. Elke soort informatie heeft één bron. Haal de informatie op via de
connectors, per merk. Zet nooit merk-ID's of klantgegevens vast in een skill.

| Wat | Bron | Hoe ophalen |
|---|---|---|
| Merk, toon, do's en don'ts, verplichte elementen | Adflow-document "Brand guidelines — <merk>" | Zoek het document in de workspace (type Document) en lees het |
| Persona's, angles, producten, offers, creators, awareness, talen | Adflow-dims | Haal de dimensions en hun waardes op |
| Concepten, briefs, status | Adflow-concepten | Zoek het concept en lees het |
| Research (reviews, comments, bewijs per dimensie) | Adflow-documenten met tag research | Zoek het document en lees het. De ruwe CSV's staan in de Drive-klantmap |
| Winners en performance | Live, nooit uit een bestand | Adflow (top ads, performance per dimension, analyse per ad) of de Meta Ads MCP |
| Ad copy die al bestaat | Adflow Copy library | Zoek in de Copy library |
| Landingspagina's | Adflow landingspagina-library, los van de ad copy | Zoek in de landingspagina-library |
| Hoe we briefen, copy schrijven en launchen voor dit merk | Drive-handleidingen, zie hieronder | Zoek de handleiding in Drive en lees hem |
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
