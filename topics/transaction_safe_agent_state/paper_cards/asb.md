# Paper Card: Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents

## 1. 基本信息

- Title: Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents
- Year: 2025
- Venue: ICLR
- Authors: Hanrong Zhang; Jingyuan Huang; Kai Mei; others
- Link: https://arxiv.org/abs/2410.02644
- Code: https://github.com/agiresearch/ASB
- Benchmark / Dataset: ASB

## 2. 它研究什么问题？

LLM agent 同时使用外部工具和 memory，攻击面覆盖 system prompt、user prompt、tool usage、memory retrieval 等多个阶段。

## 3. 它的核心贡献是什么？

提出 ASB，系统化 formalize 并 benchmark LLM agent 的攻击和防御，覆盖 direct/indirect prompt injection、memory poisoning、Plan-of-Thought backdoor 和 mixed attacks。

## 4. 它的方法是什么？

构建 10 个场景、10 类 agent、400+ tools、27 种 attack/defense，评估不同 LLM backbone 的 utility/security trade-off。

## 5. 它怎么实验？

### Task

e-commerce、finance、autonomous driving 等 agent scenarios。

### Dataset / Environment

ASB benchmark。

### Baselines

10 prompt injection attacks、memory poisoning attack、PoT backdoor、mixed attacks、11 defenses。

### Metrics

7 个 utility/security metrics，包括平衡 utility 和 security 的指标。

## 6. 它发现了什么失败模式？

Agent 越能遵循指令，越可能被恶意指令、工具返回或 memory retrieval 操控。现有 defense 效果有限。

## 7. 它没有覆盖什么？

ASB 关注攻击和防御成功率，不直接研究 checkpoint/retry/recovery 后如何清理、隔离或回滚 memory 和 tool state。

## 8. 它和我的课题有什么关系？

它为 memory poisoning 和 tool attack surface 提供强证据。我的课题应避免重新做 ASB，而是关注 recovery 后 state hygiene。

## 9. 它是否削弱我的创新性？

部分覆盖安全维度，但不覆盖 transaction-safe recovery 的核心机制。

## 10. 我可以从它的 limitation 里切什么？

攻击写入 memory 后，agent 恢复或分支执行时是否继续复用污染状态；defense 后状态是否真正 clean。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
