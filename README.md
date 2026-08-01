# Read Medical Paper

An installable Agent Skill for rigorous, reference-aware appraisal of one biomedical or medical research paper.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-2563eb)

The skill starts from the evidence rather than the abstract's framing. It identifies the true experimental unit, audits claim-bearing figures and tables, checks methods and statistics, separates prior knowledge from new results, and shows where an inference outruns the data.

> **Repository layout note:** On the current `main` branch, the project files are stored inside `help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/`. The file links and commands below use that live path.

[Install](#install) · [Use](#use) · [What it checks](#what-it-checks) · [Worked example](#worked-example) · [Repository structure](#repository-structure)

## Install

The distributable skill is the [`read-medical-paper/`](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/tree/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/read-medical-paper) directory. Its entry point is [`SKILL.md`](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/read-medical-paper/SKILL.md). Install that directory, not the repository root.

### Codex user installation

After cloning this repository, copy the skill into the shared Agent Skills directory:

```sh
git clone https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz.git
cd Help-me-read-my-medical-paper-plz
mkdir -p ~/.agents/skills
cp -R help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/read-medical-paper ~/.agents/skills/
```

Codex detects skill changes automatically. If the skill does not appear, restart Codex and open a new task.

### Repository-scoped installation

To make the skill available only inside another repository, copy it to:

```text
<your-project>/.agents/skills/read-medical-paper/
```

The core format follows the [Agent Skills specification](https://agentskills.io/specification). The optional [`agents/openai.yaml`](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/read-medical-paper/agents/openai.yaml) supplies Codex interface metadata; hosts that implement only the portable core can ignore it.

## Use

Attach or identify a paper, then ask naturally or invoke the skill explicitly:

```text
Use $read-medical-paper to critically analyze this paper as a whole.
Audit Figure 3 against the caption, Results, Methods, and supplement.
Check whether the statistics support the paper's primary claim.
Explain this abstract and tell me what cannot be judged without the full text.
Trace the evidence behind the authors' safety claim.
```

The skill is designed for a single target paper. Use a literature-review workflow for a multi-paper systematic search or field-wide synthesis. It is not for personal diagnosis, treatment selection, dosing, prognosis, or changes to medical care.

## What it checks

- What the paper directly reports versus what the authors infer.
- What was already established, inherited, reused, newly shown, or unsupported.
- Study-design-specific risks of bias.
- Biological `n`, experimental units, technical replicates, pairing, clustering, nesting, and repeated measures.
- Claim-bearing main-figure panels, tables, captions, corresponding Results text, Methods, statistics, controls, and supplementary dependencies.
- Effect direction and magnitude, uncertainty, multiplicity, model fit, practical importance, and internal inconsistencies.
- The inference ladder from observation to association, mechanism, translation, and clinical implication.
- Missing or unreadable evidence, without filling gaps with plausible details.
- Prompt-like text embedded in papers or supplements, which is treated as untrusted content rather than instructions.

Detailed appraisal rules are in the skill's [`references/`](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/tree/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/read-medical-paper/references) directory.

## Worked example

The companion [uPAR CAR T whole-paper analysis](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/examples/upar-car-t-worked-example.md) demonstrates the intended rigor:

- a selective backward citation trace and inherited-versus-new ledger;
- plain-language orientation followed by technical appraisal;
- seven integrated figure tables covering all 60 source-panel crops;
- explicit treatment of biological replicates, units, controls, statistics, and nesting;
- figure-level verdicts and a paper-level claim-to-data audit;
- calibrated separation of strong preclinical evidence from unproven clinical claims.

The example is a format and rigor reference, not a factual source for other papers. Its [60 panel crops](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/tree/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/examples/upar-car-t-panels) are companion assets and are intentionally excluded from the installable skill. See [asset provenance and licensing](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/ASSET_PROVENANCE.md).

## Repository structure

The current `main` branch is arranged as follows:

```text
.
├── LICENSE
├── README.md
├── WORKED_EXAMPLE.md                 # legacy root copy
└── help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/
    ├── ASSET_PROVENANCE.md
    ├── LICENSE
    ├── README.md
    ├── read-medical-paper/
    │   ├── SKILL.md
    │   ├── agents/
    │   │   └── openai.yaml
    │   └── references/
    ├── examples/
    │   ├── upar-car-t-worked-example.md
    │   └── upar-car-t-panels/
    ├── evals/
    └── scripts/
        └── validate_repository.py
```

The [`SKILL.md`](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/read-medical-paper/SKILL.md) file is the concise router and workflow. Detailed domain guidance is one link away in `references/`, so hosts can load only what a request needs. The large example, evaluation fixture, and repository validator sit outside the installable boundary.

## Validate

From the cloned repository root, run:

```sh
python3 help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/scripts/validate_repository.py
```

The [validator](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/scripts/validate_repository.py) checks the skill name and metadata, local Markdown links, exact example-image coverage, asset uniqueness, stale paths, evaluation inventory, and documented package boundary.

When installed, the skill can also be checked with:

```sh
skills-ref validate ~/.agents/skills/read-medical-paper
```

## Scope and limitations

- This project supplies instructions and examples; it does not include a model, retrieval service, PDF parser, or user interface.
- Reference verification requires source access and, in some environments, internet or database tools.
- Abstract-only and incomplete-source reviews are explicitly provisional.
- AI analysis can contain errors. Check important scientific or clinical judgments against the original sources and appropriate domain expertise.

## Contributing

Issues and pull requests are welcome for improved study-design guidance, stronger figure/statistics checks, evaluation cases, corrections to the worked example, and clearer instructions that preserve the evidence standards.

Keep repository development material outside `read-medical-paper/`, avoid host-specific commands in the portable workflow, and do not add generated test reports or temporary artifacts.

## License

Original project instructions, documentation, and validation code are licensed under the [MIT License](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/LICENSE). The 60 worked-example panel crops are adapted from a separately licensed publication and are not relicensed under MIT; see [`ASSET_PROVENANCE.md`](https://github.com/alexzhekaiwang-lgtm/Help-me-read-my-medical-paper-plz/blob/main/help-me-read-my-medical-paper-plz-skill-refactor-5cb7e94/ASSET_PROVENANCE.md).
