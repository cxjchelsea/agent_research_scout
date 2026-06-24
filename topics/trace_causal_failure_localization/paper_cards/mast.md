# Paper Card: Why Do Multi-Agent LLM Systems Fail?

> **card_status**：close_read
> **是否最大威胁 work**：是

## 1. 基本信息

- Title: Why Do Multi-Agent LLM Systems Fail?
- Year: 2025
- Venue: arXiv
- Authors: MAST authors
- Link: https://arxiv.org/pdf/2503.13657v2
- Code:
- Benchmark / Dataset: MAST

## 2. 它研究什么问题？

系统分析 multi-agent LLM systems 的失败模式，并提出 MAST taxonomy。

## 3. 它的核心贡献是什么？

1. 分析多个开源 MAS framework 的 execution traces。
2. 总结 14 个 failure modes，分成 specification、inter-agent misalignment、task verification 等类别。
3. 构建 LLM-as-a-judge pipeline，并用人工标注验证。

## 4. 它的方法是什么？

使用 grounded theory 对 MAS traces 做人工分析，形成 taxonomy，再验证自动判断 pipeline。

## 5. 它怎么实验？

### Task

Failure taxonomy and scalable diagnosis。

### Dataset / Environment

多种 MAS frameworks 与任务 traces。

### Baselines

人工标注与 LLM-as-a-judge。

### Metrics

Cohen's kappa / judge agreement。

## 6. 它发现了什么失败模式？

MAS failure 不只是单 agent 推理错误，还包括 agent 间信息错配、任务验证失败、规范理解问题等。

## 7. 它没有覆盖什么？

它偏 taxonomy 和 judge pipeline，不主打 decisive step localization、critical failure step 或 repair artifact generation。

## 8. 它和我的课题有什么关系？

提供 root-cause category 的重要 taxonomy 基线。

## 9. 它是否削弱我的创新性？

部分削弱。若 C1 只做 failure category taxonomy，会被覆盖；若做 repair/test generation，仍可能有空间。

## 10. 我可以从它的 limitation 里切什么？

将 taxonomy category 连接到 minimal failing trace slice 和 repair target。

## 11. 重要引用句

- “14 distinct failure modes, clustered into 3 categories”
- “LLM-as-a-judge evaluation pipeline integrated with MAST”

## 12. 我的判断

- 相关度：4
- 是否必须精读：是
- 是否作为 related work 核心论文：是
