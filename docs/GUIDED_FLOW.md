# Guided flow (product note)

**Intent:** a **low-support** path: confirm **repo + branch**, **push**, ensure a **PR exists**, then print a small success line + **clickable PR URL**. Optional: open the browser. This is the “breadcrumb” experience — not the long-term revenue center.

## Reference script

- [`../scripts/guided-pr-flow.sh`](../scripts/guided-pr-flow.sh)

Behavior:

- Shows `Repository` (`gh` `nameWithOwner`) + **remote URL** + **current branch** before any network I/O. Default: confirm (bypass with `SKIP_CONFIRM=1`).
- Pushes `HEAD` to `origin` (or `PUSH_REMOTE`).
- If there is no PR for this head: `gh pr create --fill --draft` (or `--fill` only with `NO_DRAFT=1`). If a PR already exists, reuses its URL.
- Prints a one-line “celebration” + the PR URL. `OPEN=1` → `open` / `xdg-open` the URL on macOS / Linux.

## Environment

| Var | Effect |
|-----|--------|
| `SKIP_CONFIRM=1` | Non-interactive (CI / agents) |
| `DRY_RUN=1` | Print steps only |
| `OPEN=1` | Open PR URL in browser after success |
| `NO_DRAFT=1` | Create **ready** PR instead of draft (default: draft) |

## Future upsell ladder (placeholder names)

| Tier (idea) | Unlocks (sketch) |
|-------------|------------------|
| **git-butler** | Guided flow, free tier, commit footer, docs-first support |
| **steward** | Team registry, Slack, shared policy, audit |
| **Higher tiers** | TBD; consulting for DX / perf beyond git |

**Positioning:** the script is for **dopamine + the link** so people **finish the PR**; long-term value is **trust in the brand** and optional **consulting** for teams that outgrow a shell script.

## `SPEC.md`

The full `git-steward` CLI design: [SPEC.md](./SPEC.md).
