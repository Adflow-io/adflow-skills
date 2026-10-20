# Ad-naamconventie (bron van waarheid)

De naam labelt elke creative zodat performance per dimensie leesbaar is (welke persona/angle/creator/offer trekt wat).
Workflow D3 in [workflow-map.md](workflow-map.md). Gebruikt door skill `ad-naming`.

## Format

```
<ID>-PR-<product>-PRS-<persona>-AN-<angle>-CR-<creator>-OF-<offer>-AW-<awareness>-LNG-<taal>[_<ratio>]
```

- **`<ID>` komt ALTIJD uit Adflow** — dat is de klantcode + volgnummer (bv. `<KLANTCODE>-143`). Verzin die nooit
  zelf; laat 'm leeg als placeholder `<ID>` tot Adflow 'm geeft.
- Velden na de ID (de gebruiker noemt het kort): **product · persona · angle · creator · offer · awareness · language**.
- De prefixes (`PR- PRS- AN- CR- OF- AW- LNG-`) horen erbij; zo staan de ads ook echt in het account
  (bv. `<KLANTCODE>-103-PR-<product>-PRS-<persona>-...-LNG-<taal>_9x16`).
- `_<ratio>` optioneel achteraan: `9x16` (1080×1920), `1x1` (1080×1080), `4x5`.
  **Statics: standaard altijd `_1x1` (1080×1080) én `_9x16` (1080×1920)** — elke static-creative in beide ratio's.

## Gecontroleerde woordenlijst

**Regel:** hergebruik een bestaand token; verzin geen nieuwe spelling voor iets dat al bestaat. Ontbreekt een waarde,
markeer 'm als nieuw token (dan kan de gebruiker 'm bevestigen). Casing volgt per klant de bestaande stijl.

> **Klant-agnostisch bestand.** De concrete token-woordenlijst per klant (product/persona/angle/creator/offer +
> casing-stijl + eventuele legacy-formats) staat op klantniveau in de dims in Adflow.
> Voeg nieuwe tokens dáár toe, niet hier.

### Awareness-ladder (voor alle klanten)
`unaware` (kent probleem niet) → `problem-aware` (voelt probleem) → `solution-aware` (weet dat er oplossingen
bestaan, nog niet jouw merk) → `product-aware` (kent jouw type product) → `most-aware` (kent merk, wil deal/reden).
Kies op basis van de hook/angle.
