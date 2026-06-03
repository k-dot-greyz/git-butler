# Contributing to git-butler 🔮

Thank you for your interest in contributing to **git-butler**! This project aims to build deterministic, token-saving git and GitHub CLI workflow helpers (like the future `git-steward` CLI) to make development smoother, faster, and less wasteful for both humans and AI agents.

By contributing, you help shape a more mindful, automated, and robust developer experience.

---

## 🌌 1. The Prime Directive: Pure Code in Submodules, Guides in Superproject

This repository is maintained as a git submodule within the larger **zenOS / dev-master** monorepo ecosystem. Because of this, we enforce a strict boundary between public code and internal documentation:

### ⚠️ The Boundary Violation Rule
**NEVER commit internal documentation, fork-specific guides, or monorepo-specific configurations into this repository.**

* **Why?** This is a public open-source project. Misplacing internal files (like private workflows, local setup notes, or monorepo standards) pollutes the repository, causes PR rejections, and leaks private architectural details.
* **The Standard**: This repository must contain **pure code and public-facing documentation only**. All internal guides, fork-specific documentation, and monorepo-specific notes must live in the superproject under `dev-master/dex/03-docs/guides/`.

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
Always branch off the latest `upstream/main`:
```bash
git fetch upstream
git checkout -b feat/your-feature-name upstream/main
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
   * Are there any `.md`, `.txt`, `.json`, or `.yaml` files that describe internal workflows, private fork notes, or monorepo standards?
   * *Action*: Move them to the superproject (`dev-master/dex/03-docs/guides/`) and delete them from this repository's staging area.
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

### Shell Scripting Best Practices
* **Portability**: Write scripts compatible with standard POSIX shells or `bash` (specify `#!/usr/bin/env bash` in the shebang).
* **Strict Mode**: Use `set -euo pipefail` in Bash scripts to catch errors early.
* **Non-Interactive Fallbacks**: Always provide non-interactive options or environment variable overrides (e.g., `SKIP_CONFIRM=1`) so scripts can run seamlessly in CI/CD or agent environments.
* **User Feedback**: Provide clear, colorized (optional), and structured output. Use `stderr` for logs/prompts and `stdout` for the final result (like the PR URL) to support piping.

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
