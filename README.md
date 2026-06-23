# Agent Research Scout

Research scouting workspace for literature review, gap analysis, adversarial review, and experiment planning.

---

## 目录总览

```
agent-research-scout/
├── README.md                 ← 本文件：仓库说明与文件索引
├── .gitignore                ← Git 忽略规则（PDF、.env、pilot 运行产物等）
├── skills/                   ← Cursor Agent 调研技能（指导 AI 如何写 topics/）
├── templates/                ← 各调研产出文件的空白模板
├── topics/                   ← 按课题存放的结构化调研结果（核心产出）
├── papers/                   ← 可选：人工归档原始 PDF / 笔记 / bib（不参与自动化）
├── benchmarks/               ← 实验协议与 benchmark 扩展说明
├── scripts/                  ← 可执行脚本（目前主要是 pilot 实验）
└── outputs/                  ← 脚本运行产出（pilot 轨迹、指标等）
```

---

## 根目录

| 文件 | 作用 |
|------|------|
| `README.md` | 项目说明、目录索引、workflow 与 pilot 快速入门 |
| `.gitignore` | 忽略 `.env`、`papers/raw/` 下的 PDF、`outputs/pilot/` 中的运行日志与轨迹等大文件；保留目录结构用的 `.gitkeep` |

---

## `skills/` — Agent 调研技能

| 文件 | 作用 |
|------|------|
| `paper_research_skill.md` | **Cursor Agent 的主技能文件**。定义如何系统调研 AI/LLM Agent 课题：检索范围、必须回答的问题、贡献类型判断、真实性核验规则、产出应写入 `topics/<topic>/` 的哪些文件、严格 workflow 顺序，以及 Go/Narrow/Hold/No-Go 决策标准。在 Cursor 中 @ 此文件即可让 Agent 按规范做文献调研。 |

> **注意**：技能指导 Agent 把结构化产出写到 `topics/`，**不会**自动往 `papers/` 写任何东西。

---

## `templates/` — 调研文件模板

新开课题时，从这里复制对应模板到 `topics/<your_topic>/`，再按 workflow 顺序填写。

| 文件 | 对应产出 | 作用 |
|------|----------|------|
| `topic_brief_template.md` | `topic_brief.md` | 定义课题：一句话定义、核心失败模式、研究边界、目标会议。收窄后只保留一版，须与 `gap_analysis.md` 同步 |
| `paper_card_template.md` | `paper_cards/<slug>.md` | 单篇核心论文精读卡片：问题、方法、实验、失败模式、与课题关系、可借鉴/需警惕点 |
| `gap_analysis_template.md` | `gap_analysis.md` | 空白分析：已有工作覆盖什么、缺什么、是否只是换名、MVP 方向、课题收窄记录 |
| `adversarial_review_template.md` | `adversarial_review.md` | 审稿人视角攻击：八问自检、最危险竞品、minimum evidence、拒稿风险 |
| `file_consistency_check_template.md` | `file_consistency_check.md` | 全库一致性审计：各文件是否互相矛盾、core_read 是否有 card、decision 是否过早 |
| `decision_template.md` | `decision.md` | Go / Narrow / Hold / No-Go 决策及条件检查表 |
| `experiment_plan_template.md` | `experiment_plan.md` | 实验方案：任务定义、三种条件、指标、样本量、pilot 规格。**不得早于** gap + adversarial + consistency |

---

## `topics/` — 结构化调研产出（核心）

每个子目录代表一个研究课题。当前示例：`state_contamination/`（Dual-State Contamination in SWE Agents）。

### 课题目录标准文件

