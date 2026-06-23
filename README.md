# Agent Research Scout

Research scouting workspace for literature review, gap analysis, adversarial review, and experiment planning.

## Structure

```
agent-research-scout/
├── README.md
├── skills/
│   └── paper_research_skill.md
├── templates/
│   ├── paper_card_template.md
│   ├── topic_brief_template.md
│   ├── gap_analysis_template.md
│   ├── adversarial_review_template.md
│   ├── experiment_plan_template.md
│   ├── decision_template.md
│   └── file_consistency_check_template.md
├── topics/
│   └── state_contamination/
│       ├── paper_cards/
│       ├── topic_brief.md
│       ├── paper_table.csv
│       ├── related_work.md
│       ├── gap_analysis.md
│       ├── adversarial_review.md
│       ├── experiment_plan.md
│       ├── decision.md
│       └── file_consistency_check.md
├── papers/
│   ├── raw/
│   ├── notes/
│   └── bib/
├── benchmarks/
├── scripts/
└── outputs/
    └── pilot/                 ← pilot trajectories & metrics
```

## Pilot (state_contamination)

Literature workflow complete → **Decision: Narrow** → run 10-question pilot:

```powershell
cd scripts/pilot
pip install -r requirements.txt
python sample_instances.py
python run_pilot.py --mock --reset-log  # pipeline test (no Docker)
python analyze_pilot.py --allow-mock
python update_decision_draft.py
```

Real run: `python validate_pilot_setup.py` → `python run_pilot.py --smoke-test` → `python run_pilot.py --execute --reset-log`.
See `outputs/pilot/checklist.md` and `outputs/pilot/README.md`.

## Topic 文件职责

| 文件 | 职责 |
|------|------|
| `topic_brief.md` | 定义**当前版本**课题（收窄后只保留一版） |
| `paper_table.csv` | 论文索引 + 核验（url, source_type, verified_status） |
| `paper_cards/` | 核心论文精读（`core_read=yes` 必须有 card） |
| `related_work.md` | 文献地图（按类总结，非流水账） |
| `gap_analysis.md` | 找空白、判断是否换名、MVP 方向 |
| `adversarial_review.md` | 审稿人攻击：会不会被拒 |
| `file_consistency_check.md` | 全库一致性审计 |
| `decision.md` | Go / Narrow / Hold / No-Go |
| `experiment_plan.md` | **gap + adversarial + consistency 通过后**再写 |

## Research Workflow

```
1. topic_brief.md          定义课题
2. paper_table.csv         收集并核验论文
3. paper_cards/            核心论文精读
4. related_work.md          文献地图
5. gap_analysis.md          空白分析 + 收窄
6. adversarial_review.md    审稿人攻击
7. file_consistency_check.md  文件一致性审计
8. decision.md              Go / Narrow / Hold / No-Go
9. experiment_plan.md       仅在有明确决策后写 MVP
10. outputs/                pilot / 实验产出
```

**重要顺序**：`experiment_plan.md` 不应早于 `gap_analysis.md` 和 `adversarial_review.md`。

## 新开课题

复制 `templates/` 下对应模板到 `topics/<your_topic>/`，按 workflow 顺序填写。
