# Paper Card: AgentTelemetry

> **card_status**：close_read
> **是否最大威胁 work**：否

## 1. 基本信息

- Title: AgentTelemetry: A Fault Detection Benchmark and Toolkit for LLM Agent Observability
- Year: 2026
- Venue: OpenReview
- Authors: AgentTelemetry authors
- Link: https://openreview.net/attachment?id=owdmAYFk6k&name=pdf
- Code: https://github.com/Krishnachaitanyakc/AgentTelemetry
- Benchmark / Dataset: AgentTelemetry

## 2. 它研究什么问题？

现有 OpenTelemetry / GenAI telemetry 不能表示 planning、reasoning、guardrails、delegation、memory 等 agent-specific spans，导致 fault detection 不完整。

## 3. 它的核心贡献是什么？

1. 9 种 agent-specific span kinds。
2. 14 种 fault types。
3. 2940 configurations 的 controlled evaluation harness。
4. 多框架 adapters。
5. SWE-bench Lite case study。

## 4. 它的方法是什么？

扩展 OpenTelemetry span taxonomy，让 agent lifecycle 的关键阶段都能被结构化观测。

## 5. 它怎么实验？

### Task

Fault detection and observability coverage。

### Dataset / Environment

Controlled benchmark + SWE-bench Lite case study。

### Metrics

Fault Detection Rate；patch-rate lift。

## 6. 它发现了什么失败模式？

reasoning loops、stale retrieval、guardrail bypass、planning failure、memory corruption 等 agent-specific faults 对 vanilla telemetry 不可见。

## 7. 它没有覆盖什么？

它偏 observability/representation，不直接做 critical failure step attribution 或 repair generation。

## 8. 它和我的课题有什么关系？

为 trace representation 和 span taxonomy 提供强相关基础。

## 9. 它是否削弱我的创新性？

中等削弱。若 C1 做 span schema，会被覆盖；若做 repair/test generation，仍可用它作 instrumentation baseline。

## 10. 我可以从它的 limitation 里切什么？

基于 agent-specific spans 生成 causal slices 和 regression tests。

## 11. 重要引用句

- “9 agent-specific span kinds”
- “14 fault types”
- “reasoning loops account for 75% of agent failures”

## 12. 我的判断

- 相关度：4
- 是否必须精读：是
- 是否作为 related work 核心论文：是
