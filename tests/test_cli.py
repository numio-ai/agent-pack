"""Smoke tests for the CLI."""

from click.testing import CliRunner

from agent_conf.cli import cli


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_init_stub():
    runner = CliRunner()
    result = runner.invoke(cli, ["init"])
    assert result.exit_code == 0


def test_generate_stub():
    runner = CliRunner()
    result = runner.invoke(cli, ["generate"])
    assert result.exit_code == 0


def test_sync_stub():
    runner = CliRunner()
    result = runner.invoke(cli, ["sync"])
    assert result.exit_code == 0
