# Static ad-formats + messaging-wetten (Meta)

**Bron:** Adcrate "ULTIMATE Guide to Static Ads 2026" ([videos/adcrate-static-ads-2026.md](videos/adcrate-static-ads-2026.md)).
**Rol in de machine:** dit is de static-tegenhanger van [ugc-format-templates.md](ugc-format-templates.md) (die is
video/UGC). Kies hier het **static-format**, pas de **messaging-wetten** toe, en schrijf dan de
[Designer-brief](designer-brief-static.md). Dekt de "vehicle = static"-as van de coverage-matrix.

> **Klant-agnostisch bestand.** Dit is de herbruikbare format-taxonomie — géén klant-fit. De weging "welk format past
> bij déze klant" hoort op klantniveau: `clients/<klant>/format-fit.md`.

---

## Deel A — De 12 bewezen static-formats
In prioriteitsvolgorde uit de video (bovenaan = meest gebruikt). ~95–98% van alle statics zit in deze 12.

| # | Format | Kern | Werkt voor |
|---|---|---|---|
| 1 | **Headline + benefits** | grote heldere headline (= de ad) + product + benefits eromheen | TOF acquisitie, elk merk |
| 2 | **Testimonial** | klantwoorden **letterlijk** op de ad (mét aanhalingstekens/★); klant-tegen-klant | veel reviews/comments |
| 3 | **Offer** | korting/aanbod centraal | BOF, most-aware, deal |
| 4 | **Persona-based** | 1 regel/beeld dat één persona direct aanspreekt | scherpe persona + eigen funnel |
| 5 | **Collection / grid** | meerdere SKU's/poses in één beeld | multi-SKU, bundel |
| 6 | **Comparison** | before/after · us-vs-them · timeline; contrast visueel | transformatie, prijs/waarde |
| 7 | **Publication / press / native** | ziet eruit als artikel/redactioneel | vertrouwen, koud verkeer |
| 8 | **Policy / "gimmick"** | regel/aankondiging-look; iets gimmicky maar werkt vaak | breed |
| 9 | **Post-it note** | boodschap als geschreven briefje | native/organisch gevoel |
| 10 | **Meme** | herkenbaar meme-format | breed, jong publiek |
| — | *(Alex noemt er 12; #11–12 vallen onder varianten van bovenstaande: native + press apart geteld)* | | |

## Deel B — De twee static-messaging-wetten (altijd checken)
1. **Assume no one knows or cares.** Schrijf elke TOF-static-headline alsof de kijker het merk nooit zag: is dit
   **meteen relevant** voor iemand die je niet kent? **De headline ís de ad.** Uitzondering = BOF/offer-ads (mogen
   merkkennis + prijs aannemen). → QC-lat in de [Designer-brief](designer-brief-static.md).
2. **Clarity ↔ Curiosity — kies, blijf niet in het midden.** Beslis waar de sale valt:
   - **Clarity** (op de ad): duidelijke TOF-static, precies wat het is / voor wie / waarom relevant.
   - **Curiosity** (na de klik): native/advertorial; de ad opent een gap, de landingspagina verkoopt.
   "No man's land" = half duidelijk, half nieuwsgierig → presteert slecht.

> **Klanten = je copywriters.** De sterkste headline/on-image copy komt uit `clients/<klant>/reviews` / `comments`
> (klantwoorden-bank), niet uit eigen kop. Dit is al onze werkwijze; de video bevestigt het.

## Deel C — Verzoening met de tier-list (belangrijk, niet blind overnemen)
`ugc-format-templates.md` bevat de **Dara Denney tier-list** (20.000 ads, breed). Die twee bronnen zijn het
**oneens** over een paar statics:

| Format | Adcrate (static-specialist) | Dara Denney tier-list |
|---|---|---|
| Testimonial-static | favoriet | **E** (laag) |
| Post-it / notes | fan | **F** (laag) |
| Press / publication | werkt breed | **F** (laag) |
| Headline / grid-static | sterk | Headline **B** · Grid-static **A** |

**Waarom het verschil:** Adcrate is een static-specialist met een eigen creatie-systeem; de tier-list meet breed
over alle vehicles (video inbegrepen) en straft formats die zonder sterk systeem snel generiek/fatigue worden.
**Vuistregel:** formats waar **beide** bronnen positief zijn (headline+benefits, grid, comparison, persona) zijn de
veiligste dragers; formats waar de bronnen botsen (testimonial, post-it, press) zijn context-afhankelijk — of ze
dragen of alleen supporting zijn, is een **klant-keuze** (zie `clients/<klant>/format-fit.md`), niet iets wat hier
vastligt.

## Deel D — Uitbreiding: extra visual-formats (bron: visual-formats swipe-library)
**Bron:** `github.com/alyshadotmd/visual-formats` (43 visual-formats, ~90 merken, 196 voorbeeld-creatives).
**Voorbeeldbank:** de bladerbare/filterbare swipe → Artifact `Visual Formats Swipe`
(claude.ai/code/artifact/c1bcab04-9b76-4129-902c-d640e530a91d) — klik een tegel voor het originele bestand.
**Rol:** Deel A blijft de **dragers** (~95% van je statics). Deel D = extra *looks* om een gekozen slot te variëren
of een supporting-ad te maken. De video-formats uit de library (founder, yapper, greenscreen, behind-the-scenes,
ai-animation, asmr, podcast, street-interview, whiteboard, explainer, unboxing) staan al in
[ugc-format-templates.md](ugc-format-templates.md); die herhaal ik hier niet.

**Al gedekt in Deel A (zelfde format, andere naam):** us-vs-them / before-and-after → Comparison (#6) ·
press / news → Publication-press (#7) · post-it → Post-it (#9) · meme → Meme (#10) · product-grid → Collection/grid (#5) ·
review → Testimonial (#2).

### Nieuwe static visual-formats
`Relatie` = nieuw, of variant van welk Deel-A-format.

| Visual-format | Kern (de "look") | Relatie |
|---|---|---|
| **instagram-text-overlay** | organische IG-post-look, korte tekst over een echt/native beeld (grootste in de library, 32×) | nieuw (native-static) |
| **feature-benefit-callout** *(pointout)* | pijlen/labels wijzen features direct op de productfoto aan | variant van Headline+benefits (#1) |
| **matching-chart** | "welke past bij jou"-matrix / quizuitslag die product aan persoon koppelt | nieuw |
| **bento-grid** | bento-raster van meerdere blokken (beeld + claims + SKU's) in één | variant van Collection/grid (#5) |
| **flatlay** | product netjes platgelegd, van bovenaf, onderdelen uitgelegd | nieuw (static) |
| **comment-screenshot** | screenshot van lovende comments als social proof | nieuw |
| **comment-response** | screenshot van merk dat publiekelijk op een comment/bezwaar antwoordt | nieuw (static comment-reply) |
| **letter** | "brief van de oprichter" op briefpapier-look | nieuw (static founder's-letter) |
| **text-message** | iMessage/chat-gesprek als beeld | nieuw |
| **web-search** | nep Google-zoekresultaten / SERP-look | nieuw |
| **statistic** | één groot cijfer/stat centraal | nieuw |
| **flowchart** | beslisboom / stroomschema ("start hier → …") | nieuw |
| **venn-diagram** | venn/overlap van twee eigenschappen | nieuw |
| **toggle** | aan/uit- of voor/na-toggle als UI-element | variant van Comparison (#6) |
| **listicle** | genummerde lijst op beeld ("3 redenen…") | nieuw (static) |
| **flyer** | flyer/poster-aankondiging-look | nieuw |
| **sign** | bordje/sign met de boodschap vastgehouden | nieuw (fysieke variant van post-it) |
| **ad-in-the-wild** | de ad getoond in een echte omgeving (OOH/mockup/screenshot) | nieuw |
| **ai-generated-static** | volledig AI-gegenereerd beeld als drager | nieuw (productiewijze) |
| **case-study** | case-study/onderzoek-look, resultaat centraal | nieuw |
| **line-chart** | datagrafiek (resultaat over tijd) | nieuw |
| **written-on-body** | tekst op huid/lichaam geschreven | nieuw |

> Dit zijn *looks*, geen boodschap. De messaging-wetten (Deel B) en "klanten = copywriters" gelden onverkort —
> kies eerst de slot (Persona × Angle × Awareness), dan een format hieruit, dán de [Designer-brief](designer-brief-static.md).
> **Welke van deze formats bij een klant passen → `clients/<klant>/format-fit.md`.**

## Volgende stap
Format gekozen → schrijf de [Designer-brief](designer-brief-static.md) (leesvolgorde, headline, on-image copy,
visuele behandeling, QC).
