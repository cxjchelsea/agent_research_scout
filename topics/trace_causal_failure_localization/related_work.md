# Related Work: Trace-Causal Failure Localization for Agent Workflows

> 文献库：见 `paper_table.csv`
> 精读核心集：见 `paper_cards/`（core_read=yes）

---

## 1. Trace Diagnosis and Issue Localization

TRAIL 是本方向的最大威胁之一。它已经把 agent evaluation 从 end-to-end success 推到 step-level trace analysis，并使用 GAIA / SWE-bench Lite 派生 148 条 OpenTelemetry-style traces，标注 841 个 reasoning / planning / execution errors。它强覆盖“trace reasoning / issue localization / error taxonomy”。

AgentRx 进一步覆盖 failed trajectory diagnosis：它定义 critical failure step，用 tool schemas 与 domain policies 合成 executable constraints，逐步检查 constraint violations，并生成 auditable validation log。它的 115 条 manually annotated failed trajectories 来自 tau-bench、Flash、Magentic-One，已非常接近“causal failure step localization”。

AgentDebug / AgentErrorBench 也覆盖 root-cause failure isolation 和 corrective feedback。它把错误分到 memory、reflection、planning、action、system modules，并报告 targeted feedback 可提升 task success。

## 2. Multi-Agent Failure Taxonomy and Attribution

MAST 提供 multi-agent failure taxonomy：14 个 failure modes，覆盖 specification、inter-agent misalignment、task verification 等类别。它说明 multi-agent failure 不是单步推理错误，而是跨 agent 协调、规范理解和验证失败的组合。

Who&When 正式提出 automated failure attribution for LLM multi-agent systems，标注 failure-responsible agent 与 decisive error step。TraceElephant 进一步提供 full execution traces 与 reproducible environments，证明完整观测比 partial observation 更适合 developer-facing debugging。

这些工作使“识别哪个 agent / 哪一步导致失败”这个方向已经很拥挤。

## 3. Agent Benchmarks as Trace Sources

SWE-bench、GAIA、AgentBench、WebArena、OSWorld、tau-bench、AppWorld、TheAgentCompany 都可作为 trace source 或 failure environment。它们本身多数关注 final success、state-based checks 或 task completion，不一定提供 causal labels；但 TRAIL、AgentRx、TraceElephant 已经开始把这些 benchmark 转成 failure diagnosis datasets。

## 4. Failure Representation and Repair Targets

当前可保留的空白不再是“failure localization 本体”，而是 localization 之后的 developer-facing artifact：

1. 从 critical failure step 生成可执行 regression test；
2. 从 root-cause category 生成具体 repair target（prompt / tool schema / policy / retrieval / planner / handoff）；
3. 用 counterfactual rerun 验证修复目标是否真的阻断失败；
4. 评估定位结果是否降低人工 debug time，而不是只提升 attribution accuracy。

## 5. 当前结论

- 原始题目 **Trace-Causal Failure Localization for Agent Workflows** 被强覆盖，不建议按原题继续。
- 建议收窄为：**Repair-Test Generation from Agent Failure Traces**。
- 该收窄方向仍需继续核验 AgentRx、AgentDebug、TraceElephant 是否已覆盖 regression-test generation。
