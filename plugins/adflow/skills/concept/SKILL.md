---
name: concept
description: Create or fill the concept document in Adflow (hypothesis, insight and evidence, slot and dims, ad copy and landing page, launch place) for a chosen slot, after the script or voorzet is approved. Use for "make the concept", "write the hypothesis", "put this in Adflow as a concept", or before the brief. Not for the brief itself (use video-brief or designer-brief) and not for writing the copy (use meta-copy).
---

# Concept (between S5 and S6)

Turns an approved slot (and, for video, an approved script) into a **concept** in Adflow: a concept with its dims and
a short document that holds the thinking. The production work goes into a separate brief afterwards. Structure and
writing rules: [concept-document.md](../../references/concept-document.md). Pipeline:
[ad-pipeline.md](../../references/ad-pipeline.md).

## Steps
1. **Collect what is decided**: the slot (persona × angle × awareness), the product and offer per variant, the
   delivery and arc (video) or format (static), and the approved script or voorzet. Missing something? Ask, don't guess.
2. **Check if a concept already exists** for this slot in Adflow. If so, continue in it and don't create a duplicate.
3. **Gather the evidence** from the sources in [bronnen.md](../../references/bronnen.md): research (reviews and
   comments), live winners judged on spend first, and the brand's handbooks. Note any confound (audience, offer,
   volume).
4. **Check the dims.** Reuse values that exist. List new values you would need and ask the user to confirm the names
   before you create them. Never remove or replace values on other concepts.
5. **Create the concept** (a root concept, not a brief) with a plain name: the idea in words, then the persona in
   brackets. Attach the dims that exist. The concept number comes from Adflow; never invent one.
6. **Write the document** in the five sections of [concept-document.md](../../references/concept-document.md).
   - Ad copy: write it with `meta-copy` if it is not written yet, and put it in the concept, not in the brief.
   - Launch place: use the brand's launch handbook for ad set naming and for what has to be created new.
   - Empty document: write it. Document with text: don't overwrite, show the text in the chat instead.
7. **Show the user** the sections and the open `[check]` points, and stop. The brief is made afterwards with
   `video-brief` or `designer-brief` as a child of this concept, only after the user agrees with the concept.

## Rules
- **No client data in this skill or its references.** Client knowledge lives in Adflow and the brand's handbooks.
- **Hypothesis without target numbers.** Targets belong to the media buyer.
- **Spend first** when you judge what works; results second.
- **Name the confounds.** Evidence from a different offer or audience says less than it seems.
- **Additive only.** Create, attach, write; don't delete, rename or overwrite what others made.
- **Short.** The concept fits on one screen; detail belongs in the brief.

## Output
A concept in Adflow with its dims and a filled document (five sections), plus a short chat summary: the concept
number, which dims are attached, which values still have to be created, and the open points. Next step for the user:
check the concept, then ask for the brief.
