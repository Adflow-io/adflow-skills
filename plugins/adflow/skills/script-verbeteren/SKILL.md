---
name: script-verbeteren
description: Keuzemenu om een video-script te verbeteren, direct na het volledige script (S5) en vóór de briefing (S6). Toont genummerde verbeter-opties (inkorten, menselijker, scherper/concreter, kijker vasthouden, hook herschrijven, psychologische variatie, doelgroep-pass); de gebruiker kiest één of meer, en elke gekozen optie draait één voor één met een stop en akkoord ertussen. Gebruik bij "hoe kan ik dit script beter maken", "verbeter het script", "welke checks kan ik nog doen", of nadat een volledig script klaar is. Alleen video. Lean output.
---

# Script verbeteren (S5b · video)

De verbeterstap van de [ad-pijplijn](../../references/ad-pipeline.md), tussen **S5 (volledig script)** en **S6 (brief)**.
Je krijgt een **volledig script** binnen en laat de gebruiker **kiezen** welke verbeteringen erop draaien. Je beslist
niet zelf welke; de gebruiker kiest (mag meerdere). Werkwijze: één stap per beurt, stoppen en op de keuze wachten.

> **Alleen video.** Statics hebben geen S5; daar is het voorzet al de copy.

## Input
- **Het volledige script** (NL en/of EN) zoals het nu staat. Staat het in Adflow, lees het daar uit de briefing/het concept.
- **Slot:** persona × angle × awareness (+ delivery/arc), als die er zijn.
- **Brand guidelines** en klantwoorden (reviews/comments) van het merk, uit Adflow (zie [bronnen.md](../../references/bronnen.md)). Alles wat je aanpast moet daarmee kloppen.

## Stap 1: toon het menu
Toon dit menu (aangepast met een korte opmerking per optie waar het script er iets over zegt), **en stop**. Kies niet zelf.

| # | Wat het doet | Skill / bron |
|---|---|---|
| 1 | Korter en strakker maken | `script-fluff-remover` |
| 2 | Menselijker laten klinken (humanizer) | `anti-ai-writing` + [humanizer-passes](../../references/humanizer-passes.md) |
| 3 | Scherper en concreter schrijven | `copy-levers` |
| 4 | De kijker langer vasthouden (lussen, specificiteit, fluff) | `content-principles` |
| 5 | Hook herschrijven | `gap-hook` · `power-hooks` · `hook-levers` |
| 6 | Controleren op psychologische variatie | `ad-reviewer` |
| 7 | Doelgroep-pass (zou deze persona dit zo zeggen?) | persona-vriendentest, zie hieronder |

Sluit af met de vraag: *"Welke wil je draaien? Bijvoorbeeld 'doe 4, 2 en 7'."*

## Stap 2: draai de gekozen opties, één voor één
Per gekozen optie, in de volgorde van de gebruiker (of, bij geen voorkeur, 1 → 4 → 3 → 5 → 6 → 2 → 7, zodat de menselijke
laag als laatste komt):
1. Draai de bijbehorende skill/bron op het **huidige** script (inclusief wat eerdere opties al hebben aangepast).
2. Lever **alleen**: wat er gevonden is (kort, per punt), het aangepaste script, en een wijzigingstabel (was → nu → waarom).
3. **Stop** en vraag akkoord, of de volgende optie, voordat je doorgaat. Voer niets door in het document zonder akkoord.

### Optie 7: doelgroep-pass
Loop elke regel langs en toets: *zou déze persona dit écht zo tegen een vriend(in) zeggen?* Let op:
- productjargon i.p.v. spreektaal (vakterm → alledaags woord)
- merk-tagline midden in de tekst
- te net of generiek; liever een concreet beeld
- voornaamwoorden die een deel van de doelgroep uitsluiten
- feitelijke fouten t.o.v. het product (wat het product wél en niet doet)

## Regels
- **Feiten, claims en productwaarheid blijven staan.** Geen verzonnen cijfers, autoriteit, resultaatbeloftes of klantverhalen.
  Is er iets nodig dat niet in de data staat, markeer het als vraag voor de klant in plaats van het in te vullen.
- **Brand-DON'Ts blijven gelden** (de do's en don'ts uit de brand guidelines).
- **Angle van de slot blijft gelijk.** Verschuift de boodschap, dan is het een ander slot.
- **Eerlijke eindregel per optie:** is het script al goed op dit punt, zeg dat en verander niets. Verzin geen problemen.
- **Product minstens één keer natuurlijk benoemd** en de afsluiter niet vast.
- Meerdere opties achter elkaar kunnen elkaar tegenwerken (bv. inkorten haalt iets weg dat de lus nodig heeft). Meld dat zodra het zich voordoet.

## Stap 3: afronden
Als de gebruiker klaar is: één regel samenvatting van wat er is veranderd, het definitieve script, en de vraag of het naar
**S6 (brief)** gaat. De brief (`video-brief`) maak je pas na akkoord.

## Notes
- Dit is een **menu**, geen vaste pijplijn: de gebruiker mag een stap overslaan of meerdere keren draaien.
- Klant-agnostisch: geen klantvoorbeelden in dit bestand. Klant-fit komt uit de documenten van het merk in Adflow.
