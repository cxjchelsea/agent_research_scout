# Paper Card: MemoryAgentBench

## 1. 基本信息

- Title: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (MemoryAgentBench)
- Year: 2026
- Venue: ICLR 2026
- Authors: Yuanzhe Hu, Yu Wang, Julian McAuley (UCSD)
- Link: https://arxiv.org/abs/2507.05257
- Code: https://github.com/（论文指向 dataset HuggingFace Kakezh/MemoryAgentBench）
- Benchmark / Dataset: MemoryAgentBench（2071 题；含 EventQA, FactConsolidation 等新集）

## 2. 它研究什么问题？

Memory agent 的四能力——**准确检索、测试时学习、长程理解、选择性遗忘**——缺乏在 **incremental multi-turn** 场景下的统一 benchmark；现有 long-context QA benchmark 不能反映 agent 逐步累积 state 的过程。

## 3. 它的核心贡献是什么？

- 提出 **MemoryAgentBench** 统一评测框架。
- 将 long-context 数据集重构为 multi-turn incremental feed。
- 新增 EventQA（检索）、FactConsolidation（**selective forgetting**）。
- 评测 MemGPT、RAG、MIRIX、Mem0 等 memory agents。

## 4. 它的方法是什么？

- 模拟 agent 逐 chunk 接收信息（非一次性注入）。
- 四能力分项评测 + 跨架构对比（RAG / long-context / agentic memory）。

## 5. 它怎么实验？

### Task

AR / TTL / LRU / SF 四能力 QA。

### Dataset / Environment

重构 NIAH 等 + EventQA + FactConsolidation；2071 questions。

### Baselines

GPT-4o-mini full-context；Self-RAG；MemGPT；Mem0；MIRIX 等。

### Metrics

四能力分项 accuracy。

## 6. 它发现了什么失败模式？

- Commercial memory systems **信息压缩损失**（Mem0 fact extraction）。
- 缺乏 temporal/structural metadata → 检索失败。
- **Selective forgetting** 普遍弱：错误/过时 fact 难以 purge。
- RAG 擅 AR 但 LRU 弱；long-context 成本高。

## 7. 它没有覆盖什么？

- **无 tool side-effect**、无 executable state（file/DB/bash）。
- 无 rollback / checkpoint / retry contamination。
- 偏 textual memory，非 SWE/web agent trajectory。
- 未连接 CCRM 或 state contamination 术语。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| memory | ✓ |
| long-horizon | ✓ incremental |
| selective forgetting | ✓ 与污染清除相关 |
| tool-use | ✗ |
| rollback | ✗ |
| contamination | 间接（错误 memory 持久化） |

## 9. 它是否削弱我的创新性？

**部分覆盖（benchmark 维度）。**

- 若我做 memory-only contamination benchmark → 与 MemoryAgentBench + Wang et al. state contamination **重叠**。
- 若我做 **tool-agent dual-state benchmark** → 互补。

## 10. 我可以从它的 limitation 里切什么？

1. 扩展 SF 任务为 **Tool-State Forgetting**：错误 file edit 需 rollback。
2. 在 incremental feed 中注入 **failed attempt** 测 contamination。
3. 复用 MemoryAgentBench 协议，增加 executable env channel。

## 11. 重要引用句

> "Existing benchmarks ... do not reflect the interactive, multi-turn nature of memory agents that incrementally accumulate information."

> Four competencies: accurate retrieval, test-time learning, long-range understanding, and selective forgetting.

## 12. 我的判断

- 相关度：4 / 5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
