# Pilot Execution Checklist

> Topic: Dual-State Contamination on SWE-bench Verified  
> Plan: `topics/state_contamination/experiment_plan.md`  
> Scripts: `scripts/pilot/`

---

## Phase 0 — Prerequisites

- [ ] Python 3.10+
- [ ] Docker (x86 Linux containers; WSL2 on Windows)
- [ ] `pip install -r scripts/pilot/requirements.txt`
- [ ] `pip install mini-swe-agent` (for real runs)
- [ ] Model API key configured (`OPENAI_API_KEY`, etc.)
- [ ] Set model: `$env:MINI_SWE_MODEL = "your/model"`

---

## Phase 1 — Sample instances (Day 1)

```powershell
cd scripts/pilot
python sample_instances.py
```

- [ ] `outputs/pilot/instances.json` exists (10 IDs, seed=42)
- [ ] Spot-check IDs against [SWE-bench Verified](https://www.swebench.com/)

---

## Phase 2 — Environment smoke test (Day 1–2)

```powershell
mini-extra swebench-single --subset verified --split test -i django__django-11099 -m $env:MINI_SWE_MODEL --exit-immediately
```

- [ ] Docker pulls SWE-bench container successfully
- [ ] Single instance completes without infra errors
- [ ] Trajectory JSON written

---

## Phase 3 — Three-condition wrapper (Day 2)

Conditions (see `scripts/pilot/conditions.py`):

| ID | Context on retry | World on retry |
|----|------------------|----------------|
| dirty-retry | retain | retain |
| clean-restart | reset | retain |
| full-reset | reset | reset |

- [ ] Read `python run_pilot.py --dry-run` output
- [ ] Implement/fork mini-SWE-agent hook if `--execute` does not yet reset context/world  
      (env vars: `PILOT_CONTEXT_POLICY`, `PILOT_WORLD_POLICY`, `PILOT_ATTEMPT`)
- [ ] Log each attempt to `outputs/pilot/run_log.jsonl`

**Pipeline test (no Docker):**

```powershell
python run_pilot.py --mock
```

- [ ] `run_log.jsonl` has rows (10 × 3 conditions × up to 3 attempts)

---

## Phase 4 — 10-question pilot (Day 3–5)

```powershell
python run_pilot.py --execute
```

- [ ] 10 instances × 3 conditions × k≤3 attempts
- [ ] Trajectories under `outputs/pilot/trajectories/<instance>/<condition>/`
- [ ] Each attempt logged with: `resolved`, `first_step_error`, `workspace_hash`

---

## Phase 5 — Metrics & decision (Day 6–7)

```powershell
python analyze_pilot.py
python update_decision_draft.py
```

- [ ] `outputs/pilot/metrics/pilot_summary.json` generated
- [ ] Recovery Gap (RG) computed
- [ ] World-reset wins counted (C > B)
- [ ] Recommendation: Go / Hold / No-Go

| RG | World wins | Action |
|----|------------|--------|
| ≥ 5 pp | ≥ 2/10 | Merge draft → **Go** |
| 3–5 pp | — | **Hold**, expand sample |
| < 3 pp | — | **No-Go** review |

- [ ] Update `topics/state_contamination/decision.md`
- [ ] Re-run `topics/state_contamination/file_consistency_check.md`
- [ ] Optional: copy protocol to `benchmarks/dual_state_contamination/`

---

## Phase 6 — Error analysis (optional before full scale)

- [ ] Sample 5 trajectories; tag pollution step (context / world / both)
- [ ] Report fraction: full-reset saves but clean-restart does not
- [ ] Document in `outputs/pilot/error_analysis.md`
