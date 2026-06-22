# Dual-State Contamination Pilot

10-question pilot for `topics/state_contamination/` on SWE-bench Verified.

## Directory layout

```
outputs/pilot/
├── README.md              ← this file
├── checklist.md           ← step-by-step execution
├── instances.json         ← 10 sampled instance IDs
├── run_log.jsonl          ← one row per attempt (from run_pilot.py)
├── trajectories/          ← mini-SWE-agent trajectory JSON per run
└── metrics/
    └── pilot_summary.json ← CR / RG / WSD + Go recommendation
```

## Quick start

```powershell
cd scripts/pilot
pip install -r requirements.txt

# 1. Sample 10 Verified instances
python sample_instances.py

# 2a. Pipeline test (no Docker) — synthetic trajectories
python run_pilot.py --mock
python analyze_pilot.py
python update_decision_draft.py

# 2b. Real run (Docker + mini-swe-agent + API key)
pip install mini-swe-agent
$env:MINI_SWE_MODEL = "openai/gpt-4o-mini"
python run_pilot.py --dry-run    # inspect commands
python run_pilot.py --execute    # run (slow, costly)

# 3. Analyze and draft decision update
python analyze_pilot.py
python update_decision_draft.py
```

## Success criteria (pilot → Go)

| Metric | Threshold |
|--------|-----------|
| Recovery Gap (clean-restart − dirty-retry) | ≥ **5 pp** |
| World-reset wins (C resolved, B not) | ≥ **2 / 10** |

See `topics/state_contamination/experiment_plan.md` §9.

## After pilot

1. Merge `decision_draft.md` into `topics/state_contamination/decision.md`
2. Re-run `file_consistency_check.md`
3. If Go: scale to 50–100 instances per `experiment_plan.md`
