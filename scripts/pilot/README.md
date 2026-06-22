# Pilot scripts — Dual-State Contamination

Run from this directory:

```powershell
pip install -r requirements.txt
python sample_instances.py
python run_pilot.py --mock          # test pipeline
python analyze_pilot.py
python update_decision_draft.py
```

| Script | Purpose |
|--------|---------|
| `config.yaml` | Pilot config (10 instances, 3 conditions, thresholds) |
| `sample_instances.py` | Sample SWE-bench Verified IDs → `outputs/pilot/instances.json` |
| `conditions.py` | dirty-retry / clean-restart / full-reset definitions |
| `run_pilot.py` | Orchestrate runs (`--dry-run`, `--mock`, `--execute`) |
| `analyze_pilot.py` | Compute CR, RG, WSD → `metrics/pilot_summary.json` |
| `update_decision_draft.py` | Draft decision update from metrics |
| `trajectory_schema.py` | JSONL record format |

Full checklist: `outputs/pilot/checklist.md`
