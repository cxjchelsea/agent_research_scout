# Gap Analysis: Trace-Causal Failure Localization for Agent Workflows

> 文献库：见 `paper_table.csv`
> 精读核心集：见 `paper_cards/`（core_read=yes）

---

## 0. 课题收窄记录（如适用）

| 字段 | 内容 |
|------|------|
| **原始题目** | Trace-Causal Failure Localization for Agent Workflows |
| **风险** | TRAIL、AgentRx、TraceElephant、Who&When 已经覆盖 trace issue localization、critical failure step、responsible component / decisive step attribution。 |
| **建议新题目** | Repair-Test Generation from Agent Failure Traces |
| **一句话定义** | 给定已定位的 agent failure trace，生成可执行的 regression test 或具体 repair target，并用 rerun / counterfactual 验证该 artifact 是否阻断失败。 |
| **删除** | 通用 trace localization、issue taxonomy、只预测 responsible step / agent、单纯 multi-agent failure attribution |
| **保留** | repair-target recommendation、regression-test generation、counterfactual rerun validation、人类调试成本降低 |
| **实验边界** | 优先复用 TRAIL / AgentRx / TraceElephant 的 traces 或 schema，避免重新造 localization benchmark |

---

## 1. 已有工作已经覆盖什么？

### 1.1 问题定义与形式化

| 子问题 | 代表论文 | 已覆盖 | 本案 scope |
|--------|----------|--------|------------|
| Trace issue localization | TRAIL | step-level trace analysis、reasoning/planning/execution taxonomy、148 traces / 841 errors | 不再作为主 claim；只能作为 trace source / baseline |
| Critical failure step diagnosis | AgentRx | failed trajectory diagnosis、critical failure step、constraint validation log、115 trajectories | 不再主张 critical step localization；转向 repair/test artifact |
| Full-observability failure attribution | TraceElephant | full execution traces、responsible component、decisive step、reproducible environments | 不再主张 attribution benchmark；可用其环境做 counterfactual validation |
| Multi-agent failure taxonomy | MAST | 14 failure modes 与 LLM-as-judge pipeline | taxonomy 可作为 label space |
| Agent / step attribution | Who&When | failure-responsible agent 和 decisive error step | multi-agent attribution 已覆盖 |

### 1.2 方法与 benchmark 边界

- 已有工作覆盖了 localization / taxonomy / attribution 的主要问题。
- 仍待核验的边界：定位结果是否能自动转成 regression test、repair target 或 verified intervention。

### 1.3 本案可 claim 的空白

1. 从 failure localization 输出到 executable regression test。
2. 从 root-cause category 到 concrete repair target（prompt / tool schema / policy / retrieval / planner / handoff）。
3. 用 rerun / counterfactual execution 验证 repair target 是否阻断失败。

---

## 2. 是否只是换名？

| 提案 | 判断 |
|------|------|
| Trace-Causal Failure Localization | 基本是 TRAIL + AgentRx + TraceElephant + Who&When 的组合，不建议作为原题继续。 |
| Repair-Test Generation from Agent Failure Traces | 不是简单换名；它把输出从“定位失败”改为“生成可执行修复/回归验证 artifact”，但仍需继续核验 AgentDebug / AgentRx 是否已经覆盖。 |

---

## 3. 最危险 related work 正面比较

（至少 3 篇，逐篇对比维度）

### 3.1 Claim Coverage Matrix（最大威胁 1–3 篇必填）

| Threat work | Claim component | Covered by threat work? | Evidence | Implication |
|-------------|-----------------|--------------------------|----------|-------------|
| TRAIL | 核心问题定义 | yes | paper card: step-level analysis of traced agentic workflows; 148 traces / 841 errors | 原始 trace localization claim 被覆盖 |
| TRAIL | proposed mechanism | partial | structured traces + taxonomy + benchmark, but not repair-test generation | 可作为 baseline / data source |
| AgentRx | 核心问题定义 | yes | paper card: pinpoints critical failure step in failed agent trajectory | 原始 causal step localization 被覆盖 |
| AgentRx | proposed mechanism | yes | constraints + auditable validation log + LLM judge | 方法空间被强占 |
| AgentRx | benchmark / evaluation setting | yes | 115 failed trajectories across tau-bench, Flash, Magentic-One | 新 benchmark 空间小 |
| TraceElephant | 核心问题定义 | yes | responsible agent/component and decisive failure step | attribution claim 被覆盖 |
| TraceElephant | benchmark / evaluation setting | yes | 220 full execution traces + reproducible environments | full trace attribution benchmark 被覆盖 |
| Who&When | 核心问题定义 | yes | identifies failure-responsible agent and decisive error step | multi-agent attribution 被覆盖 |
| AgentDebug | utility / risk trade-off | partial | root-cause isolation + corrective feedback improves task success | repair-target 方向仍有强威胁 |

