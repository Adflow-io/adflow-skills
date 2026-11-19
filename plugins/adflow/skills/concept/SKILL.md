---
name: concept
description: Create or fill the concept document in Adflow (hypothesis, reference, key message, launch proposal) for a chosen slot, after the script or voorzet is approved, following the brand's own concept format when the brand instructions have one. Use for "make the concept", "write the hypothesis", "put this in Adflow as a concept", or before the brief. Not for the brief itself (use video-brief or designer-brief) and not for writing the copy (use meta-copy).
metadata:
  adbase: "true"
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
3. **Read the brand instructions** in Adflow. If they have a Concept format, use that layout and its rules instead of
   the default in [concept-document.md](../../references/concept-document.md). Brand-specific rules live there, not in
   this skill. No Concept format? Use the default.
4. **Gather the evidence** from the sources in [bronnen.md](../../references/bronnen.md): research (reviews and
   comments), live winners judged on spend first, and the brand's handbooks. Note any confound (audience, offer,
   volume).
5. **Check the dims.** Reuse values that exist. List new values you would need and ask the user to confirm the names
   before you create them. Never remove or replace values on other concepts.
6. **Create the concept** (a root concept, not a brief), under the pillar if there is one, with a plain name: the idea
   in words, then the persona in brackets. Attach the dims that exist. The concept number comes from Adflow; never
   invent one.
7. **Write the document** in the four sections: Hypothesis, Reference, Key message, Launch proposal.
   - Write it after the concept exists, with the document edit tools. Text and embeds placed while creating the
     concept can disappear. Read the document back when you are done.
   - Key message: from the approved voorzet or script, or from the pillar agreements.
   - Launch proposal: use the brand's launch handbook for campaign and ad set naming and for what has to be created new.
   - Ad copy: write it with `meta-copy` if it is not written yet. It goes in the Copy library, and in the optional
     Ad copy section of the concept, not in the brief.
   - Empty document: write it. Document with text: don't overwrite, show the text in the chat instead.
8. **Show the user** the sections and the open `[check]` points, and stop. The brief is made afterwards with
   `video-brief` or `designer-brief` as a child of this concept, only after the user agrees with the concept.

## Rules
- **No client data in this skill or its references.** Client knowledge lives in Adflow and the brand's handbooks.
- **The brand's concept format wins** over the default layout.
- **Hypothesis without target numbers.** Targets belong to the media buyer.
- **Spend first** when you judge what works; results second.
- **Name the confounds.** Evidence from a different offer or audience says less than it seems.
- **Additive only.** Create, attach, write; don't delete, rename or overwrite what others made. Teammates edit the
  document too: read it again before every edit and keep their wording.
- **Short.** The concept fits on one screen; detail belongs in the brief.
- **No `/` in the text.** The Adflow editor uses it to place nodes. Links keep theirs; everything else is rephrased, see
  [adflow-documents.md](../../references/adflow-documents.md).

## Output
A concept in Adflow with its dims and a filled document (four sections), plus a short chat summary: the concept
number, which dims are attached, which values still have to be created, and the open points. Next step for the user:
check the concept, then ask for the brief.
