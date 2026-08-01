# Whole-Paper Workflow

Use this sequence for a complete biomedical-paper analysis, journal-club preparation, an abstract-versus-data check, or an independent evidence audit.

## Establish Scope And Availability

1. Record only the citation metadata visible in the supplied paper or in a source you actually opened.
2. Inventory the available abstract, full text, figures, tables, Methods, supplements, protocols, and cited sources.
3. State important missing material and the resulting limits before making strong conclusions.
4. Treat the title, abstract, conclusion, and discussion as claim sources rather than proof.

## Build Background Before Judging Novelty

5. Apply [reference-tracing.md](reference-tracing.md) to the small set of load-bearing references.
6. Separate what prior work established, what this paper inherits or reuses, what it newly demonstrates, and what remains unsupported.
7. Define only the background concepts and jargon needed to follow the paper.
8. Keep the novelty and broader-significance judgment provisional when primary sources or publication-status checks are unavailable.

## Reconstruct The Study

9. State the research question and why it matters.
10. Classify the design with [study-design-routing.md](study-design-routing.md), then apply the relevant design-specific reference.
11. Identify the population or model, intervention or exposure, comparator, outcomes or readouts, timing, sample sizes, experimental units, and analysis sets.
12. Extract the major author claims, including claims made only in the abstract or discussion.

## Audit Evidence Before Accepting The Narrative

13. Read figures and claim-bearing article tables before accepting the prose summary.
14. Apply the integrated panel and article-table rules in [figures-and-tables.md](figures-and-tables.md) to every main figure and table.
15. Inspect claim-relevant supplementary material, null results, adverse-event tables, baseline tables, and sensitivity analyses. Reserve exhaustive supplement coverage for an explicit request.
16. Match each major claim to the relevant Results evidence and then to the Methods details needed to trust that evidence.
17. Apply [methods-and-statistics.md](methods-and-statistics.md) to effect sizes, uncertainty, multiplicity, transformations, missingness, unit structure, nesting, and model assumptions.
18. Record funding, conflicts of interest, sponsor role, protocol or analysis-plan deviations, and other design-specific threats when they could change interpretation.

## Triangulate Sections

For each major claim:

- Compare the abstract and discussion wording with the actual Results.
- Check whether the Methods can produce the claimed inference.
- Check whether figures, tables, supplements, or limitations qualify or contradict the headline.
- State any mismatch and prefer the data-supported version.
- Use `claim -> evidence -> limitation -> confidence`.

Classify evidence directness, transferability, logical sufficiency, independence, and confidence with the labels in [core-principles.md](core-principles.md). Identify the first unjustified step on the inference ladder.

When a claim is too strong, write:

- **Authors claim:**
- **Available data support:**
- **More defensible conclusion:**

## Test The Major Claims

Construct the visible claim-to-data matrix defined in [core-principles.md](core-principles.md). Put the decisive missing assumption, alternative explanation, bias, or dependence on redundant evidence in `weakest link`.

Ask whether:

- Several panels are genuinely orthogonal or repeat the same model, assay, proxy, bias, or missing control.
- A causal claim has temporality, specificity, adequate controls, and appropriate perturbation or adjustment.
- A mechanistic step is directly shown or inferred from a marker.
- A statistically detectable effect is biologically or clinically meaningful.
- The study supports transfer from the tested model or population to the stated target.

## Recheck Status And Deliver

19. When lookup tools are available and the question warrants it, check later versions, forward citations, corrections, retractions, expressions of concern, and materially contradictory evidence.
20. Deliver the answer using the applicable structure in [output-contracts.md](output-contracts.md).
21. Run the final scan in [quality-and-failure-checks.md](quality-and-failure-checks.md).

## Avoid These Shortcuts

- Do not let the abstract decide the verdict.
- Do not treat a cited source, same-team companion paper, reused dataset, or inherited model as independent validation.
- Do not mistake repeated weak evidence for convergence.
- Do not call a model, method, dataset, signature, or therapeutic result new when the paper inherited it.
- Do not omit negative, supplementary, underpowered, or contradictory evidence that bears on a headline claim.
- Do not equate correlation with causation or statistical significance with importance.
