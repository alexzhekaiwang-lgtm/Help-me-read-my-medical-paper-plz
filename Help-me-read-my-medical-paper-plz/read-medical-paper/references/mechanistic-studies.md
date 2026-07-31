# Basic-Science And Mechanistic Appraisal

## Purpose

Evaluate mechanistic biomedical papers, including cancer biology, immunology, molecular biology, cell biology, animal models, and assay-heavy studies.

## When To Use

Use when a paper claims a mechanism, pathway, causal chain, or biological model.

## Core Checklist

- Model relevance: cell line, organoid, animal, tissue, human sample, or in vitro assay.
- Controls: negative, positive, vehicle, untreated, isotype, loading, housekeeping, batch controls.
- Perturbation logic: knockout, knockdown, inhibitor, overexpression, activation, depletion.
- Rescue logic: does restoring the target restore the phenotype? Stronger rescue uses target-specific or knockdown-resistant constructs, credible expression levels, target engagement, inactive-mutant controls where relevant, and clear interpretation of partial or failed rescue.
- Orthogonal validation: independent method, reagent, assay, model, readout, or dataset.
- Dose and time response: does the effect behave plausibly?
- Replication and experimental unit: biological vs technical replicates; independent cohorts or experiments; avoid pseudoreplication from treating fields, images, cells, wells, cages, litters, plates, or repeated measures as independent when they are clustered.
- Sample size: number of animals, donors, cells, fields, experiments.
- Assay specificity: off-target effects, antibody/reagent validation, specificity controls.
- Imaging/quantification rigor: representative images plus quantification; blinded gating, histology, scoring, or image analysis when relevant; randomization of animals, plates, batches, or treatment order where feasible.
- Causal-chain strength: link each step with evidence rather than narrative.
- Proxy vs function: marker expression, pathway readout, or morphology may suggest function but does not prove it unless paired with a functional assay.
- Redundancy analysis: ask whether several experiments truly add independent support or repeat the same cell line, assay, perturbation, proxy readout, or missing control.
- Alternative explanations: toxicity, proliferation, batch effects, cell-state shifts, immune context.
- Translation: cell-line, animal, and human relevance are different evidence levels.

## Common Pitfalls

- Treating one model as general biology.
- Ignoring failed or partial rescue.
- Accepting representative images without quantification.
- Treating inhibitor data as target-specific without orthogonal support.
- Treating multiple similar panels as independent proof when all share the same weak assumption.
- Claiming mechanism from perturbation alone without rescue, specificity, or causal-chain evidence.
- Ignoring unit-of-analysis mismatch or clustered data.

## Minimal Example

Synthetic mechanism: "Kinase Y activates pathway Z." Stronger evidence includes phosphorylation change, target-specific perturbation, rescue, independent assay, and relevant model validation.

If every panel uses the same inhibitor in one cell line, the evidence may be redundant rather than orthogonal, even if there are many panels.
