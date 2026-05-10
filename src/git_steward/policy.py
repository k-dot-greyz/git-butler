"""Policy file loader — reads .git-steward.yaml from repo root."""
from __future__ import annotations

from pathlib import Path
from typing import List, Optional

try:
    from pydantic import BaseModel, Field
except ImportError:
    raise ImportError("pydantic is required: pip install pydantic")


class SubmodulePolicy(BaseModel):
    require_pinned: bool = True
    allowed_branches: List[str] = ["main"]


class PolicyConfig(BaseModel):
    commit_types: List[str] = Field(
        default=["feat", "fix", "docs", "chore", "refactor", "test", "ci", "perf", "style", "revert"]
    )
    branch_prefixes: List[str] = Field(
        default=["feat/", "fix/", "chore/", "docs/", "ci/", "refactor/"]
    )
    protected_branches: List[str] = Field(default=["main", "master"])
    submodule_policy: Optional[SubmodulePolicy] = None


DEFAULT_POLICY_FILENAME = ".git-steward.yaml"


def find_policy_file(start: Path = Path.cwd()) -> Optional[Path]:
    """Walk up from start to find .git-steward.yaml."""
    for parent in [start, *start.parents]:
        candidate = parent / DEFAULT_POLICY_FILENAME
        if candidate.exists():
            return candidate
        if (parent / ".git").exists():
            break
    return None


def load_policy(path: Optional[Path] = None) -> PolicyConfig:
    """Load and validate policy; fall back to defaults if no file found."""
    target = path or find_policy_file()
    if target is None:
        return PolicyConfig()
    try:
        import yaml
    except ImportError:
        raise ImportError("pyyaml is required: pip install pyyaml")
    raw = yaml.safe_load(target.read_text()) or {}
    return PolicyConfig(**raw)
