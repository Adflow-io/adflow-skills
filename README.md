# Adflow skills

The Claude plugin `adflow`: the connection to Adflow plus the skills we use to make ads, from concept slot to brief and
copy. Distributed as a private marketplace. The skills themselves (`SKILL.md`) also work in other agents.

Skills are invoked as `adflow:<skill>`, for example `adflow:slots`. Overview and pipeline:
[plugins/adflow/README.md](plugins/adflow/README.md).

## Using the plugin (one-time setup)

You need a GitHub account that is a member of `Adflow-io`.

1. Open Claude (desktop or claude.ai) → **Customize** → **Add marketplace**.
2. Connect your GitHub account and give the Claude GitHub App access to `Adflow-io/adflow-skills`.
3. Enter exactly `Adflow-io/adflow-skills`, turn on **Sync automatically** and install `adflow`.
4. The first time, sign in to Adflow with your own Adflow account (in Claude Code via `/mcp`, server
   `plugin:adflow:mcp`). If you also have Adflow as a connector in claude.ai, turn that one off, or you will have it
   twice.
5. Turn on the Google Drive and (for winners) Meta Ads connectors in claude.ai.

After that you have the plugin in Chat, Cowork and Claude Code. Whatever lands on `main` is updated automatically.

**Adding it fails** ("Repository not accessible")? Check that you accepted the invitation to `Adflow-io` and that the
same GitHub account is connected in Claude (Settings → Connectors → GitHub). Disconnect and reconnect if in doubt.

## Changing skills with Claude Code

You change skills by telling Claude Code what you want to change. Claude follows the rules in [AGENTS.md](AGENTS.md):
own branch, checks, pull request. Nicky approves, after which everyone has the new version.

### One-time setup

```bash
brew install gh
gh auth login
gh auth setup-git
gh repo clone Adflow-io/adflow-skills ~/Projects/adflow-skills
```

### How it works

1. Open Claude Code in the `adflow-skills` folder (desktop: Code tab → choose the folder; terminal:
   `cd ~/Projects/adflow-skills` and `claude`).
2. Say what you want, as concretely as possible. For example:
   - *"`meta-copy` writes headlines that are too long. Max 40 characters, and give 3 options instead of 1."*
   - *"Create a new skill `tiktok-copy`, based on `meta-copy`, for TikTok captions."*
   - *"`video-voorzet` should always include a CTA direction."*
3. Claude creates a branch, changes the skill and runs the checks. Read what it changed.
4. Test the skill for a real brand: open a new session with `claude --plugin-dir ./plugins/adflow` and invoke the
   skill, or ask a question that should trigger it.
5. Happy with it? Ask Claude to open a pull request. Write in it what you tested.
6. Nicky reviews and merges. Within minutes everyone has the new version.

Want to start over or throw a change away? Tell Claude ("discard this branch and start again from main").

### Ground rules

- **One topic per pull request.** Small and easy to review.
- **No client data in the repo**: no client names, reviews, winners, numbers or briefs, not even as an example.
  Client knowledge lives in Adflow, the per-brand handbooks in Drive.
- **Brand-specific rules belong in the brand's Drive handbook**, not in a skill.
- **The `description` decides when Claude uses a skill.** If you change it, test that Claude still picks the skill
  for an ordinary question.
- **Rename or delete only after agreement.** Users and other skills rely on the name.
- **No copied text** from courses, books or swipe files. Your own words, with the source cited.

All rules for the agent are in [AGENTS.md](AGENTS.md).

## Layout

```
AGENTS.md                         rules for agents (CLAUDE.md points to it)
.claude-plugin/marketplace.json   the marketplace
plugins/adflow/
  .claude-plugin/plugin.json      plugin name and description
  .mcp.json                       the connection to Adflow
  skills/<name>/SKILL.md          the skills
  references/                     frameworks shared by several skills
scripts/check.py                  the check that runs on every pull request
```
