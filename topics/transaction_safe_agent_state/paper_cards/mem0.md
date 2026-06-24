# Paper Card: Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

## 1. 基本信息

- Title: Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory
- Year: 2025
- Venue: arXiv
- Authors: Prateek Chhikara; Dev Khant; Saket Aryan; Taranjeet Singh; Deshraj Yadav
- Link: https://arxiv.org/abs/2504.19413
- Code: 未核验
- Benchmark / Dataset: LoCoMo and memory benchmarks

## 2. 它研究什么问题？

Production AI agents 需要可扩展长期 memory，以支持多 session consistency，同时降低 token cost 和 latency。

## 3. 它的核心贡献是什么？

提出 Mem0，通过 extraction、update、retrieval 管线维护 salient memory；Mem0-g 用 graph memory 表示关系结构。

## 4. 它的方法是什么？

从对话中抽取和更新关键事实，将 memory 存入可检索结构，并在回答时检索相关 memory；graph variant 连接实体关系。

## 5. 它怎么实验？

### Task

long-term memory QA 和多类别 memory benchmark。

### Dataset / Environment

LoCoMo 等 memory benchmarks。

### Baselines

full-context、RAG、MemoryBank、MemGPT、A-Mem、ReadAgent 等。

### Metrics

accuracy、LLM-as-a-judge score、token cost、latency。

## 6. 它发现了什么失败模式？

长期 memory 系统需要在准确率、token 成本、延迟之间取舍；简单扩展上下文不适合作为生产方案。

## 7. 它没有覆盖什么？

它不关注 memory 被攻击、来自哪个分支、是否过期、是否应在 rollback 后被 quarantine。

## 8. 它和我的课题有什么关系？

它代表 production memory architecture，提醒本课题的 memory provenance 机制不能只停留在安全抽象，也要考虑 update/retrieval 成本。

## 9. 它是否削弱我的创新性？

低到中。它覆盖 scalable memory，不覆盖 transaction-safe state boundary。

## 10. 我可以从它的 limitation 里切什么？

为 memory item 增加 provenance、branch、validity、rollback generation，并测量成本/延迟。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：3
- 是否必须精读：是
- 是否作为 related work 核心论文：是
