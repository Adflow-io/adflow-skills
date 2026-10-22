---
name: video-brief
description: Maak een editor-brief of creator-brief voor een video-concept, in de opbouw en met de naamgeving uit de briefing handleiding van het merk in Drive. Leest het concept uit Adflow, kiest het brieftype en het concepttype, vult de vaste opbouw en levert een producereerbare brief. Stap S6 (video) van de ad-pijplijn. Alleen video. Lean output.
---

# Video-brief (S6 · video)

De laatste stap van de [ad-pijplijn](../../references/ad-pipeline.md) voor **video**: zet een concept (en, waar de
handleiding dat vraagt, een goedgekeurd script) om in een **producereerbare brief** voor de editor of de creator.

> **De handleiding van het merk is leidend.** Naamgeving, concepttypes, briefdiepte en tekstregels verschillen per
> merk en staan in Drive. Deze skill bevat alleen de generieke werkwijze. Zie [bronnen.md](../../references/bronnen.md).
> **Alleen video.** Voor static: `designer-brief`.

## Voordat je begint
1. **Zoek de handleiding** in Drive: `<Merk> – Editor briefing handleiding` en/of `<Merk> – Creator briefing
   handleiding` (of één gecombineerde `<Merk> – Briefing handleiding`). Lees hem helemaal.
2. **Bestaat er geen handleiding?** Zeg dat. Werk dan met de generieke voorbeelden in
   [voorbeelden.md](voorbeelden.md) en stel voor om de handleiding voor dit merk eerst op te zetten. Verzin geen
   merkspecifieke regels.
3. **Kies het brieftype:** editor-brief (bestaand beeld monteren) of creator-brief (nieuw filmen). Vraag het als het
   uit het concept niet blijkt.

## Input (lees eerst, raad niet)
- **Het concept uit Adflow** (`search_concepts`, `get_concept`): nummer, dims (product, persona, angle, awareness,
  offer, creator, taal) en het gekoppelde conceptdocument. Het conceptnummer komt uit Adflow, **nooit zelf verzinnen**.
- **Het concepttype** zoals de handleiding het noemt (bv. remake, taalversie, nieuw format, founders ad). Het type
  bepaalt hoe uitgebreid de brief wordt.
- **Het voorzet of script**, voor zover het type er een vraagt. Bij een remake of taalversie is de originele ad het
  script. Bij typen met een uitgeschreven script (bv. nieuw format, founders ad) maak je de brief pas **na akkoord op
  het script** (S5, met humanizer-pass).
- **De brand guidelines** en **de research** voor klantwoorden en DON'Ts (zie bronnen.md).
- **De Referentiebriefs** uit de handleiding: haal de brief van hetzelfde type op in Adflow (`get_document`) en gebruik
  hem voor inhoud en opbouw. Niet voor de naam: oudere briefs gebruiken een andere naamgeving.

## Werkwijze
1. **Analyse in een losse notitie boven de brief** (concepttype, waarom, wat je overneemt van de referentiebrief).
   De brief zelf bevat alleen wat de editor of creator nodig heeft.
2. **Naam van de brief en variantcodes** volgens het kopje Naamgeving in de handleiding. Het ID zie je al in Adflow en
   zet je niet in de naam. Elke variant (hook, taal, formaat) is een eigen creative met een eigen code.
3. **Vul de vaste opbouw** uit de handleiding (typisch: Instructie, Voorbeeld, Messaging, Varianten, Beelden of Script,
   plus de extra onderdelen van het concepttype en het blok Probeer).
4. **Embeds, geen links.** Voorbeelden, b-roll, muziek en CTA scene zet je als embed in de brief.
5. **Tekst in beeld** volgt het kopje Tekst op creatives in de handleiding (taalregels, notatie, verboden woorden).
6. **Loop de check voor oplevering** uit de handleiding en de QC-lat hieronder.

## Waar de brief terechtkomt
De brief is een **eigen brief onder het concept** (een creator-brief of editor-brief als kind van het concept), niet
tekst in het conceptdocument zelf. Het conceptdocument bevat de hypothese, het bewijs, de dims, de ad copy en de
launchplek (zie [concept-document.md](../../references/concept-document.md) en de skill `concept`). Bestaat het
concept nog niet, maak het dan eerst met `concept`. De brief erft de dims van het concept.
Staat er in een bestaande brief al tekst, overschrijf dan niets: lever de brief in de chat. Een lokaal bestand maak
je niet. Gebruik lijsten, geen tabellen: tabellen worden in Adflow platte tekst.

## Output-format
De losse notitie (kort) en daaronder de brief exact in de opbouw van de handleiding. Lean.

## QC-lat
- [ ] De handleiding van het merk is gelezen en gevolgd (of expliciet gemeld dat hij ontbreekt).
- [ ] Conceptnummer en dims komen uit Adflow, niets verzonnen.
- [ ] Brief- en variantnamen volgen het kopje Naamgeving.
- [ ] Briefdiepte past bij het concepttype (geen script waar de originele ad het script is).
- [ ] Elke hook of taal is een eigen variant met een eigen code.
- [ ] Voorbeelden, b-roll, muziek en CTA staan als embed.
- [ ] Tekst in beeld klopt met de tekstregels in de handleiding en de brand guidelines.
- [ ] Analyse en tags staan boven de brief, niet erin.
- [ ] De check voor oplevering uit de handleiding is afgevinkt.

## Notes
- Workflow **S6 (video)** in `references/ad-pipeline.md`. In = concept uit Adflow (+ goedgekeurd script waar nodig).
  Uit = brief onder het concept, daarna productie, launch volgens de Launch handleiding, en feedback uit de cijfers.
- Beslist niet over de copy. Die is in S4 en S5 gekozen; deze skill maakt hem producereerbaar.
- De Meta-adnaam maakt Adflow bij het launchen uit de dims. Zie `naming`.
