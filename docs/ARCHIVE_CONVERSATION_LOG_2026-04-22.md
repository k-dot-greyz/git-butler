# Conversation log (unfiltered) — git-steward / Git Butler + pricing + kitties follow-up

**Source:** Cursor agent session, 2026-04-22.  
**Note:** Preserved as a design archive; includes opinionated review of in-repo kitties-tts work from the same session. Not edited for tone.

---

## User (review / Opus handoff)

> how is the progress after your minions did what they did? how compliant are with with the new guidelines?

## Assistant (compliance audit — summary)

- Phase 0 constitution / AGENTS / audit doc: largely done.
- Phase 1 SSOT (tts-config, server wiring, UI, docker, docs): substantial progress.
- Phases 2–6 from the long plan (TDD integration tests, thiserror split, handler SoC, defense middleware, TLS feature, tracing): **not** fully implemented; several config fields **dead** (timeouts, body limits, rate limit) until middleware lands.
- Table: §1 strong; §2 partial; §3/5/6/7 still gaps; `map_synth_error` string-matching called out as anti-pattern for §3.

---

## User (worktrees for remaining plan work)

> how would you orchestrate a worktree for the rest?

## Assistant (worktrees)

- Dependency: **§5 SoC split is the bottleneck** — unlocks parallel §3/§6/§7 after.
- Suggested layout: parallel worktrees for `tdd-config`, `docker-prod`, `immutability-audit` early; **solo** `soc-split`; then parallel `fail-fast`, `defense`, `observability` after split merges.
- Subagent types: `best-of-n-runner` for SoC split optional; `generalPurpose` for others; `ci-watcher` on PRs.
- Risks: submodule SHA drift in dev-master, `.kitties-runtime.json` port collisions, duplicate `target/` dirs — suggest `CARGO_TARGET_DIR` or accept compile cost.

---

## User (git watchdog subagent?)

> would it make it better if there was a git watchdog or similar subagent that handled git processes?

## Assistant

- Prefer **deterministic automation** + **hooks** over an LLM “watching” git.
- **Steward** subagent *on demand* for submodule bumps / rebase sweeps / merge queue — possible; **polling watchdog** — no.
- Three layers: hooks block bad commands; scripts/proc for repetitive ops; GitHub branch protection as outer wall.

---

## User (mechanical git assistant + market)

> a dedicated automaton assistant that literally just mechanically does git mgmt… so the coding agent doesn't even have to keep all that in mind

## Assistant (Git Butler / git-steward CLI)

- **Not an LLM** — domain CLI wrapping `git`/`gh` + org scripts; policy in YAML; JSON for agents.
- Harvest existing `dex/04-scripts/*.sh` as backends.
- Cursor `preToolUse` hook blocks raw mutating git; agents call `git-steward` only.
- Token savings: partial strip in Cursor (can’t remove built-in system prompt); full strip in self-hosted agents; ROI measurable.
- **“Git Butler” name collision** with existing product — rename for ship.

---

## User (marketability, n8n-style UI, middle management)

> Git Butler - I like that… token costs… config UI like n8n nodes… middle management favorite

## Assistant

- Token + discipline scaling model; **GUI as sales / exec demo**, **YAML as source of truth** for devs (Grafana-style viz, not full n8n editor as daily driver).
- Buyers: platform / DevEx / VP Eng at AI-heavy shops — not literal “middle managers” as IC buyers.
- Competitive grid: pre-commit, Mergify, Graphite, GitButler (Chacon), etc. — **unfilled niche**: agent-native + policy-as-code + teaching + stacked surfaces.
- GitButler name taken — rebrand.

---

## User (ROI scaling, “shitty git discipline”, redundancy Slack)

> estimate how the git tooling token costs scale… graceful degradation… ping slack when something actually fails

## Assistant

- Per-op token bands (clean vs messy vs disaster); **compound decay** of messy-rate over months.
- Scenarios: 10 dev / 50 dev / 500 dev — waste superlinear with org size if unchecked.
- **Layered defense** diagram: CLI → hook → Action → App → branch protection; each with Slack tier.
- **Stash-intent** / retry pattern for flaky network.

---

## User (solo / team / lifetime pricing — personal philosophy)

> individual licenses… 3.33 coffee… 6-8 team… lifetime ~50… people interpret numbers illogically

## Assistant

- **$3.33** awkward + **fee %** + **lifetime vs annual** cannibalism (50 vs 40/yr).
- Prefer **Free** tier + **$3.99–$4** personal + **$8 team** + **Founder’s cap** not permanent lifetime.
- Support burden at low price — community support on cheap tier.

---

## User (6.9/mo 42/yr, not main product, ecosystem funnel)

> 6.9/mo 42/yr, im not going to make this my main product… promotional breadcrumb into the larger ecosystem… foot in the door… familiar with the brand being useful

## Assistant

- Validates “breadcrumb” strategy; still recommends **free** tier + **capped founder** + **OSS core** for distribution.
- **Teaching mode** as differentiator for “people who don’t know git.”
- Infra floor ~$130–300/mo before profit; **Commercial** seats fund rent; **Personal** is distribution.
- Distribution: OSS CLI, build in public, HN, Cursor communities, `/learn` content SEO.

---

## User (this session — PR + log + TTS upstream)

> fork butler spec from here and submit as draft PR with the conversation log dump (unfiltered) along with it. then make sure all the TTS changes are up to snuff and can also be found upstream

## Assistant (this PR)

- Add `dex/01-templates/git-butler/{README,SPEC,CONVERSATION_LOG}.md`.
- Verify kitties-tts: `cargo test --workspace`, `pnpm -C ui check`, `pnpm -C ui build`.
- Branch + draft PR on **dev-master** (spec) and **kitties-tts** (code); submodule bump PR on dev-master pointing at kitties commit.

---

## Raw user quotes (pricing / product intent, captured verbatim where possible)

- “6.9/mo 42/yr, im not going to make this my main product, this is more like a promotional breadcrumb into the larger ecosystem… just to get the foot in the door and familiarize the brand with being useful”
- Earlier: “perpetual license probably just as an intro perk as I need cashflow and customers asap”
- Earlier: “free for open-source/single seat + commit footer, but full personal (non-commercial) is at most 3.69”
- Earlier: “commercial licenses 6.9-8.8 range… undercut and overdeliver… symbolic profit margins… street cred”

---

*End of log as committed for draft PR archival.*
