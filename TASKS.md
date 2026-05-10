# git-steward — Epic TODO Scaffold

> Living task board. Each section maps to a dev-master Epic. Check boxes are atomic deliverables.
> See [`docs/SPEC.md`](docs/SPEC.md) for full product context.

---

## EPIC 1 — Python/Typer CLI skeleton

> Goal: `git-steward --help` works, exits cleanly, all verbs stubbed.

- [ ] `pyproject.toml` with `[project.scripts]` entry point (`git-steward`)
- [ ] `src/git_steward/__init__.py` + version constant
- [ ] `src/git_steward/cli.py` — Typer app root with `--json` / `--verbose` flags
- [ ] Stub commands: `status`, `commit`, `push`, `rebase`, `sync`, `doctor`
- [ ] Stub command group: `pr` (subcommands: `open`, `ready`, `merge`)
- [ ] Stub command group: `wt` (subcommands: `add`, `list`, `rm`)
- [ ] Stub command group: `sub` (subcommands: `bump`, `status`, `repair`)
- [ ] Exit codes wired: `0` ok · `2` bad args · `3` policy violation · `4` drift · `5` conflict
- [ ] `README` quickstart updated to reference `git-steward` binary

---

## EPIC 2 — Policy file loader

> Goal: `.git-steward.yaml` drives all validation decisions.

- [ ] `src/git_steward/policy.py` — Pydantic model for `.git-steward.yaml`
- [ ] Fields: `commit_types`, `branch_prefixes`, `protected_branches`, `submodule_policy`
- [ ] Auto-discover: walk up from cwd to repo root
- [ ] Fallback to bundled defaults when no file found
- [ ] `git-steward doctor` prints policy load report (human + `--json`)
- [ ] Example `.git-steward.yaml` added to repo root
- [ ] Tests: valid config loads, missing file falls back, invalid field errors cleanly

---

## EPIC 3 — `guided-pr-flow` port → `git-steward pr flow`

> Goal: existing bash script fully replicated as native Python command.

- [ ] `src/git_steward/commands/pr.py` — `flow` subcommand
- [ ] Confirm repo + branch (interactive, or `SKIP_CONFIRM=1` / `--no-confirm`)
- [ ] `git push` with upstream tracking
- [ ] `gh pr create --fill --draft` (or detect existing PR and return URL)
- [ ] `OPEN=1` / `--open` flag opens PR URL in browser
- [ ] JSON output mode: emit `{"pr_url": "...", "status": "created|existing"}`
- [ ] Feature-parity test vs `scripts/guided-pr-flow.sh`
- [ ] Deprecation notice added to `scripts/guided-pr-flow.sh` header

---

## EPIC 4 — MCP tool wrapper

> Goal: agents can call `git-steward` verbs via MCP without shelling out.

- [ ] `src/git_steward/mcp_server.py` — FastMCP or raw MCP server scaffold
- [ ] Expose tools: `steward_status`, `steward_commit`, `steward_pr_flow`, `steward_doctor`
- [ ] All tools return structured JSON (reuse `--json` output layer)
- [ ] `mcp` optional dep group in `pyproject.toml`
- [ ] `docs/MCP.md` — usage guide for Cursor / Claude / other hosts
- [ ] Integration test: invoke MCP tool → assert JSON shape

---

## EPIC 5 — GitHub Actions templates

> Goal: drop-in workflow files for any repo adopting git-steward.

- [ ] `.github/workflow-templates/git-steward-policy-check.yml` — PR policy lint on push
- [ ] `.github/workflow-templates/git-steward-doctor.yml` — drift report on schedule
- [ ] Parameterized via `inputs` (policy path, fail-on-drift bool)
- [ ] `docs/ACTIONS.md` — setup guide
- [ ] Tested in this repo's own CI

---

## EPIC 6 — Theme / personality loader

> Goal: `--theme` flag loads curated tone packs; agents/`--json` always skip persona copy.

- [ ] `src/git_steward/themes.py` — loader for YAML theme packs
- [ ] Bundled theme: `default` (calm, ND-friendly — see `docs/THEMES_AND_ONBOARDING.md`)
- [ ] Theme fields: `greeting`, `success_quip`, `error_quip`, `long_op_tip`, `verbosity`
- [ ] Local override: `~/.config/git-steward/theme.yaml`
- [ ] Optional account sync stub (API shape TBD)
- [ ] `--json` and agent detection always bypass theme output
- [ ] Onboarding flow: first-run wizard sets verbosity + theme preference

---

## EPIC 7 — Packaging & distribution

> Goal: `pip install git-steward` and `brew install git-steward` work.

- [ ] PyPI namespace decision: `git-steward` vs `git_steward` vs scoped name (resolve collision check)
- [ ] Homebrew formula stub
- [ ] `CHANGELOG.md` initialized
- [ ] GitHub Release workflow (`release.yml`)
- [ ] Version bump script / `bump2version` / `commitizen` config
- [ ] `NOTICE` + license headers audit

---

## EPIC 8 — Docs & onboarding

> Goal: a new contributor can be productive in < 5 min.

- [ ] `CONTRIBUTING.md`
- [ ] `AGENTS.md` — agentic invocation guide (mirrors dev-master protocol)
- [ ] `docs/POLICY_REFERENCE.md` — full `.git-steward.yaml` field reference
- [ ] `docs/TEACHING_MODE.md` — teaching / explain mode spec
- [ ] `docs/COMMERCIAL.md` — pricing tiers + funnel intent (see SPEC commercial section)
- [ ] Quickstart updated in `README.md` to cover all epics

---

## Cross-cutting / infra

- [ ] `pytest` + `pytest-cov` baseline (≥ 80% on policy + CLI layers)
- [ ] `ruff` + `black` pre-commit hooks
- [ ] `mypy` strict on `src/git_steward/`
- [ ] CI workflow: lint → test → build on every PR
- [ ] Dependabot config
- [ ] `SECURITY.md`

---

> **Naming note:** CLI ships as `git-steward`. This GitHub repo stays `git-butler` for OSS identity. See `docs/SPEC.md §Differentiation`.
