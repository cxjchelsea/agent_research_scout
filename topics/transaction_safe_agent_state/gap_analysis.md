# Gap Analysis: Transaction-Safe Agent State Boundaries

> 文献库：见 `paper_table.csv`
> 精读核心集：见 `paper_cards/`（core_read=yes）

---

## 0. 课题收窄记录（如适用）

| 字段 | 内容 |
|------|------|
| **原始题目** | Transaction-Safe Agent State Boundaries |
| **风险** | ACRFence 可能已覆盖 semantic rollback attack 的核心 novelty。 |
| **建议新题目** | 待 Phase 3 深研后决定 |
| **一句话定义** | 暂以 `topic_brief.md` v1 为准 |
| **删除** | 通用 prompt injection defense、完整 agent framework、大规模 benchmark audit |
| **保留** | tool-effect ledger、memory provenance、credential invalidation、branch/replay semantics |
| **实验边界** | mock tool scenarios：email/payment/file/GitHub-like tasks |

---

## 1. 已有工作已经覆盖什么？

### 1.1 问题定义与形式化

| 子问题 | 代表论文 | 已覆盖 | 本案 scope |
|--------|----------|--------|------------|
| Semantic rollback attack | ACRFence | Action Replay、Authority Resurrection、replay-or-fork | 必须判断是否还有 memory provenance / branch contamination 空白 |
| Tool observation attack | AgentDojo | 间接 prompt injection 与动态工具环境 | 作为 tool boundary 风险背景 |
| Agent security attack taxonomy | ASB | prompt injection、memory poisoning、PoT backdoor、mixed attacks | 作为 memory/tool attack surface 背景 |
| Agent runtime / sandbox | OpenHands、SWE-agent、AutoGen | agent execution platform、ACI、多代理 conversation | 作为实际系统语境 |

### 1.2 方法与 benchmark 边界

- 待 Phase 3 深研补充：ACRFence 的具体假设、benchmark 规模、是否覆盖 memory writes、credential scope、multi-branch workflows。
- 待核验 ToolEmu / InjecAgent 与 ASB 的覆盖边界。
- 待补充 memory provenance、stale memory、memory poisoning 专门论文。

### 1.3 本案可 claim 的空白

1. 如果 ACRFence 只覆盖 external side effects，则可尝试收窄到 memory provenance + rollback / branch semantics。
2. 如果 ASB 只覆盖攻击成功率，而不覆盖恢复后的状态清理，则可尝试定义 state hygiene after attack / recovery。
3. 如果现有 framework 只提供 sandbox/checkpoint，但不提供 transaction semantics，则可做最小 state boundary benchmark。

---

## 2. 是否只是换名？

| 提案 | 判断 |
|------|------|
| “semantic rollback attack” 改名 | 高风险，ACRFence 已覆盖，不能直接作为核心 claim。 |
| “transaction-safe state boundary” | 待核验。只有在同时覆盖 tool effects、memory provenance、credential scope、branch semantics 且有新 benchmark 时才可能成立。 |
| “memory contamination after rollback” | 可能是可收窄方向，需补充 memory poisoning / memory update 文献。 |

---

## 3. 最危险 related work 正面比较

待 Phase 3 深研，至少比较：

1. ACRFence
2. AgentDojo
3. Agent Security Bench

---

## 4. 最小可行创新点（MVP）

**贡献类型**：Problem + Representation + Benchmark + Method（待确认）

1. 构造最小 mock tool benchmark，包含 irreversible write、one-time credential、memory write、branch restore。
2. 定义 state boundary event schema：tool effect、credential state、memory provenance、branch id。
3. 比较普通 retry、idempotency-key-only、ACRFence-like replay、memory quarantine / branch-aware replay。

---

## 5. 当前结论（gap 视角）

**方向判断**：继续进入 Phase 3 深研，但当前还不能给 Promising / Narrow / Go。

> 审稿人攻击见 `adversarial_review.md`
> 文件一致性见 `file_consistency_check.md`
> 阶段性决策见 `decision.md`

---

## 6. 核心论文

| # | 论文 | 角色 |
|---|------|------|
| 1 | ACRFence | 最大威胁 |
| 2 | AgentDojo | 工具边界安全 benchmark |
| 3 | Agent Security Bench | agent security / memory poisoning benchmark |
| 4 | OpenHands | agent runtime 语境 |
| 5 | SWE-agent | ACI 与 SWE agent 语境 |
