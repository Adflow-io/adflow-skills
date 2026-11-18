---
name: meta-partnership-ads
description: "Turn the Meta ads of an Adflow launch into partnership ads, with the creator's Instagram handle from the concept document. Checks the connections first, reads the launch, tries the Meta Ads MCP per creator and falls back to Claude in Chrome (Ads Manager) when the MCP cannot link the creator. Shares links to publish and checks afterwards that everything is right. Use when someone says 'zet de partnership ads goed', 'koppel de creators aan deze launch', 'make these partnership ads', or shares an Adflow launch URL and asks to add the creators as partners. Meta only. Never publishes by itself. Not for writing ad copy (use meta-copy)."
---

# Meta partnership ads from an Adflow launch

The launch is already in Meta (the ads were sent), but as plain brand ads. This skill puts the creator from each
concept on its ads as partner, so the ad runs under the creator's name and the brand's. It is the step after launch
in the [pipeline](../../references/ad-pipeline.md).

> **Core:** the Meta Ads MCP cannot switch partnership on for an existing ad, because a creative cannot change after
> it is created. The MCP route therefore makes a **new partnership creative** with the same video, texts, link and
> UTM tags, and stages it on the existing ad in the Ads Manager draft. The ad ID stays the same, so the link with
> Adflow stays intact. When that fails for a creator, do it in **Ads Manager through Claude in Chrome**, where it is
> one switch plus the identities.

## Fixed rules
- **Never publish.** The user publishes through the links from step 5.
- **Always say that publishing switches the ads on.** Paused ads become ACTIVE after publishing.
- **Never build a creative inline** on the ad (an object story spec with branded content). Meta answers "Unknown
  Error" and leaves a broken draft. Always attach an existing creative by its ID.
- **Discard a broken draft per ad through the Meta Ads MCP only** (preview first, then confirm), and only after the
  user agrees. Never use the "Discard Draft" button in Ads Manager: it can also discard drafts of other ads.
- **Never swap the creative in a draft that is already open.** That also gives "Unknown Error". Discard it first.
- **Default order:** creator as first identity, brand as second, header "Dynamic identity". Follow the brand's
  `<Brand> – Launch handleiding Meta` in Drive when it says otherwise.
- **Ads that already run** (spend, likes, comments): a new creative means a new review, possibly a new learning phase
  and losing the social proof on the old post. Say so and ask before changing them.

## Steps

### 0. Check the connections (first; stop when one is missing)

| What | How | Needed for |
|---|---|---|
| Adflow connection, logged in | the brand of the launch is in the list of brands | always |
| Meta Ads MCP | the ad account list loads and the account has MCP access enabled | always |
| Right ad account | the account of the ad sets in the launch (step 1) is in that list | always |
| Brand identity | the brand's Instagram account and its Facebook Page ID, from the Instagram accounts of the ad account | MCP route |
| Claude in Chrome | the browser tools answer | Chrome route only |
| Logged in to Ads Manager | the editor of one ad opens without a login screen | Chrome route only |

- Adflow or Meta missing: stop and say which connector to add.
- Check Chrome only when a creator needs that route, but say up front: "for creators with only Instagram, Claude in
  Chrome is needed, logged in to Ads Manager".

### 1. Read the launch
1. Open the launch from the URL (`…/brands/<brand>/launch/queue?launch=<id>`): its concepts and the cells it sent to
   Meta, with the Meta ad set per cell.
2. Per concept, read the concept document and take the handle from the text (for example "Insta: …"). Strip `@`,
   spaces and formatting tags. Missing handle: stop and ask for it.
3. Match the Meta ads to the concepts: ad names contain `_C<concept number>_`. Per ad note the ID, status, effective
   status, creative ID and ad set.
4. Read each current creative, including its object story spec and URL tags. Take the video ID and image hash **from
   the object story spec**, not the video ID at the top level (it sometimes differs).
5. Show a table: concept → handle → ads (market) → status. Stop for approval.

### 2. Pick the route per creator (MCP first)
Per creator, one test with the real data of their first ad (so no loose test creatives are left behind): create an
Instagram partnership creative with the creator's handle as Instagram account, the brand's Instagram account and
Page as sponsor, and the video, image hash, primary text, headline, link, call to action and URL tags of the current
creative. Then check the creative's status a few times: IN_PROCESS usually takes 1–2 minutes.

