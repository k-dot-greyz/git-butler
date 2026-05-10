"""pr command group — open, ready, merge, flow."""
from __future__ import annotations

import typer

app = typer.Typer(help="Pull-request helpers.")


@app.command()
def flow(
    no_confirm: bool = typer.Option(False, "--no-confirm", envvar="SKIP_CONFIRM"),
    open_browser: bool = typer.Option(False, "--open", envvar="OPEN"),
    json_output: bool = typer.Option(False, "--json"),
) -> None:
    """Guided PR flow: confirm branch → push → gh pr create → print URL."""
    typer.echo("[stub] pr flow — port of scripts/guided-pr-flow.sh, not yet implemented")
    raise typer.Exit(0)


@app.command()
def open_pr(json_output: bool = typer.Option(False, "--json")) -> None:
    """Open (undraft) an existing draft PR."""
    typer.echo("[stub] pr open")
    raise typer.Exit(0)


@app.command()
def ready(json_output: bool = typer.Option(False, "--json")) -> None:
    """Mark PR ready for review."""
    typer.echo("[stub] pr ready")
    raise typer.Exit(0)


@app.command()
def merge(json_output: bool = typer.Option(False, "--json")) -> None:
    """Policy-guarded PR merge."""
    typer.echo("[stub] pr merge")
    raise typer.Exit(0)
