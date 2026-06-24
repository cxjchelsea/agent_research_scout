# Paper Card: Evaluating Very Long-Term Conversational Memory of LLM Agents

## 1. 基本信息

- Title: Evaluating Very Long-Term Conversational Memory of LLM Agents
- Year: 2024
- Venue: ACL
- Authors: Adyasha Maharana; Dong-Ho Lee; Sergey Tulyakov; Mohit Bansal; Francesco Barbieri; Yuwei Fang
- Link: https://aclanthology.org/2024.acl-long.747/
- Code: https://github.com/snap-research/locomo
- Benchmark / Dataset: LoCoMo

## 2. 它研究什么问题？

现有长期对话评价不足以测试跨很多 session 的 long-term conversational memory。

## 3. 它的核心贡献是什么？

构建 LoCoMo，非常长期、多 session、多模态对话 benchmark，用于测试 QA、event summarization 和 dialogue generation。

## 4. 它的方法是什么？

通过 LLM-based agent architecture 生成长对话，再由人工验证和编辑，以保证长期一致性和 event graph grounding。

## 5. 它怎么实验？

### Task

question answering、event summarization、multi-modal dialogue generation。

### Dataset / Environment

10 个长期 conversation，每个可达数百轮和多 session。

### Baselines

long-context LLMs、RAG methods。

### Metrics

QA accuracy、summarization/dialogue generation quality。

## 6. 它发现了什么失败模式？

LLM 对长程 temporal / causal dynamics 的理解仍明显落后于人类；RAG 和长上下文只能部分改善。

## 7. 它没有覆盖什么？

它不处理工具副作用或 checkpoint recovery，也不测试 memory write 是否被污染或是否可以撤销。

## 8. 它和我的课题有什么关系？

它说明长期 memory 有 temporal consistency 难题。本课题可以借用 temporal validity 概念，但需要转向 tool/memory state boundary。

## 9. 它是否削弱我的创新性？

低到中。它覆盖 long-term memory benchmark，不覆盖 transaction-safe recovery。

## 10. 我可以从它的 limitation 里切什么？

把 temporal memory consistency 扩展成 recovery 后 memory validity 和 branch-specific memory。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：3
- 是否必须精读：是
- 是否作为 related work 核心论文：是
