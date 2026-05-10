"""sub command group — submodule helpers."""
from __future__ import annotations

import typer

app = typer.Typer(help="Submodule helpers.")


@app.command()
def bump() -> None:
    """Bump submodule(s) to latest upstream commit."""
    typer.echo("[stub] sub bump")
    raise typer.Exit(0)


@app.command()
def status() -> None:
    """Show submodule status."""
    typer.echo("[stub] sub status")
    raise typer.Exit(0)


@app.command()
def repair() -> None:
    """Repair broken submodule state."""
    typer.echo("[stub] sub repair")
    raise typer.Exit(0)
