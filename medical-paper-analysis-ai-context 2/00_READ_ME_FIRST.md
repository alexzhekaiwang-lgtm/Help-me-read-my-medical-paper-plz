# Medical Paper Analysis AI Context

## Purpose

This is the AI entry point. `README.md` is human-facing project orientation and is not governing analysis context.

## Authority And Precedence

1. Read `custom_gpt/core_instructions.md` completely. It governs behavior, grounding, safety, and output.
2. Use the user's request to select the task scope within those rules.
3. Use only the relevant knowledge modules below; they refine rather than override the core.
4. Treat `sample_output/uPAR_CAR_T_whole_paper_analysis_sample.md` only as a format and rigor example. The supplied paper and its supplements are the primary sources for the new analysis.

## Task Routing

- **Whole paper:** use `knowledge/01_paper_analysis_workflow.md`, `knowledge/07_figure_table_analysis.md`, and `knowledge/09_reference_tracing_strategy.md`. Add `knowledge/02_study_design_router.md` when the design is unclear. Add a module from `knowledge/03` through `knowledge/06` when one applies; otherwise use the design-specific checks in the core/router. Use `knowledge/08_methods_statistics_glossary.md` when statistical interpretation needs support.
- **Figure or article table:** use `knowledge/07_figure_table_analysis.md`; add `knowledge/08_methods_statistics_glossary.md` for statistical interpretation.
- **Methods or statistics:** use `knowledge/08_methods_statistics_glossary.md`; add `knowledge/07_figure_table_analysis.md` when interpreting a plotted result.
- **Reference or citation tracing:** use `knowledge/09_reference_tracing_strategy.md`.
- **Focused design appraisal:** use `knowledge/02_study_design_router.md` and a module from `knowledge/03` through `knowledge/06` when one applies; otherwise use the design-specific checks in the core/router.
- **Requested output format:** use `knowledge/10_output_templates.md`.
- **Final quality check:** use `knowledge/11_common_failure_modes.md`.
- **Abstract only:** the core is sufficient; state that conclusions are provisional because the full evidence is unavailable.

Review the worked sample only when a concrete depth or formatting example is useful. Do not load unrelated design modules merely because they are present.
