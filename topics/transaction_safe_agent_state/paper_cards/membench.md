# Paper Card: MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents

## 1. 基本信息

- Title: MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents
- Year: 2025
- Venue: ACL Findings
- Authors: Haoran Tan; Zeyu Zhang; Chen Ma; Xu Chen; Quanyu Dai; Zhenhua Dong
- Link: https://aclanthology.org/2025.findings-acl.989/
- Code: https://github.com/import-myself/Membench
- Benchmark / Dataset: MemBench

## 2. 它研究什么问题？

LLM agent memory evaluation 往往只覆盖有限 memory levels 或单一交互场景，不能全面评价 memory effectiveness、efficiency、capacity。

## 3. 它的核心贡献是什么？

构建 MemBench，区分 factual memory 和 reflective memory，并区分 participation 与 observation 场景。

## 4. 它的方法是什么？

用多层 memory 任务和不同交互模式评估 agent memory 机制，比较多种 memory baselines。

## 5. 它怎么实验？

### Task

factual memory、reflective memory、participation、observation。

### Dataset / Environment

MemBench dataset。

### Baselines

FullMemory、RetrievalMemory、RecentMemory、GenerativeAgent、MemoryBank、MemGPT、SCMemory。

### Metrics

accuracy、recall、capacity、temporal efficiency。

## 6. 它发现了什么失败模式？

不同 memory 机制在记忆层次、容量、效率和交互模式上的能力差异明显。

## 7. 它没有覆盖什么？

它不是安全或 recovery benchmark，不研究 memory 是否来自可信分支、是否可撤销、是否在 rollback 后隔离。

## 8. 它和我的课题有什么关系？

它提供 memory evaluation 的维度，可用于设计 memory provenance / stale memory / branch contamination 的评测指标。

## 9. 它是否削弱我的创新性？

部分相关。它说明 memory evaluation 已有人做，但本课题可聚焦 transaction/recovery hygiene。

## 10. 我可以从它的 limitation 里切什么？

在 memory effectiveness 之外加入 provenance、branch id、write validity、post-recovery contamination。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：4
- 是否必须精读：是
- 是否作为 related work 核心论文：是
