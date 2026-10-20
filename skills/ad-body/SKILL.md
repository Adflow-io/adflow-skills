---
name: ad-body
description: Schrijf of scherp de body (primary text / tekst-op-scherm) van een Meta-ad aan. Kiest de structuur die bij het concept past, voedt zich met klantwoorden uit reviews/comments, en haalt AI-slop eruit. Lean output.
---

# Ad Body

Een body verkoopt niet met mooie zinnen maar met een **natuurlijk verhaaltje in de stem van de persona**, met
klantwoorden erin verweven en een concreet moment dat de kijker herkent. Deze skill schrijft die body, of scherpt
een bestaande aan. Output blijft kort en zonder ruis.

## Kies de structuur die bij het concept past

**Geen vaste default.** Lees eerst het concept/angle en kies dan de vorm die er het beste bij past. Als het niet
duidelijk is, kies de structuur die je zou pakken en zet er in één regel bij waarom (geen menu voorleggen tenzij de
gebruiker twijfelt). Volledige uitwerking staat in `references/script-frameworks.md` en `references/ugc-format-templates.md`.

| Structuur | Beats | Past bij |
|---|---|---|
| **Demo** | Herkenning → Payoff → Proof → CTA | product met zichtbaar moment/gebruik; connectie-/samen-doen-concepten |
| **PAS** | Probleem → Agitatie → Oplossing | een scherpe frictie of bezwaar (prijs, suiker, gedoe) |
| **Fact → Insight** | Feit → wat dat voor jou betekent | educatief/transparantie (gembergehalte, weinig suiker) |
| **Story / ons-verhaal** | Aanleiding → hoe/waarom wij → nu | merk, makers, authenticiteit (founders ad) |
| **BAB** | Before → After → Bridge | transformatie/ritueel-verandering (koffie inruilen) |

**De CTA volgt het doel/type van de video, niet één vaste vorm.** Kies:
- **Zacht/organisch** (awareness, connectie, brand/ons-verhaal): één warme slotregel die als onderschrift van een
  organische post kan staan. Geen "koop nu".
- **Direct/DR** (conversie, deal, offer, most-aware): expliciete actie of aanbod (bv. de korting, "nu op de site",
  een reden om nu te klikken). Mag verkopen.

Twijfel je? Leid het af uit de angle/awareness en het format (deal-ad = direct, founders/connectie = zacht).
Ongeacht de vorm: **proof verweef je als natuurlijk verhaal, nooit een letterlijke review tussen aanhalingstekens.**
Natuurlijk > citaat.

## Harde regels (de "done"-lat)

Een body is pas af als hij dit allemaal haalt. Check ze voor je 'm teruggeeft.

- [ ] **Klantwoorden.** De taal komt uit `reviews.md` / `comments.md` van de klant, niet uit je eigen kop. In een
      klantproject: lees die eerst. Geen letterlijke quotes tussen aanhalingstekens, wel hun woorden verweven.
- [ ] **Geen lange gedachtestreep (—).** Komma, punt of spatie. Zo schrijft niemand.
- [ ] **Geen faux-casual openers** ("Eerlijk,", "Look,", "Kijk,", "Here's the thing"). Begin met de zin zelf.
- [ ] **Geen AI-slop.** Geen tricolon-drama ("Sneller. Slimmer. Beter."), geen holle intensifiers ("echt", "gewoon"
      als vulling), geen stapeling van bijvoeglijke naamwoorden. Bij twijfel: draai `anti-ai-writing` eroverheen.
- [ ] **Natuurlijk, niet over-gecomprimeerd.** Korter mag, maar niet tot het niet meer als een mens klinkt.
- [ ] **Persona-vriendentest.** Elke regel: zou déze persona dit écht zo tegen een vriend(in) zeggen? Geen
      productjargon, geen merk-tagline in de body, concreet i.p.v. glad. Zie [[feedback-persona-friend-test]].
- [ ] **Product minstens één keer natuurlijk benoemd** (wát het is), ook in organische ads. Zie [[feedback-name-product-once]].
- [ ] **CTA/afsluiter varieert** (geen vaste tagline, geen verplichte merk-eindtag; volgt de funnel). Zie [[feedback-cta-not-fixed]].
- [ ] **Eén body kan meerdere hooks bedienen** als de gebruiker dat vraagt — dan mag de body niet naar één
      specifieke hook terugverwijzen.
- [ ] **Klopt met de winnende angle/taal** uit `clients/<klant>/winners.md` (bv. een NL-first merk → NL eerst).

**Vorm:** primary text (Meta-copy) mag iets meer ademen; tekst-op-scherm = korte losse regels. Vraag of leid af
welke van de twee, en schrijf ernaar.

**Scope:** deze skill is voor **video** (primary text + tekst-op-scherm bij broll/UGC). Voor **static-ads** gelden
eigen regels (o.a. de headline ís de ad, "assume no one knows or cares", clarity↔curiosity) — die staan in
`references/static-formats.md` en de `references/designer-brief-static.md`, niet hier.

## Twee modes

### Mode A — Body schrijven
1. Verzamel de grondstoffen: concept/angle, persona, de hook(s), en de klantwoorden uit reviews/comments.
2. Kies de structuur die bij het concept past (zie tabel boven).
3. Schrijf **één body**. Geen drie varianten dumpen; één goede, plus eventueel één alternatieve opening als je
   twijfelt tussen twee ingangen.
4. Zet er in één regel onder welke structuur + beats je aanhield en welke klantwoorden je gebruikte. Kort.
5. Stel daarna **2-3 alternatieve structuren voor die ook bij dit concept passen** — alleen benoemd, niet
   uitgewerkt: de framework-naam + één regel welke andere hoek het zou geven. Zo ziet de gebruiker de opties zonder
   dat je drie bodies dumpt.

### Mode B — Body aanscherpen
1. Leg de bestaande body naast de "done"-lat en benoem wat mist (meestal: te AI, geen klantwoorden, te lang, of een
   streep/faux-casual opener).
2. Herschrijf 'm. Toon **Was → Nu** met één regel waarom het beter is. Max één herschrijving tenzij gevraagd.
3. Behoud de stem van de gebruiker; sand 'm niet glad tot marketing-taal.

## Output-format

Lean en scanbaar. **Alleen de body en een korte waarom, geen intro of samenvatting.**

```
<body, in doorlopende regels>

structuur: <framework> — <beats>
klantwoorden: <de 2-3 woorden/frasen die je verweefde>

andere hoeken (niet uitgewerkt):
- <framework> — <één regel welke hoek dit geeft>
- <framework> — <één regel welke hoek dit geeft>
```

Voor een aanscherp-pass: toon Was → Nu met één regel waarom.

## Notities

- In een klantproject: `clients/<klant>/reviews/reviews.md`, `comments/comments.md` en `winners.md` zijn je bron.
  Zonder die data eerst gelezen te hebben schrijf je geen body.
- Sluit aan op `power-hooks` (levert de hook) en `anti-ai-writing` (eindcheck op slop). Deze skill is workflow C3 in
  `references/workflow-map.md`.
- De body is één copy-artefact dat zowel de editor-brief (D1) als de creator-brief (D2) voedt. Hou 'm format-neutraal
  genoeg dat beide 'm kunnen gebruiken, tenzij de gebruiker expliciet één vorm vraagt.
