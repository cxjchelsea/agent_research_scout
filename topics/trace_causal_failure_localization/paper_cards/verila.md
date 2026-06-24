# Paper Card: VeriLA

> **card_status**：close_read
> **是否最大威胁 work**：否

## 1. 基本信息

- Title: VeriLA: A Human-Centered Evaluation Framework for Interpretable Verification of LLM Agent Failures
- Year: 2025
- Venue: CHI HEAL Workshop
- Authors: Yoo Yeon Sung, Hannah Kim, Dan Zhang
- Link: https://megagon.ai/publications/verila-eval-framework/
- Code:
- Benchmark / Dataset: VeriLA case study

## 2. 它研究什么问题？

Compound AI systems 中 LLM agents 的 failures 很难被人理解和检查，人工审计成本高。

## 3. 它的核心贡献是什么？

1. 人定义 agent criteria。
2. 训练 human-aligned agent verifier。
3. 给 agent execution output 做 interpretable verification。
4. 降低 human cognitive load。

## 4. 它的方法是什么？

把任务分解成可验证的 agent criteria，用 verifier 模块评估每个 agent output 是否符合人类标准。

## 5. 它怎么实验？

### Task

Human-centered verification of agent failures。

### Dataset / Environment

Case study，偏 compound AI / reasoning。

### Metrics

Verifier performance、人类交互效率。

## 6. 它发现了什么失败模式？

opaque reasoning、human expectation mismatch、agent dependency complexity 会让失败难以审计。

## 7. 它没有覆盖什么？

不主打 execution trace causal attribution，也不提供大型 benchmark。

## 8. 它和我的课题有什么关系？

相关于 human audit reduction 和 interpretable failure verification。

## 9. 它是否削弱我的创新性？

轻到中等。它覆盖 human-centered verification，但不覆盖 full trace causal repair/test generation。

## 10. 我可以从它的 limitation 里切什么？

把 interpretable verification 接到 trace slices 与 regression tests。

## 11. 重要引用句

- “human-centered evaluation framework”
- “human-aligned agent verifier”
- “reduce human effort and make these agent failures interpretable”

## 12. 我的判断

- 相关度：3
- 是否必须精读：是
- 是否作为 related work 核心论文：是
