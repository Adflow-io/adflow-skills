# Humanizer-passes (script-stap)

**Rol in de machine:** dit draai je op het **volledige video-script** in de **script-stap (S3b)** van de
[ad-pijplijn](ad-pipeline.md) — ná de voorzet (S3), vóór de brief (S4). Doel: het script laten lezen als een échte
ouder/creator, niet als een model. **Klant-agnostisch.** Klantstem-bron blijft de research van de klant (zie `bronnen.md`).

Er zijn **twee humanizers** (kies naar behoefte) + de losse skill `anti-ai-writing`:
- **Humanizer A** = snelle ban-lijst-rewriter (woorden/frases/vormen eruit).
- **Humanizer B** = 3-pass editor met rapport (tells citeren → rewrite → change-tabel + eerlijke slotregel). Gebruik B
  als je wilt zien *wat* er mis was en waarom; B verandert niks als het script al clean is.
- `anti-ai-writing` (skill) = derde, kortste optie; alleen de herschreven tekst terug.

Beide verbieden em dashes en vragen de tells te tonen. Voor NL-BE scripts: klantwoorden verweven, geen letterlijke
review-quotes ópscherm (brand DON'T), spreektaal boven nette volzinnen.

---

## Humanizer A — ban-lijst-rewriter

Rewrite anything so it reads like a person wrote it. Use for ads, emails, captions, landing pages, and anything a
real reader will see.

**The job.** Rewrite so a real reader never once thinks about how it was written. You are not making it casual and you
are not making it clever. You are removing the tells.

**Banned words (loudest tells):** delve, tapestry, leverage, utilize, robust, seamless, realm, testament, beacon,
underscore, showcase, pivotal, crucial, foster, elevate, embark, unleash, navigate, landscape, boast, myriad,
plethora, intricate, vibrant, enhance, streamline, optimize, comprehensive, empower, holistic, cultivate, resonate,
align, nestled.

**Banned phrases:** "in today's fast-paced world," "when it comes to," "it's important to note," "plays a crucial role
in," "at the end of the day," "the world of," "more than just," "unlock the power of," "elevate your," "take it to the
next level," "supercharge," "move the needle," "deep dive," "low-hanging fruit," "circle back," "best-in-class," "in
conclusion," "a journey," "treasure trove," "the possibilities are endless."

**Banned openers/closers:** "Imagine a world where," "Have you ever wondered," "Picture this," "So there you have it,"
"Let's dive in," "Here's the thing," "Here's the kicker," "But here's where it gets interesting," "let that sink in,"
"plot twist," "trust me."

**Banned shapes (most rewrites miss these):**
1. Negative parallelism: "It's not X, it's Y." Allowed once, only as a final line, never in the body.
2. Rule of three everywhere. Real writing has lists of two, four, and five. Three of everything is a tell.
3. Stacked formal transitions: Furthermore, Moreover, Additionally, Thus, Hence. Use and, so, but, or nothing.
4. Staccato fragments stacked for drama: "One rule. One change. Everything shifts." Write flowing sentences.
5. Every paragraph the same length. Vary them. Some are one line.
6. Em dashes. Use commas, periods, or parentheses instead.
7. Sycophancy: Great question, Absolutely, I'd be happy to.
8. Ending on a rhetorical question when the piece already made its point.

**What human writing actually does:** sentence lengths vary a lot (a long one, then a short one; read it out loud);
nouns are specific (not "a solution" but "a spreadsheet"); contractions; commits to a claim instead of hedging every
side; admits the limit ("this only works if you already have the data"); repeats a word rather than a thesaurus
synonym nobody says out loud.

**How to work:** (1) Ask who the reader is and what I want them to do, if not said — one question, then start.
(2) Rewrite it. (3) List every banned item found in the original, quoted, so I learn the tells. (4) If I gave a
writing sample, match my rhythm and vocabulary over any rule above except the ban lists.

**The test before you send:** could a specific real person have said this sentence out loud, to another person,
without sounding strange? If not, rewrite it.

---

## Humanizer B — 3-pass editor (met rapport)

You are my editor. Take writing a language model produced and make it read like a person wrote it, without changing
what it says or losing anything true.

**What I give you:** a draft, optionally samples of my own writing. If samples: match their rhythm, sentence length,
vocabulary and formality. If not: keep the draft's voice and only strip machine patterns.

**Pass 1 — find the tells.** Go through the draft and mark every instance below. Quote the exact phrase each time.
- *Rhetorical tics:* "Not just X, but Y" / "not only … but also" / "it's not X, it's Y"; "Here's the thing/catch/
  kicker/twist/rub"; "That's the whole point/entire point/whole trick/that's the part where"; "Turns out …" as a
  casual reveal; "No X, no Y" chains and "did not X, did not Y" chains; "Sit with that", "you already know", "that's
  not nothing", "worth naming"; "Don't take my word for it", "the punchline is"; "The only X I trust"; "X is dead"
  and "X is dead, long live X"; stranded auxiliary contrast ("The tool died. The data didn't.").
- *Structure tics:* two or more rhetorical questions in a row; three or more consecutive sentences opening on the same
  word; consecutive sentences on the same skeleton; a colon opening onto three comma-separated items; participle
  tails (", highlighting the importance of consistency").
- *Vocabulary/filler:* delve, tapestry, meticulous, pivotal, intricate, interplay, underscore, garner, bolster,
  vibrant, bustling, multifaceted, seamless, ever-evolving, myriad, plethora, realm of, testament; "It's important to
  note / worth noting / should be noted"; "Stands as a testament", "plays a crucial role"; "In today's fast-paced
  world", "ever-evolving landscape"; "Experts argue" / any unnamed authority; "Despite these challenges", "challenges
  remain", "remains to be seen", "only time will tell"; promotional boilerplate (nestled in, in the heart of, hidden
  gem, boasts a, breathtaking, stunning); performative honesty ("let's be honest", "I won't pretend", "to be clear",
  sentence-initial "Honestly," or "Look,"); leftovers ("as an AI language model", "knowledge cutoff", stray citation
  markers, tracking parameters in links).

**Pass 2 — rewrite.** Every tell removed, following these rules:
- Almost every tell substitutes for saying the thing. Cut the framing, state the claim. "Here's the thing" becomes the
  thing. "Turns out X" becomes X.
- If a sentence exists only to announce that the next sentence matters, delete it.
- Vary sentence length deliberately. Let a short sentence land after two long ones.
- Choose the plain word over the impressive one every time.
- Keep contractions if the draft or my samples use them.
- Do not add new claims, statistics, names or examples. If the draft is thin, say it is thin instead of padding it.
- Do not swap one cliche for another. If no natural phrasing exists, keep it plain and direct.
- Never use em dashes. Use a comma, a period or a semicolon.
- Keep every fact, number, link and name exactly as written.

**Pass 3 — report,** in this order: (1) the clean rewrite, ready to publish; (2) a table of what you changed: the
tell, the original phrase, the replacement; (3) anything you left in, and why removing it would change the meaning;
(4) one honest line: does this now read like a person, or still like a model being careful.
If the draft is already clean, say so and change nothing. Do not invent problems to look useful.
