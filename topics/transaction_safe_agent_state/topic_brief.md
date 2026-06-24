# Topic Brief: Transaction-Safe Agent State Boundaries

> **版本**：v1
> **同步规则**：若 `gap_analysis.md` 收窄课题，本文件必须同步更新。

---

## 1. 一句话课题定义

研究 LLM agent 在 checkpoint、rollback、retry 或分支恢复后，如何避免 local agent state 与外部工具副作用、权限令牌、持久记忆之间产生不可见的不一致。

## 2. 核心失败模式

Agent 本地状态可以回滚，但外部世界通常不能回滚：邮件已发送、支付已提交、文件已删除、一次性 token 已消费、memory 已写入。恢复后的 agent 可能重新生成语义相近但不完全相同的工具调用，使外部服务把它视为新请求，导致重复副作用、权限复活、污染记忆复用或分支语义混淆。

## 3. 为什么重要

真实 agent 系统越来越依赖 checkpoint、human-in-the-loop recovery、自动重试和多分支探索。如果状态边界不清楚，agent 的“恢复能力”会反过来制造安全和可靠性问题：重复执行不可逆操作、复用已失效授权、把攻击内容写入长期记忆，或在不同分支之间泄漏状态。

## 4. 研究边界

### 保留

- Tool-effect ledger：记录不可逆工具副作用与结果。
- Memory provenance：记录长期 memory 的来源、分支、可信度和写入时机。
- Credential invalidation：处理一次性凭证、短期授权和恢复后的权限复活。
- Branch / replay semantics：区分同一意图 replay、语义分叉 fork、危险重复执行。
- 最小 mock tool benchmark：email/payment/file/GitHub-like tasks。

### 删除（本轮不做）

- 通用 prompt injection 防御。
- 完整 agent framework 或生产级 runtime。
- 大规模 SWE-bench / WebArena 复现实验。
- 投稿级安全审计或全量 related work 扩库。

## 5. 研究问题

**RQ1**: 现有 agent checkpoint / retry / recovery 机制在哪些工具副作用、memory 写入和授权状态下会产生不可见不一致？

**RQ2**: 能否用统一的 state boundary 表示（tool-effect ledger + memory provenance + branch semantics）形式化这些失败？

**RQ3**: 一个最小 replay-or-fork / quarantine 机制是否能降低重复副作用、权限复活和 memory 污染复用，同时保持合理的 benign recovery success？

## 6. 预期贡献

1. 问题贡献：定义 transaction-safe agent state boundary failure taxonomy。
2. 表示贡献：提出用于工具副作用、memory provenance 与分支恢复的统一状态边界表示。
3. Benchmark / Method 贡献：构造最小 mock tool benchmark，并比较普通 retry、idempotency-key-only、ACRFence-like replay 与本案机制。

## 7. 最危险 related work

| 论文 | 关系 |
|------|------|
| ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore | 最大威胁；已直接覆盖 semantic rollback attacks，需要检查是否完整覆盖本案 claim。 |
| AgentDojo | 工具边界与 adversarial observation benchmark，说明 tool outputs 可劫持 agent。 |
| Agent Security Bench (ASB) | 覆盖 memory poisoning、tool attacks 和 security-utility trade-off。 |
| ToolEmu | 外部工具风险模拟相关；需核验是否覆盖 irreversible side effects。 |
| OpenHands / SWE-agent | 真实 software agent runtime 与 agent-computer interface 场景。 |

## 8. 当前最大风险

- ACRFence 可能已经覆盖核心 novelty，本课题必须在 Phase 3 中正面比较并收窄到 ACRFence 未覆盖的 memory provenance、credential scope 或 multi-branch workflow。
- 如果 benchmark 全是 mock tool，可能被认为太人工；需要确保任务足够贴近 email/payment/file/GitHub 等真实工具语义。
- 如果方法只是 checkpoint + retry + prompt guard 的工程组合，会有 engineering-only 风险。
