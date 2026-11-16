# Writing in Adflow documents

**Role in the machine:** every skill that puts text into an Adflow document (concept document, briefs, ad copy)
follows these rules. The document editor in Adflow has quirks that break text written the way you would in chat or in
a markdown file. Skills: `concept`, `video-brief`, `designer-brief`, `meta-copy`.

**Client-agnostic.** This file contains no client data.

## Never use the slash character

The editor uses `/` to place nodes (a menu for headings, embeds, lists and so on). A `/` in running text triggers that
menu and causes bugs. So no `/` in any text you write into a document, in any language.

Write it out instead:

| Instead of | Write |
|---|---|
| and/or, en/of | or, of |
| NL/DE, NL/BE | NL and DE, NL en BE |
| before/after, voor/na | before and after, voor en na |
| 9:16 and 1:1 as 9:16/1:1 | 9:16 and 1:1 |
| 24/7, per week as 3/week | every day, 3 per week |
| him/her, hij/zij | them, die persoon |
| a pair that is a choice (red/blue) | red or blue |
| a pair that is a combination (UGC/B-roll) | UGC with B-roll, or UGC and B-roll |
| a range or label (hook/body) | hook and body, or hook, then body |

Rules of thumb:
- A choice becomes **or**. A combination becomes **and**. A label becomes a dash-free phrase, or two words.
- Don't replace it with a dash as a pause mark either; the house style avoids those.
- **Links and embeds are not text.** A URL (`https://...`) has to keep its slashes. Paste links as links, embeds as
  embeds, and don't touch the characters inside them.
- Dates as `12 March`, not `12/03`. Fractions and ratios in words or with a colon.
- This includes quoted copy: on-screen text, headlines and example hooks that you put in a document. Rephrase them
  without the `/` and tell the user you did.

## Layout

Write the document as structured markdown, not as a column of `Label: value` lines. The editor turns it into real
headings and lists.
- Every section of the template (Instructie, Varianten, Messaging, Dimensions and so on) becomes a `##` heading.
- Several items, such as variant codes, languages, steps or shots, become a bulleted list. Order matters: numbered list.
  Things to check off: `- [ ]` checklist.
- Use **bold** only for a short label in front of a value (`**Format:** 9:16`) or a UI name, never for whole sentences.
- Keep paragraphs to two or three sentences.
- Follow the template's order and wording, not its plain layout.

## Other editor limits
- **Lists, not tables.** Markdown tables show as plain text in Adflow documents.
- **Never overwrite** a document that already has text. Ask first, or hand the text over in chat. An empty document can
  hold a single empty paragraph: insert after it.
- Use the headings the skill prescribes, so every document reads the same.

## Before you hand over
Search your own text for `/` before it goes into the document. The only slashes left are inside links.
