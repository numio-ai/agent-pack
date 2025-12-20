# agent-conf

A tools to manage agents configuration.


**1. What problem does it solve?**

Managing AI agent configurations across multiple tools (Claude Code, Cursor, etc.) is a fragmented mess. Each tool has its own config format — `CLAUDE.md`, `.cursor/rules/`, `AGENTS.md` — and teams end up duplicating, drifting, and losing track of rules across repos and tools. The pain is compounded in monorepos with submodules, multi-tool teams, and enterprise environments where you need consistent AI behavior at global, org, project, repo, and user levels. There's no single source of truth.

**2. What does the CLI do?**

It's an AI agent configuration manager. Core workflows:
- **Init**: Bootstrap the `agent-conf/` directory structure in a new repo
- **Generate**: Transform vendor-neutral canonical rulesets (YAML + markdown in `agent-conf/`) into tool-specific outputs (`.agent-conf/` → `CLAUDE.md`, `.cursor/rules/`, etc.)
- **Sync**: Pull shared agent-conf from remote git repos (a public general-purpose agent-conf repo, plus org-private ones)
- **Hierarchical inheritance**: Resolve agent-conf across global → org → project → repo → user levels, controlled via `agent-conf.yaml` (specifying target agents, `nested_depth`, etc.)

**3. Target users**

- **Individual developers** managing AI agent configs across Cursor + Claude Code
- **Teams** needing consistent AI agent behavior across a shared codebase, especially monorepos with submodules
- **Enterprise environments** wanting top-down governance of AI agent behavior with hierarchical overrides

**4. Language/runtime**

**Python**, using `uv tool install` for distribution.

**5. Additional context**

- The tool is rooted in the concept of a **"Agent Configuration"** — a vendor-neutral canonical format that compiles to multiple targets, analogous to how `rustc`/`tsc` compile source to different outputs. This compilation model is what distinguishes it from simpler sync tools like `rulesync`.
- It already exists in prototype form in your `agenture-root` repo with the `agent-conf/` directory structure, `agent-conf.yaml`, and generated outputs.
- Your startup is **Agenture** (`agenture.org`), and the tool serves as both an internal necessity and a potential product.
- A key unsolved friction: developers naturally edit tool-specific files (like `CLAUDE.md`) directly during coding, and those changes need to propagate **back** to the canonical agent configurations — a reverse-sync problem.
- The public repo would host general-purpose, community-contributed agent configurations, while orgs maintain private agent configurations.


## Contributing

Contributions are welcome.


---

Maintained by the Agenture team.
