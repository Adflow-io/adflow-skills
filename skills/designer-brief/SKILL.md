---
name: designer-brief
description: Vul de static designer-brief in vanuit een goedgekeurd voorzet (S4) + gekozen format + slot. Levert een puur producereerbare brief met Dimensions-blok bovenaan (leesvolgorde/eye-flow, on-screen, visuele behandeling, QC). Adnaam staat NIET in de brief (apart via ad-naming). Stap S6 van de ad-pijplijn. Alleen statics. Lean output.
---

# Designer-brief (S6)

De laatste stap van de ad-pijplijn (`references/ad-pipeline.md`): zet een **goedgekeurd voorzet** (uit S4) om
in een **producereerbare designer-brief** die de designer zo kan bouwen. Format en velden staan in
`references/designer-brief-static.md` — deze skill vult dat in en levert de adnaam.

## Input (lees eerst)
- **Goedgekeurd voorzet** uit S4: de headline(s) + on-image kernregels.
- **Slot + format** (uit S1/S2): Persona × Angle × Awareness × format.
- `references/designer-brief-static.md` — het brief-format + QC-lat.
- `references/static-formats.md` — messaging-wetten (om de brief tegen te checken).
- `brand.md` (DON'Ts + verplichte elementen) + `reviews.md`/`comments.md` (exacte klantwoorden).
- `references/naming-convention.md` + skill `ad-naming` (voor de naam; ID komt uit Adflow, nooit zelf verzinnen).

## Werkwijze
1. **Analyse in een losse notitie bóven de brief** (format, slot, waarom, messaging-keuze) — NIET in de brief zelf.
   De brief bevat alleen wat op de static komt (zelfde discipline als editor/creator-brief).
2. Begin met een **Dimensions**-blok bovenaan (Product · Persona · Angle · Awareness · Format · Taal) en vul dan de
   vaste velden uit `designer-brief-static.md`: **To do · Leesvolgorde/eye-flow (sizing/contrast/witruimte) ·
   Op scherm (headline · on-image copy · trust · offer/CTA) · Visuele behandeling · Assets · Swipe-ref**.
   **Ratio (vaste standaard, in To do — niet in Dimensions): elke static in 1:1 (1080×1080) én 9:16 (1080×1920)**,
   met een korte noot dat 9:16 verticaler stapelt.
3. **Meerdere tekstvarianten** (bv. 2 headlines) → **één brief**, gedeeld beeld/grid, maar elke variant is een
   **aparte static** met eigen headline **en eigen adnaam** (elke headline = eigen creative). Dus N varianten = **N
   statics**, niet 1. Met de vaste 2 ratio's: **N × 2 = aantal bestanden** — zet dat expliciet in "To do".
4. **Geen adnaam in de brief.** De token-adnaam is meta → die maak je apart met `ad-naming` bij het uploaden, niet
   in de brief. De brief identificeert zich via het **Dimensions**-blok. (Komt er bij het apart benoemen een nieuw
   token bovendrijven → dan pas bevestigen, zie [[feedback-token-confirm-timing]].)
5. Loop de **QC-checklist** uit `designer-brief-static.md` en vink af.

## Output-format
De losse notitie (kort, in comment/kop) + daaronder de brief exact in het `designer-brief-static.md`-format. Lean.
Sla de brief op in `clients/<klant>/ads/` als de gebruiker akkoord is.

## QC-lat (uit designer-brief-static.md)
- [ ] Assume-no-one-knows op TOF-headline (of bewust BOF).
- [ ] Eén duidelijke eye-first (squint-test).
- [ ] Klantwoorden i.p.v. merktaal.
- [ ] Clarity of curiosity gekozen.
- [ ] Leesbaar op mobiel.
- [ ] Klopt met brand.md (quote mág op testimonial-static; niet in broll/video).
- [ ] **Dimensions-blok bovenaan**; **geen adnaam** in de brief (die maak je apart met `ad-naming`).

## Notes
- Workflow **S6** in `references/ad-pipeline.md`. In = goedgekeurd voorzet (S4) → Uit = producereerbare brief
  (Dimensions-blok bovenaan; adnaam apart via `ad-naming`) → Adflow → live → `winners.md` (E-loop).
- Beslist niet over de copy — die is in S4 al gekozen; deze skill maakt 'm producereerbaar.
- Analyse/tags nooit in de brief; alleen wat op de static komt.
