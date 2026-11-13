# AGENTS.md

Rules for AI agents (Claude Code, Codex, Cursor) that change skills in this repo. Marketers direct the agent; the agent
follows these rules, even when a request sounds different. When in doubt, ask the user instead of guessing.

## What this repo is

One Claude plugin, `adflow`, distributed as a private marketplace. Everything that lands on `main` reaches everyone who
has the plugin within minutes, including clients later on. A mistake on `main` is a mistake for everyone, immediately.

```
.claude-plugin/marketplace.json    the marketplace (do not change without Nicky)
plugins/adflow/
  .claude-plugin/plugin.json       plugin name and description (do not change without Nicky)
  .mcp.json                        the connection to Adflow (do not change without Nicky)
  skills/<name>/SKILL.md           one folder per skill; this is where you work
  skills/<name>/*.md               examples or helper files that belong to that skill only
  references/*.md                  frameworks shared by several skills
scripts/check.py                   the check that runs on every pull request
```

Skills are invoked as `adflow:<name>`, for example `adflow:slots`.

## Workflow (required)

1. **Always start from a fresh `main`:** `git switch main && git pull`.
2. **Create a branch** with a short name that says what changes: `git switch -c skill/meta-copy-headlines`.
   Don't work on `main` or push to it, unless the user has said they may commit directly to `main`. For those users
   (and only when they say so) skip the branch and the pull request: run the checks, commit on a fresh `main` and push.
3. **One topic per pull request.** Change one skill, or add one new skill. No unrelated cleanups.
4. **Read first**: the skill you change, the references it links to, and the skills that refer to it
   (`grep -rn "<name>" plugins/`).
5. **Run the checks** and fix every error before you commit:
   ```bash
   python3 scripts/check.py
   claude plugin validate .
   ```
6. **Test the skill** in a real session with the local version of the plugin (see *Testing*). Write in the pull
   request what you tested and what came out.
7. **Commit and open a pull request:** `git push -u origin HEAD` and `gh pr create --fill`, or with a title and
   description following the template. Nicky does not need to approve pull requests; the user decides when it is merged.

## Writing a skill

### Name and folder
- The folder name is the skill name: lowercase letters, digits and hyphens, at most 64 characters (`static-voorzet`).
- `name:` in the frontmatter is exactly the folder name.
- No `adflow-` or `ad-` prefix: the plugin already puts `adflow:` in front of the name.
- Platform-specific? Start with the platform: `meta-copy`, `tiktok-copy`. If it works for every platform, leave the
  platform out of the name.

### Frontmatter
```yaml
---
name: meta-copy
description: Schrijf de Meta ad copy (primary text, headline, description) voor een concept volgens de ad copy handleiding van het merk. Gebruik bij "schrijf de copy", "maak de ad copy", of als een concept klaar is voor launch.
---
```
- `description` is on **one line** and at most 1024 characters.
- The `description` decides when Claude picks the skill. Say **what** the skill does, **when** to use it (in words a
  user actually types) and **what not** (point to the skill that does).
- One more field is allowed: `metadata` with `adbase: "true"`, which also gives the skill to the agent inside Adbase (the
  Adflow app). Add it only when the skill works with Adflow data alone: no Google Drive, no local files or programs
  (ffmpeg, scripts), no other tools. Leave it out when unsure; skills without it stay out of Adbase.
  ```yaml
  metadata:
    adbase: "true"
  ```
- Do not add other fields without agreement.

### Content
- Write skills in English. Existing Dutch skills stay as they are until someone translates them. Terms the team uses
  (hook, angle, persona, awareness, b-roll) stay as they are.
- Open with one paragraph: what the skill delivers and which step of the pipeline it serves
  ([references/ad-pipeline.md](plugins/adflow/references/ad-pipeline.md)).
- Then the steps in order, as a numbered list. Concrete and actionable, no background story.
- End with the shape of the output (a table, a list, a brief) and what the user does next.
- Keep `SKILL.md` under 300 lines. Longer explanations, or a framework several skills use, belong in `references/`;
  examples that belong to one skill go in that skill's folder (`voorbeelden.md`).
