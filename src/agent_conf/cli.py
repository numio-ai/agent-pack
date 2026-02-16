"""CLI entry point for agentconf."""

from typing import Optional

import typer

from agent_conf import __version__

app = typer.Typer(help="AI agent configuration manager.")


def version_callback(value: bool):
    if value:
        print(f"agentconf {__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True,
        help="Show version and exit.",
    ),
):
    """AI agent configuration manager."""
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


@app.command()
def init():
    """Bootstrap the agent-conf/ directory structure."""
    print("agentconf init: not yet implemented")


@app.command()
def generate():
    """Compile canonical rulesets into tool-specific configs."""
    print("agentconf generate: not yet implemented")


@app.command()
def sync(
    remote: Optional[str] = typer.Argument(None, help="Remote repository URL."),
):
    """Pull shared configurations from a remote repository."""
    print("agentconf sync: not yet implemented")
