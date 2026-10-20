# Creative Diversity Checklist (account-niveau)

**Bron:** eigen checklist Lowie ("My quick and basic creative diversity checklist").
**Rol in de machine:** dit is een **account-brede diagnose**, geen ad-productie. Draai 'm periodiek per klant om te
zien of het account een compleet **creatief ecosysteem** heeft — niet één winnende ad, maar creatives die samen de
customer journey dragen. Vult de coverage-matrix aan vanaf de *creative-type*-as (naast Persona × Angle × Awareness
uit [ad-pipeline.md](ad-pipeline.md)).

> **Klant-agnostisch bestand.** Dit is de herbruikbare check + werkwijze — géén klant-uitkomst. De ingevulde
> scorecard + gaps + voorzetjes horen op klantniveau: een klantdocument in Adflow.

---

## De kern-gedachte
> In de meeste gevallen zien mensen niet één ad en besluiten dan te kopen. Het gaat om hoe de ads **samen** een
> customer journey vormen die per individu anders loopt. Soms is het "een nieuwe winnende ad vinden" — vaak is het
> het juiste creatieve **ecosysteem** bouwen zodat het account als geheel presteert.

## De 10 checks — heeft het account…
1. **How-to / educational content** — leren/uitleggen (hoe het werkt, hoe het gemaakt wordt, hoe te gebruiken).
2. **Native reels content** — organisch aanvoelende creator-/UGC-reels (geen ad-look).
3. **Partnership ads** — echte Meta Partnership Ads (paid-partnership label, draaiend vanaf het creator-account) —
   niet alleen jouw eigen ad met creator-footage.
4. **Objection handling video** — video die het/de belangrijkste kooptwijfel(s) frontaal pakt (prijs, smaak,
   werkt-het, tijd, twijfel). Check tegen de #1-objectie van déze klant.
5. **TOF statics** — koude statics (unaware / problem-aware); headline = de ad.
6. **BOF statics** — warme statics (product-/most-aware): offer, packshot, combodeal.
7. **Founders ad of Employee Generated Content (EGC)** — gezicht van het merk / team, niet-ingehuurde creator.
8. **AI animation video** — nieuwe ontwikkeling / trend-experiment.
9. **Top performer hergemaakt met nieuwe creator OF nieuwe visuals** — zelfde winnende angle, ander gezicht/beeld
   (incl. andere taal).
10. **Top performer hergemaakt met nieuwe persona** — zelfde winnende angle, andere persona-lens.

> #9–10 zijn **remake-checks**: ze kijken of je de winnaar systematisch uitmelkt over creators/visuals/personas,
> niet of er losse nieuwe ads zijn.

---

## Werkwijze (via Adflow MCP)
1. `set_active_brand` → juiste klant. Kies venster (default 90d voor diversity — breed genoeg voor alle types).
2. `get_top_ads` (main_metric = **spend**) voor de winners + `list_ads` voor de volledige type-inventaris.
3. Map elke ad op de 10 checks. De **adnaam-tokens** doen het meeste werk
   ([naming-convention.md](naming-convention.md)): `AN` (angle) → #1/#4, `CR` (creator: none/founders/naam) → #2/#3/#7,
   `TY` (video/image) + `AW` (awareness) → #5/#6, `AN`×`CR`/`LNG` variatie → #9, `AN`×`PRS` variatie → #10.
4. **Spend-first oordeel:** markeer niet alleen aanwezigheid, maar of het type ook écht spend draagt. Een type dat
   bestaat maar niet loopt = zwak, geen ✅.

## Output-format (op klantniveau)
- **Scorecard-tabel:** per check ✅ aanwezig / ⚠️ deels / ❌ gat, met de concrete bewijs-ad erbij.
- **Gaps geprioriteerd:** grootste funnel-/ecosysteem-gat eerst, elk met een kort 1-regel-voorzet wat te maken.
- Wat niet uit de adnaam te lezen is (bv. #3 formele Partnership-setup): flaggen en via **Meta Ads-connector**
  verifiëren i.p.v. aannemen.

## Lees-tips per check
- **#3 Partnership:** creator-footage in je eigen ad ≠ Partnership Ad. Alleen ✅ als het als paid partnership draait.
- **#4 Objection:** weeg tegen de **#1-objectie van de klant** (staat in de research van de klant), niet generiek.
- **#8 AI animation:** trend-vinkje; 1 experiment telt. Afwezigheid is een makkelijk te dichten gat.
