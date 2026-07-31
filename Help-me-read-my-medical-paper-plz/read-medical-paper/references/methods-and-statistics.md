# Methods And Statistics Glossary

## Purpose

Explain common methods and statistics in undergraduate-friendly language.

## When To Use

Use when the user asks about methods, statistics, effect sizes, plots, or how to interpret results.

## Core Checklist

- p-value: probability of data at least this extreme if the null model were true; not the probability the hypothesis is true.
- Confidence interval: range of effect sizes compatible with data and model assumptions; width reflects precision.
- Effect size: magnitude of a difference or association; often more important than a p-value.
- Practical/biological/clinical significance: whether an effect is large enough to matter in context, not just statistically detectable.
- Hazard ratio: relative event rate over time; common in survival analysis.
- Odds ratio: ratio of odds; can exaggerate risk ratio when outcomes are common.
- Relative risk: probability ratio between groups.
- Kaplan-Meier curve: estimated time-to-event curve with censoring.
- Cox regression: model for hazard ratios adjusted for covariates if assumptions are reasonable.
- ROC/AUC: discrimination of a test or model; AUC does not prove clinical usefulness.
- Sensitivity: proportion of true positives detected.
- Specificity: proportion of true negatives correctly excluded.
- PPV/NPV: chance a positive/negative result is correct in a specific population; changes with disease prevalence.
- Likelihood ratio: how much a test result changes pretest probability.
- Calibration: whether predicted risks match observed risks.
- Power: chance to detect a specified effect under assumptions; mainly for planning, not a rescue for a completed null study.
- Adjusted model: statistical model controlling for measured covariates; cannot remove unmeasured confounding.
- False discovery rate: expected proportion of false positives among declared discoveries.
- t-test: compares means between two groups under assumptions.
- ANOVA: compares means across more than two groups; post hoc tests may be needed.
- Regression: models relation between predictors and outcome; linear is often for continuous outcomes, logistic for binary outcomes, and Cox/survival models for time-to-event outcomes.
- Interaction: evidence that an effect differs across groups; stronger than comparing one significant subgroup with one non-significant subgroup.
- Multiplicity: many tests increase false-positive risk; prespecification and correction help.
- Subgroup/post hoc finding: exploratory unless prespecified and supported by an interaction test or independent validation.
- Proxy/surrogate outcome: indirect stand-in for the outcome of interest; useful only if the link to the real outcome is justified.
- Meta-analysis heterogeneity: variation in effects across studies; I2 estimates inconsistency, tau2 estimates between-study variance, and prediction intervals show the range expected in a future setting.
- Normalization: scaling data to a baseline/control; can hide absolute differences.

Replication and uncertainty terms:

- Experimental unit: the smallest independently assigned or sampled entity that could receive a different condition, such as a patient, animal, donor, culture, litter, or sometimes a well.
- Biological replicate: an independently sampled biological unit; it supports generalization across biological variation.
- Technical replicate: repeated measurement of the same biological unit; it estimates measurement noise but does not increase biological `n`.
- Nesting/clustering: observations share a higher-level unit, such as cells within a donor or animals within a litter; the analysis must preserve that dependence.
- Pseudoreplication: treating nested, technical, or repeated observations as independent units, which makes precision look stronger than it is.
- Paired or repeated measures: the same unit is measured across conditions or times; use a model/test that represents within-unit dependence.
- SD: spread of observed values. SEM: precision of the estimated mean, not sample variability. CI: range of effect estimates compatible with data and model assumptions.

For test selection, ask: What is the outcome type? Are observations independent? How many groups or time points are compared? Is the test prespecified? Are assumptions plausible?

Power/sample-size audit:

- Was power planned a priori for the primary endpoint and actual analysis model?
- What effect size was powered: smallest meaningful effect, prior/pilot estimate, or convention?
- Were dropout, clustering/pseudoreplication, unequal allocation, and multiplicity accounted for?
- For completed studies, avoid observed/post-hoc power; inspect effect size, CI width, and minimum detectable effect instead.

## Common Pitfalls

- Reading p < 0.05 as proof.
- Treating non-significant as no effect.
- Using observed/post-hoc power as if it adds information after the p-value is known.
- Ignoring dropout, multiple comparisons, or clustered/nested observations in power reasoning.
- Confusing SD, SEM, and CI.
- Ignoring whether the chosen test matches data type and design.
- Treating discrimination, calibration, and clinical utility as the same thing.
- Letting a small p-value substitute for effect size, design quality, or direct measurement of the claim.

## Minimal Example

Synthetic result: "p = 0.04, tiny effect size, large sample." Statistically detectable does not automatically mean biologically or clinically meaningful.
