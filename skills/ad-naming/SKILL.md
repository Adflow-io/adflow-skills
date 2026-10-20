---
name: ad-naming
description: Check of de dims van een concept in Adflow compleet en consistent zijn, laat zien welke Meta-adnaam Adflow daaruit maakt (product-persona-angle-creator-offer-awareness-taal), en geef de variantcodes voor de bestanden volgens de briefing handleiding van het merk. Het ID komt uit Adflow (nooit zelf verzinnen). Lean output.
---

# Ad Naming

Er zijn twee namen, en ze hebben verschillende bronnen.

| Naam | Waar | Wie maakt hem |
|---|---|---|
| **Meta-adnaam** | In het ad account | Adflow, bij het launchen, uit de dims van het concept |
| **Variantcode** | Bovenaan de brief en als bestandsnaam | Het conceptnummer plus de regels uit de briefing handleiding van het merk |

Gebruik nooit een Meta-adnaam als bestandsnaam, en typ de Meta-adnaam nooit zelf.

## Meta-adnaam

Bron van waarheid voor het format en de awareness-ladder: `references/naming-convention.md`.

```
<ID>-PR-<product>-PRS-<persona>-AN-<angle>-CR-<creator>-OF-<offer>-AW-<awareness>-LNG-<taal>[_<ratio>]
```

De `<ID>` (merkcode plus volgnummer) komt uit Adflow. Verzin hem nooit. Weet je hem niet, laat `<ID>` staan.

De velden zijn de waardes van de **dims in Adflow**. Er is geen aparte woordenlijst meer. Controleer daarom de dims
van het concept en zorg dat de waardes kloppen voor het launchen.

## Werkwijze
1. Haal het concept en zijn dims op (`get_concept`, `list_dimension_values` voor de bestaande waardes).
2. Controleer de 7 velden: product, persona, angle, creator, offer, awareness, taal. Ontbreekt er een, meld dat.
   Awareness kun je afleiden uit de hook en de angle (zie de ladder in de referentie). Offer is `none` als er geen
   aanbod is.
3. **Hergebruik bestaande waardes.** Staat er een bijna-dubbele waarde in de dim (andere spelling of casing), meld dat
   en kies de bestaande. Verzin geen nieuwe spelling voor iets dat al bestaat.
4. Is een waarde echt nieuw (nieuwe persona, angle of creator)? Markeer hem als **nieuwe dim-waarde** en laat de
   gebruiker bevestigen voordat hij in Adflow wordt aangemaakt.
5. Laat zien welke Meta-adnaam daaruit volgt, zodat de gebruiker hem vooraf kan controleren.

## Variantcodes

Volg het kopje Naamgeving in de briefing handleiding van het merk (Drive, zie `references/bronnen.md`). Een gangbaar
patroon is `[concept]_[sub]-[TAAL]-[n]`, bijvoorbeeld `64_1-NL-2`. Bij statics komt het formaat erachter.
Het conceptnummer komt uit Adflow. Heeft het merk geen handleiding, gebruik dan het patroon uit
`skills/video-brief/voorbeelden.md` en zeg dat het een vertrekpunt is.

## Harde regels
- [ ] ID en conceptnummer nooit zelf verzinnen.
- [ ] Alle 7 velden aanwezig, in vaste volgorde, met hun prefix.
- [ ] Alleen bestaande dim-waardes; nieuwe expliciet gemarkeerd.
- [ ] Meta-adnaam en variantcode niet door elkaar gebruikt.

## Output-format
Lean. De verwachte Meta-adnaam (of namen, één per regel) en de variantcodes, plus alleen een regel toelichting als je
iets afleidde of een nieuwe dim-waarde markeerde.

```
Meta-adnaam: <ID>-PR-...-PRS-...-AN-...-CR-...-OF-...-AW-...-LNG-...[_9x16]
Variantcodes: 64_1-NL-1, 64_1-NL-2

(alleen indien nodig)
afgeleid: awareness=most-aware (deal-hook)
nieuwe dim-waarde: AN-<...>, bevestigen voor aanmaken
```

## Notities
- Workflow D3 in `references/workflow-map.md`. Input = het gekozen concept met zijn dims.
