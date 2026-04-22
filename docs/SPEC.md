# git-steward — consolidated spec (fork from design session, 2026-04-22)

> This file lives in the **git-butler** OSS repo. The long-term **CLI** name is likely `git-steward` to avoid confusion with the unrelated “GitButler” app.

## Problem

- Coding agents spend significant **input + reasoning tokens** re-deriving git policy (Conventional Commits, branch rules, submodule procedures) that already lives in repo docs.
- **Policy drift** compounds over time (messy ops increase messy-rate month over month).
- **Human git learners** need **teaching at point of use**, not only opaque errors.

## Solution shape

**Not an LLM.** A **deterministic CLI** (`git-steward <verb>`) that:

1. Reads **policy-as-code** (YAML), versioned in-repo — single source of truth.
2. Wraps `git`, `gh`, and (optionally) org-specific scripts in your monorepo.
3. Returns **structured JSON** for agents; human-readable output for terminals.
4. Sits under **defense in depth**: editor hooks / MCP → local hooks → GitHub Actions → App → branch protection; optional **Slack** on hard failures.

## Core verbs (future)

- `status`, `commit`, `push`, `rebase`, `sync`
- `wt add|list|rm` (worktrees)
- `sub bump|status|repair` (if you vendor submodule helpers)
- `pr open|ready|merge` (via `gh`, policy-guarded)
- `doctor` — policy compliance report

Exit codes: `0` ok, `2` bad args, `3` policy violation, `4` drift, `5` conflict.

## Policy file

Per-repo e.g. `.git-steward.yaml` — conventional commit types, branch prefixes, protected branches, etc.

## Teaching mode

Optional verbose path: every operation explains *what* happened and *why* a rule exists (links to short docs).

**Tonal / personality layer** (curated theme packs, verbosity, quips, long-op tips) is specified in [THEMES_AND_ONBOARDING.md](./THEMES_AND_ONBOARDING.md) — local-first; optional account for sync; `--json` / agents skip persona copy.

## Commercial / funnel (intention: breadcrumb, not core business)

- Free: OSS / single seat, **commit footer** optional.
- Personal: low cap (e.g. ≤ $3.69/mo) — *indicative only* until a storefront exists.
- Commercial: ~$6.90/mo or ~$42/yr type band for teams — **intentionally** low margin, street cred, funnel to other products and consulting.
- “Founder’s / perpetual” only in **limited** runs, not an unlimited LTV burn.

## Differentiation

- `pre-commit` / Husky: hooks, not agent-native.
- Merge queue SaaS: server-only.
- **git-steward** (this effort): policy compiler + agent JSON + optional teaching + stacked surfaces.

## Shipped in this repo today

- [scripts/guided-pr-flow.sh](../scripts/guided-pr-flow.sh) — [GUIDED_FLOW.md](./GUIDED_FLOW.md) — *working bash*, not the full `git-steward` binary yet.

## See also (monorepo of origin)

Internal scripts and `git-ops` conventions: [k-dot-greyz/dev-master](https://github.com/k-dot-greyz/dev-master) (template copy lived under `dex/01-templates/git-butler/`).

## Open items

- [ ] Rename / namespace for PyPI/ Homebrew to avoid “GitButler” collision in marketing copy.
- [ ] fold `guided-pr-flow` as `git-steward pr flow` (or keep standalone script).
- [ ] Python / Typer + tests + JSON output; MCP; GitHub Action templates; optional hosted dashboard.
- [ ] Theme / personality loader + tip packs — see [THEMES_AND_ONBOARDING.md](./THEMES_AND_ONBOARDING.md).
