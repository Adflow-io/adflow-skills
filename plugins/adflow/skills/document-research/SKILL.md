---
name: document-research
description: Leg research voor een merk vast als Google Doc in de Research-map van het merk in Drive (format Door / Datum / Inzicht / Vertaling) en zet het in het Index-doc. Gebruik bij "zet dit in een research doc", "maak hier een research doc van", "documenteer deze research", of als er research is gedaan (web, reviews, prijzen, data van het team) die bewaard moet worden. Niet voor het concept zelf (gebruik concept) of voor klantwoorden uit reviews in Adflow (gebruik review-research). Lean output.
---

# Document research

Research that we do for a brand (web research, reviews, prices, data from the team) has to be findable for the whole
team. This skill puts that research in one fixed format in the brand's Drive folder and adds it to the brand's Index
doc. It serves the research stage that comes before `slots` in the [ad pipeline](../../references/ad-pipeline.md).

The doc is written in Dutch, in the format below. The folder is shared with the client's team, so everything in the
doc can be seen by the client.

## What does and does not belong in a research doc
- **Yes:** the research itself and what we take from it (angles, messaging, ideas, claims that can or cannot be made).
- **No:** sparring about one specific concept or one specific ad (for example headlines for one static, feedback on an
  image the user uploads). That stays in the chat or goes to the concept in Adflow (see `concept`).
- Not sure? Ask briefly.
- **One topic per doc.** Does the chat cover several topics (for example discolouration and prices)? Make several
  docs.

## Steps
1. **Find the place in Drive** (see [bronnen.md](../../references/bronnen.md)):
   1. The brand's folder.
   2. In it, the folder that is shared with the client's team (its name contains `Adflow` and `Gedeeld met team`).
   3. In it, the folder `Research`. Missing? Create it in the shared folder.
   4. In the shared folder, the Index doc (named `<Merk> – Index`).

   Can't find the folder or the Index doc? Ask where it should go. Never create a new Index without asking.
2. **Write the doc** in the format below. Name: `Research – [Onderwerp] ([Naam], DD-MM-JJJJ)`.
   - Naam is who did the research. Does the data come from someone else (for example a sheet from a colleague)? Then
     it is that person.
   - Datum is the day the research was done.
   - Example: `Research – Terug op voorraad bestsellers (Anna, 26-11-2026)`
3. **Create it in Drive** as an HTML file (content type `text/html`) in the Research folder. Drive then converts
   headings, lists, tables and links into a proper Google Doc.
4. **Add it to the Index.** Under the heading about research (for example "Research en creative strategie") add one
   bullet: `[Research – Onderwerp (Naam, DD-MM-JJJJ)](link): what is in it, in one line (map Research)`
   - Only the title is a link.
   - New docs go under the earlier research docs, so the order stays right.
   - Read the Index again right before you write, because positions change after every edit.
5. **Check and report.**
   1. Read the new doc back: is the format right, do the links work, is there no concept sparring in it?
   2. Read the Index back.
   3. Report in a few lines (see Output).

## Format of the doc

```
# Research: [onderwerp]

Door: [naam] (met Claude als Claude heeft meegeholpen; bij data van een collega: "[naam] (data), uitwerking [naam] (met Claude)")
Datum: [dag maand jaar]

## Inzicht
The research itself.
- Start with one or two sentences: what is the question and where does the info come from.
- Then the findings in themes (### per theme), with bullets.
- A link to the source at every point. Short customer quotes stay verbatim.
- Data from a sheet: copy the table (with links) and put "Wat valt op" under it.
- Say honestly what is missing (for example "Reddit kwam niet boven", "geen volledig onderzoek").

## Vertaling
Ideas for angles, messaging, etc.
- Per angle a ### heading, one sentence on why, and 2 to 3 example lines.
- A heading "Let op" for claims that still have to be checked or are not allowed.
```

## Writing rules
- Dutch, simple language (around age 10 reading level), short sentences.
- No em dashes. No inflated sales talk. (The dash in the doc name is part of the naming pattern.)
- Only facts that are in the source. Own conclusions belong in Vertaling, not in Inzicht.
- Claims (for example "lasts longer", "waterproof", numbers sold): say in Vertaling whether they are on the website or
  in the data. If not, put them under "Let op".
- Refer to other research docs when they connect (for example "zie Research – Prijzen").

## Output
A short report to the user:
- the name of the doc, as a link;
- what is in it: Inzicht and Vertaling in a few bullets;
- what the user still has to check (claims under "Let op", missing sources, anything the client should not see).

Next step: `slots` to turn the angles from Vertaling into concept slots.
