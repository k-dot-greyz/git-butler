# Contributing to git-butler 🔮

Thank you for your interest in contributing to **git-butler**! This project aims to build deterministic, token-saving git and GitHub CLI workflow helpers (like the future `git-steward` CLI) to make development smoother, faster, and less wasteful for both humans and AI agents.

By contributing, you help shape a more mindful, automated, and robust developer experience.

> **Naming:** This GitHub/OSS project is **git-butler**. The future deterministic CLI is likely **`git-steward`** (to avoid confusion with the unrelated “GitButler” desktop app). See [README.md](README.md) and [docs/SPEC.md](docs/SPEC.md).

---

## 📂 Repository layout (what belongs here)

| Path | Purpose |
|------|---------|
| [scripts/guided-pr-flow.sh](scripts/guided-pr-flow.sh) | Runnable guided PR flow (`gh` + `git push`) |
| [docs/SPEC.md](docs/SPEC.md) | Product / technical spec for future `git-steward` CLI |
| [docs/GUIDED_FLOW.md](docs/GUIDED_FLOW.md) | UX notes and env vars for the guided script |
| [docs/THEMES_AND_ONBOARDING.md](docs/THEMES_AND_ONBOARDING.md) | Theme / personality / onboarding design |
| [docs/ARCHIVE_CONVERSATION_LOG_2026-04-22.md](docs/ARCHIVE_CONVERSATION_LOG_2026-04-22.md) | Design archive (session transcript) |

