---
name: video-broll
description: Maak een b-roll shotlist vanuit een goedgekeurd video-script (S5), alleen als er nieuwe footage geschoten wordt (eigen productie of externe creator, niet bij bestaande b-roll). Levert een tabel per shot: wat de shot moet overbrengen (leidend, zelfstandig leesbaar) + een voorbeeld-shot (suggestie, ruimte voor eigen invulling). Mix van product, proces, mensen en zuiverheid. Realistisch produceerbaar. Stap S6 (video) van de ad-pijplijn. Alleen video. Lean output.
---

# Video B-roll shotlist (S6 · video)

De b-roll-stap van de [ad-pijplijn](../../references/ad-pipeline.md) voor **video**, tussen het script (S5) en de
brief (S7). Zet een **goedgekeurd script** om in een **shotlist** die vertelt *wat elke shot moet overbrengen*, met
een voorbeeld-shot erbij. Voedt het broll-blok van de `video-brief` (S7).

> **Alleen video, en alleen bij nieuwe footage.** Deze stap draait als de footage-bron (gekozen bij **S2**)
> **eigen productie** of **externe creator** is. Bij **bestaande b-roll / stock** sla je S6 over en ga je van S5
> direct naar S7.

## Input (lees eerst)
- **Goedgekeurd volledig script** uit S5 (hooks + gedeelde body) — de shotlist volgt de VO/het verhaal.
- **Delivery/format + footage-bron** (uit S2). Voor VO over b-roll: **wall-to-wall dekking** nodig (elke gesproken
  regel = beeld). Bij eigen productie is alles binnen handbereik (ook de werkvloer/machines); bij een externe
  creator: splits wat de creator zelf kan filmen van wat het merk moet aanleveren.
- **Slot** (Persona × Angle × Awareness) + `brand.md` (DON'Ts, wat wel/niet in beeld mag) + `reviews/`/`comments/`.

## Het format (vast)
Een **tabel**, gegroepeerd per soort. Kolommen in deze volgorde:

| # | Wat de shot moet overbrengen | Shot (voorbeeld) |

- **"Wat de shot moet overbrengen" is leidend** en moet **zelfstandig leesbaar** zijn — je snapt het zónder de
  voorbeeld-shot te lezen. Benoem het **onderwerp + de indruk/het effect** ("laat zien hoevéél een halve kilo is",
  niet het abstracte "bewijst dat het veel is").
- **De shot is maar een voorbeeld/suggestie** — zo houdt de productie/creator ruimte om er zelf iets op te vinden.

**Groepeer de shots** in soorten zodat de ad zowel iets bewijst als een gezicht heeft, bv.:
- **Product / vers** — het product en de versheid concreet en aantrekkelijk.
- **Proces** — dat ze het echt zelf maken; het volume grondstof; het echte proces.
- **Mensen / personality** — echte, enthousiaste mensen achter het merk (geeft het merk een gezicht).
- **Zuiverheid / contrast / CTA** — puur/eerlijk, het onderscheid, en het aanbod.

## Harde regels
- **Realistisch produceerbaar.** Alleen shots die je in díe setting echt kunt filmen. Een gekunsteld beeld (bv.
  "gember rolt over de tafel") vervang je door iets natuurlijks (handen die door een bak gember woelen). Twijfel je of
  het te filmen is → kies iets beters.
- **Puur b-roll.** **Geen "tekst in beeld"** benoemen — tekstoverlay is een andere stap. Elke shot moet het puur
  **visueel** overbrengen.
- **Niet mooier maken dan het is.** Claim in de doel-kolom niks wat de beelden niet waarmaken (geen "dik sap" als het
  sap niet dik is). Blijf eerlijk over kleur, hoeveelheid, textuur.
- **Concurrent niet tonen als de klant dat niet wil.** Kun je het contrast dan niet direct filmen, laat de **voice-over**
  de claim dragen en bewijs je kant met je **eigen** sterke beelden (volume verse grondstof, het echte proces). Claims
  die je zonder concurrent óf tekst niet kunt tonen (bv. "minder suiker"), laat je aan de VO.
- **Mensen niet regisseren.** Laat ze hun werk doen; een echte lach werkt beter dan een geposeerde.
- **Humanized, geen em dashes** (`references/humanizer-passes.md` / `anti-ai-writing`): natuurlijke spreektaal, komma's
  en punten i.p.v. em dashes.

## Werkwijze
1. Lees script + delivery + footage-bron + brand.md. Bepaal of S6 draait (nieuwe footage) of overslaan (bestaande b-roll).
2. Loop de VO/beats langs en bedenk per stuk **wat een beeld daar moet overbrengen**. Voeg mensen-/personality-shots toe
   zodat het merk een gezicht krijgt.
3. Schrijf de doel-kolom **zelfstandig leesbaar**; hang er een **realistische** voorbeeld-shot aan.
4. Bij VO over b-roll: zorg voor **genoeg dekking** (film lang, 2–3 takes per shot).
5. Geef één **referentieclip/moodboard** mee als tip — dat is de sterkste hefboom of goede shots terugkomen.

## Output-format
Lean: korte kop (slot · delivery · footage-bron) + de tabel(len) per groep + evt. één regel tip. Geen intro/samenvatting.
Sla op in `clients/<klant>/ads/` als de gebruiker akkoord is. Het broll-blok gaat als input naar `video-brief` (S7).

## QC-lat (check vóór je teruggeeft)
- [ ] **Footage-bron klopt**: S6 draait alleen bij nieuwe footage (eigen productie/creator), niet bij bestaande b-roll.
- [ ] **Doel-kolom leidend en zelfstandig leesbaar** (snap je zonder de voorbeeld-shot).
- [ ] **Shot = voorbeeld**, realistisch te filmen in díe setting.
- [ ] **Mix** van product/proces/mensen/zuiverheid; minstens een paar **personality**-shots.
- [ ] **Geen "tekst in beeld"**; puur visueel.
- [ ] **Niks mooier gemaakt dan het is**; concurrent alleen in beeld als de klant dat wil.
- [ ] Bij VO over b-roll: **dekking** voor de hele runtime.
- [ ] **Humanized, geen em dashes**; klopt met brand.md.

## Notes
- Workflow **S6 (video)** in `references/ad-pipeline.md`. In = goedgekeurd script (S5) + delivery/footage-bron (S2).
  Uit = b-roll shotlist → broll-blok van **S7 (`video-brief`)**.
- Beslist niet over de copy — die ligt in S4/S5 vast. Deze stap maakt de beelden producereerbaar en overtuigend.
