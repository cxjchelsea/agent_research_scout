# Related Work: Recovery-Safe Memory Provenance for Tool-Using Agents

> **状态**：Phase 3 Deep Dive 更新版。
> **文献库**：见 `paper_table.csv`。
> **当前 scope**：从 broad transaction-safe state boundary 收窄到 recovery / rollback / branch 后的 memory provenance 与污染隔离。

---

## 1. Checkpoint / Rollback / Recovery Semantics

ACRFence 是本课题的最大威胁。它已经定义 semantic rollback attacks，指出 LLM agent 在 checkpoint-restore 后会重新生成语义相近但参数不同的工具请求，导致 external side effects 重复执行或 consumed credentials 复活。其 mitigation 是 tool-boundary effect log 和 replay-or-fork。

这意味着本课题不能再把“外部副作用不可回滚”作为核心新颖性。可保留的空白只能来自 ACRFence 未充分覆盖的部分：长期 memory / store 写入、失败分支 memory provenance、恢复后 retrieval quarantine，以及 tool observation 到 persistent memory 的污染路径。

LangGraph persistence / time-travel 文档说明，真实 agent framework 已支持 checkpoint、replay、fork、store 和 checkpointer 分离；这提供了工程现实性，但不是论文贡献。

## 2. Tool-Boundary Security and Prompt Injection

AgentDojo 和 ASB 证明 tool outputs 与 observations 是 agent 安全边界。AgentDojo 关注 indirect prompt injection，在动态工具环境中同时衡量 benign utility 和 attack success。ASB 覆盖 direct/indirect prompt injection、memory poisoning、Plan-of-Thought backdoor 和 mixed attacks。

ToolEmu 提供 LM-emulated sandbox，可在不搭建真实工具环境的情况下发现高风险工具行为。它对本课题的启发是：MVP 可以用 emulated / mock tools 快速构造，但必须避免只做“工具风险模拟”的重复工作。

这些工作覆盖 attack / defense 成功率，但通常不问：攻击或错误 observation 是否被写入长期 memory？恢复或 fork 后，这些 memory 是否还会被检索？这就是本课题当前的切入点。

## 3. Memory Poisoning and Persistent Memory Risk

AgentPoison 证明长期 memory 或 RAG knowledge base 可以被投毒，未来检索时触发恶意行为。ASB 也将 memory poisoning 纳入 agent security benchmark。MPBench 和 MINJA 进一步指出，memory poisoning 不一定等价于 prompt injection；攻击可能发生在 write phase，并在后续 retrieval phase 才表现出来。

这些工作强烈支持“memory 是持久 agent state”的判断。但它们主要研究攻击如何成功，不直接研究 checkpoint/recovery/fork 后如何撤销、隔离或标记 memory writes。

因此，本课题应避免 claim “memory poisoning 是新问题”，而应 claim “recovery-induced memory contamination / branch-stale memory reuse” 是现有 poisoning benchmark 没有正面评测的状态一致性问题。

## 4. Memory Evaluation and Memory Architecture

MemBench、LoCoMo、Mem0 提供长期 memory evaluation 与 scalable memory architecture 语境。MemBench 强调 memory effectiveness、efficiency、capacity 与不同交互场景；LoCoMo 强调长期多 session 中 temporal / causal memory；Mem0 强调 production memory 的 extraction、update、retrieval、token cost 与 latency。

这些工作有助于设计 memory utility 指标，避免本课题只降低攻击但破坏正常记忆能力。但它们不处理 memory provenance 是否与 checkpoint、branch、tool observation 和 recovery 绑定。

## 5. Software Agent Runtime and Agent-Computer Interfaces

OpenHands、SWE-agent、AutoGen 说明 agent runtime、sandbox、tool use、multi-agent conversation 和 evaluation platform 已经成熟。它们提供真实应用场景，但不构成本课题的主要 novelty。

## 6. 当前文献地图结论

已有工作分别覆盖：

- **rollback external side effects**：ACRFence；
- **tool/prompt security**：AgentDojo、ASB、ToolEmu；
- **memory poisoning**：AgentPoison、ASB、MPBench、MINJA；
- **memory capability evaluation**：MemBench、LoCoMo、Mem0；
- **agent runtime**：OpenHands、SWE-agent、AutoGen、LangGraph。

当前可能成立的空白是：**当 agent recovery / rollback / branch 与 long-term memory write/retrieval 同时存在时，现有 benchmark 没有明确评估污染 memory 是否会跨恢复边界被复用，也没有要求 memory item 绑定 branch/checkpoint provenance 与 validity state。**
