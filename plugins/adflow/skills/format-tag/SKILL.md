---
name: format-tag
description: Give concepts and ads in Adflow the right value of the brand's Format dimension, judged from what is on screen (the per-second analysis for video, the image for statics), with the brand's own names or the format gallery. Works on one concept (a link or number, judged from its ads, else its brief, else its concept document and reference) or on a batch (the untagged creatives with the most spend). Proposes a value with a reason, sets doubtful ones apart, and only writes to Adflow after approval. Use for "check format", "welk format is dit concept", "tag de formats", "welke format is deze ad", "vul de Format-dimensie", "audit de format-tags", or before a format analysis. Not for choosing a format for a new ad (use static-format or video-format) and not for creating new Format values without approval.
metadata:
  adbase: "true"
---

# Format tag

Gives existing concepts and ads the right **Format** value, so that everyone on the team tags the same ad the same way
and format performance can be trusted. It serves step **E (feedback)** of the
[ad pipeline](../../references/ad-pipeline.md): clean format tags are what a format analysis and the next
`static-format` / `video-format` menu rest on. The rules for which value an ad gets are in
[format-classification.md](../../references/format-classification.md); this skill applies them to one concept or
to a batch.

## One concept ("check format")

The user shares a concept (a link or number). Read the brand's format setup (step 2 below), then judge from the best
evidence the concept has, in this order, and say which one you used:

1. **Its ads or delivered creatives**: what is on screen decides (step 4 below). Several creatives with different
   forms? Flag it (step 5).
2. **No creatives yet: its brief(s)**: the planned form (delivery, shots, what the editor or designer makes).
3. **No brief yet: the concept document and its reference** (an asset, a link, a winner it copies): judge the
   reference as in step 4, and the format is what the concept plans to make from it.

A value from 2 or 3 is **planned**: tag it only if the user wants that now, and check it again when the creatives are
delivered. Already a Format value on the concept? Compare and say whether it holds. Then show the short output below
and follow step 7 to write after approval.

```
# Format check — <concept number and name>
Based on: <ads / brief / concept document + reference> (<planned or delivered>)
What is on screen: <1–2 lines>
Format: <brand value> (gallery: <gallery format>) · zeker/twijfel · <reason, and the other format if twijfel>
Now on the concept: <value or empty> → <ok / add / conflict>
Write it? (yes / pick another value)
```

## Steps (batch; the one-concept check uses steps 2, 4, 5 and 7)

1. **Agree the scope.** One brand, and either a list the user gives (concepts, ads, a launch) or "the untagged
   creatives with the most spend". Default period: the last 90 days. Default batch: the top 20 creatives by spend.
2. **Read the brand's format setup**, in the order of
   [format-classification.md](../../references/format-classification.md):
   - the brand's **Format dimension** in Adflow and its values (the name or slug can differ, for example a renamed
     dimension). No Format dimension? Stop, say so, and ask whether to create one (see
     [dimension-hygiene.md](../../references/dimension-hygiene.md));
   - the `## Format` section in the brand's AI instructions, if there is one: its definitions win. The brand
     instructions come along with the Adflow responses for that brand; no `## Format` section? Say so;
   - for everything the brand did not define: the cards in [format-gallery.md](../../references/format-gallery.md)
     and `references/formats/`.
   - Check the brand's existing values against the rules. Values that are not a form (a message, a sender, a
     production style) stay usable, but list them under "Values that are not a format" with the matching gallery
     format, so the user can decide.
3. **Find what needs a tag.** Pull performance for the period and see which spend already has a Format value and
   which does not. Grouping performance by the brand's own Format dimension may not work; then filter on all its
   values for the tagged spend, pull the same period unfiltered, and take the difference per creative. Report the
   coverage first: the share of total spend that is tagged. Then list the untagged creatives, most spend first, one
   row per creative family (all ads, sizes and markets of the same creative together). The concept code in the ad
   name may be used to group rows, never to judge them; link each row to its concept before writing.
   Already tagged ones are only in scope for an audit; never change them without asking.
4. **Look at each creative.** Judge what is on screen, never the thumbnail, the ad name or the concept title:
   - **Video:** the per-second analysis in Adflow, following [judging-video.md](../../references/judging-video.md).
     Song lyrics are not speech; text on screen is not always a caption. No analysis? Leave it open and say so.
   - **Static:** the image, and read the text on it yourself. An ad shows one size; open the creative itself when
     the sizes might differ.
   - Adflow's own automatic format label may be a hint. It uses other names and is never the answer.
5. **Pick the value** with the decision tree and the cards in
   [format-classification.md](../../references/format-classification.md):
   - Use the brand's value names exactly. When the right form has no brand value, say which gallery format it is and
     propose adding it as a new value; do not create it yourself.
   - Who is on screen (founder, creator), what it argues (review, gift, us vs them), the deal, or how it was made (UGC,
     AI, selfie) is **not** the format. Note it as a remark for the matching dimension, if useful.
   - Mark each one **zeker** (one card clearly fits) or **twijfel** (two cards fit). For a twijfel, name both formats
     and the rule that decides between them.
   - A concept whose creatives have different forms (a talking head and a static) gets no single value: flag it and
     suggest splitting the concept or tagging the exception.
6. **Show the proposal** (shape below) and stop. The user approves, corrects, or picks per row. Do not write yet.
7. **Write after approval only.**
   - Tag on the **concept**: its value passes to all its ads, and Adflow may rename those ads. Say that before writing.
   - Adding a dimension value **adds**; it does not replace, and there is no undo. Only fill concepts and ads where the
     Format is empty. A concept that already has a different value is a conflict: report it, do not add a second.
   - Write one concept first and read it back (value attached, ad names as expected), then do the rest.
8. **Report back** the new coverage (share of spend tagged), what was written, what was left open, and why.

## Output

```
# Format tags — <brand> · <period> · coverage <x>% of spend tagged

| # | Concept | Spend share | What is on screen (1 line) | Format (brand value) | Gallery format | Zeker/twijfel | Note |
|---|---|---|---|---|---|---|---|
| 1 | <concept name or number> | 12% | woman talks to camera in her car, product in hand | <brand value> | Talking head | zeker | Creator: founder? not confirmed |
| 2 | … | 8% | split image, old vs new product | — (no brand value) | Split screen | twijfel | or Comparison table: no rows, so Split screen |
| 3 | … | 5% | no per-second analysis | — | — | open | please check by eye |

Spend share = share of the brand's total spend in the period.
Missing brand values: <gallery format> for #… (propose to add?)
Values that are not a format: <brand value> → <gallery format or other dimension>
Conflicts: <concept already tagged with another value>
Which rows may I write? (for example "all zeker", "1–5, 8")
```

Number every row so the user can approve by number. Keep "What is on screen" factual and short; no transcripts.

## Notes
- Never create or rename Format values, and never remove values, without the user's approval.
- One correction from the user about a value is a signal for the brand's `## Format` section: offer to add it there
  (a brand rule, not a change to this skill).
- Is the brand's value list itself in doubt (values that are not a form, no descriptions)? Run `format-audit`
  first, then tag.
- Next step: with good coverage, a format analysis (spend first, then ROAS per format), then `static-format` or
  `video-format` for the formats the brand has not tested.
