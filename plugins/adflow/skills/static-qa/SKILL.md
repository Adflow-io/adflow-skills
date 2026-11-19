---
name: static-qa
description: "Review a finished static (image) ad before it goes to the client, as the last quality check of the creative strategist. Looks at the delivered designs in Adflow next to the designer brief and the brand guidelines, checks scroll-stop, message, brand or native fit, visual quality, spelling, formats and safe zones, ad copy and delivery, and ends with approve or concrete feedback per fix. Use when someone says 'QA deze static', 'review de static ads', 'check het design', 'is deze static klaar voor de klant', 'keur de statics', or shares a delivered static asset or board. Static only: not for briefs (use designer-brief), not for video, not for psychological copy review (use ad-reviewer)."
---

# Static QA

The last check on a delivered static ad before it goes to the client. It comes after the designer has built the brief
from `designer-brief` (S6 in the [pipeline](../../references/ad-pipeline.md)) and before ad copy and launch. The
output is a verdict per creative, **Approve** or **Feedback**, with every fix concrete enough for the designer to act on.

The checks summarise Adflow's own SOP for the creative strategist ("QA review static ads"). The brand's Drive handbooks
win when they say otherwise (see [bronnen.md](../../references/bronnen.md)).

## Rules
- **Look at the image itself.** Open every creative and size. Can't see an image: say so for that creative, and do not
  judge it from its name or the brief.
- **One "no" means Feedback.** Approve only when every check in step 9 is yes.
- **Red flags** (step 8) mean Feedback straight away, whatever else is good.
- **Do not mark anything as approved in Adflow and do not post feedback yourself.** Show the verdict and the feedback;
  post a comment or change a status only when the user says so.
- **No guessing on spelling.** Read every word on the image in the language of the market. Not sure about a word in a
  language you know less well: flag it as "check", not as an error.
- **Read the text yourself.** The automatic description or tags of an asset in Adflow can misread the text on it.
- **The brief wins over the defaults here.** Sizes, texts, number of variants and file names come from the brief
  first, then the brand's handbook, then this skill.

## Steps

### 1. Gather
1. **The creatives:** from the concept, its designer brief or the board the user shares. Per creative: every size
   (normally 1:1 at 1080×1080 and 9:16 at 1080×1920), file name, file size, resolution.
2. **The designer brief** of the concept: headline, on-image copy, offer, CTA, format, reading order, required sizes.
3. **Brand guidelines** of the brand in Adflow: tone, do's and don'ts, logo, colours, fonts.
4. **Drive handbooks** of the brand, when they exist: designer briefing (sizes, naming, delivery) and ad copy.
5. **The ad copy** of the concept (primary text, headline), when it is already there.

### 2. Type and completeness
1. **Type**, from the brief or the format:
   - **Native**: should look like organic content.
   - **Branded**: should be recognisable as the brand.
   - **Overlay or template**: a frame that goes over product photos (for example a catalogue overlay in a feed tool),
     often a transparent PNG. Judge it **on top of a product photo**, light and dark, not on its own: a preview of a
     transparent PNG shows white where the photo will be. Ask for the example with product when the brief asks for
     one. Steps 3 and 7 count less; readability on every photo counts most.
   Unclear: ask.
2. **Review round or final delivery.** Designers often first upload one overview (a screenshot of all designs from
   the design tool) for approval, and export the separate files only after the OK. An overview is a **review round**:
   judge the design, text and completeness of what is visible, zooming in per design. Missing separate files are no
   Feedback in this round; list the file checks (resolution, file size, file names, every file there) as "at final
   delivery". With separate files it is the **final delivery**: run all steps, including step 10.
3. **Brief contradicts itself** (for example two different totals): say so first, judge against the most specific
   part, and ask the user which is right.
4. **Completeness:** count what the brief asks (variants × languages × sizes, plus any examples) against what was
   delivered. Name what is missing.
