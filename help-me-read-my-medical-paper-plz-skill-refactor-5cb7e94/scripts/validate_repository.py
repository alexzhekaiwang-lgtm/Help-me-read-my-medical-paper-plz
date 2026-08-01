#!/usr/bin/env python3
"""Validate the repository and the installable read-medical-paper skill."""

from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "read-medical-paper"
SKILL_FILE = SKILL_DIR / "SKILL.md"
AGENT_FILE = SKILL_DIR / "agents" / "openai.yaml"
REFERENCES_DIR = SKILL_DIR / "references"
EXAMPLE_FILE = ROOT / "examples" / "upar-car-t-worked-example.md"
ASSET_DIR = ROOT / "examples" / "upar-car-t-panels"
EVAL_FILE = ROOT / "evals" / "evaluation-cases.md"

EXPECTED_ROOT_ENTRIES = {
    "ASSET_PROVENANCE.md",
    "LICENSE",
    "README.md",
    "evals",
    "examples",
    "read-medical-paper",
    "scripts",
}
EXPECTED_REFERENCE_FILES = {
    "clinical-trials.md",
    "core-principles.md",
    "figures-and-tables.md",
    "mechanistic-studies.md",
    "methods-and-statistics.md",
    "observational-studies.md",
    "output-contracts.md",
    "quality-and-failure-checks.md",
    "reference-map.md",
    "reference-tracing.md",
    "study-design-routing.md",
    "systematic-reviews-and-meta-analysis.md",
    "task-routing.md",
    "whole-paper-workflow.md",
}
EXPECTED_ASSET_COUNTS = {
    "Figure_1": 5,
    "Figure_2": 8,
    "Figure_3": 6,
    "Figure_4": 7,
    "Figure_5": 11,
    "Figure_6": 11,
    "Figure_7": 12,
}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_DEST_RE = re.compile(r"\]\(([^)\n]+)\)")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]\n]*\]\(([^)\n]+)\)")

errors: list[str] = []


