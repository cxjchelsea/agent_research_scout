# Paper Card: Identifying the Risks of LM Agents with an LM-Emulated Sandbox

## 1. 基本信息

- Title: Identifying the Risks of LM Agents with an LM-Emulated Sandbox
- Year: 2024
- Venue: ICLR
- Authors: ToolEmu authors
- Link: https://openreview.net/forum?id=GEcwtMk1uA
- Code: 未核验
- Benchmark / Dataset: ToolEmu

## 2. 它研究什么问题？

Tool-use agents 可能在高风险工具环境中造成数据泄漏、金融损失等严重后果，但真实搭建每个工具 sandbox 成本很高。

## 3. 它的核心贡献是什么？

提出 ToolEmu，用 LM 模拟工具执行和 sandbox 状态，以更低成本发现 agent 的 long-tail 高风险行为。

## 4. 它的方法是什么？

用 LM 扮演工具 emulator 和 safety evaluator，也引入 adversarial emulator 主动构造更容易暴露风险的 sandbox 状态。

## 5. 它怎么实验？

### Task

高风险工具套件中的 agent 行为测试。

### Dataset / Environment

36 toolkits、144 test cases。

### Baselines

不同 LM agents 和 safety prompts。

### Metrics

failure rate、risk severity、人类验证的有效失败比例。

## 6. 它发现了什么失败模式？

Agent 会在工具环境中执行潜在严重后果的动作，即使有安全提示也不能完全避免。

## 7. 它没有覆盖什么？

ToolEmu 关注单次工具执行风险，不直接建模 checkpoint、replay、branch、memory provenance 或 external state 不可回滚的问题。

## 8. 它和我的课题有什么关系？

它提供了 mock/emulated tool benchmark 的方法参考。本课题可以借鉴它构造 email/payment/file/GitHub-like tools，但加入 recovery 和 transaction semantics。

## 9. 它是否削弱我的创新性？

部分相关。它削弱“工具风险模拟”本身的新颖性，但不覆盖 rollback/recovery state boundary。

## 10. 我可以从它的 limitation 里切什么？

在 ToolEmu 式 sandbox 中增加 state history、irreversible effects、replay/fork 语义和 memory writes。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：4
- 是否必须精读：是
- 是否作为 related work 核心论文：是
