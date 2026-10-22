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
   Never work directly on `main` and never push to `main`.
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
- Do not add other fields without agreement.

### Content
- Write skills in Dutch, the language of the team. Terms the team uses in English (hook, angle, persona, awareness,
  b-roll) stay English.
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

## What an agent never does

- Push to `main`, force-push, or rewrite history.
- Change `.claude-plugin/`, `plugins/adflow/.mcp.json`, `scripts/` or `.github/` unless Nicky asks for it.
- Add a `version` to `plugin.json`: without a version, every merge reaches users automatically.
- Put passwords, tokens or API keys in a file.
- Disable or work around a check to get a pull request green.