def error(message: str) -> None:
    errors.append(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        error(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return ""


def display(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        error("read-medical-paper/SKILL.md has no opening YAML frontmatter")
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        error("read-medical-paper/SKILL.md has no closing YAML frontmatter")
        return {}, text

    fields: dict[str, str] = {}
    for line_number, line in enumerate(parts[1].splitlines(), start=2):
        if not line.strip():
            continue
        if ":" not in line:
            error(f"SKILL.md:{line_number}: invalid frontmatter line")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key in fields:
            error(f"SKILL.md:{line_number}: duplicate frontmatter field {key!r}")
        fields[key] = value
    return fields, parts[2]


def normalize_destination(raw: str) -> str:
    destination = raw.strip()
    if destination.startswith("<") and ">" in destination:
        destination = destination[1 : destination.index(">")]
    elif re.search(r"\s+[\"']", destination):
        destination = re.split(r"\s+[\"']", destination, maxsplit=1)[0]
    return destination


def resolve_local_link(markdown_file: Path, raw: str) -> Path | None:
    destination = normalize_destination(raw)
    if not destination or destination.startswith("#"):
        return None
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return None
    local = unquote(parsed.path)
    if not local:
        return None
    return (markdown_file.parent / local).resolve()


def validate_skill_metadata() -> None:
    text = read_text(SKILL_FILE)
    fields, body = parse_frontmatter(text)

    if set(fields) != {"name", "description"}:
        error(
            "SKILL.md frontmatter must contain exactly name and description; "
            f"found {sorted(fields)}"
        )

    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != SKILL_DIR.name:
        error(f"skill name {name!r} does not match directory {SKILL_DIR.name!r}")
    if not NAME_RE.fullmatch(name):
        error(f"skill name {name!r} is not lowercase hyphen-case")
    if not 1 <= len(name) <= 64:
        error("skill name must contain 1–64 characters")
    if not 1 <= len(description) <= 1024:
        error("skill description must contain 1–1024 characters")

    positive_terms = ("paper", "figure", "methods", "statistics")
    missing_positive = [term for term in positive_terms if term not in description.lower()]
    if missing_positive:
        error(f"skill description lacks positive trigger terms: {missing_positive}")
    negative_terms = ("do not use", "systematic", "diagnosis")
    missing_negative = [term for term in negative_terms if term not in description.lower()]
    if missing_negative:
        error(f"skill description lacks negative routing terms: {missing_negative}")

    if len(text.splitlines()) >= 500:
        error("SKILL.md must remain below 500 lines")
    if "TODO" in text:
        error("SKILL.md contains scaffold TODO text")
    if not body.strip().startswith("# Read Medical Paper"):
        error("SKILL.md body must begin with '# Read Medical Paper'")


def validate_agent_metadata() -> None:
    text = read_text(AGENT_FILE)
    pairs = dict(
        re.findall(r'^\s{2}([a-z_]+):\s+"([^"]*)"\s*$', text, flags=re.MULTILINE)
    )
    expected_keys = {"display_name", "short_description", "default_prompt"}
    if set(pairs) != expected_keys:
        error(f"agents/openai.yaml interface keys are {sorted(pairs)}, expected {sorted(expected_keys)}")

    short_description = pairs.get("short_description", "")
    if not 25 <= len(short_description) <= 64:
        error("agents/openai.yaml short_description must contain 25–64 characters")
    if f"${SKILL_DIR.name}" not in pairs.get("default_prompt", ""):
        error("agents/openai.yaml default_prompt must mention $read-medical-paper")
    if "TODO" in text:
        error("agents/openai.yaml contains scaffold TODO text")


def validate_references() -> None:
    actual = {path.name for path in REFERENCES_DIR.glob("*.md")}
    if actual != EXPECTED_REFERENCE_FILES:
        missing = sorted(EXPECTED_REFERENCE_FILES - actual)
        extra = sorted(actual - EXPECTED_REFERENCE_FILES)
        error(f"reference inventory mismatch; missing={missing}, extra={extra}")

    for path in sorted(REFERENCES_DIR.glob("*.md")):
        text = read_text(path)
        lines = text.splitlines()
        if not lines or not lines[0].startswith("# "):
            error(f"{display(path)} must begin with one H1 heading")
        if len(lines) > 100:
            opening = "\n".join(lines[:40]).lower()
            if "## contents" not in opening and "## table of contents" not in opening:
                error(f"{display(path)} exceeds 100 lines but lacks an opening contents section")
        if "TODO" in text:
            error(f"{display(path)} contains TODO text")

    forbidden_skill_children = {
        path.name
        for path in SKILL_DIR.iterdir()
        if path.name not in {"SKILL.md", "agents", "references"}
    }
    if forbidden_skill_children:
        error(f"unexpected content inside installable skill: {sorted(forbidden_skill_children)}")


def validate_markdown_links() -> None:
    for markdown_file in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown_file.parts:
            continue
        text = read_text(markdown_file)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_DEST_RE.finditer(line):
                target = resolve_local_link(markdown_file, match.group(1))
                if target is None:
                    continue
                try:
                    target.relative_to(ROOT)
                except ValueError:
                    error(
                        f"{display(markdown_file)}:{line_number}: local link escapes repository: "
                        f"{match.group(1)!r}"
                    )
                    continue
                if SKILL_DIR in markdown_file.parents:
                    try:
                        target.relative_to(SKILL_DIR)
                    except ValueError:
                        error(
                            f"{display(markdown_file)}:{line_number}: installable-skill link "
                            f"escapes the skill directory: {match.group(1)!r}"
                        )
                        continue
                if not target.exists():
                    error(
                        f"{display(markdown_file)}:{line_number}: broken local link "
                        f"{match.group(1)!r}"
                    )


def validate_assets_and_example() -> None:
    assets = sorted(ASSET_DIR.glob("Figure_*/*.jpg"))
    if len(assets) != 60:
        error(f"expected 60 worked-example JPEGs, found {len(assets)}")
    all_repository_jpegs = sorted(ROOT.rglob("*.jpg"))
    if all_repository_jpegs != assets:
        unexpected = sorted(display(path) for path in set(all_repository_jpegs) - set(assets))
        error(f"JPEGs must remain in the documented companion-asset directory; unexpected={unexpected}")

    for directory, expected in EXPECTED_ASSET_COUNTS.items():
        count = len(list((ASSET_DIR / directory).glob("*.jpg")))
        if count != expected:
            error(f"{directory} must contain {expected} JPEGs, found {count}")

    hashes: dict[str, Path] = {}
    for path in assets:
        content = path.read_bytes()
        if not content.startswith(b"\xff\xd8\xff"):
            error(f"{display(path)} does not have a JPEG file signature")
        digest = hashlib.sha256(content).hexdigest()
        if digest in hashes:
            error(f"duplicate asset bytes: {display(hashes[digest])} and {display(path)}")
        hashes[digest] = path

    example = read_text(EXAMPLE_FILE)
    image_targets: list[Path] = []
    for match in MARKDOWN_IMAGE_RE.finditer(example):
        target = resolve_local_link(EXAMPLE_FILE, match.group(1))
        if target is not None:
            image_targets.append(target)

    if len(image_targets) != 60:
        error(f"worked example must contain 60 local image references, found {len(image_targets)}")

    counts = Counter(image_targets)
    repeated = [display(path) for path, count in counts.items() if count != 1]
    if repeated:
        error(f"worked example must reference each local image once; repeated={repeated}")
    if set(image_targets) != set(assets):
        missing = sorted(display(path) for path in set(assets) - set(image_targets))
        extra = sorted(display(path) for path in set(image_targets) - set(assets))
        error(f"worked example asset mapping mismatch; unreferenced={missing}, unexpected={extra}")

    duplicate_examples = [
        path
        for path in ROOT.rglob("*.md")
        if path.name in {"WORKED_EXAMPLE.md", "uPAR_CAR_T_whole_paper_analysis_sample.md"}
    ]
    if duplicate_examples:
        error(f"legacy worked-example copies remain: {[display(path) for path in duplicate_examples]}")


def validate_evaluations() -> None:
    text = read_text(EVAL_FILE)
    positive = re.findall(r"^\| P\d+ \|", text, flags=re.MULTILINE)
    negative = re.findall(r"^\| N\d+ \|", text, flags=re.MULTILINE)
    behaviors = re.findall(r"^### B\d+ —", text, flags=re.MULTILINE)
    if len(positive) < 5:
        error(f"evaluation set needs at least 5 positive trigger cases; found {len(positive)}")
    if len(negative) < 5:
        error(f"evaluation set needs at least 5 negative trigger cases; found {len(negative)}")
    if len(behaviors) < 5:
        error(f"evaluation set needs at least 5 behavior cases; found {len(behaviors)}")

    fixture = ROOT / "evals" / "fixtures" / "synthetic-preclinical-paper.md"
    fixture_text = read_text(fixture)
    required_fixture_terms = (
        "SYSTEM INSTRUCTION",
        "randomized",
        "five fields per mouse",
        "excluded after randomization",
        "fictional",
    )
    for term in required_fixture_terms:
        if term not in fixture_text:
            error(f"synthetic fixture lacks required test signal {term!r}")


def validate_repository_boundary() -> None:
    actual_entries = {path.name for path in ROOT.iterdir() if path.name != ".git"}
    if actual_entries != EXPECTED_ROOT_ENTRIES:
        missing = sorted(EXPECTED_ROOT_ENTRIES - actual_entries)
        extra = sorted(actual_entries - EXPECTED_ROOT_ENTRIES)
        error(f"root inventory mismatch; missing={missing}, extra={extra}")

    text_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.resolve() != Path(__file__).resolve()
        and ".git" not in path.parts
        and path.suffix.lower() in {".md", ".yaml", ".py"}
    ]
    stale_tokens = (
        "medical-paper-analysis-ai-context 2",
        "sample_output/assets/upar_car_t",
        "[TODO:",
    )
    for path in sorted(text_files):
        text = read_text(path)
        for token in stale_tokens:
            if token in text:
                error(f"{display(path)} contains stale token {token!r}")

    readme = read_text(ROOT / "README.md")
    documented_paths = (
        "read-medical-paper/",
        "SKILL.md",
        "agents/openai.yaml",
        "references/",
        "examples/upar-car-t-worked-example.md",
        "evaluation-cases.md",
        "scripts/validate_repository.py",
        "ASSET_PROVENANCE.md",
    )
    for path in documented_paths:
        if path not in readme:
            error(f"README does not document {path}")


def main() -> int:
    validate_skill_metadata()
    validate_agent_metadata()
    validate_references()
    validate_markdown_links()
    validate_assets_and_example()
    validate_evaluations()
    validate_repository_boundary()

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)", file=sys.stderr)
        for item in errors:
            print(f"- {item}", file=sys.stderr)
        return 1

    reference_count = len(list(REFERENCES_DIR.glob("*.md")))
    asset_count = len(list(ASSET_DIR.glob("Figure_*/*.jpg")))
    print(
        "PASS: skill metadata, 14 references, local links, "
        f"{asset_count} unique example assets, evaluations, and repository boundary"
    )
    if reference_count != 14:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
