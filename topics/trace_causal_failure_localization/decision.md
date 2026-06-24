# Decision: Repair-Test Generation from Agent Failure Traces

> **审计日期**：2026-06-24
> **Skill 版本**：paper_research_skill.md
> **联动文件**：`gap_analysis.md` · `adversarial_review.md` · `file_consistency_check.md` · `experiment_plan.md`

---

## Decision: Narrow

> **Current Phase**：3.5（Targeted Verification）
> Go 仅用于 Phase 4：表示创新点已通过 MVP 验证，值得继续投入。

原始 C1（Trace-Causal Failure Localization）被 AgentRx、TraceElephant、TRAIL、Who&When 强覆盖，应视为 No-Go。可继续投入的只是不等价的收窄题：从已定位 failure trace 生成可执行 regression test / repair target，并用 rerun 或 counterfactual validation 验证。

---

## Reason

### Phase 3 条件检查（深研后，尚未 Go）

| # | 条件 | 状态 |
|---|------|------|
| 1 | 至少 8 篇核心论文 metadata_verified | Pass |
| 2 | 至少 5 篇核心论文 close_read 或 threat_verified | Pass |
| 3 | 最大威胁 1–3 篇 work 均 threat_verified | Pass |
| 4 | 最大威胁 work 有 claim coverage matrix，且 Evidence 不为空 | Pass |
| 5 | gap_analysis 明确已有工作覆盖/未覆盖 | Pass |
| 6 | adversarial_review 已完成且风险有回应 | Pass |
| 7 | file_consistency_check 的 file consistency 与 evidence readiness 均通过 | Pass |
| 8 | 最危险 related work 已正面比较 | Pass |
| 9 | 课题已收窄到可实验场景 | Pass |
| 10 | 有 benchmark / data、baseline 与 ≥3 个指标 | Partial |
| 11 | uncertain 论文没有作为核心论据 | Pass |

### Phase 3.5 Targeted Verification Gate

| Gate | 状态 |
|------|------|
| 最大威胁 work 是否覆盖核心 claim | yes（原题）/ partial（收窄题） |
| 最大威胁 work 是否覆盖 proposed mechanism | yes（AgentRx 对原题）/ partial（收窄题） |
| 最大威胁 work 是否覆盖 benchmark / evaluation setting | yes（原题） |
| 如果扩展最大威胁方法，是否自然得到本案方法 | partial |
| 是否允许 experiment_plan 从 draft 升为 ready | no |
| 是否允许进入 Phase 4 execution | no |

### Phase 4 条件检查（Quick Proof 后，才可 Go）

| # | 条件 | 状态 |
|---|------|------|
| 1 | experiment_plan ready | Fail |
| 2 | outputs/ 有 minimum evidence | Fail |

### No-Go 条件检查

| 条件 | 是否触发 |
|------|----------|
| 核心问题已被已有论文完整覆盖 | yes（原始 trace localization claim） |
| 只能通过换术语制造新颖性 | yes（若坚持原题） |
| 没有可复现实验路径 | unknown |
| 没有强 baseline | unknown |
| MVP 无法构造或成本明显超出 2–4 个月 | unknown |
| 主要论据依赖 uncertain 论文 | no |

---

## 课题收窄确认（如适用）

| 项 | 内容 |
|----|------|
| 旧题目 | Trace-Causal Failure Localization for Agent Workflows |
| 新题目 | Repair-Test Generation from Agent Failure Traces |

---

## Minimum next step

不要继续原题。若继续，下一步只验证收窄题：构造 20–50 条 failure-to-regression-test / repair-target 样例，并核验 AgentRx / AgentDebug 是否已经覆盖该 artifact generation。

---

## What evidence would change this decision

| 证据 | 决策变化 |
|------|----------|
| AgentRx / AgentDebug 未覆盖 executable regression-test generation，且小样本 artifact 可执行 | Narrow → Promising |
| AgentRx / AgentDebug 已自然覆盖 repair-test generation | Narrow → No-Go |
| 无法获得可运行 traces 或 artifact 标注成本过高 | Narrow → No-Go / 回到 scout |

---

## 评分表（10 分制，可选）

| 维度 | 分 | 说明 |
|------|-----|------|
| 重要性 | 9 | agent debugging 和 benchmark diagnosis 是真实痛点。 |
| 新颖性 | 6 | 原题被覆盖；收窄题仍需证明不是 AgentRx / AgentDebug 的自然扩展。 |
| 可形式化 | 8 | regression test、repair target、rerun success 可定义。 |
| 可验证性 | 7 | 可复用现有 traces，但 artifact 标注和运行环境需核验。 |
| 方法空间 | 7 | 可做 artifact generation，但空间较窄。 |
| 泛化性 | 7 | 可跨 tau-bench / Magentic-One / SWE-Agent / GAIA traces。 |
| 顶会匹配 | 9 | 符合 agent evaluation / reliability / debugging。 |
| 工程可行 | 8 | MVP 可控，但标注成本需确认。 |
| Baseline 清晰 | 8 | full-trace LLM judge、last-error、taxonomy classifier。 |
| 风险可控 | 5 | 最大威胁很强，必须继续收窄。 |

**总评**：7.0。原题 No-Go；收窄题可作为谨慎 Narrow 继续验证，但不能进入 Phase 4 execution。

---

## 引用

- 空白分析 → `gap_analysis.md`
- 审稿攻击 → `adversarial_review.md`
- 一致性审计 → `file_consistency_check.md`
