"""Checks every skill in skills/: front matter, size, and that relative links resolve.

Run from the repo root: python3 scripts/check_skills.py
Exits 1 and lists every problem if any check fails.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
MAX_SKILL_WORDS = 1200  # SKILL.md is read on every use; detail belongs in references/
problems: list[str] = []


def front_matter(path: pathlib.Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        problems.append(f"{path.relative_to(ROOT)}: no front matter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        problems.append(f"{path.relative_to(ROOT)}: front matter is not closed")
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def check_links(path: pathlib.Path) -> None:
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        file = (path.parent / target.split("#")[0]).resolve()
        if not file.exists():
            problems.append(f"{path.relative_to(ROOT)}: link to missing file {target}")


skill_dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
if not skill_dirs:
    problems.append("skills/: no skills found")
for folder in skill_dirs:
    skill = folder / "SKILL.md"
    if not skill.exists():
        problems.append(f"{folder.relative_to(ROOT)}: no SKILL.md")
        continue
    fields = front_matter(skill)
    name, description = fields.get("name", ""), fields.get("description", "")
    if name != folder.name:
        problems.append(f"{skill.relative_to(ROOT)}: name '{name}' does not match its folder")
    if not NAME.match(name):
        problems.append(f"{skill.relative_to(ROOT)}: name must be lower-case words joined by hyphens")
    if not description.lower().startswith("use "):
        problems.append(f"{skill.relative_to(ROOT)}: description must say when to use the skill, starting 'Use when' or 'Use before'")
    if len(description) > 1024:
        problems.append(f"{skill.relative_to(ROOT)}: description is over 1024 characters")
    words = len(skill.read_text(encoding="utf-8").split())
    if words > MAX_SKILL_WORDS:
        problems.append(f"{skill.relative_to(ROOT)}: {words} words; keep SKILL.md under {MAX_SKILL_WORDS} and move detail to references/")
    for doc in folder.rglob("*.md"):
        check_links(doc)

plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
listed = sorted(pathlib.PurePosixPath(p).name for p in plugin.get("skills", []))
if listed != [d.name for d in skill_dirs]:
    problems.append(f".claude-plugin/plugin.json: skills listed {listed} do not match folders {[d.name for d in skill_dirs]}")
market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
if market["plugins"][0]["version"] != plugin["version"]:
    problems.append(".claude-plugin: plugin.json and marketplace.json versions differ")
check_links(ROOT / "README.md")

for problem in problems:
    print(problem)
print(f"{len(skill_dirs)} skills checked, {len(problems)} problems")
sys.exit(1 if problems else 0)
