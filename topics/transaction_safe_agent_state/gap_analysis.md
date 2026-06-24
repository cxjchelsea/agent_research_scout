# Gap Analysis: Recovery-Safe Memory Provenance for Tool-Using Agents

> 文献库：见 `paper_table.csv`
> 精读核心集：见 `paper_cards/`（core_read=yes）

---

## 0. 课题收窄记录（如适用）

| 字段 | 内容 |
|------|------|
| **原始题目** | Transaction-Safe Agent State Boundaries |
| **风险** | ACRFence 已强覆盖 checkpoint-restore 下的 external side effects 与 credential resurrection。 |
| **建议新题目** | Recovery-Safe Memory Provenance for Tool-Using Agents |
| **一句话定义** | 研究 tool-using agent 在 rollback/retry/fork 后如何避免失败分支或攻击性 observation 写入的长期 memory 被无声复用。 |
| **删除** | 泛化 external side-effect rollback 防御、通用 prompt injection 防御、完整 agent framework |
| **保留** | memory provenance、branch/checkpoint id、validity state、quarantine / branch-aware retrieval |
| **实验边界** | mock tool + memory scenarios：email/payment/file/GitHub-like observations 写入 memory 后 rollback/retrieval |

---

## 1. 已有工作已经覆盖什么？

### 1.1 问题定义与形式化

| 子问题 | 代表论文 | 已覆盖 | 本案 scope |
|--------|----------|--------|------------|
| Semantic rollback attack | ACRFence | Action Replay、Authority Resurrection、tool-effect replay-or-fork | 本案删除泛化 rollback claim，转向 memory provenance |
| Tool observation attack | AgentDojo | 间接 prompt injection 与动态工具环境 | 作为 tool-output-to-memory 风险背景 |
| Agent security attack taxonomy | ASB | prompt injection、memory poisoning、PoT backdoor、mixed attacks | 作为 memory poisoning 背景，但不重复做 attack benchmark |
| Memory poisoning | AgentPoison、MPBench、MINJA | memory/RAG 被投毒后未来检索触发恶意行为 | 本案关注 recovery/fork 后污染 memory 是否被复用 |
| Memory capability evaluation | MemBench、LoCoMo、Mem0 | memory effectiveness、capacity、temporal reasoning、production efficiency | 本案借用 memory utility 指标，加入 provenance / validity |
| Agent runtime / checkpoint systems | OpenHands、SWE-agent、AutoGen、LangGraph | agent execution、checkpoint、replay、fork、store/checkpointer 分离 | 作为工程现实性，不作为 novelty |

### 1.2 方法与 benchmark 边界

- ACRFence 是必须正面比较的 baseline，但目前从发现材料看它主攻 external side effects 与 credential resurrection，而不是 memory write provenance。
- AgentPoison / ASB / MPBench 证明 memory poisoning 真实存在，但它们主要测攻击成功率，不测 recovery 后 memory state 是否干净。
- MemBench / LoCoMo / Mem0 可提供 memory utility 评估维度，避免防御机制只会 quarantine 一切 memory。

### 1.3 本案可 claim 的空白

1. **Recovery-induced memory contamination**：失败分支或攻击 observation 写入长期 memory 后，即使 agent rollback，本地轨迹已恢复但 memory store 仍被污染。
2. **Branch-stale memory reuse**：从旧 checkpoint fork 出新分支后，agent 仍检索到不属于当前分支或已被 invalidate 的 memory item。
3. **Provenance-aware retrieval**：为 memory item 绑定 checkpoint/branch/tool-source/validity metadata，并在 recovery 后控制是否可检索。

---

## 2. 是否只是换名？

| 提案 | 判断 |
|------|------|
| “semantic rollback attack” 改名 | 不可做。ACRFence 已覆盖。 |
| “transaction-safe state boundary” | 过宽，容易被 ACRFence 和普通系统事务语义夹击。 |
| “recovery-safe memory provenance” | 可继续。它不是 memory poisoning 本身，也不是 external side-effect rollback，而是二者交界处的持久状态一致性问题。 |

---

## 3. 最危险 related work 正面比较

| 论文 | 已覆盖 | 未覆盖 / 本案切口 |
|------|--------|------------------|
| ACRFence | checkpoint-restore 后 external side effects 与 credential resurrection；replay-or-fork | 未明确覆盖长期 memory write provenance、污染 memory quarantine、branch-aware retrieval |
| AgentDojo | tool-returned untrusted data 的 prompt injection benchmark | 不研究被污染 observation 是否写入 long-term memory，也不研究 recovery 后复用 |
| ASB | agent security taxonomy 和 memory poisoning attack | 不专注 recovery / rollback 后的状态清理 |
| AgentPoison | 证明 memory / RAG poisoning 可持久影响未来 agent 行为 | 不处理 checkpoint、branch、rollback 或 memory validity |
| MemBench / LoCoMo / Mem0 | memory capability 与 production memory architecture | 不处理 malicious provenance 或 recovery-induced contamination |

---

## 4. 最小可行创新点（MVP）

**贡献类型**：Problem + Representation + Benchmark + Method

1. 构造最小 benchmark：tool observation 写入 memory → rollback/fork/retry → 后续任务检索 memory。
2. 定义 memory provenance schema：memory_id、source_tool_call、source_observation、checkpoint_id、branch_id、validity_state、trust_state。
3. 比较普通 persistent memory、prompt guard、ACRFence-like tool-effect log、branch-aware memory quarantine / provenance-filtered retrieval。

---

## 5. 当前结论（gap 视角）

**方向判断**：Narrow。原始 C3 过宽，应收窄为 **Recovery-Safe Memory Provenance for Tool-Using Agents**。该方向有 MVP 路径，但仍需更精确核验 ACRFence 是否完全排除了 memory provenance 空白。

> 审稿人攻击见 `adversarial_review.md`
> 文件一致性见 `file_consistency_check.md`
> 阶段性决策见 `decision.md`

---

## 6. 核心论文

| # | 论文 | 角色 |
|---|------|------|
| 1 | ACRFence | 最大威胁；external side-effect rollback baseline |
| 2 | AgentDojo | tool observation attack benchmark |
| 3 | Agent Security Bench | agent memory poisoning / security benchmark |
| 4 | AgentPoison | memory/RAG poisoning evidence |
| 5 | ToolEmu | tool-risk sandbox / MVP inspiration |
| 6 | MemBench | memory capability metric source |
| 7 | LoCoMo | long-term temporal memory benchmark |
| 8 | Mem0 | production memory architecture baseline |
