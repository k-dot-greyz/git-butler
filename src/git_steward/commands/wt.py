"""wt command group — worktree helpers."""
from __future__ import annotations

import typer

app = typer.Typer(help="Worktree management.")


@app.command(name="add")
def wt_add() -> None:
    """Add a new worktree."""
    typer.echo("[stub] wt add")
    raise typer.Exit(0)


@app.command(name="list")
def wt_list() -> None:
    """List worktrees."""
    typer.echo("[stub] wt list")
    raise typer.Exit(0)


@app.command(name="rm")
def wt_rm() -> None:
    """Remove a worktree."""
    typer.echo("[stub] wt rm")
    raise typer.Exit(0)
