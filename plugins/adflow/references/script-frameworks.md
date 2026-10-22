# Script-frameworks — arc-structuren + DR-laag (video)

**Rol in de machine:** dé bron voor de **narratieve arcs** (verhaalstructuur). De arcs zijn het **S3-menu (arc)** van de
[ad-pijplijn](ad-pipeline.md); de gekozen arc wordt in **S5 (script)** uitgeschreven. **Klant-agnostisch.**
(Samenvoeging van de vroegere `dr-script-frameworks.md` + de arc-bibliotheek.)

Verhouding tot de andere assen/bronnen:
- **Arc (dit bestand, S3)** = *wat* je vertelt: de beat-volgorde. **Delivery/format (S2)** = *hoe* het gedragen wordt
  (VO/talking-head/tekst-only…). Twee onafhankelijke assen; zie `ad-pipeline.md`.
- **Notion "UGC Format Templates"** = het uitgeschreven **beat-skelet per arc/format** (Founders Ad, This vs That,
  Before/After…). Heeft de gekozen arc een gevuld Notion-template, dan is dat leidend voor de beats; anders het
  arc-schema hieronder.
- **Dit bestand** = de generieke **arc-bibliotheek** (20 stuks) + de DR-laag (anatomie, psychologie, visualisatieregels).

Kies: slot (S1) → delivery/format (S2) → **arc hier (S3)** → voorzet (S4) → **script uitschrijven met deze arc +
DR-laag** (S5).
Bron: FoamGrip Creative Strategy Playbook (Adflow-lead) + arc-set. Vult aan op `deal-ad-frameworks.md` (offer) en `ad-reviewer` (psych-diversiteit).

---

