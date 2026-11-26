---
name: video-format
description: Brainstorm een menu delivery/formats (het vehicle + de uitvoering) voor een gekozen concept-slot, met de Format-namen van het merk of uit de format-gallery — talking head, b-roll with voice-over, product demo, green screen, skit, POV, unboxing, try-on en meer. Elk met een 1-regel-concept, Rol (drager/verkenner) en fit-rating. Stap S2 (video) van de ad-pijplijn. Levert een menu (mag meerdere), beslist niet. Alleen video. Gebruik bij "welke video formats", "hoe brengen we deze slot in beeld" of "talking head of voice-over?". Niet voor statics (gebruik static-format). Lean output.
metadata:
  adbase: "true"
---

# Video Delivery/Format (S2 · video)

De **delivery/format**-stap van de [ad-pijplijn](../../references/ad-pipeline.md) voor **video** — de éérste van twee
pre-copy-assen: het **vehicle + hoe het gedragen wordt** (*hoe* het gefilmd/gedragen wordt). De **arc** (verhaalstructuur,
*wat* je vertelt) komt daarna in S3. Je krijgt een **concept-slot** binnen (uit S1) en levert een **menu** van
delivery/formats; de gebruiker kiest (mag meerdere → testvarianten).

> **Vaste werkwijze (voorkeur gebruiker):** S2 = altijd een menu in tabelvorm. Geen enkel-antwoord.
> **Alleen video.** Voor static: `static-format`. **Arc (verhaalstructuur) = S3**, niet hier.

## Input (lees eerst)
- **Concept-slot:** Persona × Angle × Awareness (uit S1).
- **De formatnamen, in deze volgorde** (zie [format-classification.md](../../references/format-classification.md)):
  1. de **Format-dimensie van het merk** in Adflow (dimensions). Heeft het merk eigen waarden, dan gebruik je in het
     menu precies die namen;
  2. de sectie `## Format` in de AI-instructies van het merk, als die bestaat;
  3. anders de drie video-families uit de [format-gallery](../../references/format-gallery.md), met precies de namen
     uit de galerij. Per format staat een kaart in `references/formats/`. **Klant-agnostisch.**
- de format-fit van de klant (zie `references/bronnen.md`) — de **klant-fit** (welke delivery-vormen passen bij déze klant).
- de winners (live opgehaald, zie `references/bronnen.md`) — wat op spend draait (bv. VO/observational over ouder-kind broll).
  Bepaal de delivery van een winner uit de analyse per seconde (beeld, tekst in beeld, spraak of alleen muziek), nooit
  uit de thumbnail of de adnaam: zie [judging-video.md](../../references/judging-video.md).
- de brand guidelines — DON'Ts + client-specifieke regels.

## De video-formats (galerij)
Gebruikt het merk geen eigen Format-waarden, kies dan uit deze 19 formats in drie families. Varianten (yapper, walk
and talk, how-to, stress test, day in the life…) staan op de kaart en tag je als het format zelf.
- **Een persoon in beeld:** Talking head · Street interview · Podcast · Green screen · Comment reaction ·
  Whiteboard · Phone call.
- **Het product in beeld:** Product demo · Unboxing · Try-on · First-try reaction · Before / after.
- **Beeld met stem of tekst:** B-roll with voice-over · B-roll with text · Behind the scenes · POV · Vlog · Skit ·
  Animation.

## Methode
1. Loop de formats langs; houd wat bij deze slot + klant past. **Alle formats mogen als optie op tafel**; laat
   duidelijk niet-passende weg met één reden. **Welke formats bij déze klant werken, bepaalt de eigen performance in
   Adflow** (spend eerst, dan ROAS) en de format-fit van de klant (zie `references/bronnen.md`). Het signaal in de
   galerij is algemeen, geen oordeel.
2. Geef per optie een **concreet 1-regel-concept voor déze slot** (met een klantwoord/moment erin).
   - **Een idee is geen format.** Testimonial, founder, challenge, us vs them, VSL: dat is de boodschap, de afzender
     of de structuur. Zet zo'n idee in de kolom **Idee** naast een echt format (bv. Talking head + founder, Product
     demo + challenge). Waar elk idee hoort, staat in de galerij onder "Ideas from the sources that are not a format".
   - **Format ≠ arc.** Het format is wat je ziet (*hoe* het in beeld komt); de verhaalstructuur kies je pas in S3.
3. Tag per rij de **Rol** (drager = bewezen/klassiek · verkenner = diversificatie) + een **fit-rating** (✅ · 🟡 · ➖).
4. **Balans:** minstens 2–3 **dragers** (uit winners/format-fit) + een paar **verkenners**.
5. Respecteer de brand guidelines (DON'Ts; bv. geen letterlijke review-quotes ópscherm in broll/video).
6. Sluit af met een **aanrader (1–2)** + de vraag welke naar **S3 arc**.

## Output-format
Lean tabel. **Alleen het menu + korte wegingen + aanrader. Geen intro/samenvatting.**

```
# S2 delivery/format-menu — <slot: persona × angle × awareness>

| # | Format | Idee | Concept voor deze slot | Rol | Fit |
|---|---|---|---|---|---|
| 1 | <naam uit merk-dimensie of galerij> | <optioneel: founder, testimonial…> | … (1 regel, met klantwoord/moment) | drager/verkenner | ✅/🟡/➖ |
| 2 | … | … | … | … | … |
…

Wegingen: <1–2 regels — dragers + de verkenner-spreiding>
Aanrader: <1–2 nummers>. Welke haal ik door S3 (arc)? (bv. "ga verder met 1, 2, 5" — mag meerdere)
```

**Altijd nummeren** (kolom `#`).

## QC-lat
- [ ] **Genummerd** (kolom `#`); **menu, geen enkel antwoord**.
- [ ] Elk concept bevat een **klantwoord/moment**.
- [ ] **Rol** (drager/verkenner) per rij; **≥2–3 dragers** + verkenners.
- [ ] Dit is **delivery/format** (vehicle + uitvoering), géén arc — arc is S3.
- [ ] **Formatnamen** komen precies uit de Format-dimensie van het merk, of anders uit de galerij. Geen idee
      (testimonial, founder, UGC) in de kolom Format.
- [ ] **Klopt met de brand guidelines + de format-fit** (client-DON'Ts + client-fit); winners herkenbaar.

## Notes
- Workflow **S2 (video)** in `references/ad-pipeline.md`. Uit (gekozen delivery/format(s)) → in voor **S3 arc**.
- Beslist niet — levert een menu; de gebruiker kiest.
- Nieuwe token dat bij de gekozen slot hoort? Bevestigen bij de keuze om uit te werken.