5. **Text check against the brief:** compare the text on every creative, per language, **word for word** with the
   text in the brief. A missing line, other wording or another offer is Feedback, even when the new text is fine.

### 3. First impression (scroll-stop)
Look at it as someone scrolling on a phone:
- Would you stop? Is the visual hook strong enough?
- Is the message clear **within 3 seconds**?
- Does the tone fit the audience? Does it look attractive and finished (branded) or authentic (native)?
- Squint test: with eyes half closed, do you still see what matters most?

### 4. Strategy
- **Message:** one main message, no confusion. The value for the customer is clear.
- **Hierarchy:** the eye goes to the most important element first, in the reading order of the brief.
- **Text:** scannable, not too much and not too little.
- **Offer and CTA:** attractive, clear and visible, and they match the brief and the current offer.
- **Branded only:** brand guidelines followed (do's, don'ts, tone), colours, fonts and style consistent, product clearly
  visible, logo placed right.
- **Native only:** looks like organic content, branding subtle or absent, not too polished, tells a story instead of selling.

### 5. Visual quality and text
- Clear hierarchy, balanced (not too busy, not empty), enough white space.
- No pixelated or low-quality images.
- **Spelling and grammar 100% right**, in every size and language. Also check that each translation sounds natural to
  a native speaker, not only that it is correct.
- Fonts readable on a small screen, text large enough, enough contrast with the background.
- At most 2–3 fonts (branded) or a native font style (native).

### 6. Sizes and technical
- **Every required size is there** (from the brief or the handbook; default 1:1 and 9:16).
- **Safe zones:** nothing important where it can be cut off or covered. In 9:16 keep roughly the top 14%, the bottom
  35% and 6% on each side free of text, logo and CTA (Meta's Stories and Reels interface).
- Nothing important cut off in any size; 9:16 is a re-stack, not a crop of the 1:1.
- Resolution at least 1080 px on the short side; file at most 30 MB (Meta).

### 7. Ad copy (when present)
- First line is a hook; benefits over features; no jargon.
- Urgency or social proof where it fits; CTA clear.
- Tone fits the audience: conversational (native) or the brand voice (branded).
- Copy and image tell the same story, with the same offer.

### 8. Red flags (Feedback straight away)
- Spelling mistake, or text that differs from the brief
- Text without its own background on an overlay, so it disappears on some product photos
- Unreadable text: too small or too little contrast
- Pixelated image
- Brand guidelines broken (branded) or too branded (native)
- Important element cut off, or outside the safe zone
- Unclear message, or no clear CTA
- Too busy: the eye does not know where to look

### 9. Verdict
Answer per creative, yes or no:
1. Would you stop scrolling for it?
2. Is the message clear within 3 seconds?
3. Can it convert?
4. Would you click on it as the audience?
5. Native: does it look organic? Branded: is the brand clear and consistent?
6. Are we proud to send this to the client?

All yes: **Approve**. One no: **Feedback**.

### 10. Delivery check (final delivery only)
- The creative sits in Adflow in the right place (the concept's brief board or the agreed view).
- File names follow the brand's handbook (see `naming`).
- Canva link added when Canva was used; source files (PSD, AI, Canva) in the client folder.

Missing items here are Feedback for delivery, not for the design. Say which.

### 11. Feedback
Per fix: **what**, **where** (size and place on the image), **why** and **how** it could be better. Name what is strong
too, specifically. Propose a realistic deadline. Post it (as a comment in Adflow, or in the team's channel) only when
the user says so.

## Output
Short, so the user can act right away:

1. One line per creative: **Approve** or **Feedback**, and the red flag if there is one.
2. Per creative with Feedback, a table: check · problem · fix.
3. What you could not check yourself (see below), as a short list.
4. One closing question, for example "Shall I post this feedback as a comment in Adflow?"

## What you cannot check
Say this at the end, briefly: the test on a real phone, the fast-scroll test in a real feed, and the file size or source
files when they are not visible in Adflow. Those stay with the user.
