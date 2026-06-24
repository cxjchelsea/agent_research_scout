# Topic Brief: Agentic Regression Scenarios for Tool-Using Agent Failures

> **版本**：v1
> **同步规则**：若 `gap_analysis.md` 收窄课题，本文件必须同步更新。

---

## 1. 一句话课题定义

给定 tool-using / multi-step agent 的 failure trace 与诊断证据，生成可重放的 agentic regression scenario，用于验证 scaffold / prompt / tool schema / policy / memory / handoff 修复是否阻断同类失败。

## 2. 核心失败模式

现有新近工作已经能定位 critical failure step / responsible component，软件工程领域也已有大量 failure/bug/stack trace 到 reproducing test 的传统。但 agent workflow 的失败往往依赖用户目标、tool schema、policy、mock backend state、memory/retrieval、handoff protocol 和非代码 scaffold。核心失败模式是：系统知道“哪里错了”，但缺少可重放的 agentic regression scenario 来验证 agent-level 修复。

## 3. 为什么重要

真实 agent 部署需要从“哪里错了”继续走到“如何验证修复”。AgentRx、TraceElephant、TRAIL 等已经推进了定位与归因；传统软件测试已经推进了 crash / issue reproduction。本题若继续，必须聚焦 agent-specific scenario artifact，而不是传统 unit test 或自然语言修复建议。

## 4. 研究边界

### 保留

- agentic regression scenario generation
- tool / policy / memory / handoff mock state reconstruction
- fail/pass oracle for rerun validation
- human debug time reduction
- 基于现有 localization datasets 的 agent-level scenario artifact 生成

### 删除（本轮不做）

- 通用 trace localization
- issue taxonomy / failure category benchmark
- responsible agent / decisive step attribution
- 传统软件 crash reproduction / bug reproduction test generation
- 只做自然语言 repair suggestion
- 只预测 final success

## 5. 研究问题

**RQ1**: 已定位的 tool-using agent failure trace 能否自动转成可重放 agentic regression scenario？

**RQ2**: scenario 是否能包含足够的 environment state、tool/policy/mock backend、memory/retrieval 和 oracle，使其区别于传统软件 unit test？

**RQ3**: 生成的 scenario 能否通过 rerun 或 counterfactual validation 证明 agent-level 修复阻断失败，并降低人工调试成本？

## 6. 预期贡献

1. 一个 failure-trace-to-agentic-scenario 的任务定义与小型 benchmark。
2. 一个 agentic regression scenario schema（goal、environment state、tool mocks、policy/memory context、oracle）。
3. 一个与 AgentRx validation log、AgentDebug corrective feedback、传统 issue-to-test generator 对比的 scenario generation baseline。

## 7. 最危险 related work

| 论文 | 关系 |
|------|------|
| AgentRx | 最大威胁；覆盖 critical failure step、constraint validation log，可能提供 oracle 线索。 |
| AgentDebug | 最大威胁；覆盖 root-cause isolation 和 corrective feedback。 |
| TraceElephant | 最大威胁；覆盖 full execution trace attribution 与 counterfactual probing 基础。 |
| ReCrash / EvoCrash / Issue2Test / BRT Agent / Echo | 跨领域威胁；覆盖传统软件 failure / issue / stack trace 到 reproducing test。 |
| TRAIL | trace source / issue localization 强基线。 |
| Who&When | multi-agent attribution 强基线。 |

## 8. 当前最大风险

- 若输出退化成传统 software bug reproduction test，本方向应 No-Go。
- 若无法表达 agent-specific scenario state / tool mocks / policy oracle，本方向会退化为自然语言 repair suggestion，创新性不足。
