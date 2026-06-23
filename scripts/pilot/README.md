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
| `backend/mini_swe_adapter.py` | Python API backend with env/agent lifecycle state control |

Full checklist: `outputs/pilot/checklist.md`
