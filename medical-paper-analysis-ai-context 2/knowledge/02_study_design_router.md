# Study Design Router

## Purpose

Classify the paper type before choosing an appraisal framework.

## When To Use

Use when the design is unclear, mixed, or itself under discussion. When the design is already known, proceed directly to the relevant module or core checks.

## Core Checklist

Decision tree:

1. Are participants assigned by investigators to an intervention?
   - Random assignment: randomized controlled trial. Use CONSORT-style appraisal and identify superiority, noninferiority, or equivalence.
   - Nonrandom assignment or no concurrent control: nonrandomized or single-arm interventional trial. Use `03_clinical_trial_appraisal.md`; identify phase, allocation method, dose/escalation design, and whether the comparator is concurrent, historical, or absent. Add observational confounding checks when comparisons are nonrandomized.
2. Are existing groups observed without assignment?
   - Exposure to outcome over time: cohort study.
   - Outcome to prior exposure: case-control study.
   - Exposure and outcome measured at one time: cross-sectional study.
   - Use STROBE-style reporting prompts plus internal-validity appraisal.
3. Does it systematically search and synthesize multiple studies?
   - Systematic review or meta-analysis. Use PRISMA-style prompts.
4. Does it test mechanisms in cells, animals, tissues, or assays?
   - Basic-science/mechanistic paper. Use model, control, perturbation/rescue, assay, and causal-chain appraisal.
5. Does it evaluate a diagnostic or prognostic model/test?
   - Use STARD-style prompts for diagnostic accuracy, TRIPOD-style prompts for prediction models, and PROBAST/QUADAS-2-style bias concepts where helpful.
   - Check sensitivity, specificity, PPV/NPV, likelihood ratios, pretest probability, ROC/AUC, calibration, internal/external validation, decision curves or net benefit, spectrum bias, verification bias, incorporation bias, overfitting, and clinical utility.
6. Does it describe one or a few patients?
   - Case report/series. Treat as hypothesis-generating.
7. Is it a narrative review, guideline, or methods paper?
   - Separate expert synthesis, recommendation, or method proposal from direct empirical evidence.

Use CASP- or NIH-style appraisal concepts when useful: selection, comparability, measurement quality, attrition, precision, applicability, and bias risk.

Routes can stack. If the goal is prediction or diagnosis, apply diagnostic/prognostic checks even when the source data are observational. If the question is causal and observational, apply both observational confounding checks and the relevant outcome/model checks.

## Common Pitfalls

- Calling any human study a clinical trial.
- Treating STROBE, CONSORT, or PRISMA as quality scores.
- Missing whether a trial is noninferiority or equivalence.
- Accepting a high AUC without checking calibration, validation, or clinical usefulness.

## Minimal Example

Synthetic prompt: "Patients choosing Drug A had better survival than Drug B." If treatment was not randomized, route as observational and look for confounding by indication.
