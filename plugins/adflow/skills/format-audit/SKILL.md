---
name: format-audit
description: Audit a brand's Format dimension in Adflow as a list. Per value the spend and number of creatives, whether it is a real form under the format rules, what is actually inside it, and advice to keep, rename, merge, move to another dimension or retire, plus the forms that are missing. Changes values only after approval, in a safe order. Use for "audit de formats", "kloppen onze formats", "check de Format-dimensie", "zijn deze formats goed", when a brand starts with format tagging, or every few months. Not for tagging single ads or concepts (use format-tag) and not for choosing a format for a new ad (use static-format or video-format).
metadata:
  adbase: "true"
---

# Format audit

Checks whether a brand's **Format** dimension is a list of real forms that the team can tag the same way, before
anyone tags or analyses with it. It looks at the list, not at single ads: `format-tag` does those. It serves step
**E (feedback)** of the [ad pipeline](../../references/ad-pipeline.md). Rules for what a format is:
[format-classification.md](../../references/format-classification.md). Rules for adding, merging and retiring values:
[dimension-hygiene.md](../../references/dimension-hygiene.md).

## Steps

1. **Read the setup.** The brand's Format dimension and all its values (name, slug, description), and the `## Format`
   section in the brand's AI instructions if there is one. No Format dimension? Say so and stop.
2. **Measure each value.** Default period: this year, or the last 6 months. Per value: spend, number of creatives,
   and whether they are static, video or both. Filter on each value one by one when grouping by the dimension does not
   work. Also measure the spend with no Format value at all, and give the coverage (share of spend tagged).
3. **Test each value** against [format-classification.md](../../references/format-classification.md):
   - **Is it a form?** Visible, and independent of the message. A sender (founder, creator, expert) belongs in
     Creator, a message (testimonial, us vs them, gift) in Angle, a deal in Offer, production (UGC, AI, selfie) in a
     tag, a funnel stage (retargeting) in Awareness.
   - **One box?** Does it overlap with another value? Does it hold both statics and videos (a static and a video are
     never the same form)?
   - **Gallery name:** which [gallery](../../references/format-gallery.md) format it matches, if any.
   - **Use:** values with no spend or under about five creatives (the volume test in
     [dimension-hygiene.md](../../references/dimension-hygiene.md)).
   - **Definition:** does it have a short description of what you see? An empty or copied description is a finding:
     people and other tools tag from it.
4. **Look inside.** For each value with real spend, check the 2–3 creatives with the most spend: does the content
   match the name? Judge from what is on screen ([judging-video.md](../../references/judging-video.md)), not the ad
   name. Say how many you checked; anything you judged from names only is marked as such.
5. **Find the gaps.** Which gallery formats do the untagged spend and the not-a-form values actually contain (from the
   creatives you looked at)? Those are the candidates to add. Propose only forms with enough creatives to repeat.
6. **Advise per value** (shape below) and stop. Advice options: keep · rename (to the gallery name or a clearer one) ·
   add a description · merge into <value> · move to <other dimension> · retire. The user decides per row.
7. **Change after approval only**, in this order, because adding a value adds and there is no undo:
   1. rename values and fill in descriptions (names and tags on ads stay the same; the slug does not change);
   2. add the missing form values;
   3. re-tag the creatives of values that are not a form with `format-tag`, and put the sender or message in Creator or
      Angle;
   4. only then retire the old values, never while ads still depend on them without a new value;
   5. write the decisions with a date in the `## Format` section of the brand's AI instructions.
   Read each change back once before the next.

## Output

```
# Format audit — <brand> · <period> · coverage <x>% of spend tagged

| # | Value | Spend | Creatives | Static/video | Form? | Gallery | What is inside (checked n) | Advice |
|---|---|---|---|---|---|---|---|---|
| 1 | <value> | €12.0k | 9 | static | ✅ | Product hero | packshots with headline (3) | rename to Product hero, add description |
| 2 | <value> | €8.5k | 14 | video | ❌ sender | — | b-roll with voice-over about the making (2) | move to Creator, re-tag |
| 3 | <value> | €0 | 0 | — | ✅ | Skit | — | keep or retire: unused |

Missing forms: <gallery format> (seen in #…, about n creatives)
Untagged spend: <x>% — tag with format-tag after the list is clean
Which rows do I change? (for example "1, 3" or "all renames")
```

Number every row. Keep "What is inside" to one line per value and say how many creatives were checked.

## Notes
- Brand values that differ from the gallery are allowed when the brand defines them; the audit flags, the brand
  decides. Record the decision in the brand's `## Format` section.
- Run it when a brand starts with format tagging, before a format analysis, and every two to three months.
- Next step: `format-tag` for the untagged and re-tagged creatives.
