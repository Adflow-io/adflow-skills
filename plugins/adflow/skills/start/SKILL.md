---
name: start
description: The front door for making or planning ads. Asks what the user wants (plan several concepts or quickly make one), for which brand and based on what (iterating winners, existing pillars, research, promo, own input (an idea, wish or briefing), or something new such as research, promo, a season, a launch, competitors, a new market or business signals), checks in Adflow what is already there, gives short advice and routes to the right next step. Use when someone says "ik wil ads maken", "ik wil concepten plannen", "planning voor Q4", "nieuwe ronde", "waar begin ik", "snel een conceptje", or starts ad work without naming a step. Not for a step the user already names (go straight to `slots`, `video-format`, `video-brief`, etc.).
---

# Start (S0)

The entry point of the [ad pipeline](../../references/ad-pipeline.md). It turns a vague "I want ads" into a clear
starting point: goal, brand, basis and what is already available, then hands off to the right step (usually S1
`slots`). Written so a first-timer knows what to do at every step, and short enough for daily use.

## Rules
- **One question per turn.** Ask, stop, wait. Never stack two questions.
- **Numbered options**, one line each, so the user can answer with `1` or `1+4`.
- **Skip what is already known.** If the message already names the goal, brand or basis, do not ask it again; say in
  one line what you took from it.
- **Short.** No intro, no recap of what the user said. Questions in the user's language (usually Dutch).
- **Check, don't guess.** The inventory in step 4 comes from Adflow (and Drive or Meta where needed), see
  [bronnen.md](../../references/bronnen.md). Missing is missing; never fill a gap with assumptions.

## Steps

### 1. Goal
Ask what the user wants to do:

```
Wat wil je doen?
1. Plannen: meerdere concepten voor een periode of pillar (bv. Q4)
2. Maken: snel één concept uitwerken
```

### 2. Brand
Ask which brand, unless it is clear. Then load the brand guidelines and the brand's Drive handbooks (see
[bronnen.md](../../references/bronnen.md)).

### 3. Basis
Ask what the work is based on. Options run from most to least used. Several answers are allowed, and a combination is normal (a Q4 plan can be season +
promo + winners last year).

```
Waar baseer je het op? (meerdere mag, bv. 1+5)
Bestaand
1. Winners itereren (variaties op wat nu draait)
2. Bestaande pillars
3. Bestaand research (reviews, comments, organic)
4. Lopende promo
Nieuw
5. Seizoen of moment
6. Launch nieuw product of collectie
7. Bestaand product of collectie pushen
8. Nieuwe promo
9. Nieuw research
10. Concurrenten en inspiratie
11. Business-signalen (bestsellers, voorraad, marge)
12. Nieuwe markt of taal
Eigen input
Typ je eigen idee, wens of briefing (mag samen met nummers)
```

**Before asking, load the brand's active pillars** and show them under option 2 as `2a`, `2b`, … (code and name,
one line each), so the user can pick a pillar directly. No active pillars: leave option 2 out. Keep the other numbers
as they are, so daily users can rely on them. Own input is its own group without a number: the user types it, alone or next to
numbers.

**End the list with a suggestion** of one line: the numbers you would pick and why, based on a quick look at the
brand (winners now, pillars, research, the date and upcoming moments). For example:
`Suggestie: 1+5, er draaien 12 winners en kerst komt eraan.`

**Quick path (goal 2, Maken):** if the user already has an idea or slot in mind, skip this list. Ask only:
"Heb je al een idee of slot? Zo ja, welk?" Then do step 4 only for the sources that idea needs and go to step 6.

### 4. Inventory: what is there, what is not
Check the sources that matter for the chosen basis yourself and show one table. Only rows that matter for this
basis; always include research and winners now.

| Source | What to check |
|---|---|
| Pillars | Active pillars and their agreements in Adflow |
| Promo | Offer values in the dims, promo agreements in the pillar or brand guidelines |
| Reviews | Research document with reviews; date of the last update |
| Comments | Research document with ad comments; date of the last update |
| Organic | Viral videos in the brand's Inspiratie board in Adflow; date of the last upload |
| Winners now | Live, last 30 days, judged on spend first, ROAS second |
| Winners same period last year | Live, same weeks last year. Always for a season (5) or a seasonal brand |
| Own input | What the user brings (an idea, wish or briefing); recent meeting notes or mail if a connector is available; otherwise ask |
| Existing concepts | Open concepts and briefs, so nothing is made twice |
| Markets and languages | Markets in Adflow (for 12) |
| Handbooks | The brand's briefing and ad copy handbooks in Drive, and its AI instructions in Adflow for launch rules |

Status per row: ✅ present and recent · ⚠️ present but old (older than 3 months) or thin · ❌ missing.

Output:

```
| Bron | Status | Suggestie |
|---|---|---|
| Pillars | ✅ 4 actief | – |
| Comments | ⚠️ laatst bijgewerkt in juni | opnieuw minen |
| Winners vorig jaar | ❌ | ophalen, merk is seizoensgebonden |

Advies: <one line: what to do first and why>
Zo doen, of direct door?
1. Advies volgen
2. Direct door naar <next step>
```

### 5. Pillars (only for goal 1, Plannen)
Pillars are the output of a plan, not a basis. Slots fall inside a pillar, so this comes before `slots`.
- **Fitting pillars exist:** let the user pick them and skip the rest of this step.
- **None, or they do not fit the basis:** propose 2 to 4 pillars from the chosen basis and the research. Mix both kinds:
  - **Time-bound:** a promo, season or launch (for example a holiday sale, a gifting moment, a new collection).
  - **Evergreen:** a winning angle, a core persona or a hero product that keeps running.
  One line per pillar: name · kind · why. Let the user choose, then create the chosen pillars in Adflow.

### 6. Route
Send the user to the next step, in one line ("Door naar slots, per pillar."). Then follow that skill.

| Basis | Next step |
|---|---|
| 1 Iterate winners | `slots` with the winners as replica slots; for a single winner skip to `video-format` or `static-format` with the same slot |
| 2 Existing pillars | `slots` within the chosen pillar(s) |
| 3 Existing research | `slots` |
| 4 Running promo, 8 New promo | `slots` with the offer as a fixed condition |
| Own input | Turn the input into conditions (what, why, deadline), then `slots` |
| 5 Season or moment | List what fits the brand in that period (moments, gifting, weather, payday), then `slots` with that as a condition |
| 6 Launch, 7 Push product | Check that the product exists in the dims (add after approval), then `slots` for that product |
| 9 New research | `review-research` for reviews and ad comments; for organic follow [organic-research.md](../../references/organic-research.md) (Claude makes the keywords, the person searches on a phone and uploads to Inspiratie). Then `slots` |
| 10 Competitors | Collect 5 to 10 relevant competitor or inspiration ads and name the pattern in each, then `slots` |
| 11 Business signals | Ask the user (or the brand's data) which products to push, then `slots` for those products |
| 12 New market or language | Check market and fallback language in Adflow; winners in the main language are the first candidates for a language version |

**Plan (goal 1):** after `slots`, ask how many concepts fit the period and spread them over the pillars in one
table: concept · pillar · slot · vehicle · deadline. Then work them out one by one through the pipeline.

## Output shape
Each turn is one question with numbered options, or the inventory table with one line of advice. Never more than
one screen. The flow ends with the handoff line and the next skill.
