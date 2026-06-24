# Topic Brief: Repair-Test Generation from Agent Failure Traces

> **版本**：v1
> **同步规则**：若 `gap_analysis.md` 收窄课题，本文件必须同步更新。

---

## 1. 一句话课题定义

给定已定位或可定位的 agent failure trace，生成可执行的 regression test 或具体 repair target，并用 rerun / counterfactual 验证该 artifact 是否阻断失败。

## 2. 核心失败模式

现有新近工作已经能定位 critical failure step / responsible component，但定位结果通常还没有直接转化为 developer-facing repair artifact。核心失败模式是：系统知道“哪里错了”，但仍不能自动生成能复现失败、验证修复、或指导改 prompt/tool schema/policy/planner 的最小测试。

## 3. 为什么重要

真实 agent 部署需要从“哪里错了”继续走到“如何验证修复”。AgentRx、TraceElephant、TRAIL 等已经推进了定位与归因；下一步若成立，应是把这些定位结果转成 regression tests、repair targets 和 rerun validation，从而真正降低调试成本。

## 4. 研究边界

### 保留

- repair-target recommendation
- executable regression test generation
- counterfactual rerun / intervention validation
- human debug time reduction
- 基于现有 localization datasets 的下游 artifact 生成

### 删除（本轮不做）

- 通用 trace localization
- issue taxonomy / failure category benchmark
- responsible agent / decisive step attribution
- 只做 multi-agent failure attribution
- 只预测 final success

## 5. 研究问题

**RQ1**: 已定位的 agent failure trace 能否自动转成可执行 regression test？

**RQ2**: root-cause category 与 failure evidence 能否映射到具体 repair target（prompt / tool schema / policy / retrieval / planner / handoff）？

**RQ3**: 生成的 test / repair target 能否通过 rerun 或 counterfactual validation 证明其阻断失败，并降低人工调试成本？

## 6. 预期贡献

1. 一个 failure-to-regression-test 的任务定义与小型 benchmark。
2. 一个从 failure evidence 到 repair target 的结构化表示。
3. 一个与 AgentRx validation log、AgentDebug corrective feedback、full-trace LLM suggestion 对比的 repair-test generation baseline。

## 7. 最危险 related work

| 论文 | 关系 |
|------|------|
| AgentRx | 最大威胁；覆盖 critical failure step、constraint validation log，可能自然扩展到 repair tests。 |
| AgentDebug | 最大威胁；覆盖 root-cause isolation 和 corrective feedback。 |
| TraceElephant | 最大威胁；覆盖 full execution trace attribution 与 counterfactual probing 基础。 |
| TRAIL | trace source / issue localization 强基线。 |
| Who&When | multi-agent attribution 强基线。 |

## 8. 当前最大风险

- 若 AgentRx / AgentDebug 已经覆盖 executable regression-test generation，本收窄题应 No-Go。
- 若无法构造可执行 test artifact，本方向会退化为自然语言 repair suggestion，创新性不足。
