"""Root CLI entry point for git-steward."""
from __future__ import annotations

import typer

app = typer.Typer(
    name="git-steward",
    help="Deterministic git + GitHub workflow helper. Policy-as-code, agent-native.",
    no_args_is_help=True,
)

# ---------------------------------------------------------------------------
# Sub-apps (stubbed)
# ---------------------------------------------------------------------------
from git_steward.commands import pr, wt, sub  # noqa: E402

app.add_typer(pr.app, name="pr")
app.add_typer(wt.app, name="wt")
app.add_typer(sub.app, name="sub")


# ---------------------------------------------------------------------------
# Top-level verbs (stubbed)
# ---------------------------------------------------------------------------

@app.command()
def status(
    json_output: bool = typer.Option(False, "--json", help="Emit JSON."),
) -> None:
    """Show policy-aware repo status."""
    typer.echo("[stub] status — not yet implemented")
    raise typer.Exit(0)


@app.command()
def commit(
    json_output: bool = typer.Option(False, "--json"),
) -> None:
    """Policy-guarded conventional commit."""
    typer.echo("[stub] commit — not yet implemented")
    raise typer.Exit(0)


@app.command()
def push(
    json_output: bool = typer.Option(False, "--json"),
) -> None:
    """Push with upstream tracking + policy check."""
    typer.echo("[stub] push — not yet implemented")
    raise typer.Exit(0)


@app.command()
def rebase(
    json_output: bool = typer.Option(False, "--json"),
) -> None:
    """Policy-guarded rebase."""
    typer.echo("[stub] rebase — not yet implemented")
    raise typer.Exit(0)


@app.command()
def sync(
    json_output: bool = typer.Option(False, "--json"),
) -> None:
    """Sync branch with upstream."""
    typer.echo("[stub] sync — not yet implemented")
    raise typer.Exit(0)


@app.command()
def doctor(
    json_output: bool = typer.Option(False, "--json"),
) -> None:
    """Policy compliance report."""
    typer.echo("[stub] doctor — not yet implemented")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()