| 文件 / 目录 | 作用 | 填写顺序 |
|-------------|------|----------|
| `topic_brief.md` | **当前版本**课题定义。收窄后更新此文件，删除旧版歧义表述 | ① |
| `paper_table.csv` | 论文索引表。每行一篇论文，含 title、venue、url、source_type、verified_status、core_read 等。所有引用必须可核验 | ② |
| `paper_cards/` | 核心论文精读目录。`paper_table.csv` 中 `core_read=yes` 的每篇必须有对应 `.md` 卡片 | ③ |
| `related_work.md` | 文献地图：按类别（benchmark / method / failure analysis 等）总结，不是逐篇流水账 | ④ |
| `gap_analysis.md` | 找研究空白、判断创新性、决定是否收窄课题、提出 MVP 实验方向 | ⑤ |
| `adversarial_review.md` | 模拟顶会审稿人攻击：会不会被拒、需要哪些 minimum evidence | ⑥ |
| `file_consistency_check.md` | 审计 topic 内所有文件是否一致（brief ↔ gap ↔ experiment ↔ decision） | ⑦ |
| `decision.md` | 最终决策：**Go** / **Narrow** / **Hold** / **No-Go**，附条件检查表 | ⑧ |
| `experiment_plan.md` | 可执行实验方案（条件、指标、样本量）。仅在前述文件通过后再写 | ⑨ |

### 示例：`topics/state_contamination/paper_cards/`

每文件对应一篇 `core_read=yes` 的核心论文，文件名用 slug 命名：

| 文件 | 对应论文 |
|------|----------|
| `ccrm_context_contamination.md` | Why Retrying Fails: Context Contamination in LLM Agent Pipelines (CCRM) |
| `state_contamination_memory_agents.md` | State Contamination in Memory-Augmented LLM Agents |
| `ga_rollback.md` | GA-Rollback: Generator-Assistant Stepwise Rollback |
| `acrfence.md` | ACRFence: Preventing Semantic Rollback Attacks |
| `agentdebug.md` | AgentDebug: Where LLM Agents Fail |
| `memoryagentbench.md` | MemoryAgentBench |
| `hell_or_high_water.md` | Hell or High Water: Agentic Recovery from External Failures |
| `swe_bench.md` | SWE-bench / SWE-bench Verified |

---

## `papers/` — 原始资料归档（可选，不参与自动化）

**与 `topics/` 和 `scripts/` 无耦合**：没有任何脚本读取或写入此目录。留空是正常的。

| 目录 | 作用 | Git 行为 |
|------|------|----------|
| `papers/raw/` | 手动下载的论文 PDF | 内容被 `.gitignore` 忽略；仅保留 `.gitkeep` 占位 |
| `papers/notes/` | 个人阅读笔记、高亮摘录 | 可提交文本笔记；PDF 等大文件仍建议忽略 |
| `papers/bib/` | BibTeX / Zotero 导出等引用文件 | 可提交 |

调研结构化产出（表格、卡片、分析）写在 `topics/<topic>/`；`paper_table.csv` 中的 `url` 直接指向在线来源，**不依赖**本地 PDF。

---

## `benchmarks/` — 实验协议说明

| 路径 | 作用 |
|------|------|
| `dual_state_contamination/README.md` | Dual-State Contamination 评估协议：ContextState / WorldState 操作定义、三种 retry 条件（dirty-retry / clean-restart / full-reset）、指标公式（CR / RG / WSD）、pilot 规格（N=10, k=3）、与 CCRM 的对齐说明、可复现性要求（应发布哪些文件） |

实际执行代码在 `scripts/pilot/`，benchmark 目录只存**协议文档**，不含可执行代码。

---

## `scripts/` — 可执行脚本

### `scripts/pilot/` — Dual-State Contamination Pilot

在 SWE-bench Verified 上跑 10 题 × 3 条件 × 3 次 attempt 的 pilot 实验。详见 `scripts/pilot/README.md` 与 `outputs/pilot/checklist.md`。

#### 配置文件

