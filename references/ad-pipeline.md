# Ad-pijplijn (static + video) — rol → workflows → skills → keten

**Methode:** stap 4–5 uit [videos/youre-not-behind-ai-content.md](videos/youre-not-behind-ai-content.md) (Personal Brand
Launch): één **rol** → breek af in **workflows** → **elke workflow = één skill (SOP)** → test op een echte taak &
verfijn tot ≥ jij → **koppel de handoffs** tot één lineaire keten. Aangescherpt met de kniplijn-principes uit
[workflow-map.md](workflow-map.md).
**Rol:** *Ad-creatie* (Creative Strategist + Designer/Editor). **Master-context = `clients/<klant>/brand.md`** (elke skill laadt die).
**Twee gouden regels:** ultra-specifiek (meetbaar), en niks vervangen tot AI het even goed doet als jij. Mens houdt
**ideation, prioritering, eindbeslissing en QC**.

> **Dit is de vaste werkwijze voor élke ad — static én video.** Het **vehicle wordt gekozen bij S2**. Voor **video**
> zijn er twee onafhankelijke pre-copy-assen: **S2 delivery/format** (het vehicle + hoe het gedragen wordt) en **S3 arc**
> (de verhaalstructuur). **S3 (arc) en S5 (script) zijn video-only**; static vouwt de structuur in zijn eigen format
> (`static-formats.md`) en slaat S3/S5 over. S1 (slots) en E (feedback) zijn gedeeld.

## De keten (output van elke stap = input van de volgende)

```
dimensions + gaps + winners
        │  S1 slots  [mens beslist · AI stelt voor]          ← gedeeld (vehicle-agnostisch)
        ▼
  concept-slots  (Persona × Angle × Awareness)
        │  S2 delivery/format  [AI + mens QC]                ← vehicle + uitvoering · kies ook static/video
        ▼
  slot + vehicle + delivery/format
        │  S3 arc  [VIDEO only · AI stelt menu voor · mens kiest]   ← verhaalstructuur (20 arcs)
        ▼
  slot + delivery/format + arc
        │  S4 voorzet  [AI · mens kiest]   ← voorzetjes-first (copy in delivery × arc)
        ▼
  goedgekeurde voorzetjes (static: headline+on-image · video: hook(s)+body)
        │  S5 script  [VIDEO only · AI schrijft · mens keurt goed]   ← volledig script + humanizer-pass
        ▼
  goedgekeurd volledig script (video)
        │  S6 brief  [AI + mens QC]
        ▼
  producereerbare brief + adnaam  →  Adflow → live
        │  E feedbackloop  [AI pullt · mens beslist]          ← gedeeld
        ▼
  winners.md  ──(welke persona/angle/vehicle/delivery/arc wint)──► terug naar S1
```

## De workflows — per stap, per vehicle

| # | Stap | Static-skill | Video-skill | Wie |
|---|---|---|---|---|
| **S1** | slots | `ad-slots` *(vehicle-agnostisch; dient beide)* | *idem* | **mens beslist**, AI stelt voor |
| **S2** | delivery/format | `static-format` (static visuele formats, bron `static-formats.md`) | `video-format` (vehicle + uitvoering) | AI + mens QC |
| **S3** | arc *(video only)* | — *(structuur zit in static-format)* | **menu** van de 20 arcs (`script-frameworks.md`) met fit → mens kiest | AI stelt voor · **mens kiest** |
| **S4** | voorzet | `static-voorzet` (headline + on-image) | `video-voorzet` (hook(s) + body, via `hook-levers` + `power-hooks` + `ad-body`) | AI · **mens kiest** |
| **S5** | script *(video only)* | — *(static: voorzet ís de copy)* | volledig script (arc-skelet in de gekozen delivery) → **humanizer-pass** (`humanizer-passes.md`) → mens keurt goed | AI schrijft · **mens keurt goed** |
| **S6** | brief | `designer-brief` (`designer-brief-static.md`) | `video-brief` (editor/creator-briefing) | AI + mens QC |
| **E** | feedback | Meta MCP → `winners.md` → terug naar S1 | *idem* | AI pullt, mens beslist |

**Klant-fit per stap:** welke slots/delivery/arcs/hooks bij déze klant passen → `clients/<klant>/format-fit.md`,
`hooks.md`, `winners.md`, `brand.md`. De referenties (`references/*`) zijn klant-agnostisch — zie
[[feedback-no-client-data-in-refs]].

