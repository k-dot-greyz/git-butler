# git-butler

Breadcrumb / promo lane for a future **`git-steward`**: deterministic **git + GitHub CLI** workflow helpers that cut down on LLM token waste re-deriving the same Conventional-Commit and branch policy every session — plus a **guided PR flow** that shows repo/branch, pushes, and drops a **clickable PR URL** when done.

> **Name collision note:** a commercial product also uses “Git Butler” branding. This repo uses **git-butler** as the GitHub / OSS project name; the shipping CLI is likely to be called **`git-steward`**. See [docs/SPEC.md](docs/SPEC.md).

## What’s here now

| Path | What |
|------|------|
| [scripts/guided-pr-flow.sh](scripts/guided-pr-flow.sh) | **Runnable:** confirm `Repository` + **branch** → `git push` → `gh pr create --fill --draft` (or use existing PR) → success line + **PR link** |
| [docs/SPEC.md](docs/SPEC.md) | Product / technical spec (future Typer/MCP/Actions) |
| [docs/THEMES_AND_ONBOARDING.md](docs/THEMES_AND_ONBOARDING.md) | **Design:** theme/personality YAML, local vs account, onboarding, tips & loading behavior |
| [docs/GUIDED_FLOW.md](docs/GUIDED_FLOW.md) | UX + env vars + upsell-ladder ideas |
| [docs/ARCHIVE_CONVERSATION_LOG_2026-04-22.md](docs/ARCHIVE_CONVERSATION_LOG_2026-04-22.md) | Design archive (session transcript) |

## Quick start

Requires [GitHub CLI `gh`](https://cli.github.com/) (`gh auth login` in the repo you care about).

```bash
# From a clone of a repo with a current branch
./scripts/guided-pr-flow.sh
OPEN=1 ./scripts/guided-pr-flow.sh
SKIP_CONFIRM=1 ./scripts/guided-pr-flow.sh   # CI / agents
```

## Origin

Spec and first script started in [dev-master](https://github.com/k-dot-greyz/dev-master); it now ships as the **`dex/09-repos/git-butler`** submodule (replacing the old `dex/01-templates/git-butler/` doc mirror). This repository is the **dedicated** home for the public OSS track.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the fork-and-PR workflow, boundary rules (public OSS vs dev-master internal docs), and architecture guidelines.

## License

Apache-2.0 — see [LICENSE](LICENSE).
