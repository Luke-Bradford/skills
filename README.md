# Skills

General-purpose skills for coding agents. Each one is plain Markdown: a short `SKILL.md` that says when
to use it and what to do, with reference files the agent reads only when a step needs them. Nothing here
is tied to one project, stack or client.

| Skill | Use it when |
| --- | --- |
| [designing-dashboards](skills/designing-dashboards/SKILL.md) | Planning, building or reviewing a dashboard, KPI or metrics page, report, status board, admin panel or operations console |
| [plain-talk](skills/plain-talk/SKILL.md) | Writing anything a person will read and act on: an update, a question, an error, a ticket, a pull request description |

## Install

**Claude Code, as a plugin** (available in every project):

```text
/plugin marketplace add Luke-Bradford/skills
/plugin install common@luke-bradford
```

**Any agent that reads skill folders** (Claude Code, Codex and others): copy a folder from `skills/` into
the project's skills directory, for example `.claude/skills/`, or into your personal one, for example
`~/.claude/skills/`.

## How the skills are written

- **Grounded.** Rules come from published research, standards and design-system guidance. Each skill
  lists its sources and which rule each one supports. Where a number is our own working default, the
  skill says so.
- **Short at the top, deep underneath.** `SKILL.md` is the method and the rules that always hold. Detail
  sits in `references/`, one file per step, so an agent loads only what the task needs.
- **Tried against a baseline.** The aim for each skill and each change is to run one real task with and
  without it and compare the results, then cut guidance that changes nothing. So far
  `designing-dashboards` has had one such run; `plain-talk` comes from daily use in one project.
- **Yours wins.** A project's own design system or style guide outranks these defaults, and the reader's
  stated wishes outrank both.

## Contributing

Issues and pull requests are welcome. For a change to a rule, say what went wrong without it and cite a
source where one exists. Keep skills free of project names, product names and stack-specific code.

## Licence

[MIT](LICENSE).
