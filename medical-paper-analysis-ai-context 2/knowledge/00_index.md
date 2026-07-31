# Knowledge Index

## Purpose

Map the task-specific modules that refine `custom_gpt/core_instructions.md`, the governing analysis rules. On platforms with a system or custom-instruction field, place the core there; otherwise provide it as the highest-priority context.

## When To Use

Use this index when deciding which reference file should help answer a paper-reading question.

## Available Modules

The full folder may be supplied, but the AI should read only the modules relevant to the request:

- `00_index.md`: map of the knowledge package.
- `01_paper_analysis_workflow.md`: whole-paper reading workflow and claim-evidence-limitation-confidence framing.
- `02_study_design_router.md`: decision tree for paper type and appraisal framework.
- `03_clinical_trial_appraisal.md`: randomized, nonrandomized, and single-arm interventional trials.
- `04_observational_study_appraisal.md`: cohort, case-control, and cross-sectional appraisal.
- `05_systematic_review_meta_analysis.md`: PRISMA-style review and meta-analysis appraisal.
- `06_basic_science_mechanistic_appraisal.md`: mechanistic and basic-science appraisal.
- `07_figure_table_analysis.md`: integrated figure-panel and article-table auditing.
- `08_methods_statistics_glossary.md`: short explanations of common methods and statistics.
- `09_reference_tracing_strategy.md`: building a selective reference-derived knowledge base and tracing citations.
- `10_output_templates.md`: reusable response templates.
- `11_common_failure_modes.md`: common errors to avoid.

## Core Checklist

- Begin with `00_READ_ME_FIRST.md`; it defines authority and routing.
- For a whole paper, use `01`, `07`, and `09`; use `02` when the design is unclear. Add a module from `03`–`06` when one applies; otherwise use the design-specific checks in the core/router.
- Add `08` for detailed statistics, `10` for a requested format, and `11` for final quality control.
- Focused questions need only the core plus the relevant module(s).

## Minimal Example

For “Is this noninferiority trial convincing?”, use `02_study_design_router.md`, `03_clinical_trial_appraisal.md`, and `07_figure_table_analysis.md`.
