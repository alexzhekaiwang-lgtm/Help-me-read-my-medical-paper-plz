# Figure And Table Analysis

## Purpose

Read figures and article tables as primary evidence and keep source provenance beside the independent analysis.

## When To Use

Use for whole-paper analysis, figure- or table-specific questions, abstract-versus-data checks, and journal club preparation.

## Figure Scope And Row Structure

For each main figure, state its purpose and intended claim, then build one integrated panel-analysis table. Use one row per labeled panel; combine panels only when they form one inseparable experiment. If a compound panel contains several readouts, describe them together in that panel's row. Never create separate source-map, caption-map, article-text, and analysis tables.

Report material supplementary dependencies in the figure verdict or a nearby source note. Give a supplementary panel its own integrated row only when directly analyzing it or when the user requests exhaustive supplementary analysis.

Every panel row must keep these layers together:

- **Panel image:** use a content-preserving panel crop when accessible. Retain the panel label, axes, units, legends, gates, annotations, and scale bars; never retouch data. Link the original full figure. If extraction is impossible, show an explicit `Image unavailable` marker.
- **Figure legend:** clearly label a concise panel-specific caption paraphrase and give a locator such as `Figure 3, caption, panel D`. Do not substitute interpretation for the caption.
- **Corresponding article text:** clearly label a concise paraphrase of the most relevant Results passage and give its section plus paragraph/page locator. For load-bearing passages, add one brief key quotation when useful and quotation limits permit; when panels share that passage, quote it once and use shared-quotation references. Do not quote every row merely to fill the schema. If no direct passage exists, write `No panel-specific Results text identified`.
- **Detailed analysis:** keep design, result, inferential role, and limitations in that same row. Report mismatches among the visual data, legend, Results narrative, and Methods.

Use this canonical schema:

| Panel | Panel image | Figure legend (paraphrase + locator) | Corresponding article text (paraphrase + locator + key quote/shared reference when used) | Design/readout | Groups/controls, `n`/unit | Statistics/exact result | What it supports | Key limitation |
|---|---|---|---|---|---|---|---|---|

Use line breaks within a cell when needed; do not detach provenance from analysis.

## Panel Audit

For every row, determine:

- The question, setup, assay, model/specimen/data source, axes, units, groups, conditions, time points, and comparators.
- Positive, negative, vehicle, untreated, isotype, loading, batch, or other relevant controls.
- Nominal observations, true biological `n`, experimental unit, and whether observations are paired, repeated, clustered, or nested.
- Test/model, uncertainty display, exact readable effect/direction/interval/reported `p` value, multiplicity, normalization, transformation, exclusions, gating, thresholds, and preprocessing. Say when any item is unreadable or unreported.
- What is visually observed before interpretation; whether an image is representative, quantified, or both.
- What the panel supports, what it does not, and the most defensible panel-level conclusion.
- Missing controls, alternative explanations, Methods/Supplement dependencies, and whether the panel adds independent information.

When explicit labels improve clarity, keep these dimensions distinct:

- **Directness:** direct, proxy, correlative, or surrogate.
- **Transferability modifier:** model-limited.
- **Logical sufficiency:** sufficient, partly sufficient, insufficient, contradicted, or cannot assess.
- **Independence, when material:** redundant, partially independent, or orthogonal.

Do not infer exact values from low-resolution graphics.

## Integrated Figure Verdict

After the panel table, identify:

- A claim-support grade for each distinct claim: `strong`, `moderate`, `weak`, `contradicted`, or `cannot assess`; add `model-limited` when relevant.
- Strongest panel and why.
- Weakest inferential link.
- What the complete figure establishes and does not establish.
- Whether supplementary evidence resolves a missing control or repeats the same limitation.
- A more defensible figure-level conclusion.

## Article Table Audit

Do not force article tables into the image-panel schema. Audit each claim-bearing row or result block:

| Table/result block | Locator | Population, denominator, and unit | Comparison or estimate | Uncertainty, test, or model | What it supports | Key limitation |
|---|---|---|---|---|---|---|

Check row/column/footnote locators, missingness, adjusted versus unadjusted estimates, uncertainty, test/model assumptions, subgroup or multiplicity issues, and whether totals and denominators reconcile.

## Common Pitfalls

- Missing axis scales, units, normalization, gates, or truncated ranges.
- Treating technical repeats, cells, fields, images, sites, or repeated measures as independent biological replicates.
- Treating SEM as biological variability, a proxy marker as functional proof, or a representative image as quantified evidence.
- Accepting a cluster, embedding, heatmap, or caption assertion without validation in the underlying data.
- Reporting a figure-wide `n` when panels use different cohorts or units.
- Cropping away scientific context or repeatedly using a full multi-panel figure when panel crops are available.
- Copying long source passages, presenting a paraphrase as a quotation, or assigning general discussion text to a panel.
- Ignoring relevant supplementary dependencies, baseline tables, adverse-event tables, null results, or missing controls.

## Minimal Example

A bar plot with a reported `p` value but no raw points and unclear `n` may suggest a difference, but confidence is limited until variability, biological replication, and the experimental unit are known. A changed marker supports altered marker expression, not improved function unless a functional assay tests that stronger claim.
