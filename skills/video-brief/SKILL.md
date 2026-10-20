---
name: video-brief
description: Vul de editor/creator-briefing in vanuit een goedgekeurd video-voorzet (S4) + gekozen format + slot. Levert een puur producereerbare briefing met Dimensions-blok bovenaan (To do, per hook de hook + openingsbeeld, gedeelde body, broll + muziek). Adnaam staat NIET in de brief (apart via ad-naming). Stap S6 (video) van de ad-pijplijn. Alleen video. Lean output.
---

# Video-brief (S6 · video)

De laatste stap van de [ad-pijplijn](../../references/ad-pipeline.md) voor **video** (de video-tegenhanger van
`designer-brief`): zet een **goedgekeurd volledig script** (uit S5) om in een **producereerbare editor/creator-briefing** die
de editor/creator zo kan bouwen.

> **Alleen video.** Voor static: `designer-brief` (`references/designer-brief-static.md`).

## Input (lees eerst)
- **Goedgekeurd volledig script** uit S5 (het script dat door de humanizer-pass is gegaan en dat de gebruiker heeft
  goedgekeurd) — NIET alleen het voorzet. Maak de brief pas als het script akkoord is ([[feedback-full-script-before-brief]]).
- **Slot + format** (uit S1/S2): Persona × Angle × Awareness × format.
- `brand.md` (DON'Ts + verplichte elementen) + `reviews/`/`comments/` (exacte klantwoorden).
- `clients/<klant>/hooks.md` + `winners.md` — bewezen hooks/angles/taal om op voort te bouwen.
- `references/ad-pipeline.md` + skill `ad-naming` (voor de naam; ID komt uit Adflow, nooit zelf verzinnen).
- Bestaande briefings in `clients/<klant>/ads/` als vorm-referentie.

## Briefing-vorm (vast)
Puur producereerbaar — alleen wat de editor/creator nodig heeft. Vaste blokken:
1. **Dimensions** — Product · Persona · Angle · Awareness · Format (video) · Taal.
2. **To do** — aantal video's · story-formaat **9:16** · **lengte** (bucket + duur-inschatting, zie
   `references/video-durations.md`) · eventuele losse instructies.
3. **Per hook** (genummerd, **géén Video naam** — die zet de gebruiker niet meer in de brief): de **hook-regel(s)** · ***Beeld:***
   het openingsbeeld/de shot-richting (elke hook = ander openingsbeeld).
4. **Body** — de gedeelde beats (voor alle hooks), kort, in klantwoorden, verweven (geen letterlijke quote ópscherm).
5. **Broll + Muziek** — welke broll gebruiken + muziek-richting (bv. rustig/warm, akoestisch/piano).

## Werkwijze
1. **Analyse in een losse notitie bóven de brief** (format, slot, waarom) — NIET in de brief zelf. De brief bevat
   alleen wat de editor/creator nodig heeft (zelfde discipline als de static designer-brief).
2. Vul de vaste blokken hierboven. **Meerdere hooks → één brief**, gedeelde body/broll, maar elke hook is een
   **aparte video** met eigen adnaam (elke hook = eigen creative); geen Video naam in de brief.
3. **Video-quote-regel:** klantwoorden verweven als natuurlijk verhaaltje; **geen** letterlijke review-quotes of
   aanhalingstekens ópscherm (brand.md DON'T voor broll/video).
4. **Geen adnaam in de brief.** De token-adnaam is meta → apart met `ad-naming` bij het uploaden. De brief
   identificeert zich via het **Dimensions**-blok + de Video-namen. (Nieuw token bij het benoemen → dan pas
   bevestigen, zie [[feedback-token-confirm-timing]].)
5. Loop de QC-lat en vink af.

## Output-format
De losse notitie (kort, in comment/kop) + daaronder de briefing exact in de vorm hierboven. Lean.
Sla de brief op in `clients/<klant>/ads/` (bv. `briefing_<ID>-<ID2>_<korte-slug>.md`) als de gebruiker akkoord is.

## QC-lat
- [ ] **Dimensions-blok bovenaan**; **geen adnaam** in de brief (die maak je apart met `ad-naming`).
- [ ] Elke hook heeft een **eigen openingsbeeld** (verschillende hooks qua beeld); **geen Video naam** in de brief.
- [ ] **Body gedeeld**, kort, spreekbaar, klantwoorden **verweven** (geen letterlijke quote ópscherm).
- [ ] **To do** noemt aantal video's + 9:16 + lengte.
- [ ] **Broll + Muziek** benoemd (of expliciet als placeholder gemarkeerd).
- [ ] **Klopt met brand.md** (DON'Ts + verplichte elementen).

## Notes
- Workflow **S6 (video)** in `references/ad-pipeline.md`. In = goedgekeurd script (S5) → Uit = producereerbare
  briefing (Dimensions-blok bovenaan; adnaam apart via `ad-naming`) → Adflow → live → `winners.md` (E-loop).
- Beslist niet over de copy — die is in S4/S5 al gekozen; deze skill maakt 'm producereerbaar.
- Analyse/tags nooit in de brief; alleen wat de editor/creator nodig heeft.
