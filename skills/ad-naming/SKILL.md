---
name: ad-naming
description: Bouw de Adflow-adnaam voor een creative volgens de conventie (product-persona-angle-creator-offer-awareness-taal). Mapt elk veld op het bestaande token uit de woordenlijst; de ID komt uit Adflow (nooit zelf verzinnen). Lean output.
---

# Ad Naming

Zet een concept om in een correcte adnaam. Eén regel string, geen ruis. Bron van waarheid =
`references/naming-convention.md` (format + gecontroleerde woordenlijst per klant).

## Format

```
<ID>-PR-<product>-PRS-<persona>-AN-<angle>-CR-<creator>-OF-<offer>-AW-<awareness>-LNG-<taal>[_<ratio>]
```

**De `<ID>` komt altijd uit Adflow** (klantcode + volgnummer, bv. `<KLANTCODE>-205`). Verzin die nooit. Als de
gebruiker de ID niet geeft, laat je 'm staan als `<ID>` en zeg je erbij dat Adflow 'm invult.

## Werkwijze

1. **Lees `references/naming-convention.md`** voor het format + de awareness-ladder (klant-agnostisch), én
   **`clients/<klant>/brand.md`** (sectie Naamconventie) voor de **token-woordenlijst** van de betrokken klant.
2. Haal de 7 velden uit het concept/de brief: product · persona · angle · creator · offer · awareness · taal
   (+ eventueel ratio). Ontbreekt awareness of offer? Leid awareness af uit de hook/angle (zie de ladder in de
   referentie); offer = `none` als er geen aanbod is.
3. **Map elk veld op een bestaand token** uit de woordenlijst in `clients/<klant>/brand.md`. Casing volgt de
   klantstijl die daar staat (bv. CamelCase vs lowercase-hyphen angles). Hergebruik; verzin geen nieuwe spelling
   voor iets dat al bestaat.
4. Bestaat een waarde nog niet in de lijst (echt nieuwe persona/angle/creator)? Gebruik 'm in de klantstijl en
   **markeer 'm als nieuw token**, zodat de gebruiker 'm kan bevestigen en aan de referentie kan toevoegen.
5. Zet de naam in elkaar. Meerdere ads tegelijk = één naam per regel.

## Harde regels

- [ ] ID nooit zelf verzinnen — placeholder `<ID>` of de door de gebruiker gegeven code.
- [ ] Alle 7 velden aanwezig, in vaste volgorde, met hun prefix.
- [ ] Alleen tokens uit de woordenlijst; nieuwe tokens expliciet gemarkeerd.
- [ ] Klantstijl-casing gerespecteerd.

## Output-format

Lean. Alleen de naam (of namen), plus alleen een regel toelichting als je iets afleidde of een nieuw token markeerde.

```
<ID>-PR-...-PRS-...-AN-...-CR-...-OF-...-AW-...-LNG-...[_9x16]

(alleen indien nodig)
afgeleid: awareness=most-aware (deal/most-aware hook)
nieuw token: AN-<...> — bevestigen + toevoegen aan naming-convention.md
```

## Notities
- Woordenlijst groeit: nieuwe bevestigde tokens horen in `references/naming-convention.md`, niet in deze skill.
- Workflow D3 in `references/workflow-map.md`. Input = het gekozen concept (product×persona×angle×format) + creator +
  offer; komt uit de roadmap/brief.