| 文件 | 作用 |
|------|------|
| `config.yaml` | Pilot 主配置：实例数、seed、三种 condition 定义、mini-SWE-agent 调用参数、输出路径、Go/No-Go 阈值、`state_control.hook_validated` 开关 |
| `.env` | 本地模型配置（**gitignore**）。示例：`MINI_SWE_MODEL`、`OLLAMA_API_BASE`。复制后按需修改，勿提交 |
| `requirements.txt` | Python 依赖（`pip install -r requirements.txt`） |

#### 核心脚本

| 脚本 | 作用 | 典型输出 |
|------|------|----------|
| `sample_instances.py` | 从 SWE-bench Verified 抽样 10 个 instance ID（seed=42） | `outputs/pilot/instances.json` |
| `conditions.py` | 定义三种 retry 条件的 context/world 策略（retain / reset） | 被其他脚本 import，无独立输出 |
| `run_pilot.py` | 编排实验运行。模式：`--dry-run`（只打印命令）、`--smoke-test`（测 Docker）、`--mock`（合成数据测管道）、`--execute`（真实跑） | `run_log.jsonl`、`trajectories/`、`predictions/` |
| `analyze_pilot.py` | 从 `run_log.jsonl` 计算 CR、RG、WSD 及 Go/Hold/No-Go 建议 | `outputs/pilot/metrics/pilot_summary.json` |
| `merge_evaluation_results.py` | 将 SWE-bench harness 的 resolved 标签合并回 `run_log.jsonl` | 更新 `run_log.jsonl` |
| `update_decision_draft.py` | 根据 pilot 指标生成 decision 更新草稿 | `outputs/pilot/decision_draft.md`（gitignore） |
| `validate_pilot_setup.py` | 跑真实分析前检查：config 是否就绪、三条件 hook 是否验证、是否误用 mock 数据 | 终端报告 + exit code |
| `trajectory_schema.py` | `run_log.jsonl` 每行的 JSON schema（`AttemptRecord` dataclass） | 被其他脚本 import |

#### `scripts/pilot/backend/` — 执行后端

| 文件 | 作用 |
|------|------|
| `__init__.py` | Python 包标识 |
| `mini_swe_adapter.py` | mini-SWE-agent Python API 封装。通过 agent/environment 生命周期实现三条件：dirty-retry 复用 agent+env；clean-restart 新建 agent 保留 env；full-reset 全部重建。记录轨迹与 submission，resolved 需后续 merge |

#### `scripts/pilot/README.md`

Pilot 脚本快速参考：安装、命令顺序、各脚本职责表。

---

## `outputs/` — 脚本运行产出

### `outputs/pilot/` — Pilot 实验数据

| 文件 / 目录 | 来源 | 作用 | Git 行为 |
|-------------|------|------|----------|
| `README.md` | 手写 | Pilot 目录说明、快速开始、成功阈值 | 提交 |
| `checklist.md` | 手写 | 分阶段执行清单（Prerequisites → Sample → Smoke → Execute → Analyze → Decision） | 提交 |
| `instances.json` | `sample_instances.py` | 10 个 SWE-bench Verified instance ID + seed | 提交 |
| `run_log.jsonl` | `run_pilot.py` | 每次 attempt 一行 JSON：instance、condition、resolved、workspace_hash、first_step_error 等 | **gitignore**（运行后本地生成） |
| `trajectories/` | `run_pilot.py` | 每次运行的 mini-SWE-agent 轨迹 JSON | **gitignore**（保留 `.gitkeep`） |
| `predictions/` | `run_pilot.py` | SWE-bench 格式的 prediction JSONL，供 harness 评估 | **gitignore**（保留 `.gitkeep`） |
| `metrics/pilot_summary.json` | `analyze_pilot.py` | CR / RG / WSD 汇总 + Go 建议 | **gitignore** |
| `metrics/.gitkeep` | — | 保持空目录结构 | 提交 |
| `decision_draft.md` | `update_decision_draft.py` | 根据指标草稿更新 `topics/.../decision.md` 的建议文本，需人工 merge | **gitignore** |

---

## Research Workflow

