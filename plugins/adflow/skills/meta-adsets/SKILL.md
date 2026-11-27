---
name: meta-adsets
description: "Create the new Meta adsets of an approved adset plan as empty, paused drafts in the ad account, copying the settings of each reference adset, with start and end times converted from Dutch time to the ad account's timezone. Checks the plan and the references first, says what it will do, builds one test adset, then the rest. Never publishes. Use when someone says 'maak de adsets aan', 'zet de adsets klaar uit het plan', 'maak de concept adsets', 'create the ad sets from the plan', or points to a saved adset plan with status Concept. Meta only. Not for adding ads to an adset (use the launch in Adflow) and not for making the plan itself."
---

# Meta adsets from an adset plan

An adset plan lists the new adsets a brand needs: the name, the campaign, the reference adset to copy, the start and
end, and what differs from the reference. This skill turns every row of that plan into an **empty adset, paused, as a
draft in Meta**, so the media buyer can check it in Ads Manager and publish it. It sits before the launch in the
[pipeline](../../references/ad-pipeline.md): the adset has to exist before ads can go in.

## Fixed rules
- **Never publish or activate.** Publishing is a separate step the user asks for. Say clearly that publishing
  switches the adset on.
- **Say what you will do first, then wait for the user's OK.** Do not create anything before that.
- **Create the adset empty, do not duplicate the reference.** A duplicate takes all ads of the reference with it,
  and a draft ad can only be removed one by one, each with its own confirmation. Build a new adset from the
  reference's settings instead.
- **Copy every setting of the reference**, not only the obvious ones: campaign, optimization goal and event, pixel,
  billing, attribution windows, location and location types, age, brand safety, placements. Keep Advantage+
  audience on unless the plan or the user says otherwise. Do not touch the reference or any other existing adset.
- **Read each reference separately.** Markets can differ (a region instead of a country, another country list).
  Never assume the second reference is the same as the first.
- **A new draft adset is staged as active.** Set it to paused right after creating it and read it back.
- **Times in the plan are Dutch time**, unless the plan says otherwise. The ad account has its own timezone, so
  convert (step 3). Do not trust a note in the plan about "Meta time" without checking the account.
- **Discard a draft only after a preview and the user's OK**, and only through the Meta Ads MCP. Never use "Discard
  draft" in Ads Manager: it can discard drafts of other people.
- **Brand rules live in the brand's launch handbook in Drive**, not in this skill. Follow the handbook for names,
  campaign structure and settings when it says something the plan does not.

## Steps

### 0. Check the connections (first; stop when one is missing)

| What | How | Needed for |
|---|---|---|
| Meta Ads MCP | the ad account list loads and the account can be queried | always |
| Google Sheets | the plan's spreadsheet opens | when the plan is in a sheet |
| Adflow connection | the brand is in the list of brands | only to check pillar dates |

If one is missing, say which connector to add and stop.

### 1. Read the plan
1. Find the plan: the rows with status Concept in the adset plan of the planning sheet, or the rows the user pastes.
   Ask which plan when there is more than one.
2. Per row, note: the reference adset (name and ID), the campaign, the new name, the start and end, the location, what
   differs from the reference, and the notes.
3. Count the rows per pillar and per market. Say the total. If it does not match what the user expects, say so
   before going on.
4. Find the ad account from the brand and check that every reference is in it.

### 2. Check the references in Meta
1. Read every reference adset: it exists, it is active, it sits in the campaign the plan names, and read its full
   settings (the list is under Fixed rules).
2. Check the campaign budget level. Under a campaign budget (CBO) the new adset gets **no budget of its own**.
3. Note anything that cannot be copied or looks wrong: a missing reference, another campaign, a settings difference
   between markets.

### 3. Convert the times
1. Read the timezone of the ad account.
2. Convert every start and end from Dutch time to that timezone, with the real offset for that date. The offset is
   not always the same: in the weeks when Europe and the US change to or from summer time on different days it
   differs by an hour.
3. An end that says "23:59 on the last day" is **Dutch** 23:59. Converted to an account behind the Netherlands, that
   is an earlier time on the same day. Check that the converted end still ends on the right day in Dutch time, and
   not the next morning.
4. Show both in the report, so the user can see them side by side.

### 4. Say what you will do, then wait
Report, short:
- how many adsets, per pillar and per market, and the account;
- per adset the name, the campaign and the times in Dutch time and in the account's timezone;
- what differs from the reference (name, times, no ads) and what is copied;
- the open points from the plan (decisions not made yet, small campaign budgets that get a share of an extra adset)
  and what you would do about them.

Then wait for the OK. If the user wants a market left out, leave it out and note it.

### 5. Create one adset first
1. Create the first adset (the first market of the first pillar) with all settings from its reference.
2. Set it to paused and read it back as a draft: name, campaign, status, times, location, and no errors.
3. Compare it with the reference field by field. Show the differences, also those that the tool added by itself
   (for example automatic advertiser fields for countries in the EU, or extra targeting flags). Say what you could
   not compare.
4. Fix what is wrong in the draft and wait for the OK before making the rest.

### 6. Create the rest
1. Create the remaining adsets, one per row. They do not depend on each other, so make them in one go per pillar.
2. Set each to paused straight after creating it.
3. Read all drafts back and check, per adset: name, campaign, paused, start and end (in the account's timezone),
   location (country, region or list), no validation errors. Fix and recheck what fails.
4. Look at the adsets that are in a country or region with extra rules (advertiser or payer fields in the EU, regions
   instead of countries) and say if one lacks something that publishing might ask for.

### 7. Clean up mistakes
If a draft or a duplicate turns out wrong or is left over, make a discard preview, show what would go (the adset and
every ad in it), and discard only after the user's OK. Check afterwards that nothing is left.

### 8. Write back to the plan
After the user's OK, fill in the plan's own columns for each created row: the status, the new adset ID, the date
created and who did it. The status means "created as draft", not live. Do not change other rows, and do not change the
plan's structure unless the user asks.

## Output
A table of what is now in Meta, as drafts and paused: name, campaign, adset ID, start and end in Dutch time and in
the account's timezone. Below it the **points to check before publishing**: value rules (not visible through the
MCP), the advertiser fields for the EU, small campaign budgets, and every open point of the plan. Say that nothing is
published and that publishing switches the adsets on.

The user checks the drafts in Ads Manager and says when to publish. The ads go in afterwards through the launch in
Adflow.
