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
├── predictions/           ← SWE-bench prediction JSONL per condition/attempt
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
python run_pilot.py --mock --reset-log
python analyze_pilot.py --allow-mock
python update_decision_draft.py

# 2b. Real run (Docker + mini-swe-agent + API key)
pip install mini-swe-agent
# Optional: put these in scripts/pilot/.env instead
# MINI_SWE_MODEL=ollama/glm-5.2:cloud
# OLLAMA_API_BASE=http://your-ollama-host:11434
python run_pilot.py --dry-run    # inspect commands
python validate_pilot_setup.py   # static/log readiness
python run_pilot.py --smoke-test # one infra command with --exit-immediately
python run_pilot.py --execute --reset-log  # real run (slow, costly)

# 3. Evaluate predictions with SWE-bench, then merge resolved labels
# Example local harness command for one predictions file:
# python -m swebench.harness.run_evaluation `
#   --dataset_name princeton-nlp/SWE-bench_Verified `
#   --predictions_path ../../outputs/pilot/predictions/dirty-retry__a1.jsonl `
#   --run_id pilot-dirty-retry-a1
python merge_evaluation_results.py --results path/to/evaluation_results.json

# 4. Analyze and draft decision update
python validate_pilot_setup.py
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