## De twee assen (video): delivery/format en arc
Een videoscript wordt bepaald door **twee onafhankelijke keuzes**, allebei vóór de copy:
- **S2 delivery/format** = het **vehicle + de uitvoering** (*hoe* het gefilmd/gedragen wordt).
- **S3 arc** = de **verhaalstructuur** (*wat* je vertelt, de beat-volgorde).

Ze zijn orthogonaal: dezelfde arc (bv. Before/After) kan als VO-over-broll, talking-head óf tekst-only; dezelfde
delivery (bv. talking-head) kan een PAS-, Myth→Truth- of Listicle-arc dragen. Apart gehouden om menu-explosie
(delivery × arc) te vermijden en om varianten te kunnen testen. De copy (S4/S5) hangt van beide af, dus beide liggen
vóór de voorzet vast. Volgorde: **delivery/format (S2) → arc (S3)**.

## S2 — Delivery/format (video)
De vehicle + uitvoering. Kies uit (Notion-visuele formats als Staged Moment/POV/Flat Lay zijn instanties hiervan):
- **Talking-head (to-cam)** — spreker praat recht in de camera.
- **Voice-over over broll** — narratie over beeld, geen zichtbare spreker.
- **Observational / fly-on-the-wall** — natuurlijk geluid, geen VO; boodschap via de scène (+ evt. tekst). (bv. Staged Moment)
- **Dialoog / two-hander** — 2+ personen praten (skit, gesprek).
- **Tekst-only op broll** — geen stem; on-screen tekst + muziek dragen het.
- **Green screen** — to-cam spreker vóór relevante beelden.
- **Foto/slideshow + VO** — stills met voice-over (voiceover-format).
- **Animatie / motion graphics** — incl. AI-animation; geen live footage.
- **Hands / POV (no face)** — handen/eerste-persoon + VO of tekst. (bv. POV, Flat Lay)
- **Interview / podcast / street-interview** — Q&A of vox-pop, audio-gedreven.

Constraint/weging = klant-fit (`format-fit.md`, winners) + brand.md. De gekozen delivery gaat mee naar S3/S4/S5 en
staat in de S6-brief als productie-spec (bv. "VO over broll, rustige ouder-stem").

## S3 — Arc (video) — voorzetjes-menu
De verhaalstructuur, uit `script-frameworks.md` (20 arcs: PAS, Before/After, Objection Crusher, Listicle, Myth→Truth,
Founder Story, UGC Testimonial, Day-in-life, Curiosity/Open Loop…). Stel een **menu** voor met fit per slot/delivery,
mens kiest (mag meerdere → testvarianten). Heeft de arc een gevuld **Notion-format-template**, dan is dat het
beat-skelet voor S5; anders het arc-schema uit `script-frameworks.md` + de DR-laag (Deel B–E).

## Output-conventie (alle voorstel-stappen)
S1–S4 leveren **genummerde** opties, zodat de gebruiker met nummers kan kiezen ("ga verder met 1, 2, 5").
Voorstel-stappen **beslissen niet** — de gebruiker kiest. Voorzetjes-first: eerst korte voorzetjes (S4), pas ná
akkoord het volledige script (S5) en dán de brief (S6) — zie [[feedback-voorzetjes-first]],
[[feedback-full-script-before-brief]].

## S5 — Script-stap (video)
De delivery/format (S2) en arc (S3) liggen vast; hier schrijf je het **volledige script** uit in die delivery, met de
arc als beat-skelet (Notion-template als de arc er een heeft, anders `script-frameworks.md` + de DR-laag Deel B–E).
Draai er de **humanizer** overheen (`humanizer-passes.md` — 2 humanizers + `anti-ai-writing`), en lever het script
**puur** (geen beeld/tekst-op-scherm tenzij gevraagd). De **brief (S6) maak je pas als de gebruiker tevreden is met het
script** — zie [[feedback-full-script-before-brief]]. Static heeft S3/S5 niet (daar is het voorzet al de on-image copy).

## Verhouding tot de losse copy-skills
`power-hooks` (hooks) en `ad-body` (primary text / tekst-op-scherm) zijn de **video-copy-bouwstenen**; `video-voorzet`
(S4) orkestreert ze tot voorzetjes. `anti-ai-writing` is de gedeelde slop-eindcheck (beide vehicles). `ad-naming`
(S6, beide) bouwt de adnaam los van de brief.
