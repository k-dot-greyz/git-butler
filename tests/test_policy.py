"""Basic smoke tests for policy loader."""
from git_steward.policy import PolicyConfig, load_policy


def test_default_policy_loads() -> None:
    config = load_policy(path=None)  # no file → defaults
    assert "feat" in config.commit_types
    assert "main" in config.protected_branches


def test_policy_config_custom() -> None:
    config = PolicyConfig(commit_types=["feat", "fix"], protected_branches=["main"])
    assert config.commit_types == ["feat", "fix"]
