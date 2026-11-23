---
name: review-research
description: Turn a brand's customer reviews (and ad comments) into raw material for ads - pains, buying moments, doubts, results, intent-based personas and verbatim customer words - and save it as the brand's research document, or update that document with new reviews later. Use for "analyseer deze reviews", "review research", "haal klantwoorden uit de reviews", "nieuwe batch reviews", "werk de research bij", or when a brand has no research yet. Not for writing hooks or ads from it (use hook-levers, power-hooks or video-voorzet) and not for choosing slots (use slots).
---

# Review research (stage A)

Turns raw reviews and ad comments into the research the other skills read for customer words, doubts and personas
(see [bronnen.md](../../references/bronnen.md)). The goal is not a summary but raw material for ads: real pain, the
moment of buying, what almost stopped people, what changed, for whom, and the words they used. One living research
document per brand, updated with each new batch instead of rewritten.

## Input
- **The reviews**, uploaded by the user: a CSV export from the review app, or text pasted from the site. Reviews are
  not in Adflow. No reviews in the chat? Ask for them, don't go on without.
- **Ad comments**, if the user has them. They hold the doubts of people who did not buy.
- **The brand** in Adflow, and its existing research document if there is one (see step 1).

## Steps
1. **Check for existing research.** Look in Adflow for the brand's research document on reviews. Found one? Read it
   and work in update mode (step 10). None? Do a first run.
2. **Store the raw reviews** in the brand's Drive folder (see [bronnen.md](../../references/bronnen.md)), so the
   whole team can reach them: one file per export, with the source and date in the name (for example
   `Reviews - <platform> - <yyyy-mm-dd>`). Drive not connected? Ask the user to put the file there. In update mode,
   the earlier files there show which reviews were already used.
3. **Clean.** Remove what is not a real customer review: replies from the brand, duplicates. More than 300 reviews?
   Drop the ones under 8 words first. Read every long review in full and a sample of the rest.
4. **Group.** Several products? Group per product. Reviews that don't name a product go together. Reviews only about
   delivery or service go in a separate group "Brand and service".
5. **Score** each review 1 to 5: 1 empty ("top", a few words), 2 short and vague, 3 some detail but no feeling,
   4 a real experience with a before and after or a feeling, 5 long, vivid and emotional. Drop score 1. Use 2 and 3
   only to see patterns. Quotes come only from 4 and 5.
6. **Find the themes** per part. Per theme: a name, roughly how many reviews mention it, 2 to 3 lines of
   explanation. Biggest theme first.
   - **Pains:** the problem before buying, how long they had it, what they tried before.
   - **Desires:** what they wanted to reach or become. Look at moving away from a problem and towards something:
     ease, status, a nice gift, belonging.
   - **Buying moment:** what tipped them to buy now: an event, a tip, something on social, done with the alternative.
   - **Doubts:** what almost stopped them, with the source: [positive] in good reviews, in the past tense ("I was
     sceptical, but"), [complaint] in 1 to 3 star reviews, [comment] in the ad comments. Per doubt one idea to take
     it away in an ad.
   - **Result:** what changed, concrete and the feeling with it (relief, pride, confidence), in their words.
7. **Intent-based personas.** 3 to 6 personas based on why people buy, not who they are. Name them after the intent
   ("The quitter who tried it all before", not "woman 30+"). Largest first. Per persona: intent, situation, trigger,
   biggest doubt, how they talk (1 or 2 verbatim quotes), size (roughly how many reviews), and who (age, role, who it
   was for) only when it stands out.
8. **Customer words.** The strongest quotes, verbatim: change nothing, not even typos. Per quote the part and the
   product. Mark with ★ the quotes that work as a hook without changes. End with a line of loose words customers use
   often.
9. **Compare with Adflow.** Fetch the brand's personas and angles with their descriptions. Per intent-based persona:
   exists (with its name in Adflow), resembles (which one) or new. Fetch the ads with the most spend in the last 90
   days, judged on spend first and ROAS second. Per theme and doubt: is there already an angle or a running ad for it?
   Mark what is untested. Only read here: create or change no dims, concepts or ads.
10. **Update mode** (only when research already exists):
   - Use only reviews after the end date of the previous run. Remove duplicates on date, name and text.
   - Update the counts of existing themes, doubts and personas. Mark new ones "new since <date>".
   - Add only quotes that are not in the document yet.
   - Rework nothing that the new reviews don't touch.
11. **Save.** Ask where to save and offer only what is connected:
    - **Adflow:** the brand's research document. Adflow can't create a new document from here, so for a first run ask
      the user to create an empty document (for example "Review research", tagged research) and share the link. Edit
      it in place, never replace the whole document.
    - **Google Drive:** a Google Doc in the brand's Drive folder.
    - **A document in this chat** to download.
    Save only after the user chose.

## Rules
- No theme or persona based on one review.
- Fewer than 20 usable reviews, or few with score 4 and 5? Say so plainly.
- Health or result claims are customer stories, not product claims. Mark them so the user checks them before an ad.
- Quotes are source material. In a video the persona says it in their own words; don't put the quote on screen as is.
- Write short and in Dutch, unless the user writes in another language. Quotes stay in their own language.
- One brand per chat. Very many reviews? The last 500 to 1000 are enough to see the patterns.

## Output
The research document, in this order:
1. **Sources:** per run the date, platform or country, the period the reviews cover (from-to), the number of reviews,
   how many were dropped, how many scored 4 and 5.
2. **Themes:** pains, desires, buying moment, doubts (with source and counter idea), result.
3. **Intent-based personas** with their match in Adflow (exists, resembles, new).
4. **Customer words:** quotes with ★, then the loose words.
5. **Gaps:** themes and doubts without an angle or running ad.
6. **Summary:** the 3 main insights, the 3 biggest doubts, the largest persona, the best hook material.
7. **What changed** (from the second run on): 3 to 5 lines per run on what is new, growing or shrinking.

Next step: `slots` to turn the gaps and doubts into concept slots, or `hook-levers` / `power-hooks` for hooks from the
customer words.
