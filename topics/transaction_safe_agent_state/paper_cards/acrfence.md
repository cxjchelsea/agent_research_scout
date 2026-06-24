# Paper Card: ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore

## 1. 基本信息

- Title: ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore
- Year: 2026
- Venue: arXiv
- Authors: ACRFence authors
- Link: https://arxiv.org/abs/2603.20625
- Code: 未核验
- Benchmark / Dataset: proof-of-concept rollback attacks

## 2. 它研究什么问题？

LLM agent checkpoint-restore 只能回滚本地状态，不能回滚已经提交到外部服务的副作用。恢复后 agent 可能重新生成语义相近但参数不同的工具调用，外部服务会把它当作新请求。

## 3. 它的核心贡献是什么？

提出 semantic rollback attacks，并区分 Action Replay 与 Authority Resurrection。提出 ACRFence，在工具边界记录不可逆效果，并在恢复后执行 replay-or-fork 语义。

## 4. 它的方法是什么？

在工具调用边界维护 effect log。恢复后新工具调用与历史效果做语义比较：同一意图 replay 历史结果，不同意图必须 fork，已消费凭证不能复活。

## 5. 它怎么实验？

### Task

围绕 checkpoint-restore 后的支付、凭证、外部服务调用等不可逆副作用构造攻击。

### Dataset / Environment

proof-of-concept scenarios。

### Baselines

普通 checkpoint/retry、传统 idempotency 假设、现有恢复机制。

### Metrics

重复副作用、凭证复活、拦截效果。

## 6. 它发现了什么失败模式？

agent 恢复后会重新合成工具请求，传统程序的“同一请求可安全重试”假设失效。

## 7. 它没有覆盖什么？

从当前发现阶段看，它主要聚焦 external side effects 和 credentials。是否覆盖长期 memory 写入、memory provenance、跨分支污染，需要 Phase 3 进一步精读确认。

## 8. 它和我的课题有什么关系？

这是最大威胁。若它已经覆盖 tool effect、credential、memory provenance、branch semantics，本课题应 No-Go 或强收窄。

## 9. 它是否削弱我的创新性？

部分覆盖到高度覆盖之间。当前判断为 **最大威胁**。

## 10. 我可以从它的 limitation 里切什么？

可能从 memory provenance、rollback 后 memory quarantine、multi-branch contamination、attack-cleanup after recovery 切入。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
