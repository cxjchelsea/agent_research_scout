# Decision: Agentic Regression Scenarios for Tool-Using Agent Failures

> **审计日期**：2026-06-24
> **Skill 版本**：paper_research_skill.md
> **联动文件**：`gap_analysis.md` · `adversarial_review.md` · `file_consistency_check.md` · `experiment_plan.md`

---

## Decision: Narrow

> **Current Phase**：3.5（Targeted Verification）
> Go 仅用于 Phase 4：表示创新点已通过 MVP 验证，值得继续投入。

原始 C1（Trace-Causal Failure Localization）被 AgentRx、TraceElephant、TRAIL、Who&When 强覆盖，应视为 No-Go。第一版收窄题（Repair-Test Generation from Agent Failure Traces）又受到传统软件测试中 crash/issue/stack trace → reproducing test 工作的强威胁。因此当前再次收窄为：从 tool-using agent failure trace 生成可重放 agentic regression scenario。

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
| 最大威胁 work 是否覆盖核心 claim | yes（原题）/ partial（第一版收窄题）/ no-partial（再次收窄题） |
| 最大威胁 work 是否覆盖 proposed mechanism | yes（AgentRx 对原题）/ partial（AgentDebug/AgentRx 对 repair feedback） |
| 最大威胁 work 是否覆盖 benchmark / evaluation setting | yes（原题）；traditional testing 覆盖 software tests |
| 如果扩展最大威胁方法，是否自然得到本案方法 | partial；需要 agent-specific scenario schema 才不等价 |
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
| 没有可复现实验路径 | no（但需要 scenario schema） |
| 没有强 baseline | no（AgentRx / AgentDebug / Issue2Test-style baselines） |
| MVP 无法构造或成本明显超出 2–4 个月 | unknown |
| 主要论据依赖 uncertain 论文 | no |

---

## 课题收窄确认（如适用）

| 项 | 内容 |
|----|------|
| 旧题目 | Trace-Causal Failure Localization for Agent Workflows |
| 新题目 | Agentic Regression Scenarios for Tool-Using Agent Failures |

---

## Phase 3.5b 补充核验

| 核验问题 | 结论 | 决策影响 |
|----------|------|----------|
| AgentDebug 是否已经覆盖 repair target / executable test generation？ | partial。它覆盖 root-cause isolation、targeted corrective feedback、re-rollout recovery，但未显示生成 standalone executable regression test artifact。 | 不能做自然语言 repair feedback；必须输出可运行 agentic scenario。 |
| AgentRx validation log 是否自然等价于 regression test artifact？ | partial / no。validation log 与 executable constraints 可作为 oracle / evidence source，但不是完整 test：缺少 setup、replay harness、fail/pass criterion 和 patch validation loop。 | 可作为 baseline 或 oracle source，不能直接改名为 regression test。 |
| 软件工程 / debugging / test generation 是否已有 failure trace → regression test 强相关工作？ | yes。ReCrash、EvoCrash、Issue2Test、BRT Agent、Echo、iCoRe 等已强覆盖 crash/issue/stack trace → reproducing test。 | 第一版收窄题不能升 Promising；必须再次收窄到 agent-specific regression scenario。 |

---

## Minimum next step

不要继续原题，也不要做宽泛 failure trace → regression test。若继续，下一步只验证再次收窄题：构造 10–20 条 tool-using agent failure → agentic regression scenario 样例，检查能否表达 tool mocks、policy、memory / handoff context 和 rerun oracle。

---

## What evidence would change this decision

| 证据 | 决策变化 |
|------|----------|
| agentic scenario schema 可表达传统 software test 不能表达的 tool/policy/memory/handoff context，且 10–20 个样例可运行 | Narrow → Promising |
| 样例退化为普通 unit/regression test 或自然语言 repair suggestion | Narrow → No-Go |
| 无法获得可运行 agent traces 或 mock backend/policy state | Narrow → No-Go / 回到 scout |

---

## 评分表（10 分制，可选）

| 维度 | 分 | 说明 |
|------|-----|------|
| 重要性 | 9 | agent debugging 和 benchmark diagnosis 是真实痛点。 |
| 新颖性 | 6 | 原题和第一版收窄题均被压缩；再次收窄题仍需样例证明。 |
| 可形式化 | 8 | agentic scenario schema、oracle、rerun success 可定义。 |
| 可验证性 | 7 | 可复用现有 traces，但 mock state / replay harness 需核验。 |
| 方法空间 | 7 | 可做 scenario generation，但空间较窄。 |
| 泛化性 | 7 | 可跨 tau-bench / Magentic-One / SWE-Agent / GAIA traces。 |
| 顶会匹配 | 9 | 符合 agent evaluation / reliability / debugging。 |
| 工程可行 | 8 | MVP 可控，但标注成本需确认。 |
| Baseline 清晰 | 8 | full-trace LLM judge、last-error、taxonomy classifier。 |
| 风险可控 | 5 | 最大威胁很强，必须继续收窄。 |

**总评**：7.0。原题 No-Go；第一版收窄题不能升 Promising；再次收窄题可作为谨慎 Narrow 继续验证，但不能进入 Phase 4 execution。

---

## 引用

- 空白分析 → `gap_analysis.md`
- 审稿攻击 → `adversarial_review.md`
- 一致性审计 → `file_consistency_check.md`
