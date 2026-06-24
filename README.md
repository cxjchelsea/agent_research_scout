# Agent Research Scout

Research scouting workspace for literature review, gap analysis, adversarial review, and experiment planning.

---

## 目录总览

```
agent-research-scout/
├── README.md
├── skills/                   ← Cursor Agent 调研技能
├── templates/                ← 各调研产出文件的空白模板（通用）
├── topics/                   ← 按课题存放的结构化调研结果（核心产出）
├── papers/                   ← 可选：人工归档原始 PDF / 笔记 / bib
├── benchmarks/               ← 可选：某课题确定后的实验协议说明
├── scripts/                  ← 可选：某课题确定后的实验脚本
└── outputs/                  ← 可选：实验运行产出
```

---

## 哪些是通用的，哪些是课题定制的

| 目录 | 性质 | 说明 |
|------|------|------|
| `skills/` | **通用** | 所有课题共用同一套调研 workflow 与 Phase 规则 |
| `templates/` | **通用** | 新开任何课题时复制模板到 `topics/<topic>/` |
| `topics/<topic>/` | **课题产出** | 每次调研的结果写在这里 |
| `papers/` | **可选归档** | 手动存 PDF/笔记，不参与自动化 |
| `benchmarks/`、`scripts/`、`outputs/` | **课题定制** | 仅在某个课题进入实验阶段后再创建；当前仓库默认为空占位 |

---

## `skills/` — Agent 调研技能

| 文件 | 作用 |
|------|------|
| `paper_research_skill.md` | Cursor Agent 主技能：调研范围、核验规则、分阶段 workflow（Phase 0–4）、Go/Narrow/Hold/No-Go 决策标准 |

在 Cursor 中 @ 此文件，让 Agent 按规范把产出写入 `topics/<topic>/`。

---

## `templates/` — 调研文件模板

新开课题时，从这里复制到 `topics/<your_topic>/`，去掉 `_template` 后缀后按 workflow 填写。

| 文件 | 对应产出 |
|------|----------|
| `topic_brief_template.md` | `topic_brief.md` |
| `paper_card_template.md` | `paper_cards/<slug>.md` |
| `gap_analysis_template.md` | `gap_analysis.md` |
| `adversarial_review_template.md` | `adversarial_review.md` |
| `file_consistency_check_template.md` | `file_consistency_check.md` |
| `decision_template.md` | `decision.md` |
| `experiment_plan_template.md` | `experiment_plan.md` |

---

## `topics/` — 结构化调研产出（核心）

每个子目录代表一个研究课题，例如 `topics/my_agent_topic/`。

| 文件 / 目录 | 作用 | 填写顺序 |
|-------------|------|----------|
| `topic_brief.md` | 当前版本课题定义 | ① |
| `paper_table.csv` | 论文索引 + 核验 | ② |
| `paper_cards/` | 核心论文精读（`core_read=yes`） | ③ |
| `related_work.md` | 文献地图 | ④ |
| `gap_analysis.md` | 空白分析 + 收窄 | ⑤ |
| `adversarial_review.md` | 审稿人攻击 | ⑥ |
| `file_consistency_check.md` | 一致性审计 | ⑦ |
| `decision.md` | Go / Narrow / Hold / No-Go | ⑧ |
| `experiment_plan.md` | 实验方案（decision 允许后） | ⑨ |

---

## `papers/` — 原始资料归档（可选）

| 目录 | 作用 |
|------|------|
| `papers/raw/` | 论文 PDF（gitignore） |
| `papers/notes/` | 阅读笔记 |
| `papers/bib/` | BibTeX 等引用文件 |

与 `topics/` 无自动化耦合；结构化产出写在 `topics/`。

---

## Research Workflow

```
1. topic_brief.md
2. paper_table.csv          （≥15 篇广搜）
3. paper_cards/             （core_read=yes，通常 ≥8 篇）
4. related_work.md
5. gap_analysis.md
6. adversarial_review.md
7. file_consistency_check.md
8. decision.md
9. experiment_plan.md       （仅 decision 允许后）
10. benchmarks/ scripts/ outputs/   （某课题进入实验阶段后再建）
```

### 分阶段说明

| Phase | 名称 | 目标 |
|-------|------|------|
| 0 | Intake / Scope | 把模糊方向变成可调研课题 |
| 1 | Scouting | 判断方向是否值得继续（15+8 下限） |
| 2 | Expansion | 扩成论文级 related work（通常 40–60+ 篇） |
| 3 | Validation | 用实验或 minimum evidence 验证核心效应 |
| 4 | Paper-ready Audit | 投稿前审计 claim 与 evidence 是否对齐 |

**重要约束**：

- `experiment_plan.md` **不得**早于 `gap_analysis.md` 和 `adversarial_review.md`
- `decision.md` **不得**早于 `file_consistency_check.md`
- Phase 1 的 15+8 是选题侦察下限，不是投稿级完整调研

---

## 新开课题

1. 创建 `topics/<your_topic>/`
2. 从 `templates/` 复制各模板并重命名
3. @ `skills/paper_research_skill.md`，说明课题方向与当前 Phase
4. 按 Research Workflow 顺序填写
5. 若 decision 允许进入实验，再为该课题创建 `benchmarks/<topic>/`、`scripts/<topic>/`、`outputs/<topic>/`

可选：在 `papers/raw/` 手动存放 PDF，与 `topics/` 并行，互不影响。
