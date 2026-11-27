# Dimension hygiene: when to add a dimension or a value

A dimension or a dimension value is only worth adding when it helps decide what to make next or where budget goes.
Every extra field costs time when tagging, and every vague one makes the data less reliable. Use this reference before
proposing a new dimension or a new value in Adflow, and when cleaning up an existing one. For how to pick a Format
value, see [format-classification.md](format-classification.md).

## Before adding a dimension

All six must be a yes. One no means it is a tag, a note or a field in the concept document instead.

| Test | Question | A no means |
|---|---|---|
| **Decision** | Will you filter on it to decide what to make next or where budget goes? Write down the question it answers, in one sentence. | It is a note or a tag. |
| **One axis** | Do all values answer the same question (all about the form, or all about the sender)? | Split it, or move the odd values to the dimension they belong to. |
| **No overlap** | Is this not already captured by another dimension? | Use the existing dimension. Two places means two truths. |
| **Not derivable** | Does Adflow not already know it (ad type, length, language, market, detected format or hook)? | Use what Adflow detects. Exception: Adflow needs the value for the ad name, or its detection is not reliable enough for this brand. |
| **Five seconds** | Can someone fill it in without asking anyone? | The definitions are too vague, or it overlaps with another dimension. |
| **From when** | Can existing ads be tagged afterwards, or does it only count from now on? | Decide this up front. Without old ads tagged, there is no before and after comparison. |

## Before adding a value

| Test | Question | A no means |
|---|---|---|
| **Does not exist yet** | Does it not fit an existing value, under another name or spelling? | Use the existing value. |
| **Repeat** | Will you make at least about five creatives with it? | Use the closest existing value or the fallback. One or two ads never lead to a conclusion. |
| **Definition first** | Is there a short definition, with what not to confuse it with, before the value is created? | Write it first. In Adflow, each value has its own document for this. |
| **Approval** | Has the dimension owner agreed? | Ask first. Never create a value on your own initiative. |

## Every two or three months

For the Format dimension, the skill `format-audit` runs these tests together with the format rules.

| Test | Question | A no means |
|---|---|---|
| **Spread** | Do the values really differ between ads? If around 90% of ads share one value, the dimension teaches nothing. | Split the big value, or drop the dimension. |
| **Volume** | Has each value had enough ads and spend to judge it? | Merge it with a neighbour or retire it. |
| **Agreement** | Do two people still tag the same ad the same way? Test with about 20 ads. | Sharpen the definitions. |

## Two things every dimension needs

- **A fallback.** An `Other` value, or a tag, for what does not fit. Without one, people create new values or pick the
  nearest wrong one, and both pollute the data. Review what ends up in the fallback: a pattern there is a candidate
  for a new value.
- **An owner.** One person who decides on new values and doubtful cases, and writes each decision down with a date and
  a name, in the brand's AI instructions in Adflow.

## Where the brand's rules live

The brand's AI instructions in Adflow hold what differs per brand: which dimensions it uses, their owner, its own
definitions and its decisions. Keep that section short: only what differs from these references.
