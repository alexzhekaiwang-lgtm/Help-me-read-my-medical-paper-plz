# Systematic Review And Meta-Analysis

## Purpose

Appraise systematic reviews and meta-analyses using PRISMA-style prompts.

## When To Use

Use when a paper reports an explicit systematic search and study-selection process, with or without quantitative pooling. Route narrative reviews without systematic methods through `02_study_design_router.md` instead.

## Core Checklist

- Review question: population, intervention/exposure, comparator, outcomes.
- Protocol/registration if reported.
- Search strategy: databases, dates, terms, language limits, gray literature.
- Eligibility criteria: study designs, outcomes, populations.
- Study selection: screening process and disagreements.
- Data extraction: duplicate extraction, missing information.
- Risk of bias: tool used and domain-level concerns.
- Heterogeneity: clinical, methodological, and statistical.
- Meta-analysis model: fixed-effect or random-effects and why.
- Forest plots: direction, size, precision, weights, heterogeneity.
- Publication bias: funnel plot, small-study effects, search limitations.
- Certainty of evidence: use GRADE-style domains where helpful; confidence depends on bias, inconsistency, indirectness, imprecision, and publication bias, not just number of studies.
- Robustness: sensitivity analyses, leave-one-out checks, subgroup/meta-regression caution, and prediction intervals when heterogeneity matters.
- Appraisal tools: AMSTAR 2 for review conduct, RoB 2 for randomized studies, and ROBINS-I for nonrandomized studies when applicable.
- Limitations: quality of included studies, inconsistent definitions, selective reporting.

## Common Pitfalls

- Treating pooled precision as proof of unbiased evidence.
- Ignoring high heterogeneity.
- Combining clinically incompatible studies.
- Forgetting that meta-analysis cannot fix poor primary studies.
- Overinterpreting subgroup or meta-regression patterns as causal.

## Minimal Example

Synthetic meta-analysis: a pooled effect with high heterogeneity should be explained as an average of dissimilar studies, not a single universal effect.