严格按顺序填写 `topics/<topic>/` 下的文件：

```
1. topic_brief.md           定义课题
2. paper_table.csv            收集并核验论文（≥15 篇广搜，标记 core_read）
3. paper_cards/               核心论文精读（core_read=yes，通常 ≥8 篇）
4. related_work.md            文献地图
5. gap_analysis.md            空白分析 + 必要时收窄
6. adversarial_review.md      审稿人攻击
7. file_consistency_check.md  文件一致性审计
8. decision.md                Go / Narrow / Hold / No-Go
9. experiment_plan.md         仅 decision 允许后
10. outputs/pilot/            执行 pilot / 分析 / 更新 decision
```

上面的 10 步是**文件写作顺序**，不是一次性投稿完成标准。完整研究应按阶段推进：

| Phase | 名称 | 目标 | 典型产出 |
|-------|------|------|----------|
| 0 | Intake / Scope | 把模糊方向变成可调研课题 | `topic_brief.md` 初版 |
| 1 | Scouting | 判断方向是否值得进入 pilot | `paper_table.csv` ≥15 篇；`paper_cards/` 通常 8 篇；`gap_analysis.md`、`decision.md` |
| 2 | Expansion | 扩成论文级 related work 地图 | `paper_table.csv` 通常 40–60+ 篇；`paper_cards/` 通常 12–20 篇；重写 `related_work.md` |
| 3 | Validation | 用 pilot / minimum evidence 验证核心效应 | `outputs/pilot/` 指标、轨迹、`decision_draft.md` |
| 4 | Paper-ready Audit | 投稿前审计 claim、证据、related work 是否对齐 | 更新后的 `file_consistency_check.md` 与 `decision.md` |

因此，当前 15+8 的要求是 **Phase 1 选题侦察下限**；如果目标是写论文，需要进入 Phase 2 扩库和 Phase 4 投稿前审计。

**重要约束**：

- `experiment_plan.md` **不得**早于 `gap_analysis.md` 和 `adversarial_review.md`
- `decision.md` **不得**早于 `file_consistency_check.md`
- `gap_analysis` 收窄后，**必须同步** `topic_brief.md`
- 重调研、扩库或 Phase 回退时：**保留**旧文件，增量审计更新，不整库删除

---

## Pilot 快速入门（state_contamination）

文献 workflow 完成 → **Decision: Narrow** → 跑 10 题 pilot：

```powershell
cd scripts/pilot
pip install -r requirements.txt
python sample_instances.py
python run_pilot.py --mock --reset-log   # 管道测试（无需 Docker）
python analyze_pilot.py --allow-mock
python update_decision_draft.py
```

真实运行：

```powershell
# 可选：在 scripts/pilot/.env 中配置
# MINI_SWE_MODEL=ollama/qwen2.5-coder:7b-instruct
# OLLAMA_API_BASE=http://localhost:11434

python validate_pilot_setup.py
python run_pilot.py --smoke-test          # 测 Docker + mini-SWE-agent
python run_pilot.py --execute --reset-log # 真实跑（慢、耗 API）
python merge_evaluation_results.py --results path/to/evaluation_results.json
python analyze_pilot.py
python update_decision_draft.py
```

成功阈值（pilot → Go）：Recovery Gap ≥ 5 pp；world-reset wins ≥ 2/10。详见 `outputs/pilot/README.md` 与 `topics/state_contamination/experiment_plan.md`。

---

## 新开课题

1. 创建 `topics/<your_topic>/`
2. 从 `templates/` 复制各模板并重命名（去掉 `_template` 后缀）
3. 按 Research Workflow 顺序填写
4. 如需实验，在 `experiment_plan.md` 中定义后，可参考 `scripts/pilot/` 搭建或复制 pilot 脚手架

可选：在 `papers/raw/` 手动存放 PDF，在 `papers/notes/` 写阅读笔记——这与结构化产出并行，互不影响。
