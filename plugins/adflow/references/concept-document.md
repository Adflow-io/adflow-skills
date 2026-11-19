# Concept document: structure and rules

**Role in the machine:** a concept is one idea we want to test: one slot (persona × angle × awareness) in one or
more variants. The concept document is the place where the *thinking* lives: why we believe the idea works, what it
builds on, which message it carries and where we launch it. The *production work* (script, shotlist, design
instructions) lives in a separate brief under the concept. Skill: `concept`. Pipeline:
[ad-pipeline.md](ad-pipeline.md), after the script (video) or the voorzet (static) is approved and before the brief
(S6).

**Client-agnostic.** This file contains no client data. Everything brand-specific comes from Adflow and the brand's
Drive handbooks (see [bronnen.md](bronnen.md)).

## Brand layout comes first

A brand can have its own concept format in its **brand instructions in Adflow** (a section called Concept format, with
a template and rules). Read the brand instructions before you write. If the brand has a Concept format, follow it:
its sections, wording and rules win over this file. This file is the default for brands without one, and the method
behind the brand versions. Brand-specific rules (naming, wording, extra sections) belong in the brand instructions,
never in this file.

## Where things go

| What | Where |
|---|---|
| Hypothesis, reference, key message, launch proposal | The concept document |
| Ad copy and landing pages | The Copy library, and optionally a fifth section in the concept document |
| Instruction, script, shotlist, text on screen, film rules, check before delivery | A separate brief under the concept (`video-brief`, `designer-brief`) |
| Embeds of examples, b-roll, music | The brief |
| Dims (persona, angle, product, offer, awareness, creator, language) | Attached to the concept, not written in the document; the brief inherits them |

One concept, several variants: variants share the slot and the footage and differ in hook, opening image, closing
or offer. Each variant is its own creative with its own code (naming: see the brand's briefing handbook and `naming`).

## The four sections, in this order

### 1. Hypothesis
One or two sentences, no more.
- Formula: *If we use [approach] for [persona], then [expected effect], because [reason].*
- With variants: say what differs between variant 1 and variant 2.
- No target numbers (CPA, ROAS) in the hypothesis. Targets belong to the media buyer and the brand handbook.

### 2. Reference
What the concept builds on, so a reader sees the evidence in one look.
- **One embed** of the source ad, only the winner this concept builds on. Pick the winner by looking for the format,
  the creator or the idea in the live data, and rank the candidates per **creative family**.
- **One source line** under it: which creative it is, and the result, judged on **spend first** (spend is the
  algorithm's vote) and results second, with the period. Numbers come from live data, never from memory.
- **Judge a creative as a family**: all its ads and all its markets together, never one ad or one country. The same
  creative runs as many ads (one per language or market), so one ad shows only a slice of its spend. Say how many ads
  and markets the number covers.
- Name a **confound** when there is one: another audience, another offer, a single product or small volumes say less
  than they seem.
- No winner to build on? Write a short evidence list instead. Every line says where it comes from: the share of
  reviews or comments that mention the problem, and spend and purchases from live data with the period.

### 3. Key message
The words the concept carries, as a short list: the headline and the subline.
- Take them from the approved voorzet or script, or from the pillar agreements when the concept sits under a pillar.
- The briefs under the concept use the same words, so the concept and its briefs say the same.

### 4. Launch proposal
- **Campaign** and **Adset**, named per the brand's launch handbook. Say whether they exist or have to be created new.
- **Why:** the reasoning in one line, based on the dims (for example the offer decides the ad set type).
- Anything else to create new (copy template) and the open points as `[check]` items with an owner.

### Optional: Ad copy and landing page
Added when the copy is written with `meta-copy`. Per variant: landing page URL, primary text and headline, in the
layout of the brand's ad copy handbook. Price, saving and dates come from the landing page, never from an old ad.
Copy says the same as the creative, with no new promises. Unknown URL or price: `[check]`.

## Dims
Dims are attached to the concept, not listed in the document.
- Use values that exist in Adflow. Reuse them; never remove or replace values on other concepts.
- A value that does not exist yet: list it in the chat and create it only after the user confirms the name.
- The offer can differ per variant; dims sit on the ad, so only the variant that uses the offer gets it.

## Writing rules
- **Short.** The whole concept document fits on one screen. Details go in the brief.
- **Use lists, not tables.** Markdown tables show as plain text in Adflow documents.
- **No `/` in the text.** See [adflow-documents.md](adflow-documents.md) for the editor rules and the alternatives.
- **Headings in English as written above**, so every concept reads the same. The text under them is in the language
  the team works in.
- Numbers are dated and come from live data, not from memory.
- Plain language, short sentences, no dashes as pause marks.
- Never overwrite a document that already has text; ask first. An empty document can hold a single empty paragraph:
  insert after it.
- A team member may edit the document while you work. Read it again right before every edit, and keep their wording
  and headings.

## Generic example (invented, not a real brand)

> **Hypothesis.** The pod-in-the-cap demo of the refillable bottle also works for the gift season. A bundle offer
> turns one gift into a set.
>
> **Reference**
> - [embed of the source ad]
> - Source: the starter bottle demo video, all its ads and markets together. In the last 30 days it had the most spend of the account, with X purchases
>   (period Z). Caveat: it ran without an offer.
>
> **Key message**
> - Who do you make happy?
> - Now 3 plus 1 free
>
> **Launch proposal**
> - Campaign: the fixed sales campaign of the region, per the launch handbook.
> - Adset: new, named per the handbook with the offer as its value.
> - Why: a deal with an end date gets its own ad set. No ad set for this offer exists yet.
