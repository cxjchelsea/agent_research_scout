# Topic Brief: Recovery-Safe Memory Provenance for Tool-Using Agents

> **版本**：v2
> **同步规则**：若 `gap_analysis.md` 收窄课题，本文件必须同步更新。

---

## 1. 一句话课题定义

研究 tool-using LLM agent 在 checkpoint、rollback、retry 或分支恢复后，如何为长期 memory 写入维护 provenance、branch 与 validity 信息，避免污染记忆在恢复后被无声复用。

## 2. 核心失败模式

Agent 本地执行轨迹可以回滚或分支，但长期 memory / store 往往跨 thread 或跨 session 持久存在。攻击性 observation、错误工具结果或失败分支中的中间结论一旦写入 memory，恢复后的 agent 可能继续检索并信任它，导致污染记忆复用、分支语义混淆和恢复后状态不干净。

## 3. 为什么重要

真实 agent 系统越来越依赖 checkpoint、human-in-the-loop recovery、自动重试和长期 memory。ACRFence 已指出外部副作用不可自动回滚；AgentPoison、ASB 和 MPBench 说明 memory poisoning 是真实攻击面。两者交界处的问题是：恢复机制可能清理了本地轨迹，却没有清理或隔离已写入的长期 memory。

## 4. 研究边界

### 保留

- Memory provenance：记录 memory item 的来源 observation、tool call、branch id、checkpoint id、写入阶段和可信状态。
- Recovery / branch semantics：定义哪些 memory 写入可跨分支复用，哪些必须 quarantine、invalidate 或重新验证。
- Tool-output-to-memory pipeline：关注工具结果、恶意 observation、错误中间结论如何进入长期 memory。
- 最小 mock benchmark：email/payment/file/GitHub-like tasks 中的 memory write / rollback / retrieval scenarios。

### 删除（本轮不做）

- 泛化 external side-effect rollback 防御（ACRFence 已覆盖主要问题）。
- 通用 prompt injection 或 memory poisoning attack 设计。
- 完整 agent framework 或生产级 runtime。
- 大规模 SWE-bench / WebArena 复现实验。

## 5. 研究问题

**RQ1**: 现有 agent checkpoint / retry / recovery 机制在哪些 memory write / retrieval 场景下会保留失败分支或攻击性 observation 的污染状态？

**RQ2**: 能否用 memory provenance schema（source observation、tool call、branch id、checkpoint id、validity state）形式化这些失败？

**RQ3**: 一个最小 quarantine / branch-aware retrieval 机制是否能降低 recovery 后的污染记忆复用，同时保持合理的 benign memory utility？

## 6. 预期贡献

1. 问题贡献：定义 recovery-induced memory contamination failure mode。
2. 表示贡献：提出 recovery-safe memory provenance schema。
3. Benchmark / Method 贡献：构造最小 memory rollback benchmark，并比较普通 persistent memory、prompt guard、ACRFence-like side-effect logging 与 branch-aware memory quarantine。

## 7. 最危险 related work

| 论文 | 关系 |
|------|------|
| ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore | 最大威胁；覆盖 external side-effect rollback，但未确认覆盖 memory provenance。 |
| AgentDojo | 工具边界与 adversarial observation benchmark，说明 tool outputs 可劫持 agent。 |
| Agent Security Bench (ASB) | 覆盖 memory poisoning、tool attacks 和 security-utility trade-off。 |
| AgentPoison | 证明长期 memory / RAG poisoning 可以产生未来行为影响。 |
| MemBench / LoCoMo / Mem0 | 提供长期 memory evaluation 与 memory architecture 语境。 |

## 8. 当前最大风险

- 若 ACRFence 已覆盖 memory provenance 或 store-level rollback，本课题会被削弱，需要 No-Go 或进一步收窄。
- 如果 benchmark 只证明 memory poisoning，而没有 recovery / branch 变量，会与 ASB / AgentPoison 撞车。
- 如果方法只是给 memory 加标签而没有改变 retrieval / quarantine 行为，会有 engineering-only 风险。
