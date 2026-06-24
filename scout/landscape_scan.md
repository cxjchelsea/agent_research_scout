# Landscape Scan: Agent Research Scout 2026-06-24

> **Phase**：Discovery
> **生成日期**：2026-06-24

---

## 1. 扫描边界

- **领域**：AI / LLM Agent
- **时间范围**：优先 2023–2026，重点使用 2024–2025 顶会、arXiv 与官方 benchmark 页面；少量 2026 work 作为高威胁信号。
- **是否受用户偏好约束**：无。本轮重新从 Phase 1 Discovery 开始，扫描通用 Agent 研究空间。
- **排除范围**：不做投稿级 related work 扩库；不创建 `topics/<topic>/`；不做 paper cards；不把 blog/二手综述作为最大威胁核心依据。

---

## 2. 方向地图（按八大类或子簇）

| 类别 / 子方向 | 代表性工作（verified） | 已覆盖什么 | 明显空白 | 是否值得出候选 |
|---------------|------------------------|------------|----------|----------------|
| Agent 失败模式与 trace diagnosis | TRAIL；MAST；Who&When；SWE-bench；GAIA | 已有 trace benchmark、MAS failure taxonomy、失败归因初步数据集；证明现有模型做 trace debugging 很弱 | 缺少跨单/多 agent、跨工具/记忆/环境的 causal failure localization；缺少把失败定位接到修复或 regression test 的可复现协议 | 是，C1 |
| 长期个人 Agent / memory agent | LoCoMo；LongMemEval；MemBench；Mem0；Letta Memory Benchmark critique；AgentPoison | 已有长期会话记忆、知识更新、temporal reasoning、记忆系统比较和 memory poisoning | 现有 benchmark 多测 retrieval/QA，较少测 memory write provenance、过期事实隔离、冲突更新、恶意/错误记忆的生命周期 | 是，C3 |
| workflow / tool-use / software engineering agent | SWE-bench；AppWorld；BFCL；tau-bench；TheAgentCompany；ToolEmu | 已有 GitHub issue、app API、function calling、客户服务、多步骤办公任务和 tool risk benchmarks | 对“任务成功但造成 collateral damage”的度量仍弱；工具调用正确性、策略合规、状态副作用通常分开评估 | 是，C2 / C4 |
| 多智能体协作系统 | AgentVerse；MetaGPT；ChatDev；MultiAgentBench；MAST；Who&When | 已有协作框架、SOP、多 agent benchmark、failure taxonomy 和 attribution 数据 | 很多工作仍偏“框架比拼”；缺少在失败发生时自动判断应改 agent、改协议、改角色、还是改单步工具使用的机制 | 是，C5 |
| agent evaluation / benchmark / trace diagnosis | AgentBench；GAIA；WebArena；VisualWebArena；OSWorld；TRAIL | 已有通用、网页、视觉网页、桌面、trace 等多维 benchmark | benchmark 越来越多但诊断粒度不统一；很难把分数下降映射到可操作修复 | 是，支撑 C1 / C4 |
| 状态管理、回滚、恢复、状态污染 | ACRFence；ToolEmu；AgentDojo；AppWorld；TheAgentCompany | checkpoint-restore、irreversible tool effect、prompt injection、state-based evaluation 已出现 | 2026 ACRFence 对 rollback/tool side effect 威胁很强；若做状态方向必须避开“semantic rollback attack”已覆盖内容，切到 memory/write provenance 或 collateral damage 的新边界 | 谨慎，作为 C2/C3 威胁 |
| 个性化、长期适应、用户变化建模 | LoCoMo；LongMemEval；Mem0；MemBench | 已覆盖长期用户事实、知识更新、temporal QA、选择性记忆 | 用户偏好变化、过期记忆 quarantine、跨任务/跨工具的 memory invalidation 仍未充分形式化 | 是，C3 |
| 真实工程系统可靠性 | SWE-bench；TheAgentCompany；AppWorld；OSWorld；tau-bench | 已有真实或仿真的软件工程、办公、桌面、客户服务环境 | 缺少统一的 side-effect ledger、collateral damage 指标、以及“成功但不应算成功”的审计协议 | 是，C4 |

---

## 3. 跨方向观察

- **重复出现的 failure mode**：长链路任务中的错误传播、工具/环境状态不可见、局部成功导致全局副作用、记忆更新后事实过期、multi-agent 中责任归因困难。
- **被多个方向共同忽略的问题**：当前 benchmark 多数能判 final success，但不能稳定回答“哪一步错、错因是什么、是否造成不可逆副作用、该修复 agent 组件还是评估协议”。
- **术语/撞车风险**：state rollback 方向会被 ACRFence 强烈威胁；memory 方向会被 Mem0 / MemBench / LongMemEval 威胁；tool safety 会被 AgentDojo / ToolEmu / tau-bench 威胁；multi-agent framework 改进容易被 MetaGPT / AgentVerse / ChatDev 认为只是工程组合。
- **近期高威胁论文**（可能直接否决候选）：
  - ACRFence：覆盖 checkpoint-restore 下 irreversible tool effects 的 replay-or-fork 语义。
  - AgentDojo：覆盖动态 prompt injection 与 utility/security trade-off。
  - MemBench / LongMemEval / Mem0：覆盖长期记忆评测与记忆系统设计。
  - TRAIL / MAST / Who&When：覆盖 trace diagnosis、MAS failure taxonomy、失败归因。
  - AppWorld / TheAgentCompany：覆盖 app/API/办公任务的 state-based evaluation。

---

## 4. 发现阶段论文索引说明

- 广搜索引文件：`scout/discovery_paper_table.csv`
- 目标规模：通常 **30–50 篇**；本轮写入 30 条 verified 条目，覆盖 5 个候选方向。
- 本阶段 **不要求** `paper_cards/`；精读、claim coverage matrix、Phase 3.5 targeted verification 留给用户选中课题之后。

---

## 5. 本轮候选生成原则

1. 不选择“再做一个通用 agent benchmark”这类过宽方向。
2. 优先选择能在 2–4 个月内用现有 benchmark 派生 MVP 的方向。
3. 每个候选至少有 3 条 discovery table 支撑，并标明最大 verified 威胁。
4. 不把 `uncertain` 作为核心否定依据；本轮候选核心条目均为 verified。
