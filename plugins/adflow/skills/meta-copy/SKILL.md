---
name: meta-copy
description: Schrijf de Meta ad copy (URL, primary text, headline, description) voor een concept, volgens de ad copy handleiding van het merk in Drive, en zet die daarna met een versie per taal in de Adflow Copy library volgens de launch handleiding. Verzamelt eerst de vier bronnen (vergelijkbare ad, landingspagina, creative, brief). Gebruik bij "schrijf de ad copy", "maak de Meta copy", "headline en primary text", "zet de copy in de Copy library" of als een concept klaar is voor launch. Niet voor alleen de body (gebruik body). Lean output.
---

# Ad copy

Schrijft de ad copy van één concept en zet die klaar voor het launchen. Ad copy is niet de tekst in beeld: die staat in
de briefing handleiding. Dit gaat over primary text, headline en description.

> **De handleiding van het merk is leidend.** Opmaak, copytypes, schrijfregels en de naam van de copy staan in
> `<Merk> – Ad copy handleiding Meta` en `<Merk> – Launch handleiding Meta` in Drive. Zie
> [bronnen.md](../../references/bronnen.md). Deze skill bevat alleen de generieke werkwijze.

## Tools
Gebruik de tools van de Adflow MCP. Deze skill noemt bewust geen toolnamen, want die kunnen veranderen. Kies de tool op
wat hij doet: copy zoeken, copy lezen, copy aanmaken of bijwerken, een taal- of market-versie zetten, copy of
landingspagina aan een concept koppelen. Vind je geen tool die doet wat een stap vraagt, zeg dat. Niet gokken en niet
omheen werken.

## Voordat je begint
1. **Zoek de ad copy handleiding en de launch handleiding** van het merk in Drive en lees ze helemaal.
2. **Bestaan ze niet?** Zeg dat. Werk met [voorbeelden.md](voorbeelden.md) als vertrekpunt en stel voor om de
   handleidingen eerst op te zetten. Verzin geen merkspecifieke regels, ook niet voor talen en regio's.

## Stap 1: bronnen verzamelen
Loop de vier bronnen af en zet de bevindingen kort onder elkaar.

| Bron | Waar | Wat |
|---|---|---|
| Vergelijkbare ad | Adflow (zoek op dezelfde angle, persona of awareness) en de Copy library (zoek op dezelfde dims) | Copy van een ad met dezelfde soort hoek die goed liep |
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
Zet de copy onder het kopje Ad copy en landingspagina in het conceptdocument (niet in de brief), per variant, in de
volgorde die de handleiding noemt. Zie [concept-document.md](../../references/concept-document.md). Staat er al tekst,
overschrijf dan niets en lever de copy in de chat. Gebruik geen `/` in de tekst (ook niet in primary text, headline of
description): de editor gebruikt dat teken voor nodes. Zie [adflow-documents.md](../../references/adflow-documents.md).

## Stap 4: copy in de Copy library
Eén concept krijgt één copy in de library. Die copy heeft een versie per taal, niet per regio.

1. **Opzoeken.** Haal uit de launch handleiding de naam van de copy, de talen en de regio's. Haal de talen en markets
   van het merk ook op in Adflow.
2. **Bestaat hij al?** Zoek in de Copy library op de naam of via het concept. Bestaat hij, werk hem bij. Maak nooit
   een tweede aan.
3. **Aanmaken.** Bestaat hij niet, maak hem aan met de naam uit de handleiding, de dims van het concept, de copy in
   de mastertaal en de landingspagina als standaard-URL. Koppel hem aan het concept.
4. **Vertalen.** Lees de mastertaal, vertaal per taal volgens de vertaalinstructies in de launch handleiding
   (natuurlijk boven letterlijk, taalregels, notatie) en zet per taal één versie. Regio's met dezelfde taal delen die
   versie (bijvoorbeeld NL en BE-NL).
5. **Market-versie alleen bij afwijking.** Wijkt een regio inhoudelijk af van zijn taal (andere valuta, ander aanbod,
   andere verzenddrempel), maak dan een versie voor die market. Anders niet.
6. **Copygroepen.** Een groep die je meestuurt (primary texts, headlines, descriptions) vervangt die groep van die
   versie. Stuur alleen de groepen mee die je wilt zetten.
7. **Template of concept.** Zonder concept bewerk je de library-copy, en elk concept dat hem gebruikt krijgt de
   wijziging. Gaat het om een afwijking voor één concept, bewerk dan alleen de copy van dat concept.
8. **Twijfel.** Is een vertaling niet zeker, zet dan één of twee alternatieven in de chat met de letterlijke
   betekenis en waarom je de gekozen versie beter vindt. Klopt een bestaande vertaling al, zeg dat en verander niets.

De regio-URL hoort bij de landingspagina in Adflow, niet bij de copy. Zet de landingspagina met zijn market-paden
klaar en koppel die aan het concept.

Maak en vul de copy direct, zonder akkoordstap, tenzij de handleiding van het merk er wel een vraagt.

## Output-format
De copy in de opmaak van de handleiding. Daarna een korte lijst: welke copy is aangemaakt of bijgewerkt, welke
taalversies en market-versies zijn gevuld, en wat de gebruiker nog moet checken (zoals valuta of drempels per regio).

## QC-lat
- [ ] Handleiding(en) van het merk gelezen en gevolgd (of gemeld dat ze ontbreken).
- [ ] Vier bronnen bekeken.
- [ ] URL is de exacte pagina, niet de homepage.
- [ ] Prijs, besparing en aantallen kloppen met de landingspagina.
- [ ] Het copytype klopt: een evergreen-ad noemt geen prijs of korting.
- [ ] Geen verboden woorden of tekens uit de schrijfregels van het merk.
- [ ] Geen `/` in de tekst van het conceptdocument (alleen in links).
- [ ] Headline-lengte volgens de handleiding.
- [ ] Eén copy per concept, met de naam uit de handleiding. Bestaande copy bijgewerkt, niet gedupliceerd.
- [ ] Elke taal van het merk heeft een versie. Market-versies alleen waar een regio echt afwijkt.

## Notes
- Hoort bij de launch-voorbereiding in `references/ad-pipeline.md` (na S6, voor het launchen).
- De adnaam in Meta maakt Adflow bij het launchen. Zie `naming`.
