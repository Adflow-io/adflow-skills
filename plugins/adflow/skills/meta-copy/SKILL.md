---
name: meta-copy
description: Schrijf de Meta ad copy (primary text, headline, description) voor een concept, volgens de ad copy handleiding van het merk in Drive, en maak daarna per regio de copy templates in de Adflow Copy library volgens de launch handleiding. Verzamelt eerst de vier bronnen (vergelijkbare ad, landingspagina, creative, brief). Lean output.
---

# Ad copy

Schrijft de ad copy van één concept en zet die klaar voor het launchen. Ad copy is niet de tekst in beeld: die staat in
de briefing handleiding. Dit gaat over primary text, headline en description.

De landingspagina hoort niet bij de ad copy. Die staat in Adflow los van de copy, in een eigen library, en zit niet in
het copy template. In deze skill is de landingspagina alleen een bron voor feiten (prijs, besparing, aantallen,
einddata).

> **De handleiding van het merk is leidend.** Opmaak, copytypes, schrijfregels en de naam van de templates staan in
> `<Merk> – Ad copy handleiding Meta` en `<Merk> – Launch handleiding Meta` in Drive. Zie
> [bronnen.md](../../references/bronnen.md). Deze skill bevat alleen de generieke werkwijze.

## Voordat je begint
1. **Zoek de ad copy handleiding en de launch handleiding** van het merk in Drive en lees ze helemaal.
2. **Bestaan ze niet?** Zeg dat. Werk met [voorbeelden.md](voorbeelden.md) als vertrekpunt en stel voor om de
   handleidingen eerst op te zetten. Verzin geen merkspecifieke regels, ook niet voor talen en regio's.

## Stap 1: bronnen verzamelen
Loop de vier bronnen af en zet de bevindingen kort onder elkaar.

| Bron | Waar | Wat |
|---|---|---|
| Vergelijkbare ad | Adflow (zoek op dezelfde angle, persona of awareness) en de Copy library | Copy van een ad met dezelfde soort hoek die goed liep |
| Landingspagina | De pagina uit de brief, op het domein of de taalmap uit de launch handleiding | Productnaam, prijs, aanbod, aantallen, verzending |
| Creative | De video of image van de ad | Hook en boodschap |
| Concept en brief | Het conceptdocument en de brief in Adflow | Persona, angle, hook type, awareness |

Regels:
- Prijs, besparing, einddata en aantallen haal je van de landingspagina, nooit uit een oude ad.
- Zegt de creative iets anders dan de landingspagina, dan wint de landingspagina. Meld het verschil.
- Geen vergelijkbare ad? Gebruik het voorbeeld uit de handleiding.

## Stap 2: copy schrijven
1. Bepaal het copytype uit de handleiding (bijvoorbeeld evergreen of deal) aan de hand van de dim Offer.
2. Schrijf in de opmaak van de handleiding, in de taal die de handleiding vraagt (meestal Nederlands of Engels), met
   de schrijfregels van het merk.
3. Twijfel je over de hook, stel er twee voor en laat de gebruiker kiezen.
4. Check prijs, besparing en aantallen tegen de landingspagina.
5. Controleer dat de copy hetzelfde zegt als de creative. Geen nieuwe beloftes.

Gebruik voor de zinsbouw `body` en, voor klantwoorden, de research (zie bronnen.md). Draai bij twijfel
`anti-ai-writing` over het resultaat.

## Stap 3: opmaak in het conceptdocument
Zet de copy onder het kopje Ad copy in het conceptdocument (niet in de brief), per variant, in de
volgorde die de handleiding noemt. Zie [concept-document.md](../../references/concept-document.md). Staat er al tekst,
overschrijf dan niets en lever de copy in de chat.

## Stap 4: copy templates per regio
Pas als de gebruiker de copy heeft goedgekeurd:
1. Haal de regio's, talen en de naam van de templates op uit de launch handleiding.
2. Vertaal de copy per regio volgens de vertaalinstructies in de launch handleiding (natuurlijk boven letterlijk,
   taalregels, notatie).
3. Zoek in de Copy library of het template al bestaat. Bestaat het, werk het dan bij in plaats van een nieuw aan te
   maken. Anders maak je het aan. Kijk in de Adflow MCP welke tools er zijn voor deze taak en lees hun beschrijving voordat je ze gebruikt.
4. Een template bevat alleen primary text, headline en description. Zet er geen landingspagina in.
5. Is een vertaling niet zeker, zet dan één of twee alternatieven in de chat met de letterlijke betekenis en waarom je
   de gekozen versie beter vindt. Klopt een bestaande vertaling al, zeg dat en verander niets.

Het aanmaken of bijwerken van templates is een schrijfactie in een gedeelde library. Laat de gebruiker eerst de
vertalingen zien en vraag akkoord.

## Output-format
De copy in de opmaak van de handleiding. Daarna, na akkoord, een korte lijst: welke templates zijn aangemaakt of
bijgewerkt (naam, taal).

## QC-lat
- [ ] Handleiding(en) van het merk gelezen en gevolgd (of gemeld dat ze ontbreken).
- [ ] Vier bronnen bekeken.
- [ ] Geen landingspagina in de copy of het template.
- [ ] Prijs, besparing en aantallen kloppen met de landingspagina.
- [ ] Het copytype klopt: een evergreen-ad noemt geen prijs of korting.
- [ ] Geen verboden woorden of tekens uit de schrijfregels van het merk.
- [ ] Headline-lengte volgens de handleiding.
- [ ] Templates volgen de naam uit de launch handleiding, en bestaande templates zijn bijgewerkt, niet gedupliceerd.

## Notes
- Hoort bij de launch-voorbereiding in `references/ad-pipeline.md` (na S6, voor het launchen).
- De adnaam in Meta maakt Adflow bij het launchen. Zie `naming`.
