---
name: static-format
description: Brainstorm een breed menu static-formats voor één concept-slot (Persona × Angle × Awareness) — elk format met een concreet 1-regel-concept voor die slot, clarity/curiosity, en fit-rating. Stap S2 van de ad-pijplijn. Levert een menu om uit te kiezen (mag meerdere), beslist niet. Alleen statics. Gebruik bij "welke static formats", "format-ideeën voor deze slot" of "hoe maken we hier een static van". Niet voor video (gebruik video-format). Lean output.
metadata:
  adbase: "true"
---

# Static Format (S2)

De format-stap van de ad-pijplijn (`references/ad-pipeline.md`). Je krijgt één **concept-slot** binnen (uit
S1) en levert een **breed menu** van static-formats die bij die slot passen — **niet** één keuze met wat losse
alternatieven, maar een echte brainstorm waar de gebruiker uit kiest (mag meerdere formats naar S4). De gebruiker
beslist; jij stelt voor en raadt aan.

> **Vaste werkwijze (voorkeur gebruiker):** S2 = altijd een brainstorm-menu in tabelvorm, meerdere formats met een
> concreet concept per slot. Geen enkel-format-antwoord.

## Input (lees eerst)
- **Concept-slot:** Persona × Angle × Awareness (uit S1).
- **De formatnamen, in deze volgorde** (zie [format-classification.md](../../references/format-classification.md)):
  1. de **Format-dimensie van het merk** in Adflow (dimensions). Heeft het merk eigen waarden, dan gebruik je in het
     menu precies die namen;
  2. de sectie `## Format` in de AI-instructies van het merk, als die bestaat;
  3. anders de static-families uit de [format-gallery](../../references/format-gallery.md) (image-led, text-led,
     native screenshot), met precies de namen uit de galerij. Per format staat een kaart in `references/formats/`.
- [static-formats.md](../../references/static-formats.md) — alleen voor de **2 messaging-wetten** (deel B) en de
  tier-verzoening (deel C). De formatlijst in deel A en D gebruik je niet meer: die is vervangen door de galerij.
- de format-fit van de klant (zie `references/bronnen.md`) — de **klant-fit** per format (welke dragers/looks passen bij déze klant).
- de research (reviews en comments, zie `references/bronnen.md`) — voor concrete concept-haakjes (klantwoorden, momenten, bezwaren).
- de winners (live opgehaald, zie `references/bronnen.md`) — welke angle/vehicle al draait (repliceren in static).
- de brand guidelines — DON'Ts + client-specifieke regels (bv. prijs bij organisch, quote-regels).

## Methode
1. Loop de **static-formats** langs: de waarden van de Format-dimensie van het merk, of anders de drie
   static-families uit de galerij. Houd de formats die bij deze slot passen qua angle + awareness; laat duidelijk
   niet-passende weg. **Welke formats bij déze klant werken, bepaalt de eigen performance in Adflow** (spend eerst, dan
   ROAS) en de format-fit van de klant (zie `references/bronnen.md`). Het signaal in de galerij is algemeen, geen oordeel.
2. Geef per gekozen format een **concreet 1-regel-concept voor déze slot** (met een klantwoord/moment erin) — niet
   de generieke format-omschrijving.
   - **Een idee is geen format.** Testimonial, offer, gift guide, persona call-out, founder, us vs them: dat is de
     boodschap, het aanbod of de afzender. Zet zo'n idee in de kolom **Idee** naast een echt format (bv. Quote card +
     testimonial, Product hero + offer). Waar elk idee hoort, staat in de galerij onder "Ideas from the sources that
     are not a format".
3. Zet per format **clarity of curiosity** en een **fit-rating** (✅ sterk · 🟡 kan · ➖ zwak).
4. Zorg dat er **minstens één curiosity-optie** in staat (bv. Press als advertorial, of een native screenshot) en benoem dat dat een
   ander funnel-pad is (sale ná de klik → aparte LP nodig).
5. Pas de 2 messaging-wetten toe (assume-no-one-knows bij TOF; clarity↔curiosity keuze) en respecteer de brand guidelines.
6. Sluit af met een **aanrader (1–2 formats)** + de vraag welke naar S4.

## Output-format
Lean tabel. **Alleen het menu + korte wegingen + aanrader. Geen intro/samenvatting.**

```
# S2 format-menu — <slot: persona × angle × awareness>

| # | Format | Idee | Concept voor deze slot | Clarity/Curiosity | Fit |
|---|---|---|---|---|---|
| 1 | <naam uit merk-dimensie of galerij> | <optioneel: testimonial, offer…> | … (1 regel, met klantwoord/moment) | clarity/curiosity | ✅/🟡/➖ |
| 2 | … | … | … | … | … |
…

Wegingen: <1–2 regels — bv. sterkste kandidaat + de curiosity-uitzondering>
Aanrader: <1–2 nummers>. Welke haal ik door naar S4? (bv. "ga verder met 1, 2, 5" — mag meerdere)
```

**Altijd nummeren** (kolom `#`), zodat de gebruiker met nummers kan doorverwijzen ("ga verder met 1,2,5").

Mik op ~6–9 formats; scherp genoeg dat elke rij een echte optie is.

## QC-lat
- [ ] **Genummerd** (kolom `#`), zodat de gebruiker met nummers kan kiezen ("ga verder met 1,2,5").
- [ ] **Menu, geen enkel antwoord** — meerdere formats met elk een concreet slot-concept.
- [ ] **Formatnamen** komen precies uit de Format-dimensie van het merk, of anders uit de galerij. Geen idee
      (testimonial, offer, persona) in de kolom Format.
- [ ] Elk concept bevat een **klantwoord/moment**, niet de generieke format-uitleg.
- [ ] **≥1 curiosity-optie** benoemd (+ dat het een ander funnel-pad is).
- [ ] **TOF/BOF + clarity/curiosity** logisch per format.
- [ ] **Klopt met de brand guidelines + de format-fit** (client-DON'Ts + client-specifieke format-regels).
- [ ] Winners/angle herkenbaar terug waar relevant.

## Notes
- Workflow **S2** in `references/ad-pipeline.md`. Uit (gekozen format(s)) → in voor **S4 `static-voorzet`**.
- Beslist niet — levert een menu; de gebruiker kiest welk(e) format(s) we uitwerken.
- Nieuwe token dat bij de gekozen slot hoort? Bevestigen gebeurt bij de keuze om uit te werken.
