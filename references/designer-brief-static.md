# Designer-brief (static) — het derde brieftype

**Rol in de machine:** Stage D, workflow **D4** in [workflow-map.md](workflow-map.md). Naast de **editor-brief** (D1,
bestaande footage) en **creator-brief** (D2, nieuw filmen) is dit de brief voor de **Designer** die een static bouwt.
Format-keuze + messaging-wetten uit [static-formats.md](static-formats.md). **De adnaam staat NIET in de brief** (dat
is meta) — die maak je apart met `ad-naming` bij het uploaden. De brief begint met een **Dimensions**-blok.

> **Let op:** `ad-body` en `power-hooks` zijn **video**-skills — gebruik ze hier **niet**. Static-copy (headline +
> on-image tekst) schrijf je rechtstreeks vanuit de klantwoorden (`reviews.md`/`comments.md`) + de twee
> messaging-wetten in `static-formats.md`. Een eigen static-copy/designer-skill is nog een witte vlek (IMPROVEMENTS #4).

## Discipline (zelfde als editor/creator-brief, zie `memory/reference-briefing-format.md`)
De brief is **puur producereerbaar: alleen wat de designer op de static zet.** Analyse, angle-checks, tags en
klantwoord-verantwoording horen in een **losse notitie boven de brief**, niet in de brief zelf. Zo weet de designer
precies wat op scherm moet, zonder ruis.

## Vaste velden

> Het **Dimensions**-kop-blok is **identiek aan de editor-brief** (zie `memory/reference-briefing-format.md`) —
> zelfde velden, alleen de Format-waarde verschilt (static-format hier vs video-format daar).

```
# Designer-brief — <korte concept-naam> · <N> statics

## Dimensions
- **Product:** <naam>
- **Persona:** <naam>
- **Angle:** <naam>
- **Awareness:** <unaware / problem-aware / product-aware / most-aware>
- **Format:** <uit static-formats.md>
- **Taal:** <nl / en / de>

## To do
- <N> static(s): elke **tekstvariant = eigen static** (eigen headline, gedeeld beeld). Elke static in **beide ratio's:
  1:1 (1080×1080) én 9:16 (1080×1920)** → N × 2 = aantal bestanden. 9:16 stapelt verticaler dan 1:1.
  ·  Product + link: <productnaam + URL>

## Leesvolgorde (eye-flow)  ← wat het oog in welke volgorde ziet
1. <HOOK — grootste element, valt het eerst op>
2. <qualifier — voor wie / waarom relevant>
3. <product — het beeld>
4. <social proof / geruststelling>
Gestuurd met: sizing (grootste = 1), contrast (kleur/vlak op de hook), witruimte (rust rond de hook).

## Op scherm
- **Headline:** <de headline — assume-no-one-knows-check gehaald>
- **Sub/benefits:** <2–4 korte regels in klantwoorden>
- **Social proof / trust:** <bv. "gemaakt door <maker>" of ★-laag, indien toegestaan voor dit ad-type>
- **Offer/CTA:** <alleen bij deal/BOF; bij organisch: zacht of weglaten>

## Visuele behandeling (kies bewust; optioneel)
- Atypische tekst: <tekst op relevante plek — anders leeg laten>
- Make-the-invisible-visible: <visual van het gevoel/pijnpunt — anders leeg laten>

## Assets die je nodig hebt
- <foto's/illustraties/logo/kaartbeeld — wat de designer moet aanleveren of krijgt>

## Swipe-referentie
- <link/omschrijving van 1 voorbeeld-static waar dit op lijkt>
```

## QC-checklist (de "done"-lat — vóór oplevering)
- [ ] **Assume-no-one-knows:** headline meteen relevant voor iemand die het merk niet kent? (tenzij BOF/offer)
- [ ] **Eén duidelijke eye-first:** landt het oog op de belangrijkste boodschap? (squint-test: knijp je ogen dicht —
      zie je nog de hook?)
- [ ] **Klantwoorden i.p.v. merktaal** (uit `reviews.md`/`comments.md`).
- [ ] **Clarity of curiosity gekozen** — niet in het midden.
- [ ] **Leesbaar op mobiel:** max ~1 hoofdboodschap, genoeg contrast/witruimte, geen tekst-muur.
- [ ] **Klopt met brand.md** (DON'Ts: geen verkoop-eindscherm bij *organische* ads; prijs alleen bij deal-ads).
      NB: letterlijke klantquotes **mogen** op een testimonial-static — de "geen-quote"-regel geldt alleen voor
      broll/video.

## Notities
- **Copy-bron:** klantwoorden uit `reviews.md`/`comments.md` + de messaging-wetten in `static-formats.md`. Voor een
  static is de **headline** de hook. Gebruik hier **niet** `ad-body`/`power-hooks` (die zijn voor video).
- Design-principes komen uit [videos/adcrate-static-ads-2026.md](videos/adcrate-static-ads-2026.md) (deel 3);
  ze staan hier als **briefvelden**, niet als losse designtheorie.
- ✅ Skill `designer-brief` (S4) codificeert deze brief — `~/.claude/skills/designer-brief/`.
