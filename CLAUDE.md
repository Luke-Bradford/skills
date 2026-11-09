# Skills

General-purpose skills for coding agents. Plain Markdown; see `README.md`.

## Rules for this repo

- A skill names no project, product or stack. If an example needs one, invent a neutral one.
- A rule that cites a number or a source must be checked against that source before it is written.
- `SKILL.md` says when to use the skill and holds the method. Detail goes in `references/`.
- Text a person reads follows `skills/plain-talk/SKILL.md`.
- Every change goes through a pull request. Bump the version in both files under `.claude-plugin/` when a skill's guidance changes.

## Checks

`python3 scripts/check_skills.py` must pass. CI runs the same check.

## Mission Control

How a Mission Control crew treats this repo's board. Seats pick from Ready, highest Priority first.

```yaml
mc:
  pick_from: [Ready]
  promote_backlog: true
  needs: [done_when, size]
  checks: ["python3 scripts/check_skills.py"]
  templates:
    "documentation": small-change
    "enhancement": feature
  areas:
    "area:skills": ["skills/**"]
    "area:repo": ["scripts/**", ".github/**", "README.md", ".claude-plugin/**"]
  hard_rules:
    - "CLAUDE.md"
    - ".github/**"
  ci: null
  always_ask: []
```