> 如果最大威胁 work 的 Evidence 为空，或 paper card 未达到 `threat_verified`，不得把 Phase 3 判定为 complete。

### 3.2 Phase 3.5b：收窄题补充核验

| 核验问题 | 结论 | Evidence | Implication |
|----------|------|----------|-------------|
| AgentDebug 是否已经覆盖 repair target / executable test generation？ | partial | AgentDebug isolates root-cause failures and provides corrective / actionable feedback, then re-rolls out the agent. It evaluates recovery and task success, but retrieved evidence does not show generation of executable regression tests as standalone artifacts. | 它强覆盖 repair feedback / targeted remediation；收窄题不能只做 natural-language repair target，必须输出可执行 test/scenario artifact。 |
| AgentRx validation log 是否自然等价于 regression test artifact？ | partial / no | AgentRx synthesizes executable constraints, checks them step-by-step, and outputs validation logs (`checker_results`, `judge_output`). These logs are executable diagnostics/oracles, but not complete tests: they lack standalone setup, replay harness, fail-pass criterion, and patch validation loop. | AgentRx validation log 可作为 oracle / evidence source，但不等价 regression test artifact。收窄题必须显式生成 runnable replay/test case。 |
| 软件工程 / debugging / test generation 是否已有 failure trace → regression test 强相关工作？ | yes, strong adjacent coverage | ReCrash generates unit tests from preserved object states; EvoCrash uses crash stack traces to generate reproducing tests; Issue2Test / BRT Agent / Echo / iCoRe generate bug reproduction tests from issue reports, stack traces, execution feedback, and repository context. | “failure/bug trace → reproducing/regression test”在传统软件工程里已非常成熟；若本案只做软件 crash/bug reproduction，会 No-Go。必须再次收窄到 agent-specific workflow traces。 |

### 3.3 再次收窄建议

不建议把题目维持为宽泛的 **Repair-Test Generation from Agent Failure Traces**，因为软件测试领域已有强相关传统。更合适的下一版题目是：

**Agentic Regression Scenarios for Tool-Using Agent Failures**

一句话定义：给定 tool-using / multi-step agent 的 failure trace 与诊断证据，生成可重放的 agentic regression scenario（初始环境、用户目标、tool/policy/mock state、预期 failure oracle），用于验证 scaffold / prompt / tool-schema / policy 修复是否阻断同类失败。

这个定义避开传统软件 crash reproduction 的主战场，也区别于 AgentRx / AgentDebug：

- 输出不是自然语言 corrective feedback，而是可运行的 agentic scenario。
- oracle 不只是 violation log，而是可用于 rerun 的 fail/pass criterion。
- repair target 不限代码 patch，也包括 prompt、tool schema、policy、memory/retrieval、handoff protocol。

---

## 4. 最小可行创新点（MVP）

**贡献类型**：Method / Benchmark / System

1. 输入：已有 failure trace + localization label；输出：可执行 regression test 或 repair target。
2. Baseline：AgentRx validation log、AgentDebug corrective feedback、full-trace LLM repair suggestion。
3. Metric：regression test validity、failure reproduction rate、post-repair rerun success、human debug time reduction。

---

## 5. 当前结论（gap 视角）

**方向判断**：原始方向 No-Go；第一版收窄题被软件测试领域强相关工作压缩，不应升为 Promising。建议再次收窄为 **Agentic Regression Scenarios for Tool-Using Agent Failures**，当前 decision 维持 Narrow。

> 审稿人攻击见 `adversarial_review.md`
> 文件一致性见 `file_consistency_check.md`
> 阶段性决策见 `decision.md`

---

## 6. 核心论文

| # | 论文 | 角色 |
|---|------|------|
| 1 | TRAIL | 最大威胁 / trace diagnosis |
| 2 | AgentRx | 最大威胁 / critical failure step diagnosis |
| 3 | TraceElephant | 最大威胁 / full trace attribution |
| 4 | Which Agent Causes Task Failures and When? | 最大威胁 / attribution |
| 5 | Why Do Multi-Agent LLM Systems Fail? | taxonomy |
| 6 | AgentDebug | root-cause + corrective feedback |
