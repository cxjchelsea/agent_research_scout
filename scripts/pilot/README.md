# Pilot scripts — Dual-State Contamination

Run from this directory:

```powershell
pip install -r requirements.txt
python sample_instances.py
python run_pilot.py --mock --reset-log  # test pipeline
python analyze_pilot.py --allow-mock
python update_decision_draft.py
```

Local model configuration can live in `scripts/pilot/.env` (gitignored):

```env
MINI_SWE_MODEL=ollama/glm-5.2:cloud
OLLAMA_API_BASE=http://your-ollama-host:11434
```

| Script | Purpose |
|--------|---------|
| `config.yaml` | Pilot config (10 instances, 3 conditions, thresholds) |
| `sample_instances.py` | Sample SWE-bench Verified IDs → `outputs/pilot/instances.json` |
| `conditions.py` | dirty-retry / clean-restart / full-reset definitions |
| `run_pilot.py` | Orchestrate runs (`--dry-run`, `--smoke-test`, `--mock`, `--execute`) |
| `analyze_pilot.py` | Compute CR, RG, WSD → `metrics/pilot_summary.json` |
| `merge_evaluation_results.py` | Merge SWE-bench resolved labels into `run_log.jsonl` |
| `update_decision_draft.py` | Draft decision update from metrics |
| `trajectory_schema.py` | JSONL record format |
| `validate_pilot_setup.py` | Check config/log readiness before real decision updates |
| `state_control_validation.py` | Validate observable context/world state-control evidence |
| `backend/mini_swe_adapter.py` | Python API backend with env/agent lifecycle state control |

The 10-instance run is an **infrastructure pilot**. It can validate plumbing,
state control, merge safety, and whether metrics are computable; it should not
be treated as paper-level Go evidence. Scale to 20–30 instances for signal and
50–100 for paper-level estimates.

When merging SWE-bench results, every resolved label must identify the exact
`instance_id + condition + attempt`. If the evaluation JSON only maps
`instance_id -> resolved`, pass the metadata explicitly, for example:

```powershell
python merge_evaluation_results.py --results path/to/eval.json `
  --condition dirty-retry --attempt 1
```

Full checklist: `outputs/pilot/checklist.md`