## Deel A — De 20 arc-structuren
De arc bepaalt de **volgorde van beats** (hook → CTA). De DR-klassiekers PAS en BAB zitten er als eigen arc in
(**#1 = PAS**, **#2 = BAB**). **AIDA** (Aandacht → Interesse → Verlangen → Actie) krijgt géén eigen nummer: het is de
**overkoepelende structuur** die bijna elke arc hieronder volgt — hook = Aandacht, body = Interesse + Verlangen,
CTA = Actie.

1. **Problem → Solution (PAS)** — Hook → Problem → Agitate → Product → Demo → Benefits → CTA. Default voor producten die
   een duidelijk probleem oplossen; pijn motiveert sterker dan abstracte voordelen.
2. **Before → After (BAB)** — Hook → Before state → Product → Transformation → After state → CTA. Meer op de transformatie
   dan op het probleem. "Ik dacht dat ik gewoon slechte huid had…" → oude situatie → product → gebruik → resultaat.
3. **Product-first** — Hook → Product reveal → What it does → Demo → Benefits → Proof → CTA. Geen lange probleemopbouw;
   meteen tonen wat het is. Goed voor visueel interessante producten.
4. **UGC Testimonial** — Hook → Personal experience → Problem → Discovery → Product → Experience → Result →
   Recommendation → CTA. Voelt als een natuurlijke aanbeveling. "Oké, ik snap nu eindelijk waarom iedereen dit gebruikt…"
5. **Founder Story** — Hook → Origin/problem → Why we created it → Product → Behind the scenes → Proof → Mission → CTA.
   Sterk wanneer het merkverhaal zelf een selling point is.
6. **Demonstration / "Watch this"** — Hook → Curiosity → Demo → Unexpected result → Explanation → Benefits → CTA. De
   demo ís het verhaal. "Ik wilde testen of dit écht beter werkt dan mijn normale product." Dan laten zien.
7. **Objection Crusher** — Hook → Common objection → Address objection → Demo/proof → Benefit → Second objection →
   Proof → CTA. "Maar €40 voor een flesje?" → aantal servings → kosten per gebruik → vergelijking → bewijs. Geschikt bij
   koopintentie + twijfels.
8. **Comparison** — Hook → Old solution → Product → Side-by-side comparison → Winner → Proof → CTA. A vs B: product vs
   alternatief · vroeger vs nu · goedkoop vs duur · normaal vs nieuw · concurrentie vs jouw product.
9. **Listicle** — Hook → "3 redenen waarom…" → Reason 1 → Reason 2 → Reason 3 → Product → CTA. "3 redenen waarom ik
   nooit meer gewone havermout eet." Makkelijk schaalbaar naar veel creatives.
10. **Myth → Truth** — Hook → Myth → Contrarian statement → Explanation → Product → Proof → CTA. "Je hebt helemaal geen
    €100 serum nodig voor een goede huid." Daarna wat volgens het merk wél werkt. Goed voor pattern-interrupt.
11. **Curiosity / Open Loop** — Hook → Tease → Build curiosity → Reveal → Demo → Result → Explanation → CTA. Antwoord op
    de hook komt bewust pas later. "Ik snapte eerst niet waarom mijn collega dit iedere ochtend deed…" → "Tot ik het zelf probeerde."
12. **Social Proof Stack** — Hook → Big claim → Customer #1 → Customer #2 → Customer #3 → Product → Proof → CTA. "Meer dan
    20.000 mensen gebruiken dit inmiddels…" → verschillende reacties/resultaten.
13. **Review → Product** — Hook = review/quote → Context → Product → Demo → More reviews → CTA. Begin met het sterkste
    stukje social proof. "'Dit is letterlijk het eerste ontbijt waardoor ik tot lunch vol zit.'"
14. **"I was wrong"** — Hook → Initial belief → Why I was wrong → Product discovery → Demo → Result → Recommendation →
    CTA. Automatische verhaalboog. "Ik dacht eerlijk gezegd dat dit weer zo'n TikTok-hype was…"
15. **Day in the life** — Hook → Situation → Product naturally enters routine → Usage → Benefits → Result → CTA. Product
    is onderdeel van een dag i.p.v. het onderwerp. Sterk voor native UGC.
16. **Problem escalation** — Hook → Small problem → Bigger consequences → Failed solutions → Product → Solution →
    Outcome → CTA. Voor problemen die niet meteen urgent voelen. Probleem → frustratie → frustratie → oplossing.
17. **Failed alternatives** — Hook → "I've tried X, Y, Z…" → Why they failed → Product → Demo → Why different → Result →
    CTA. Sterk voor categorieën met veel bestaande oplossingen.
18. **Expert / Authority** — Hook → Expert insight → Problem explanation → Recommendation → Product → Evidence → CTA.
    "Als voedingsdeskundige zou ik op deze drie dingen letten…" → product als oplossing.
19. **Challenge / Experiment** — Hook → Challenge → Hypothesis → Test → Product → Results → Verdict → CTA. "Ik heb 7 dagen
    lang mijn normale ontbijt vervangen door dit." Automatisch tension + payoff.
20. **Story → Product reveal** — Hook → Story → Conflict → Turning point → Product reveal → Result → CTA. Product wordt
    laat geïntroduceerd; entertainender en minder advertentieachtig.

## Deel B — Anatomie van een DR-ad
- **Hook (eerste 3–4s)** werkt op 3 niveaus: **tekstueel** (bold statement / prikkelende vraag / claim), **audio**
  (geluidseffect, pauze, muziekshift), **visueel** (pattern-interrupt in de eerste frames). Sterkste hooks combineren
  alle drie. Vaak: leid met het **probleem** + close-up.
- **Content (midden):** presenteer product, demonstreer USP's, toon de transformatie. Volgt de arc.
- **CTA:** specifiek ("Bestel op x.nl"), verkoop het **resultaat** (niet het product), verwijder wrijving/risico
  (garantie), en voeg **verdiende** urgentie toe (echte deadline/verzending, geen nep-timers).

## Deel C — Storytelling-technieken
- **Heldenreis:** klant = held, probleem = uitdaging, product = gereedschap. 6 fasen (uitdaging → mislukte pogingen →
  beproeving/aankoop → overwinning/eerste gebruik → blijvende verandering → aanbevelen).
- **Contrastvertellen:** scherp voor/na (split-screen of sequentieel); overdrijf het probleem licht, snij naar de oplossing.
- **Als-Dan urgentie:** "Als je nog steeds X doet, dan [gevolg]" → "Als je overstapt op [product], dan [resultaat]."
- **Autoriteit:** expert/technische geloofwaardigheid + social proof + getuigenis.

## Deel D — Psychologische principes (waarom het werkt)
- **Verliesaversie** (sterkste): pijn van verlies ≈ 2× het plezier van winst. "Je beschadigt je X" > "krijg een betere X".
  Kader inactie als aanhoudend verlies, ook in de CTA.
- **Social proof:** geverifieerde quotes, review-aantallen + sterren, UGC, **segment-specifiek** bewijs.
- **Verdiende urgentie/schaarste:** echte deadlines/verzending/garantie. Geen nep-timers (schaadt vertrouwen).
- **Emotie eerst, logica daarna:** ~80% van aankopen is emotioneel; logica rechtvaardigt. Trigger per pijnpunt de juiste
  emotie (angst/verlies · opluchting/comfort · frustratie→gemak · trots/status · controle).

## Deel E — Visualisatieregels (video)
1. Toon het product binnen de eerste **5s**. 2. Demonstreer USP's visueel (niet alleen benoemen). 3. Realistische setting.
4. Modellen die de **doelgroep weerspiegelen**. 5. **20/80-regel** (20% talking head, 80% B-roll in actie). 6. Altijd
ondertitels/geanimeerde tekst (velen kijken zonder geluid).