Quick try (requires [`gh`](https://cli.github.com/) authenticated in a git repo):

```bash
./scripts/guided-pr-flow.sh
SKIP_CONFIRM=1 ./scripts/guided-pr-flow.sh   # CI / agents
```

---

## 🌌 1. The Prime Directive: Public OSS here, monorepo guides in dev-master

This repository is the **dedicated public home** for git-butler / git-steward. It is also linked from [dev-master](https://github.com/k-dot-greyz/dev-master) as submodule **`dex/09-repos/git-butler`**.

### ⚠️ The boundary violation rule
**Do not commit dev-master–internal documentation, fork-only notes, or monorepo orchestration guides into this repository.**

* **Why?** This repo is public OSS. Files such as `SUBMODULE_MANAGEMENT.md`, private fork runbooks, or zenOS agent session notes belong in the superproject, not here.
* **Allowed here:** Shell scripts, tests, and **project-facing** docs under `docs/` and the root `README.md` (spec, UX, archives for this product).
* **Belongs in dev-master:** Internal guides and monorepo standards → `dev-master/dex/03-docs/guides/` (see [Submodule Contributing Workflow](https://github.com/k-dot-greyz/dev-master/blob/main/dex/03-docs/guides/SUBMODULE_CONTRIBUTING_WORKFLOW.md) in the superproject).

---

## 🔄 2. The Fork-and-PR Workflow

To contribute changes, follow this precise workflow to ensure a clean, isolated, and mergeable contribution:

### Step 1: Configure Remotes
Ensure your local clone has both the official `upstream` and your personal fork `origin` configured:
```bash
# Check existing remotes
git remote -v

# If upstream is missing, add it (using the canonical upstream URL)
git remote add upstream https://github.com/k-dot-greyz/git-butler.git
```

### Step 2: Create a Clean Feature Branch
Always branch off the latest `upstream/main`. Use conventional prefixes (`feat/`, `fix/`, `docs/`, `chore/`, `refactor/`):
```bash
git fetch upstream
git checkout -b feat/your-feature-name upstream/main
# examples: docs/add-contributing-workflow, feat/git-steward-status-verb
```

### Step 3: Implement Pure Code Changes
Make your changes to the scripts, documentation, or CLI code. Ensure:
* No temporary files, local logs, or environment files are tracked.
* No internal markdown files or monorepo-specific guides are created here.
* Code adheres to our **Agnostic Architecture Protocol** (see Section 3).

### Step 4: Run Pre-Commit Audit Checks
Before staging or committing, run the audit checklist (see Section 4).

### Step 5: Commit and Push to Your Fork
Commit with a clear, conventional commit message and push to your fork (`origin`):
```bash
git commit -m "feat(cli): add non-interactive mode for guided PR flow"
git push -u origin HEAD
```

### Step 6: Create the Pull Request
Create the PR against the upstream repository using the `gh` CLI or the GitHub UI:
```bash
gh pr create --repo k-dot-greyz/git-butler --title "feat(cli): add non-interactive mode for guided PR flow" --body "..."
```

---

## 🏛️ 3. GlitchWorks Agnostic Architecture Protocol

All development within this repository must strictly adhere to the **GlitchWorks Agnostic Architecture Protocol**. This ensures that all modules remain completely decoupled, self-contained, and highly maintainable across different runtime environments.

### 3.1. Zero Hardcoding (Dynamic State Configuration)
* **Rule**: No magic strings, static network ports, or fixed directory paths shall exist within the domain logic.
* **Application**: Never hardcode paths, default repositories, or user-specific settings. All configurations must be dynamically configured via environment variables, configuration files, or command-line arguments at startup.

### 3.2. Polymorphism by Default (Interface-Driven Contracts)
* **Rule**: Depend on abstractions, not concretions.
* **Application**: Define strict interfaces/contracts for external dependencies (e.g., git commands, GitHub API calls, logging). The core logic must interact only with these abstractions, allowing them to be swapped out for mock implementations during testing.

### 3.3. Open Piping (Strict Inter-Process Communication)
* **Rule**: Modules must communicate via strictly typed, isolated message events rather than direct state mutation.
* **Application**: External integrations (such as MCP servers, IDE extensions, or background daemons) must interact with our scripts/CLI via standard, structured inputs/outputs (e.g., JSON payloads on `stdout`/`stdin`, exit codes, or standard custom events) rather than direct state sharing.

### 3.4. Boundary Validation (The "Hostile Edge")
* **Rule**: Never trust incoming payloads. The core logic must be protected by a rigorous validation layer.
* **Application**: All user inputs, environment variables, and external payloads must be validated at the boundary before processing (e.g., checking that paths exist, verifying git repository status, and validating JSON schemas).

### 3.5. State Hydration & Dehydration
* **Rule**: Systems must be capable of pausing, exporting their truth, and resuming from a snapshot.
* **Application**: If a workflow or wizard is interrupted, the system should support serializing its progress/state to a standard format (like JSON or a temporary state file) and cleanly restoring from it to resume seamlessly.

### 3.6. Graceful Degradation (Predictable Failure)
* **Rule**: When a pipe breaks or a dependency fails, the system must fail safely and transparently.
* **Application**: Avoid unhandled exceptions or script crashes. Use robust error handling, catch command failures (e.g., if `gh` is not installed or the user is offline), log the failure clearly, and return a safe fallback or a meaningful exit code rather than crashing the host process.

### 3.7. Agnostic Telemetry & Observability
* **Rule**: Domain logic must emit its telemetry without knowing where the logs are going.
* **Application**: Emit structured logs/telemetry via standard output streams (`stdout`/`stderr`) or injected loggers, without assuming whether the tool is running inside a local terminal, a GitHub Action, or an automated agent environment.

---

## 📋 4. Pre-Commit Submodule Audit Checklist

Before committing changes, run this quick checklist to verify boundary hygiene:

1. **Check for Misplaced Files**:
   * Run `git status`.
   * Are there new or modified files that describe **dev-master internal** workflows, private fork notes, agent RAM, or monorepo standards (not product docs for git-butler)?
   * *OK in this repo:* changes under `docs/`, `scripts/`, `README.md`, `CONTRIBUTING.md`, and root license/notice files.
   * *Action:* Move monorepo-only guides to `dev-master/dex/03-docs/guides/` and unstage them here.
2. **Verify Diff Scope**:
   * Run `git diff --name-status upstream/main` (or the default branch).
   * Are there any unexpected files modified? Are there any changes unrelated to your feature or bug fix?
   * *Action*: Revert unrelated changes using `git restore <file>`.
3. **Check for "Diff Noise"**:
   * Run `git diff` and inspect the changes.
   * Did you introduce any formatting-only changes, trailing whitespace, or commented-out debug code?
   * *Action*: Clean up formatting and debug code before committing.

---

## 🛠️ 5. How to Clean Up History After a Boundary Leak

If you accidentally committed internal documentation or unrelated files and pushed them to your fork, follow these steps to completely remove them from the branch history:

### Step 1: Soft Reset to Upstream Main
```bash
git reset --soft upstream/main
```

### Step 2: Discard Misplaced Files
Any files that exist in your working directory but not in `upstream/main` will be unstaged.
* Move any internal documentation files out of the repository and into the superproject (`dev-master/dex/03-docs/guides/`).
* Discard any other unwanted changes:
  ```bash
  # Verify status
  git status

  # Discard unwanted modifications
  git restore <file>
  ```

### Step 3: Commit the Clean Diff
Commit the remaining, clean staged changes as a single, squashed commit:
```bash
git commit -m "feat(cli): enhance guided PR flow with robust error handling"
```

### Step 4: Force-Push to Rewrite Remote History
```bash
git push origin your-branch-name --force
```

---

## 📝 Coding Standards & Style

### Shell scripting best practices
* **Portability**: Write scripts compatible with standard POSIX shells or `bash` (specify `#!/usr/bin/env bash` in the shebang).
* **Strict Mode**: Use `set -euo pipefail` in Bash scripts to catch errors early (see [scripts/guided-pr-flow.sh](scripts/guided-pr-flow.sh)).
* **Non-Interactive Fallbacks**: Support env overrides documented in [docs/GUIDED_FLOW.md](docs/GUIDED_FLOW.md) — e.g. `SKIP_CONFIRM=1`, `DRY_RUN=1`, `OPEN=1`, `NO_DRAFT=1`, `PUSH_REMOTE`.
* **User Feedback**: Provide clear, colorized (optional), and structured output. Use `stderr` for logs/prompts and `stdout` for the final result (like the PR URL) to support piping.

### After merge (dev-master submodule consumers)
If you develop inside the monorepo, bump the submodule pointer from the superproject root with `dex/04-scripts/bump-submodule.sh` after your PR merges — do not land superproject-only docs inside this repo.

### Conventional Commits
We use conventional commits for clear history:
* `feat`: New feature
* `fix`: Bug fix
* `docs`: Documentation changes
* `style`: Code style/formatting (no functional changes)
* `refactor`: Code refactoring
* `perf`: Performance improvements
* `test`: Adding or updating tests
* `chore`: Maintenance tasks

---

**Inspired by zenOS principles**: Mindful technology, user agency, and calm computing. 🧘⚡
