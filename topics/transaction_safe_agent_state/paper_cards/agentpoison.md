# Paper Card: AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

## 1. 基本信息

- Title: AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases
- Year: 2024
- Venue: NeurIPS
- Authors: Zhaorun Chen; Zhen Xiang; Chaowei Xiao; Dawn Song; Bo Li
- Link: https://arxiv.org/abs/2407.12784
- Code: https://github.com/BillChan226/AgentPoison
- Benchmark / Dataset: autonomous driving, dialogue, healthcare agents

## 2. 它研究什么问题？

LLM agents 依赖长期 memory 或 RAG knowledge bases。攻击者可以投毒这些存储，使 agent 在未来检索到恶意 demonstrations 并执行目标动作。

## 3. 它的核心贡献是什么？

提出 AgentPoison，一种针对 memory/RAG 的 backdoor poisoning 方法，通过优化 trigger 让恶意内容高概率被检索，同时保持 benign performance。

## 4. 它的方法是什么？

把恶意 demonstrations 映射到独特 embedding 区域，使带 trigger 的查询检索到恶意 memory；攻击无需训练或 fine-tuning。

## 5. 它怎么实验？

### Task

autonomous driving、dialogue、healthcare agent。

### Dataset / Environment

对应 agent 的 memory / RAG knowledge base。

### Baselines

CPA、AutoDAN 等 poisoning/backdoor baselines。

### Metrics

retrieval success rate、end-to-end attack success rate、benign accuracy drop。

## 6. 它发现了什么失败模式？

长期 memory 一旦被投毒，agent 可在未来任务中被隐藏 trigger 控制，而且良性表现几乎不下降。

## 7. 它没有覆盖什么？

它不讨论 checkpoint/rollback/recovery，也不讨论恢复后如何隔离或撤销已写入 memory 的污染。

## 8. 它和我的课题有什么关系？

它证明 memory 是持久状态边界的一部分。本课题可把 AgentPoison 类 memory contamination 接到 recovery / branch semantics 中。

## 9. 它是否削弱我的创新性？

不会直接否定，但会削弱“memory poisoning 是新问题”的 claim。本课题应 claim recovery 后 memory hygiene，而不是 poisoning attack 本身。

## 10. 我可以从它的 limitation 里切什么？

污染 memory 是否带 provenance；agent rollback 后是否重新信任污染 memory；branch fork 是否隔离 memory writes。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