| Outcome | Meaning | Route |
|---|---|---|
| Creative becomes **ACTIVE** | the MCP can make the partnership ad | **MCP** (step 3) for all ads of this creator |
| Error **"could not be resolved to a Page-compatible ads identity"** | handle found (the error names the Instagram ID), but no Page the MCP can use; often an Instagram-only account | **Chrome** (step 4) |
| Creative becomes **WITH_ISSUES** | same situation | **Chrome** (step 4) |
| Handle **not found** | typo or wrong handle in the concept | **Stop and ask** |

Passing a Page ID yourself (even the Page behind the Instagram account) does not help: the tool fails before using it.

### 3. MCP route
1. Create a partnership creative per ad as in step 2 (in parallel is fine). Name: `<short ad name>_partnership_<handle>`.
2. Wait until all creatives are ACTIVE.
3. Per ad, set the new creative on the ad by its ID. The change is staged in the draft. Check that there are no
   active errors and that the partners in the staged creative show the creator as `PARTNER_CREATOR`.
4. **Known and harmless:** in the draft Meta also puts the headline in the call to action as `link_title`. Ads
   Manager then warns "Link title and description … deprecated" and texts can briefly disappear in the editor. After
   publishing everything is right. Do not try to fix it: without a headline it is not better.

### 4. Chrome route (Ads Manager)
Per ad, in one tab you open yourself and close at the end:
1. Open `https://adsmanager.facebook.com/adsmanager/manage/ads/edit/standalone?act=<account>&business_id=<business>&selected_ad_ids=<ad>&selected_adset_ids=<ad set>&treenav=true`
   and wait until the editor has loaded (about 8 seconds).
2. Switch on **Partnership ad**.
3. Click **Edit** in the Identities section. The "Select identities" dialog opens.
4. Click the Instagram profile field of the **second** identity, type the handle and pick the option that shows
   **"Permission approved"** (or "Ad partnership"). **No such label: stop.** There is no active permission. Let the
   user check it in Business Suite → Creator Marketing → Creators → Manage permissions.
5. For a creator without a Page, Ads Manager fills in "Use Instagram account" itself. For a creator with a Page, that
   Page appears.
6. **Switch identities** so the creator comes first and the brand second. Check with a zoom of the dialog.
7. **Done**, wait about 8 seconds: no red messages. "Your ad must be associated with a Facebook Page" means the
   brand's Page is missing on the brand identity: pick it in the Page field (search by Page ID).
8. Check in the page that the URL and primary text are there and the headline is not empty.
9. Do not publish. "All edits saved" is enough.

Tip: the **Select partnership** button shows every partner of the brand with its status. Useful to see which
creators have given permission.

### 5. Share links to publish
- One link for everything plus one per ad, grouped per creator:
  `https://adsmanager.facebook.com/adsmanager/manage/ads/edit/standalone?act=<account>&business_id=<business>&selected_ad_ids=<id1>%2C<id2>…&selected_adset_ids=<as1>%2C…&treenav=true`
- Say: **publishing switches paused ads on (ACTIVE).** If the user does not want them live yet, pause them after publishing.
- Mention the known `link_title` warning (step 3.4), so nobody is alarmed.

### 6. Check after publishing
1. Read all ads again: status, effective status and creative ID. There must be no open drafts left.
2. Per new creative: the Instagram account in the object story spec is the creator's, and video, primary text,
   headline, link and URL tags match the original.
3. Report a table per creator: ads, account in the creative, status. IN_PROCESS or PENDING_REVIEW is normal right
   after publishing.

## Output
A table per creator (ads, route, status), the publish links, and after publishing a check table. The user publishes;
pausing again is their call.

## Known pitfalls
- The Instagram accounts of the ad account only show the brand's accounts, not the creators who are partners. Do not
  use that list as a permission check.
- Through the MCP a creator with active permission can still fail (WITH_ISSUES). Ads Manager is the source of truth
  for permission.
- For creators without a Facebook Page, Ads Manager makes a creative without a Page ID. The MCP always requires a
  Page ID, so it cannot rebuild such a creative.
- A blocked discard (safety check) is no reason to use the button in Ads Manager. Ask the user and try again through
  the MCP.
