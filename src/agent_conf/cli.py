"""CLI entry point for agent-conf."""

import click

from agent_conf import __version__


@click.group()
@click.version_option(version=__version__)
def cli():
    """AI agent configuration manager."""


@cli.command()
def init():
    """Bootstrap the agent-conf/ directory structure."""
    click.echo("agent-conf init: not yet implemented")


@cli.command()
def generate():
    """Compile canonical rulesets into tool-specific configs."""
    click.echo("agent-conf generate: not yet implemented")


@cli.command()
@click.argument("remote", required=False)
def sync(remote):
    """Pull shared configurations from a remote repository."""
    click.echo("agent-conf sync: not yet implemented")