- Link to files with a **relative markdown link**, from a skill for example
  `[hook-levers](../../references/hook-levers.md)`. Never a path on your own computer (`/Users/...`), never
  double-bracket links to notes outside the repo.
- Refer to another skill by its name in backticks: `` `power-hooks` ``.

### Sources: what does and does not belong in the repo
- **No client data.** No client names, reviews, comments, winners, numbers, briefs, scripts or screenshots of a
  client. Not even as an example. Use invented, generic examples.
- **Client knowledge lives in Adflow**, the per-brand handbooks in Google Drive. A skill says where it fetches them
  (see [references/bronnen.md](plugins/adflow/references/bronnen.md)), not what they contain.
- **Brand-specific rules belong in that brand's Drive handbook**, not in a skill. A skill is the method for all brands.
- Refer to Adflow data by what it is (dims, concepts, Copy library), not by the technical name of a tool. Tool names
  can change.
- **No copied text** from courses, books, swipe files or paid sources. Summarise in your own words and cite the source.

## Renaming or deleting

Users invoke skills by name, and other skills refer to them. So:
- Only rename or delete when the user explicitly asks for it.
- Find every reference (`grep -rn "<old-name>" plugins/ README.md`) and update them in the same pull request.
- Write **"Renamed: old → new"** or **"Deleted: name"** in the pull request, so the team knows.

## Testing

Load the plugin from your own checkout instead of the installed version:

```bash
claude --plugin-dir ./plugins/adflow
```

Invoke the skill (`/adflow:<name>`) or ask a question that should trigger it, for a real brand in Adflow. Check:
- Does Claude pick the skill for a normal question? If not, sharpen the `description`.
- Does the output follow the steps and the shape described in the skill?
- Does it fetch the right sources from Adflow and Drive, without making anything up?

Do not put client output from the test in the repo or in the pull request; only describe what you checked.

## Thinking along on briefing and concept templates

Marketers correct briefs and concept documents all the time: they cut a line, add a step, rewrite a format. Treat
that as a signal about how the brand's briefing templates and concept templates should work, and think along about
making them better.

- **Notice the pattern.** When the user edits a brief or a concept document, or gives feedback on one, say in one or
  two lines what changed and what seems to be behind it. Do not wait to be asked.
- **Keep the types apart.** An editor brief, a creator brief and a designer brief differ, and so do the concept types
  inside them (for example a remake, a language version, a new format on existing footage), video versus static,
  voice-over versus talking head. The same goes for the concept document: its sections (hypothesis, insight, slot
  and dims, ad copy, launch place) can weigh differently per concept type. A fix for one type is not a fix for the
  others. Say which type the feedback applies to, and do not carry it over to another type without asking.
- **One correction is not a rule.** Ask if it should become the standard before you propose it as one. A line the
  user deliberately removed stays out; note it as a conscious omission and do not add it back.
- **Say where a change belongs.** Brand-specific rules and brand-specific templates go in that brand's Drive
  handbook (for example the editor briefing handbook, or a separate template next to it). A method that works for
  every brand goes in the skill (`video-brief`, `designer-brief`, `concept`) and follows the workflow above. Never put brand
  names or client data in the repo, not even as an example.
- **Propose first.** Show the proposed change and let the user approve it before you edit a Drive handbook or open a
  pull request. Both are shared and reach other people.
- **Keep briefs lean.** Suggest cutting before adding. A brief the editor can read in half a minute beats a complete one.

## What an agent never does

- Push to `main` unless the user has said they may commit directly to `main`.
- Force-push or rewrite history, whoever the user is.
- Change `.claude-plugin/`, `plugins/adflow/.mcp.json`, `scripts/` or `.github/` unless Nicky asks for it.
- Add a `version` to `plugin.json`: without a version, every merge reaches users automatically.
- Put passwords, tokens or API keys in a file.
- Disable or work around a check to get a pull request green.
