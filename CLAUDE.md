# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**agent-conf** is a Python CLI tool that manages AI agent configurations across multiple tools (Claude Code, Cursor, Copilot, etc.). It acts as a compiler: vendor-neutral canonical rulesets (YAML + markdown) are transformed into tool-specific outputs (`CLAUDE.md`, `.cursor/rules/`, `AGENTS.md`, etc.).

The core abstraction is **hierarchical inheritance** — configurations resolve across global → org → project → repo → user levels, controlled via `agent-conf.yaml`.

## Core CLI Commands

- **`agent-conf init`** — Bootstrap the `agent-conf/` directory structure in a repo
- **`agent-conf generate`** — Compile canonical rulesets into tool-specific config files
- **`agent-conf sync`** — Pull shared configurations from remote git repos (public + org-private)

## Tech Stack

- **Language**: Python
- **Distribution**: `uv tool install`
- **Status**: Greenfield — project is being built from scratch

## Build & Development Commands

```bash
# Install dependencies
uv sync

# Run the CLI locally
uv run agent-conf

# Run tests
uv run pytest

# Lint
uv run ruff check .

# Format
uv run ruff format .
```

## Architecture

The tool follows a **compilation model**: canonical source configs are the single source of truth, and tool-specific files are generated outputs. This distinguishes it from simpler file-sync tools.

Key concepts:
- **Canonical format**: Vendor-neutral YAML + markdown stored in `agent-conf/` directory
- **`agent-conf.yaml`**: Config file specifying target agents, `nested_depth`, hierarchy resolution
- **Generation targets**: Each supported tool (Claude, Cursor, Copilot) has a generator that emits the correct format
- **Reverse-sync** (unsolved): Changes made directly to tool-specific files (e.g., editing `CLAUDE.md` during coding) need to propagate back to canonical configs

## Task Management

Tasks follow the standard in `docs/task-management.md`:
- Lifecycle: `backlog → active → done`
- Stored as markdown in `tasks/{backlog,active,done}/`
- Named: `YYYYMMDD[_NN]_<description>.md`
- Require YAML header with `status` and sections for problem statement, scope, acceptance criteria, quality gates

## Organization

Maintained by **Agenture** (`agenture.org`). Apache 2.0 license.
