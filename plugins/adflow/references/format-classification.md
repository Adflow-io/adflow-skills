# Format classification: which Format value an ad gets

How to decide which value of a brand's **Format** dimension an ad gets, so that everyone on the team tags the same ad
the same way. Use it when tagging a concept or an ad, and when auditing existing tags. For the rules on adding a new
dimension or value, see [dimension-hygiene.md](dimension-hygiene.md). For ideas on which formats to make, see
[static-formats.md](static-formats.md) and [ugc-format-templates.md](ugc-format-templates.md): those are idea lists and
also contain creative types that are not a format under the rules below.

## Order of sources

1. **The brand's AI instructions in Adflow**, the section `## Format`. What it says wins: the brand's own format
   list, definitions and decisions.
2. **This reference**, for everything the brand did not define.
3. Still in doubt? Name the two closest formats, say which rule decides it, and let the user choose. Never create a
   new Format value without the user's approval (see [dimension-hygiene.md](dimension-hygiene.md)).

## What a format is

A format is **the form of the ad: what you see and hear**, not what it says, who says it, or where it runs.

Two rules for every format:

1. **Visible.** You can recognise it from the picture and the sound, without reading the copy or knowing the angle.
2. **Independent of the message.** Any angle or offer fits into it without changing the label.

One rule for the whole list:

3. **One box.** Every ad fits exactly one format. If two fit, the cards below are missing a "Not to confuse with" line:
   add it, do not tag both.

## What does not belong in Format

| If the label says... | It is... | Put it in |
|---|---|---|
| who is on screen (founder, creator, expert) | the sender | Creator |
| what the ad argues (review, gift, us vs them, objection) | the message | Angle |
| the discount or deal | the offer | Offer |
| who sees it (retargeting, cold) | placement or funnel | Awareness |
| how it was made (UGC, AI generated, selfie, studio) | production | a tag, not a dimension value |
| the tone of the copy (bold statement, funny) | copy style | nothing, or a tag |
| the order of the story (problem to solution, listicle script) | structure | a separate dimension if the brand wants it |

Judge video from what is on screen and in the audio, second by second (the segments in Adflow), never from the
thumbnail or the ad name. Song lyrics are not speech.

## Decision tree

**Static**
1. Is it a screenshot of something native (a comment, a notes app, a message, a receipt)? Go to *Native screenshot*
   formats.
2. Is the main element text in a fixed layout (a letter, a list, a big number, a table)? Go to *Text-led* formats.
3. Otherwise it is *Image-led*: pick by what the image shows.

**Video**
1. Does one person speak to camera for most of the video? *Talking head*, unless a more specific card fits (street
   interview, comment reaction, green screen).
2. Is it footage with a voice-over or text carrying the story? Pick by what the footage shows (behind the scenes,
   product demo, b-roll with voice-over).
3. Is it acted? *Skit*.

## Format cards: static

| Format | Must be true (visible) | Not to confuse with |
|---|---|---|
| **Product hero** | One product large in frame, short headline or none | *Headline + benefits*: there the text block carries the ad |
| **Lifestyle photo** | Product in use or in a real setting, with or without a person | *Product hero*: plain or studio background |
| **Flat lay** | Products laid out, shot from above | *Grid*: separate tiles, not one photo |
| **Headline + benefits** | Big headline plus two to four benefits as text | *Feature callouts*: there the text points at parts of the product |
| **Feature callouts** | Lines or arrows from the product to labelled features | *Headline + benefits* |
| **Comparison table** | Two columns or rows: the product next to an alternative | *Split screen*: two pictures, not a table |
| **Split screen** | The image split into two halves side by side | *Before / after*: same subject, two moments |
| **Before / after** | Same subject in two states, marked as before and after | *Split screen* |
| **Grid** | Several products or photos in separate tiles | *Flat lay* |
| **Quote card** | A customer quote or review is the main visual element | *Comment screenshot*: there it is a real screenshot |
| **Comment screenshot** | A real social comment or review as a screenshot | *Quote card* |
| **Native screenshot** | Looks like a phone screen: notes app, message, receipt, search | *Comment screenshot* |
| **Letter** | A personal letter or note fills the ad, signed by a person | *Native screenshot (notes app)* |
| **Listicle** | A numbered or bulleted list is the main element | *Headline + benefits*: a few benefits, no list |
| **Statistic** | One big number is the eye-catcher | *Headline + benefits* |
| **Press** | Looks like an article, headline from a publication, or logos of press | *Quote card* |
| **Meme** | A recognisable meme template | *Lifestyle photo* |

## Format cards: video

| Format | Must be true (visible) | Not to confuse with |
|---|---|---|
| **Talking head** | One person speaks to camera for most of the video | *Street interview*, *Comment reaction*, *Green screen* |
| **Street interview** | People on the street answer a question or try the product, interviewer often off screen | *Talking head* |
| **Comment reaction** | A comment on screen at the start, then the answer | *Talking head*: no comment on screen |
| **Green screen** | A person in front of a screenshot, page or chart they react to | *Talking head* |
| **Product demo** | The product is shown being used, poured, applied or worn; no person telling a story to camera | *Behind the scenes*: production, not use |
| **Unboxing** | A package is opened on screen and the product taken out | *Product demo* |
| **Try-on** | A person puts the product on and shows how it looks | *Product demo*, *Unboxing* |
| **First-try reaction** | Someone tries the product for the first time and reacts on camera | *Street interview* (strangers), *Talking head* (no tasting or trying) |
| **Behind the scenes** | Footage of making, packing or the workplace, with voice-over or text | *Product demo* |
| **B-roll with voice-over** | Mixed footage with a voice-over carrying the story, no speaker on screen | *Behind the scenes*: that shows production |
| **B-roll with text** | Footage with on-screen text carrying the story, no speech | *B-roll with voice-over* |
| **Skit** | An acted scene with roles | *Talking head* |
| **Vlog** | Handheld, following someone through their day | *B-roll with voice-over* |

## Common mistakes

- **Founder as a format.** The founder is the sender: Creator = founder. The format is what they do on screen:
  talking head, behind the scenes, letter.
- **Testimonial as a format.** A review is a message: Angle. The format is the form: quote card, talking head,
  comment screenshot.
- **UGC as a format.** UGC says who made it. A UGC video is a talking head, a try-on, a product demo, and so on.
- **Selfie video as a format.** Selfie says how it was filmed: front camera, handheld. A selfie video is a talking
  head, a first-try reaction or a vlog. To compare selfie with tripod or studio, use a tag or a separate production
  dimension, so you can compare within one format.
- **Tagging per concept.** The format is set on the concept and passed to all its ads. If one concept holds two forms
  (a talking head and a static), split the concept or tag the exception.

## The brand's `## Format` section

Each brand can add a short section to its AI instructions in Adflow. Only list what differs from this reference.

```
## Format
- Dimension: Format (slug: <slug>)
- Our formats: <the values the brand uses>
- Different from the standard:
  - "<value>": <the brand's definition, what must be true, what not to confuse it with>
- Decisions:
  - <date>, <name>: <what was decided and why>
```

## Checking that it works

A format list works when different people pick the same value without talking. Test it: take about 20 varied ads,
let two or three people tag them separately with this reference and the brand section, and count how often they
agree. Around 80% or more is a good sign. Every ad they disagree on points to a card that needs a sharper "Must be
true" or a missing "Not to confuse with". Fix it and test again with new ads.
