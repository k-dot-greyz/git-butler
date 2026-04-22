#!/usr/bin/env bash
# guided-pr-flow.sh — Confirm repo + branch, push, ensure GitHub PR, print success + PR link.
# Low-support “breadcrumb” UX; part of the git-butler / future git-steward line.
#
# Usage (from a git repo root):
#   ./scripts/guided-pr-flow.sh
#   OPEN=1 ./scripts/guided-pr-flow.sh
#   SKIP_CONFIRM=1 ./scripts/guided-pr-flow.sh
#
# See: ../docs/GUIDED_FLOW.md (when run from repo root: docs/GUIDED_FLOW.md)
#
set -euo pipefail

# --- style (ok without color)
if [[ -t 1 ]] && command -v tput &>/dev/null; then
	bold() { printf '%s' "$(tput bold 2>/dev/null || true)$*$(tput sgr0 2>/dev/null || true)"; }
	dim() { printf '%s' "$(tput dim 2>/dev/null || true)$*$(tput sgr0 2>/dev/null || true)"; }
	grn() { printf '%s' "$(tput setaf 2 2>/dev/null || true)$*$(tput sgr0 2>/dev/null || true)"; }
	ylw() { printf '%s' "$(tput setaf 3 2>/dev/null || true)$*$(tput sgr0 2>/dev/null || true)"; }
else
	bold() { printf '%s' "$*"; }
	dim() { printf '%s' "$*"; }
	grn() { printf '%s' "$*"; }
	ylw() { printf '%s' "$*"; }
fi

if ! command -v gh &>/dev/null; then
	echo "error: gh (GitHub CLI) not found. Install: https://cli.github.com/" >&2
	exit 1
fi

REPO_SLUG="$(gh repo view 2>/dev/null --json nameWithOwner -q .nameWithOwner || true)"
if [[ -z "$REPO_SLUG" ]]; then
	echo "error: 'gh repo view' failed. From this repo: gh auth login" >&2
	exit 1
fi

if ! git rev-parse --git-dir &>/dev/null; then
	echo "error: not a git repository" >&2
	exit 1
fi

REPO_URL="$(gh repo view --json url -q .url 2>/dev/null || echo "https://github.com/${REPO_SLUG}")"
BRANCH="$(git branch --show-current 2>/dev/null || true)"
if [[ -z "$BRANCH" ]]; then
	echo "error: detached HEAD? Checkout a branch first." >&2
	exit 1
fi

PUSH_REMOTE="${PUSH_REMOTE:-origin}"
DRY_RUN="${DRY_RUN:-0}"
SKIP_CONFIRM="${SKIP_CONFIRM:-0}"
OPEN_PR="${OPEN:-0}"
NO_DRAFT="${NO_DRAFT:-0}"

print_banner() {
	printf '\n'
	echo "┌── guided-pr-flow ─────────────────────────────────"
	dim "│  "; printf "Repository:  %s
" "$REPO_SLUG"
	dim "│  "; printf "Remote:      %s
" "$REPO_URL"
	dim "│  "
	printf "Branch:      "
	ylw "$BRANCH"
	printf "\n"
	echo "└──────────────────────────────────────────────────"
	printf '\n'
}

celeb_line() {
	lines=(
		"Ship it. The tab is waiting."
		"Upstream brine is ready for you."
		"PR exists. You may now touch grass."
		"CI can fail; your link is already real."
		"Link acquired. Go get review dopamine."
	)
	# shellcheck disable=SC2206
	n=${#lines[@]}
	echo "${lines[$((RANDOM % n))]}"
}

print_banner

if [[ "$DRY_RUN" == "1" ]]; then
	dim "DRY_RUN=1 — would: git push, gh pr create/view
"
	exit 0
fi

if [[ "$SKIP_CONFIRM" != "1" ]]; then
	read -r -p "  Push to ${PUSH_REMOTE} and ensure a PR? [Y/n] " _ok || true
	[[ -z "${_ok:-}" ]] && _ok=y
	_ok_lc=$(printf '%s' "$_ok" | tr '[:upper:]' '[:lower:]')
	if [[ "$_ok_lc" == "n" || "$_ok_lc" == "no" ]]; then
		grn "  Aborted. Nothing changed.

"
		exit 0
	fi
fi

echo "  $(dim "→") git push -u ${PUSH_REMOTE} ${BRANCH}"
git push -u "$PUSH_REMOTE" "$BRANCH"

PR_WAS_NEW=0
URL=""
if URL=$(gh pr view --json url -q .url 2>/dev/null) && [[ -n "$URL" ]]; then
	:
else
	PR_WAS_NEW=1
	if [[ "$NO_DRAFT" == "1" ]]; then
		echo "  $(dim "→") gh pr create --fill"
		gh pr create --fill
	else
		echo "  $(dim "→") gh pr create --fill --draft"
		gh pr create --fill --draft
	fi
	URL=$(gh pr view --json url -q .url)
fi

if [[ -z "$URL" ]]; then
	echo "error: no PR URL" >&2
	exit 1
fi

if [[ "$PR_WAS_NEW" -eq 1 ]]; then
	created_note="New PR (default: draft). Tweak title/body on GitHub."
else
	created_note="PR already open — you just pushed. Same link, fresher commit."
fi

printf "\n"
grn "  [ok]  "
printf "%s\n" "$(celeb_line)"
printf "\n"
	bold "  →  "
	printf "%s\n" "$URL"
printf "\n"
	dim "     %s
" "$created_note"
printf "\n"

if [[ "$OPEN_PR" == "1" ]]; then
	if command -v open &>/dev/null; then
		open "$URL" 2>/dev/null || true
	elif command -v xdg-open &>/dev/null; then
		xdg-open "$URL" 2>/dev/null || true
	fi
fi

exit 0
