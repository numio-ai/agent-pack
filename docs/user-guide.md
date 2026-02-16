# agent-conf User Guide

## What is agent-conf?

agent-conf manages AI agent configurations across multiple tools. You write rules once in a vendor-neutral format, and agent-conf compiles them into tool-specific config files (`CLAUDE.md`, `.cursor/rules/`, etc.).

## Installation

```bash
# Install from GitHub
uv tool install git+https://github.com/vkroz/agent-conf

# Or install from a local clone for development
git clone https://github.com/agenture-org/agent-conf.git
cd agent-conf
uv sync
uv run agentconf --version
```

## Quick Start

```bash
# Bootstrap in your repo
cd my-project
agentconf init

# Edit your rules in agent-conf/
# Then generate tool-specific configs
agentconf generate
```

## CLI Commands

### `agentconf init`

Creates the `agent-conf/` directory structure in the current repo:

```
agent-conf/
  agent-conf.yaml       # Configuration
  rules/
    my-rule.md           # Your canonical rules
  commands/
    my-command.md        # Slash-command definitions
```

### `agentconf generate`

Reads `agent-conf/agent-conf.yaml` and canonical rules, produces tool-specific output files. Generated files are placed alongside `agent-conf/` in a `.generated-agent-conf/` directory, then copied to the locations each tool expects.

Example: with `agents: [claude, cursor]`, running `agentconf generate` produces:
- `CLAUDE.md` at the repo root
- `.cursor/rules/*.mdc` files

### `agentconf sync`

Pulls shared configurations from remote git repositories into your local `agent-conf/` directory.

```bash
# Sync from a public rules repo
agentconf sync https://github.com/agenture-org/agent-conf-community

# Sync from an org-private repo
agentconf sync git@github.com:my-org/agent-conf-shared.git
```

## Configuration: `agent-conf.yaml`

```yaml
# Which tools to generate configs for
agents: [claude, cursor]

# How many directory levels deep to generate nested configs
nested_depth: 2

# Add generated files to .gitignore
gitignore: true
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `agents` | list | `[claude]` | Target tools: `claude`, `cursor` |
| `nested_depth` | int | `1` | Directory depth for nested config generation |
| `gitignore` | bool | `true` | Auto-add generated files to `.gitignore` |

## Canonical Rule Format

Rules are markdown files with a YAML frontmatter header, stored in `agent-conf/rules/`.

```markdown
---
description: Short description of what this rule does
alwaysApply: true
---

# Rule Title

Your rule content in markdown.
```

### Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | string | yes | One-line summary, used by tools that support rule metadata |
| `alwaysApply` | bool | no | If `true`, rule is always active (default: `false`) |
| `globs` | list | no | File patterns that trigger this rule (e.g., `["*.py", "tests/**"]`) |

### Commands

Commands are markdown files in `agent-conf/commands/` that define slash-command workflows for agents. Same format as rules.

## Example

Given this structure:

```
my-project/
  agent-conf/
    agent-conf.yaml
    rules/
      code-style.md
      testing.md
    commands/
      review.md
```

With `agent-conf.yaml`:
```yaml
agents: [claude, cursor]
nested_depth: 1
gitignore: true
```

Running `agentconf generate` produces:

```
my-project/
  CLAUDE.md                          # Combined rules for Claude Code
  .cursor/
    rules/
      code-style.mdc                 # Individual rule files for Cursor
      testing.mdc
  .gitignore                         # Updated with generated file paths
```
