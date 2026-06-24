# Paper Card: Where Agents Fail and How They Can Learn From Failures

> **card_status**：close_read
> **是否最大威胁 work**：是

## 1. 基本信息

- Title: Where Agents Fail and How They Can Learn From Failures
- Year: 2025
- Venue: OpenReview / arXiv
- Authors: AgentDebug authors
- Link: https://openreview.net/pdf?id=PFR4E8583W
- Code: https://github.com/ulab-uiuc/AgentDebug
- Benchmark / Dataset: AgentErrorBench

## 2. 它研究什么问题？

Agent failures 会在 memory、reflection、planning、action、system modules 中级联传播，现有系统缺少模块化错误理解与恢复框架。

## 3. 它的核心贡献是什么？

1. AgentErrorTaxonomy：覆盖 memory、reflection、planning、action、system 的错误类型。
2. AgentErrorBench：从 ALFWorld、GAIA、WebShop 标注 failure trajectories。
3. AgentDebug：定位 root-cause failures 并提供 corrective feedback。

## 4. 它的方法是什么？

两阶段 debugging pipeline：理解/检测 root-cause failure，再生成 targeted corrective feedback 让 agent recover。

## 5. 它怎么实验？

### Task

Failure detection and recovery。

### Dataset / Environment

ALFWorld、GAIA、WebShop。

### Baselines

强 LLM debugging baselines。

### Metrics

All-correct accuracy、step accuracy、task success rate。

## 6. 它发现了什么失败模式？

早期 root-cause error 会传播到后续步骤；模块化 taxonomy 可以帮助 targeted feedback 和恢复。

## 7. 它没有覆盖什么？

它已经覆盖 root-cause 和 corrective feedback，但未必覆盖 full execution observability 或 regression-test generation。

## 8. 它和我的课题有什么关系？

它直接威胁“root-cause localization + repair feedback”方向。

## 9. 它是否削弱我的创新性？

强削弱。如果本案收窄到 repair-target recommendation，也必须正面对比 AgentDebug。

## 10. 我可以从它的 limitation 里切什么？

从 corrective feedback 转向可执行 regression tests 或 developer-facing patch targets。

## 11. 重要引用句

- “AgentErrorTaxonomy”
- “Agent Error Benchmark”
- “AgentDebug ... isolates root-cause failures and provides corrective feedback”

## 12. 我的判断

- 相关度：5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
