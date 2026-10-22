# Adflow Ads — Workflow-map (rol → workflow → actie)

**Doel:** de ad-productie afbreken in workflows die elk één skill/agent kunnen worden, zodat we stap voor stap automatiseren zonder kwaliteit te verliezen.
**Methode:** stap 4-5 uit de video You're Not Behind (Yet) (Hormozi's rol→workflow→actie), maar aangescherpt (zie principes).
**Status:** levend document. Laatst bijgewerkt 2026-08-29.

## Kniplijn-principes (hoe we het beter doen dan de video)
1. **Snij op artefact, niet op functietitel.** Eén workflow = één schone output die je aan de volgende zou overdragen (hookset, body, brief). Agents geven een *ding* door, geen "rol".
2. **Granulariteit:** klein genoeg dat één skill het haalt en 100x testbaar is, groot genoeg dat er een bruikbaar artefact uitrolt.
3. **Markeer wie het doet:** `[AI]` · `[mens]` · `[AI + mens QC]`. Ideation, prioritering en eindbeslissing blijven menselijk (zegt de video zelf).
4. **Elke workflow heeft een "done"-lat** (de QC-checklist), anders weet de agent niet wanneer goed genoeg.
5. **Vervang niks door AI tot het even goed of beter is dan jij.**

## Bevestigd
- **Team.** Editor (D1) en creator (D2) blijven twee aparte workflows → twee aparte briefing-skills.

## De pijplijn

### Stage A — Intake & research (ruwe klantdata → brein)
| # | Workflow | In → Uit | Wie | Status |
|---|---|---|---|---|
| A1 | Klantdump verwerken | Adbase/landing → `brand.md` | AI + mens QC | ✅ handmatig |
| A2 | Dimensies bouwen | brand → `dimensions/{products,personas,angles}.md` | AI + mens QC | ✅ |
| A3 | Reviews minen | reviews CSV → `reviews.md` (thema's, klantwoorden, bezwaren) | AI | ✅ |
| A4 | Ad-comments minen | comments CSV → `comments.md` (bezwaren gerankt, prijs #1) | AI | ✅ |
| A5 | Performance pullen | Meta MCP → `winners.md` (spend-first) | AI | ✅ |

### Stage B — Strategie (brein → plan)
| # | Workflow | In → Uit | Wie | Status |
|---|---|---|---|---|
| B1 | Objectie/coverage-map | reviews+comments → objectie-dekking | AI + mens QC | ⚠️ deels (in roadmap) |
| B2 | Roadmap bouwen | alles → conceptbibliotheek (prod×pers×angle×zone×format×delivery) | AI + mens QC | ✅ |
| B3 | Concepten prioriteren | roadmap+winners → wat eerst | **mens beslist** | ✅ |

### Stage C — Creatief schrijven (concept → copy)
| # | Workflow | In → Uit | Wie | Status |
|---|---|---|---|---|
| C1 | Hooks genereren | concept+klantwoorden → 3-4 hooks | AI + mens QC | ✅ skill `power-hooks` (mode A) |
| C2 | Hooks aanscherpen/scoren | hook → sterkere hook | AI + mens QC | ✅ `power-hooks` (mode B/C) |
| C3 | Body schrijven | hooks+angle+reviews → primary text | AI + mens QC | ✅ skill `body` |
| C4 | Anti-AI pass | copy → menselijke copy | AI + mens QC | ✅ skill `anti-ai-writing` |

### Stage D — Briefing (copy → producereerbare brief)
| # | Workflow | In → Uit | Wie | Status |
|---|---|---|---|---|
| D1 | Editor-brief | copy → tekst-op-scherm brief (geen beeld/tijd/meta) | AI + mens QC | ⚠️ format bekend, geen skill |
| D2 | Creator-brief | copy → talking-head/UGC regie | AI + mens QC | ⚠️ format bekend, geen skill |
| D3 | Ad benoemen | concept → naam volgens conventie | AI | ✅ skill `naming` (ID uit Adflow) |
| D4 | Designer-brief (static) | copy+format+design-intentie → producereerbare static-brief | AI + mens QC | ⚠️ format bekend (`../references/designer-brief-static.md`), geen skill |

### Stage E — Feedbackloop (resultaat → leren)
| # | Workflow | In → Uit | Wie | Status |
|---|---|---|---|---|
| E1 | Meta-cijfers pullen (1-2 wk) | MCP → update `winners.md` | AI | ⚠️ handmatig |
| E2 | Ads in buckets classificeren | numbers → scale/plateau/big-swing | AI | ❌ gap |
| E3 | Learnings terug in roadmap | winners → roadmap-update | **mens beslist** | ⚠️ handmatig |

**Handoff-lijn:** A → B → C → D → E → (terug naar B). De lineaire workflow die elkaar triggert.

## Witte vlekken (volgende skills, op frequentie)
1. ~~C3 — Body-skill~~ ✅ gebouwd: `body`.
2. ~~D3 — Naamgeving~~ ✅ gebouwd: `naming` (+ `references/naming-convention.md`).
3. **D1/D2/D4 — Briefing-skills** (editor · creator · designer-static, elk apart). D4-format staat al in
   `../references/designer-brief-static.md`.
4. **E2 — Bucket-classificatie** (scale/quick-plateau/big-swing).

## Skill-familie (stage C compleet)
`power-hooks` (C1/C2) → `body` (C3) → `anti-ai-writing` (C4). De hele copy-stage heeft nu skills.
**Deze copy-skills zijn voor video.** Voor **statics** loopt copy apart: kies eerst het format in
`../references/static-formats.md` en schrijf headline/on-image copy vanuit de klantwoorden + de messaging-wetten
daar (nog geen aparte static-copy-skill — witte vlek).
Volgende logische skill: **D1/D2/D4 briefing-skills** (de drie brieftypes).
