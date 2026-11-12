---
name: script-verbeteren
description: Choice menu to improve a video script, right after the full script (S5) and before the brief (S6). Shows numbered improvement options (shorten, more human, sharper/more concrete, hold the viewer, rewrite the hook, psychological variation, audience pass); the user picks one or more, and each chosen option runs one at a time with a stop and approval in between. Use for "how can I make this script better", "improve the script", "what other checks can I do", or when a full script is ready. Video only. Lean output.
metadata:
  adbase: "true"
---

# Improve script (S5b · video)

The improvement step of the [ad pipeline](../../references/ad-pipeline.md), between **S5 (full script)** and **S6 (brief)**.
You receive a **full script** and let the user **choose** which improvements run on it. You don't decide which; the user
chooses (one or more). Way of working: one step per turn, stop and wait for the choice.

> **Video only.** Statics have no S5; there the voorzet is already the copy.

## Input
- **The full script** (NL and/or EN) as it is now. If it lives in Adflow, read it from the brief/concept there.
- **Slot:** persona × angle × awareness (+ delivery/arc), if available.
- **Brand guidelines** and customer words (reviews/comments) of the brand, from Adflow (see [bronnen.md](../../references/bronnen.md)). Everything you change must fit them.

## Step 1: show the menu
Show this menu (with a short remark per option where the script has something to say about it), **and stop**. Don't choose yourself.

| # | What it does | Skill / source |
|---|---|---|
| 1 | Make it shorter and tighter | `script-fluff-remover` |
| 2 | Make it sound more human (humanizer) | `anti-ai-writing` + [humanizer-passes](../../references/humanizer-passes.md) |
| 3 | Sharper and more concrete writing | `copy-levers` |
| 4 | Hold the viewer longer (loops, specificity, fluff) | `content-principles` |
| 5 | Rewrite the hook | `gap-hook` · `power-hooks` · `hook-levers` |
| 6 | Check psychological variation | `ad-reviewer` |
| 7 | Audience pass (would this persona say it like this?) | persona friend test, see below |

End with the question: *"Which do you want to run? For example 'do 4, 2 and 7'."*

## Step 2: run the chosen options, one at a time
Per chosen option, in the user's order (or, with no preference, 1 → 4 → 3 → 5 → 6 → 2 → 7, so the human layer comes last):
1. Run the matching skill/source on the **current** script (including what earlier options already changed).
2. Deliver **only**: what was found (short, per point), the adjusted script, and a change table (was → now → why).
3. **Stop** and ask for approval, or the next option, before you continue. Don't write anything into the document without approval.

### Option 7: audience pass
Go through every line and test: *would this persona really say this to a friend?* Watch for:
- product jargon instead of spoken language (technical term → everyday word)
- a brand tagline in the middle of the text
- too polished or generic; prefer a concrete image
- pronouns that exclude part of the audience
- factual errors about the product (what it does and doesn't do)

## Rules
- **Facts, claims and product truth stay.** No invented numbers, authority, result promises or customer stories.
  If something is needed that isn't in the data, mark it as a question for the customer instead of filling it in.
- **Brand don'ts still apply** (the do's and don'ts from the brand guidelines).
- **The angle of the slot stays the same.** If the message shifts, it is a different slot.
- **Honest closing line per option:** if the script is already good on this point, say so and change nothing. Don't invent problems.
- **Name the product at least once, naturally**, and don't use a fixed sign-off.
- Several options in a row can work against each other (e.g. shortening removes something the loop needs). Flag it as soon as it happens.

## Step 3: wrap up
When the user is done: one line summarising what changed, the final script, and the question whether it goes to
**S6 (brief)**. You only make the brief (`video-brief`) after approval.

## Notes
- This is a **menu**, not a fixed pipeline: the user may skip a step or run one several times.
- Client-agnostic: no client examples in this file. Client fit comes from the brand's documents in Adflow.
