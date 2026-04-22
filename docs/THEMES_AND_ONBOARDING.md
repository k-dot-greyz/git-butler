# Themes, personality packs & onboarding (design one-pager)

**Status:** design for future `git-steward` — not implemented in this repo yet. **Principle:** presentation and copy are **data-driven** (YAML + curated strings), not LLM-generated on the hot path.

## Why

- Same **policy engine** for everyone; different **tone, verbosity, and hand-holding** per user or team.
- **Long operations** (network, big `git` work) become **teaching time**: rotating tips (aliases, abstractions, script one-liners) — “word of the day” energy without fake LLM wisdom.
- **Optional account** unlocks sync and “white glove” defaults; **OSS and first run** stay local and fast.

## Local-first vs account

| Layer | What | Auth? |
|--------|------|--------|
| **Repo policy** | `.git-steward.yaml` — commits, branches, protected refs | No |
| **User style (local)** | `~/.config/git-steward/theme.yaml` or `~/.git-steward/themes/<id>.yaml` | No |
| **Account (optional)** | Synced profile: theme id, tip packs, team policy links, verbosity defaults | Yes — **only** when you want cloud sync or org features |

**Default posture:** first run is **verbose + teaching**; no login required. Onboarding **offers** sign-in (“save this personality & tips across machines”) — not a gate.

## Theme / personality schema (sketch)

All numeric ranges are **0.0–1.0** unless noted. Implementations may clamp.

```yaml
# Example: ~/.config/git-steward/user-style.yaml
version: 1
active_theme: greyz-mentor  # key into themes/ or bundled pack

themes:
  greyz-mentor:
    display_name: "Mentor (default)"
    tone:
      formality: 0.3        # 0 casual … 1 formal
      humor: 0.4            # 0 none … 1 frequent
      directness: 0.7       # 0 soft … 1 blunt
      spice: 0.2            # 0 family-friendly … (you define caps in product)
    delivery:
      verbosity: 0.75       # 0 terse … 1 explain everything
      teaching: true        # expand “why” on policy hits
      quip_rate: 0.35       # frequency of one-liners / celebrations
    ui:
      max_line_width: 100
      spinner: dots           # dots | line | none — product-defined set
      long_op_threshold_ms: 400   # show spinner + tip strip only after this
    tips:
      enabled: true
      rotate: per_session     # per_command | per_session | daily
      sources:
        - bundled: pro-tips/v1
        # - file: ~/.config/git-steward/tips/custom.yaml
        # - url: (optional; account or static CDN — curated only, not scraper)
    # Escape hatch: env GIT_STEWARD_TONE=brief or flag --brief overrides
    # verbosity/teaching down for a single invocation.
```

**Curated personality packs** ship as **named themes** (files or embedded defaults). Users **pick a pack** or **fork** one — you avoid an open-ended “infinite personality” support nightmare.

## Tips content (pro tips / “word of the day”)

- **Source of truth:** static YAML (or small checked-in files), **short** lines, **verified** (aliases you actually use, abstractions that exist in repo docs).
- **Rotation:** deterministic hash from `(session_id, day)` for “word of the day” mode, or round-robin per long op.
- **Not** auto-generated from an LLM in v1 — wrong tips erode trust faster than silence.

Example tip entry:

```yaml
- id: stash-pop
  text: "`git stash pop` applies the latest stash and drops it; `git stash apply` keeps it."
  tags: [beginner, safety]
```

## Onboarding flow (sketch)

1. **First run:** `git-steward` detects no user style file → writes **default theme** (verbose + teaching) to `~/.config/git-steward/`, or prompts **non-interactive safe defaults** in CI.
2. **Teach the basics:** one screen — “How do you like explanations?” (slider or presets: Brief / Balanced / Mentor). Maps to `verbosity` + `teaching`.
3. **Optional account:** “Sync theme & tips across devices?” — OAuth / magic link / GitHub, **skippable**.
4. **Escape:** `GIT_STEWARD_TONE=brief` and `--json` for agents (no quips, minimal copy).

## Agent / JSON mode

- `--json` or `STEWARD_FORMAT=json`: **no** spinners, **no** personality quips; structured events only. Persona applies to **human** TTY only.
- Prevents “fun” copy from breaking CI parsers.

## Open decisions

- [ ] Exact bundled theme names and default file paths per OS.
- [ ] Whether **team** themes live in repo (`.git-steward.theme.yaml`) vs user only.
- [ ] Tip pack versioning and update channel (static release vs account pull).

## See also

- [SPEC.md](./SPEC.md) — policy, teaching mode, product shape  
- [GUIDED_FLOW.md](./GUIDED_FLOW.md) — current bash “breadcrumb” UX (related dopamine/PR link story)
