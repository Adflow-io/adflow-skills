---
name: ad-slots
description: Stel een geprioriteerde shortlist van ad concept-slots (Persona × Angle × Awareness) voor, op basis van dimensions, coverage-gaps, objection-map en winners. Stap S1 van de ad-pijplijn — vehicle-agnostisch (dient zowel static als video). Beslissing blijft menselijk — deze skill stelt voor en prioriteert, kiest niet. Lean output.
---

# Ad Slots (S1)

De eerste stap van de [ad-pijplijn](../../references/ad-pipeline.md): bepaal **welke concept-slots** we gaan maken.
Een concept-slot = **Persona × Angle × Awareness**. **Vehicle-agnostisch:** een slot voedt zowel static (S2
`static-format`) als video (S2 `video-format`) — het vehicle wordt pas in S2 gekozen. Deze skill **stelt voor en
prioriteert**; de gebruiker beslist (ideation/prioritering/beslissing blijven menselijk). Geen copy hier — dat is S3.

## Input (lees eerst, raad niet)
- `clients/<klant>/dimensions/personas.md` + `angles.md` — de bouwstenen (welke persona's, welke angles, beste-persona per angle).
- `clients/<klant>/winners.md` — wat op **spend** draait (bewezen angles/persona's om te repliceren).
- `clients/<klant>/comments/comments.md` + `reviews.md` — objecties (bezwaar → counter-slot) + onbenutte persona's/angles.
- `IMPROVEMENTS.md` (#3 coverage-matrix) + `brand.md` — de gaps en de master-context.

## Methode — 3 bronnen voor slots
1. **Repliceer winners.** Neem de angles/persona's die op spend dragen en zet ze in. Een winner in het ene vehicle
   (bv. video) is vaak een sterk slot om óók in het andere vehicle (static) te maken — noteer dat als kans, maar het
   vehicle kies je pas in S2. (Hoogste zekerheid.)
2. **Vul de 3 gaps** (Dara Denney):
   - **Persona-gap:** welke persona's targeten we niet / over-indexeren we? (bv. onbenutte audiences uit comments/reviews)
   - **Awareness-gap:** te veel bottom/mid → maak **TOF-acquisitieslots** bij om de funnel te voeden.
   - **Diversiteit-gap:** elke kern-persona hoort **2–3 unieke angles** + spreiding in awareness.
3. **Objection-map.** Elk top-bezwaar (bv. prijs) → minstens één counter-slot met de awareness die erbij hoort
   (prijs = meestal most-aware/BOF).

## Prioriteer op: probleemgrootte × audience-omvang × bewijs/LTV
Zwaarder = eerst. Markeer per slot of het een **[winner-replica]**, **[gap]** of **[objection]** is. Flag een
**nieuwe persona/angle** die nog geen token heeft in `clients/<klant>/brand.md` (sectie Naamconventie) als `⚠︎ nieuw token`.
**Vraag hier NIET om bevestiging** — flaggen is genoeg. Een nieuw token bevestig je pas op het moment dat de
gebruiker die specifieke slot kiest om uit te werken (de stap naar S2).

## Output-format
Lean tabel, gesorteerd op prioriteit. **Alleen de slots + korte waarom. Geen intro/samenvatting.**

```
# Ad concept-slots — <klant> (voorstel, jij prioriteert)

| # | Persona | Angle | Awareness | Type | Waarom (1 regel) |
|---|---|---|---|---|---|
| 1 | … | … | … | winner-replica | … |
| 2 | … | … | … | gap · ⚠︎ nieuw token | … |
…

Aanrader om mee te starten: #<n> (+ één regel waarom).
```

Zet er nooit meer dan ~7 slots in; liever scherp dan volledig.

## QC-lat
- [ ] Elke kern-persona heeft **2–3 angles** (diversiteit), niet één.
- [ ] Er zit minstens één **TOF-acquisitieslot** bij (awareness-gap voeden).
- [ ] Het **#1 bezwaar** heeft een counter-slot.
- [ ] Winners zijn herkenbaar terug (niet alleen nieuwe gokken).
- [ ] Nieuwe persona's/angles gemarkeerd als te bevestigen token.

## Notes
- Workflow **S1** in `references/ad-pipeline.md`. Uit (gekozen slot) → in voor **S2**: `static-format` (static) of
  `video-format` (video). Het vehicle wordt in S2 gekozen.
- Deze skill **beslist niet** — hij levert een geprioriteerd menu; de gebruiker kiest wat we maken.
- **Token-timing:** in S1 alleen flaggen (`⚠︎ nieuw token`), niet vragen te bevestigen. Bevestigen gebeurt pas
  wanneer de gebruiker die specifieke slot kiest om uit te werken; dán laat je 't bevestigen en voeg je 't toe aan
  `clients/<klant>/brand.md` (sectie Naamconventie).
