# Agent Research Scout

Research scouting workspace: **discover innovation points → select a direction → deep dive → targeted verification → quick proof**.

---

## 目录总览

```
agent-research-scout/
├── README.md
├── skills/                   ← Cursor Agent 调研技能
├── templates/                ← 调研模板（通用）
├── scout/                    ← Phase 1–2：发现与候选（跨方向）
├── topics/                   ← Phase 3–4：深研与快速验证（单课题）
├── papers/                   ← 可选：人工归档 PDF / 笔记 / bib
├── benchmarks/               ← 可选：选定课题后的实验协议
├── scripts/                  ← 可选：选定课题后的实验脚本
└── outputs/                  ← 可选：实验运行产出
```

---

## 哪些是通用的

| 目录 | 用途 |
|------|------|
| `skills/` | 所有课题共用的发现 → 验证 workflow |
| `templates/` | 发现阶段 + 深研阶段模板 |
| `scout/` | 广搜、候选对比、用户选择（**每次重新发现从这里开始**） |
| `topics/<topic>/` | 选定方向后的深研与 decision |
| `papers/` | 可选 PDF/笔记归档 |
| `benchmarks/`、`scripts/`、`outputs/` | 选定课题并进入 Phase 4 后再建 |

---

## 五阶段 Workflow

```text
Phase 1  Discovery     scout/landscape_scan + discovery_paper_table + candidates
Phase 2  Selection     scout/selection.md → 创建 topics/<topic>/
Phase 3  Deep Dive     topics/ 下 15+8 深研 → Promising / Narrow / No-Go
Phase 3.5 Targeted Verification  最大威胁 work claim-level verification
Phase 4  Quick Proof   MVP 实验 → Go（值得继续投入）/ Hold / No-Go
```

| Phase | 产出目录 | 核心文件 |
|-------|----------|----------|
| 1 Discovery | `scout/` | `landscape_scan.md`、`discovery_paper_table.csv`（30–50 篇）、`candidates.md`（3–7 候选） |
| 2 Selection | `scout/` | `selection.md`（用户选定方向） |
| 3 Deep Dive | `topics/<topic>/` | `paper_table.csv`（≥15）、`paper_cards/`（8）、gap、adversarial、decision |
| 3.5 Targeted Verification | `topics/<topic>/` | 最大威胁 paper card 达到 `threat_verified`、claim coverage matrix |
| 4 Quick Proof | `topics/<topic>/` + `outputs/` | `experiment_plan.md`、MVP 实验证据、更新 decision |

**Go 的含义**：创新点已通过最小实验验证，**值得继续投入**——不等于可以投稿。

**硬门槛**：最大威胁 work 未完成 claim-level targeted verification 前，`experiment_plan.md` 只能是 draft，不能进入 Phase 4 execution。

---

## 用户输入怎么开始

| 你说什么 | 从哪开始 |
|----------|----------|
| 「帮我找 Agent 方向」 | Phase 1 Discovery |
| 「memory agent 相关有什么可做」 | Phase 1（带约束） |
| 「我想调研 X，值不值得做」 | Phase 3 Deep Dive（可跳过发现，但仍需撞车检查） |

---

## 模板

### 发现阶段（`scout/`）

| 模板 | 产出 |
|------|------|
| `landscape_scan_template.md` | `scout/landscape_scan.md` |
| `discovery_paper_table_template.csv` | `scout/discovery_paper_table.csv` |
| `candidates_template.md` | `scout/candidates.md` |
| `selection_template.md` | `scout/selection.md` |

### 深研阶段（`topics/<topic>/`）

| 模板 | 产出 |
|------|------|
| `topic_brief_template.md` | `topic_brief.md` |
| `paper_card_template.md` | `paper_cards/<slug>.md` |
| `gap_analysis_template.md` | `gap_analysis.md` |
| `adversarial_review_template.md` | `adversarial_review.md` |
| `file_consistency_check_template.md` | `file_consistency_check.md` |
| `decision_template.md` | `decision.md` |
| `experiment_plan_template.md` | `experiment_plan.md` |

---

## 快速开始

```text
1. @ skills/paper_research_skill.md
2. 说明：从 Phase 1 Discovery 开始（或已有明确题目则 Phase 3）
3. Agent 写入 scout/ 或 topics/<topic>/
4. Phase 2 由你选定候选方向
5. Phase 4 再为该课题创建 scripts/、outputs/
```

可选：在 `papers/raw/` 手动存放 PDF，与结构化产出并行。
