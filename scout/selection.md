# Selection: agent_research_scout_2026_06_24

> **Phase**：Selection
> **生成日期**：2026-06-24
> **来源**：`scout/candidates.md`
> **用途**：记录用户最终选定的方向，作为创建 `topics/<slug>/` 的依据

> Agent 不得自行替用户做最终选择；用户确认后再填写本文件。

---

## 1. 选定方向

- **Selected topic**：Transaction-Safe Agent State Boundaries
- **Selected slug**：`transaction_safe_agent_state`
- **candidate_id**：C3

---

## 2. 选择理由

用户已明确选择 C3。该方向在发现阶段排名第一，主要原因是问题真实、MVP 可构造、工程边界清晰，并且直接贴近 agent checkpoint / rollback / retry 后的外部副作用、权限状态和 memory 状态一致性问题。最大威胁 work ACRFence 已明确，适合在 Phase 3 通过深研快速判断是否仍有可切空白。

---

## 3. 为什么没有选择其他候选

| 未选候选 | candidate_id | 主要放弃原因 |
|----------|--------------|--------------|
| Cross-Benchmark Trace Failure Diagnosis | C1 | 仍然很有潜力，但 AgentRx / TRAIL 已经非常接近，需要更高标注和 schema 设计成本。 |
| Policy-Consistent Tool-Use Reliability | C4 | 实验可控，但容易被认为是 tau-bench 的小扩展，需要更强差异化。 |
| Preference Drift and Memory Hygiene for Personal Agents | C2 | 方向重要，但 2025–2026 memory / personalization benchmark 增长很快，撞车风险较高。 |
| SWE Agent Benchmark Integrity Diagnostics | C5 | 实用价值高，但容易变成 benchmark audit，论文贡献边界较弱。 |

---

## 4. 进入 Phase 3 的初始问题定义

- **一句话定义**：研究 LLM agent 在 checkpoint、rollback、retry 或分支恢复后，如何避免 local agent state 与外部工具副作用、权限令牌、持久记忆之间产生不可见的不一致。
- **核心失败模式 / 机制问题**：agent 本地状态可回滚，但外部服务状态、一次性凭证和持久 memory 无法自动回滚，导致重复执行、权限复活、污染记忆复用或分支语义混淆。
- **预期贡献类型**（A/B/C/D/E）：A/B/C/D。
- **研究边界**（保留 / 删除）：保留 tool-effect ledger、memory provenance、credential invalidation、branch/replay semantics；删除通用 prompt injection defense、泛化 agent framework、投稿级 benchmark audit。

---

## 5. 需要重点核验的 related work

| 论文 | verified_status | 为何必须深研阶段核验 |
|------|-----------------|----------------------|
| ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore | verified | 最大威胁；必须判断它是否已经覆盖 transaction-safe state boundary 的核心 claim。 |
| AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | verified | 工具边界与 adversarial observation 的 benchmark 底座。 |
| Agent Security Bench (ASB) | verified | 覆盖 memory poisoning、tool attacks 和 security-utility trade-off。 |
| OpenHands | verified | 真实软件 agent runtime / sandbox / evaluation 平台，可作为系统语境。 |
| SWE-agent | verified | Agent-computer interface 与 SWE agent 工具交互基线。 |

---

## 6. 下一步

- [x] 创建 `topics/transaction_safe_agent_state/`
- [x] 从 `templates/` 复制深研模板
- [x] 进入 Phase 3 Deep Dive
