# Concept document: structure and rules

**Role in the machine:** a concept is one idea we want to test: one slot (persona × angle × awareness) in one or
more variants. The concept document is the place where the *thinking* lives: why we believe the idea works, what it
rests on, what we launch and where. The *production work* (script, shotlist, design instructions) lives in a separate
brief under the concept. Skill: `concept`. Pipeline: [ad-pipeline.md](ad-pipeline.md), after the script (video) or the
voorzet (static) is approved and before the brief (S6).

**Client-agnostic.** This file contains no client data. Everything brand-specific comes from Adflow and the brand's
Drive handbooks (see [bronnen.md](bronnen.md)).

## Where things go

| What | Where |
|---|---|
| Hypothesis, insight and evidence, slot and dims, ad copy, landing pages, launch place | The concept document |
| Instruction, script, shotlist, text on screen, film rules, check before delivery | A separate brief under the concept (`video-brief`, `designer-brief`) |
| Embeds of examples, b-roll, music | The brief |
| Dims (persona, angle, product, offer, awareness, creator, language) | Attached to the concept; the brief inherits them |

One concept, several variants: variants share the slot and the footage and differ in hook, opening image, closing
or offer. Each variant is its own creative with its own code (naming: see the brand's briefing handbook and `naming`).

## The five sections, in this order

### 1. Hypothesis
Two or three sentences, no more.
- Formula: *If we use [approach] for [persona], then [expected effect], because [reason].*
- Name what the variants test: what differs between variant 1 and variant 2.
- No target numbers (CPA, ROAS) in the hypothesis. Targets belong to the media buyer and the brand handbook.

### 2. Insight and evidence
A short list. Every line says where it comes from.
- Customer research: the share of reviews or comments that mention the problem, and the pattern behind it.
- Performance, judged on **spend first** (spend is the algorithm's vote), results second. Give spend and purchases
  from live data, with the period.
- Caveats that change how to read the evidence: a different audience, a different offer, small volumes. Example:
  *the same message performed far worse without the launch offer, so the data says more about the offer than the
  message.* Always name a confound if there is one.
- What the audience does not know yet (for a new market: that nobody knows the brand).

### 3. Slot and dims
List the values, one per line: persona, angle, awareness, product, language, and offer per variant.
- Use values that exist in Adflow. A value that does not exist yet is marked *(to be created)*; you create it only
  after the user confirms the name.
- The offer can differ per variant; dims sit on the ad, so only the variant that uses the offer gets it.

### 4. Ad copy and landing page
Per variant: landing page URL, primary text, headline (the layout follows the brand's ad copy handbook).
- Price, saving and dates come from the landing page, never from an old ad.
- Copy must say the same as the creative. No new promises.
- Unknown URL or price on the site? Write `[check]`.

### 5. Launch place
- The ad set (name per the brand's launch handbook) and the reasoning in one line.
- What has to be **created new**: campaign, ad set, copy template (naming per the handbook).
- Open points as a short list of `[check]` items with an owner.

## Writing rules
- **Short.** The whole concept document fits on one screen. Details go in the brief.
- **Use lists, not tables.** Markdown tables show as plain text in Adflow documents.
- **No `/` in the text.** See [adflow-documents.md](adflow-documents.md) for the editor rules and the alternatives.
- Headings as written above, so every concept reads the same.
- Numbers are dated and come from live data, not from memory.
- Plain language, short sentences, no dashes as pause marks.
- Never overwrite a document that already has text; ask first. An empty document can hold a single empty paragraph:
  insert after it.

## Generic example (invented, not a real brand)

> **Hypothesis.** A short curiosity opening about a refillable water bottle (the cap clicks, the pod pops in) will
> stop commuters who dislike carrying plastic, and a clear before and after on day five makes it believable. Test:
> result first with a bundle (variant 1) against problem first with no deal (variant 2).
>
> **Insight and evidence**
> - 30% of reviews mention leaks in bags; the before and after story is the common thread.
> - Demo videos spent most in the last 90 days (spend X, purchases Y, period Z).
> - Caveat: the same message did worse without the launch discount.
>
> **Slot and dims**
> - Persona: Daily commuters
> - Angle: PodInTheCap
> - Awareness: Problem Aware
> - Product: Starter bottle
> - Offer: variant 1 starter bundle *(to be created)*, variant 2 none
>
> **Ad copy and landing page**
> - Variant 1: URL, primary text, headline
> - Variant 2: URL, primary text, headline
>
> **Launch place**
> - Ad set: per the launch handbook. To create: campaign, ad set, copy template.
