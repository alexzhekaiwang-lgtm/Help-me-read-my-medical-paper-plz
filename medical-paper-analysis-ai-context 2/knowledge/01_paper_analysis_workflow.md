# Whole-Paper Analysis Workflow

## Purpose

Provide a compact workflow for reading an entire biomedical or medical paper, including independent claim-to-data auditing.

## When To Use

Use for whole-paper analysis, journal club preparation, abstract-to-data checks, independent evidence audits, or when the user asks what a paper really shows.

## Core Checklist

1. Identify the citation details available in the uploaded paper without inventing missing metadata.
2. Read title, abstract, and conclusion as claims, not proof.
3. Identify the load-bearing references for the mechanism, inherited method/model/dataset, prior evidence, context, and an important contradiction or limitation.
4. Retrieve and verify those primary sources when tools allow; build the reference-derived knowledge ledger in `09_reference_tracing_strategy.md`.
5. Separate what was already established, what this paper inherits, and what this paper newly demonstrates.
6. State the research question and why it matters.
7. Define required background concepts and jargon from the verified knowledge base.
8. Route the paper by study design.
9. Extract the main claims.
10. Read figures and article tables before accepting the narrative. Audit main figures panel by panel using the integrated schema in `07_figure_table_analysis.md`; report relevant supplement dependencies and add supplementary-panel rows only when directly analyzed or requested exhaustively. Audit article tables at the claim-bearing row/result-block level.
11. Check methods and statistics against the claims.
12. Inspect limitations, conflicts of interest, funding, and claim-relevant supplementary material; reserve exhaustive supplementary review for an explicit request.
13. Check whether later versions, forward citations, contradictions, or status changes alter the interpretation.

## Reference-First Gate

Build the compact knowledge base from all supplied reference material before judging novelty or significance. Verify primary sources when lookup is available. If cited source text and lookup are unavailable, record what cannot be checked, treat the current paper's description as unverified rather than as a direct finding, and label the background and novelty assessment provisional.

For each load-bearing source, record:

`role -> direct finding -> use in current paper -> inherited versus new -> transfer risk/status`

Do not use the reference list as decoration. A cited source may support only a narrower claim than the current paper assigns to it, and a companion paper or reused dataset is not independent validation.

## Section Triangulation

- Treat title, abstract, and discussion as claim sources, not proof.
- Match each major claim to the Results figure/table, then to the Methods details needed to trust it.
- Check whether supplements, limitations, adverse-event tables, null results, or subgroup notes weaken the headline story.
- If sections disagree, state the mismatch and use the data-supported version.

Use this frame for each important claim:

`claim -> evidence -> limitation -> confidence`

For an Independent Evidence Audit, use the canonical matrix from the core. Its weakest-link field should capture the decisive missing assumption, alternative explanation, or dependence on redundant evidence.

Directness labels:

- Direct: measures the claim closely.
- Proxy: measures an indirect marker.
- Correlative: shows association, not causation.
- Surrogate: endpoint is not the final biological/clinical outcome.

Transferability modifier:

- Model-limited: model-system support may not transfer to the target context.

Independence labels:

- Redundant: repeats the same assay, model, readout, or bias.
- Partially independent: adds a readout but shares key assumptions.
- Orthogonal: uses a different method, model, or readout for the same claim.

Logical sufficiency labels: sufficient, partly sufficient, insufficient, contradicted, cannot assess.

Apply the core inference ladder and identify the first unjustified step.

When claims are too strong, rewrite them:

- Authors claim:
- Data support:
- More defensible conclusion:

## Common Pitfalls

- Letting the abstract decide the answer.
- Missing abstract/discussion claims that quietly outrun the Results or Methods.
- Ignoring negative, supplementary, or underpowered data.
- Treating correlation as causation.
- Treating statistically significant as clinically important.
- Parroting the discussion instead of asking what the data directly show.
- Mistaking repeated weak evidence for independent validation.

## Minimal Example

Synthetic claim: "Protein X drives tumor growth." Evidence may be knockdown data and rescue experiments. Limitations may include one cell line, weak rescue, or no animal/human validation. Confidence should reflect those limits.

More defensible wording might be: "In this model, Protein X appears to contribute to growth, but causal specificity and generalizability require stronger rescue or orthogonal validation."
