---
name: adset-plan
description: "Make an adset plan for a pillar. It says which new Meta adsets the pillar needs, in which campaign, with which name, when they run and which adset they copy. Shows the plan as a table in the chat and, after the user's OK, saves a short version with the pillar in Adflow. Use when someone says 'maak een adset plan voor pillar X', 'welke adsets hebben we nodig voor deze pillar', 'make an adset plan', or brings a counter-proposal to an existing adset plan. Meta only. Never creates anything in Meta (use meta-adsets for that) and does not write ad copy or briefs."
---

# Adset plan for a pillar

An adset plan says which new adsets a pillar needs: the campaign, the name, the start and end, and the existing adset
each one copies. This skill delivers the plan in two shapes: a **table in the chat** with one row per adset, and after
the user's OK a **short block with the pillar in Adflow**, so everyone who works on the pillar finds it there. It
sits before the launch in the [pipeline](../../references/ad-pipeline.md): first the plan, then `meta-adsets` creates
the adsets, then the ads go in.

## Fixed rules
- **Only the plan.** Never create, copy or change anything in Meta.
- **Read before you ask.** Do not ask the user for what the brand's rules, the pillar or the ad account can tell you.
- **Brand rules win.** Names, campaign structure, time zone and which adset to copy differ per brand. Follow the
  brand's own rules (step 1). The defaults in step 3 are only for what those rules leave open.
- **The pillar is the only place this skill writes to.** A team that also keeps its own log or sheet copies the
  table there itself.
- **Never say something was checked when you could not check it.** Say what the user has to check.

## Steps

### 1. Read
1. **The brand's rules for adsets.** Look in the AI instructions of the brand in Adflow and in the brand's launch
   handbook in Drive (see [bronnen.md](../../references/bronnen.md)). Note: the campaign per market, the name pattern,
   the time zone, and which adset a new one copies. If the two disagree, say so and ask which one counts. If there
   are no rules yet, say that, use the defaults, and suggest writing the rules down first.
2. **The pillar.** Name, start and end date, main dim value and the agreements. If the agreements already hold an
   adset plan, you are making a new version (see *A new version*).
3. **The ad account in Meta.** The campaigns, the adsets in them and how they are named, the daily budget per
   campaign, and the time zone of the account. Without a connection to Meta, say which one is missing and ask the
   user for the campaign names, the adset to copy and the time zone. Do not guess them.

### 2. Ask only what you cannot find
At most three short questions, and only when the answer is not in the rules or the pillar:
- Which markets get the adset?
- Does the pillar go into the existing campaigns, or does it get a campaign of its own?
- What happens to the adset it replaces or runs next to?

If the user is not there to answer, pick the most likely answer, say which one you picked, and put the question
under the open points.

### 3. Build the plan
Use the brand's rules. Where they say nothing, use these defaults.

**Structure**
- One new adset per pillar per campaign, in the existing campaign of that market.
- A pillar gets a campaign of its own only when the brand's rules or the pillar agreements say so.

**Name**
- Follow the pattern of the adsets that are already live. Default: `[MARKET]_[Name]_[date]`.
- Name is the main dim value of the pillar, without spaces.
- The date comes from the pillar dates, as YYMMDD:

| Pillar has | Date in the name | Example |
|---|---|---|
| start and end | `YYMMDD-YYMMDD` | `NL_SummerSale_260601-260614` |
| only a start | `YYMMDD-open` | `NL_NewCollection_260901-open` |
| only an end | `until-YYMMDD` | `NL_Spring_until-260531` |
| neither | no date | `NL_Bestsellers` |

**Dates and time**
- Start and end are in the local time of the brand: Dutch time, unless the brand's rules say otherwise. Start is
  00:01 on the first day. End is 23:59 on the last day, so the end date counts.
- The dates come from the pillar. Say so when a pillar has no dates or when they look wrong.
- Convert every start and end to the time zone of the ad account and give both. Use the real difference for that
  date: summer and winter time change it, and not on the same day everywhere. Show one worked example the user can
  check.

**Copy of**
- A new adset copies the settings of an existing adset in the same campaign. Take the one the brand's rules name.
  If they name none, take the newest adset of the same kind and say which one you took.
- The new adset starts empty: no ads from the adset it copies. Location, audience, optimisation, attribution and
  brand safety come from that adset.
- Under *Anders dan referentie* write only what really differs: the name, the start and end, no ads.

**Notes**
- What is the same for every row goes **once above the plan**, not on every row: open points, checks to do in Ads
  Manager, conditions of an offer.
- *Let op* per row only when that row is different, for example a campaign budget that is small for the number of
  adsets. Put that next to the campaign budget.

**Status**
- Every row starts as Concept. The statuses are Concept, Akkoord, Aangemaakt and Vervallen.

### 4. Show the plan in the chat
First the notes for the whole plan, then one table with one row per adset and these columns, in this order:

| Column | What goes in |
|---|---|
| Status | Concept |
| Pillar | Code and name of the pillar |
| Referentie adset | Name of the adset it copies |
| Referentie ID | Meta ID of that adset |
| Campagne | Campaign the new adset goes into |
| Nieuwe naam | Name of the new adset |
| Start | Local time, dd-mm-yyyy hh:mm |
| Eind | Local time, or empty when there is no end |
| Locatie | Same as the reference, or what differs |
| Anders dan referentie | What differs from the reference |
| Let op | Only when this row is different |
| Tijdzone account | Time zone of the ad account |
| Start in Meta | Start in the account's time zone |
| Eind in Meta | End in the account's time zone, or "Geen einde" |
| Ads meenemen | Nee, unless the user asked for the ads |
| Campagnebudget per dag | Budget of the campaign today, with a note when it is small |
| Open punt besloten | Ja, Nee or "Geen open punt" |

When many rows differ only by market, also give one line per pillar with `[MARKET]` in the name, so the user sees
the pattern at a glance.

Then ask: is this plan right, and may it go into the pillar?

### 5. Save it with the pillar
Only after the user says yes.
1. Open the agreements document of the pillar and edit it in place. Never replace the whole document.
2. Add the heading `Adset plan` at the end. If the heading is already there, change the lines under it and leave the
   rest of the document alone.
3. One block per pillar. A plan that covers three pillars becomes three blocks, one in each pillar.
4. No slash in the text, it breaks the Adflow editor. Write "tot en met" in full.
5. Read the pillar back and tell the user what is there now.

The block, with the labels in the language of the brand's other documents:

```
## Adset plan

**Status:** Concept (made on [date])

**Campagne:** [campaign pattern] ([exists or new], [markets])

**Adset:** [name pattern] (new, [in which markets])

**Kopie van:** [adset it copies]

**Loopt:** [start] tot en met [end], [local time]

**In Meta:** start [start in Meta], end [end in Meta] ([account time zone and the difference])

**Ads meenemen:** No, the adset is created empty

**Overnemen van de kopie:** [what comes from the adset it copies]

**Let op:**

- [only the rows that are different]

**Open punten:**

- [ ] [open point]
```

## A new version
When the user brings a counter-proposal or wants changes, make a new version of the plan. Show first what changes
compared with the plan that is saved with the pillar. After the user's OK, change the `Adset plan` block in the
pillar and put the date of the new version in the status line. Adsets that were already created stay as they are:
say which ones, and what the user has to change by hand.

## Output
The notes for the whole plan, the table with one row per adset, and after the OK the block saved with the pillar.
Say that nothing was created in Meta.

Next: the user sets the status to Akkoord and asks for the adsets, which `meta-adsets` creates as paused drafts from
this plan.
