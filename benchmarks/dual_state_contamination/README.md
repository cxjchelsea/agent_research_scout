# Dual-State Contamination Eval Protocol

Benchmark extension for measuring **ContextState** and **WorldState** pollution during retry on SWE-bench Verified.

Full research context: `topics/state_contamination/topic_brief.md`

---

## Definitions

| Term | Operational definition |
|------|------------------------|
| ContextState | Message history + tool I/O log |
| WorldState | Docker workspace file tree + test artifacts |
| dirty-retry | Default: retain both on retry |
| clean-restart@k | Reset context; retain workspace |
| full-reset@k | Reset context + restore workspace snapshot |

## Metrics

| ID | Formula |
|----|---------|
| CR | P(first-step error \| retry) − P(first-step error \| attempt 1) |
| RG | resolve(clean-restart@k) − resolve(dirty-retry@k) |
| WSD-basic | Workspace hash drift from initial snapshot after failed attempt |
| WSD-source / residual | Source/test diff files and failed-attempt residual patch |
| WSD-harmful | Residual workspace state that plausibly causes retry failure or deviation |

## Evidence tiers

- Infrastructure pilot: **N** = 10 instances (seed 42), **k** = 3. Validates state control, strict merge, logging, and metric computability only.
- Signal pilot: **N** = 20–30. Checks whether full-reset has stable advantage over clean-restart.
- Paper-scale subset: **N** = 50–100. Reports confidence intervals, paired analysis, and harmful WSD case studies.
- Scaffold: mini-SWE-agent, bash-only
- Implementation: `scripts/pilot/`

## Citation alignment

- Context channel: compare RG with CCRM (Yang 2026, arXiv 2605.08563)
- World channel: report WSD + C vs B wins (incremental over CCRM)

## Reproducibility

Publish:

1. `instances.json`
2. `run_log.jsonl`
3. Trajectory JSON per attempt
4. `metrics/pilot_summary.json`
