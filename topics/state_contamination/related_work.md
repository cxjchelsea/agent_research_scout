# Related Work: State Contamination in Long-Chain Tool-Using Agents

调研主题：**长链路工具型 Agent 中的状态污染与恢复盲区**

调研范围：2023–2026，20 篇高相关论文（按 5 类各 4 篇）

---

## 1. Agent Benchmark

| title | year | venue | type | problem | benchmark | metrics | limitation | relevance_to_state_contamination | relevance_score |
|-------|------|-------|------|---------|-----------|---------|------------|----------------------------------|-----------------|
| WebArena: A Realistic Web Environment for Building Autonomous Agents | 2024 | ICLR | Benchmark | 简化环境 vs 真实网页长链路任务 | WebArena（812 任务） | End-to-end success rate | 不追踪中间状态污染 | 错误写入 scratchpad/历史并 conditioning 后续步骤 | 6 |
| GAIA: A Benchmark for General AI Assistants | 2024 | ICLR | Benchmark | 通用 assistant 多步 tool-use 缺乏统一评测 | GAIA（466 题） | Quasi-exact match accuracy | 不暴露 retry 后 context 污染 | 多步轨迹累积中间结论 | 5 |
| SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | 2024 | ICLR | Benchmark | 真实 GitHub issue 修复能力 | SWE-bench Verified（500） | pass@1 / resolve rate | 不度量 dirty workspace / retry 污染 | CCRM 已在 Verified 上验证 retry 效应 | 6 |
| OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | 2024 | NeurIPS | Benchmark | 桌面 open-ended 任务缺少环境 | OSWorld（369 任务） | Task success rate | 不区分状态漂移与恢复 | 跨应用操作产生持久化系统状态 | 6 |

---

## 2. Tool-use / Web Agent / Software Agent

| title | year | venue | type | problem | benchmark | metrics | limitation | relevance_to_state_contamination | relevance_score |
|-------|------|-------|------|---------|-----------|---------|------------|----------------------------------|-----------------|
| SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | 2024 | NeurIPS | System | 通用 LM 接口不适合 code agent | SWE-bench / HumanEvalFix | pass@1 | 线性 history，无 rollback | 错误 edit 持续 conditioning | 7 |
| τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | 2024 | arXiv | Benchmark | 不测 policy + 多轮 + 状态一致性 | τ-bench retail/airline | pass@1 / pass^k | 不专门研究 retry 污染 | Stateful DB + 错误 API 调用 | 7 |
| ADVOCATE: Anticipatory Reflection for LLM Agents | 2024 | EMNLP Findings | Method | 事后 reflection 代价高 | WebArena | Task success rate | 无显式 state isolation | action 前反思，部分缓解 trajectory 污染 | 7 |
| OpenHands: An Open Platform for AI Software Developers as Generalist Agents | 2024 | arXiv | System | 开源 software agent 平台缺失 | SWE-bench / GAIA | Resolve rate | append-only 轨迹 | shell/file 状态 + message 双通道污染 | 6 |

---

## 3. Memory / Long-Horizon Agent

| title | year | venue | type | problem | benchmark | metrics | limitation | relevance_to_state_contamination | relevance_score |
|-------|------|-------|------|---------|-----------|---------|------------|----------------------------------|-----------------|
| MemGPT: Towards LLMs as Operating Systems | 2023 | arXiv | System | 有限 context 无法支撑长期交互 | MSC / document QA | LLM-judge / ROUGE-L | 错误 summary 可写入 persistent memory | 状态在 memory tier 间迁移的机制基础 | 7 |
| LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | 2025 | ICLR | Benchmark | 长期记忆能力缺乏系统评测 | LongMemEval（500 题） | QA accuracy | 不覆盖 executable tool state | 知识 update / 错误记忆持久化 | 7 |
| MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | 2026 | ICLR | Benchmark | memory 四能力缺乏统一 benchmark | MemoryAgentBench | 四能力分项 accuracy | 未覆盖 tool side-effect | selective forgetting 与 incremental accumulation | 8 |
| State Contamination in Memory-Augmented LLM Agents | 2026 | arXiv | Problem+Method | 写回前未 sanitize → memory laundering | Multi-session agent 仿真 | SPG / Δμ / P95_tox | 聚焦 memory safety | **直接定义 state contamination** | **10** |

---

## 4. Agent Failure Analysis / Evaluation

| title | year | venue | type | problem | benchmark | metrics | limitation | relevance_to_state_contamination | relevance_score |
|-------|------|-------|------|---------|-----------|---------|------------|----------------------------------|-----------------|
| AgentDebug: Where LLM Agents Fail and How They Can Learn From Failures | 2025 | arXiv | Benchmark+Method | 早期错误 cascade，缺乏 modular taxonomy | AgentErrorBench | All-correct / step accuracy | 无显式 state rollback | memory 错误是最常见 cascade 源 | 8 |
| TRAIL: Trace Reasoning and Agentic Issue Localization | 2025 | arXiv | Benchmark+Taxonomy | trace 缺乏 step-level 诊断 | TRAIL（148 traces） | Joint localization accuracy | 不评 clean restart | 长链路 trace failure taxonomy | 7 |
| Which Agent Causes Task Failures and When? | 2025 | ICML | Benchmark | 多 agent 失败难以自动归因 | Who&When | Agent 53.5% / step 14.2% | 非 single-agent state 管理 | 定位传播链责任 step | 6 |
| AgentRx: Diagnosing AI Agent Failures from Execution Trajectories | 2026 | ICML | Benchmark+Method | 长链路失败难以 localize | AgentRx（115 trajectories） | Step localization | 无 rollback 协议 | critical step 信号可触发 recovery | 6 |

---

## 5. Recovery / Rollback / State Management

| title | year | venue | type | problem | benchmark | metrics | limitation | relevance_to_state_contamination | relevance_score |
|-------|------|-------|------|---------|-----------|---------|------------|----------------------------------|-----------------|
| GA-Rollback: Generator-Assistant Stepwise Rollback Framework for LLM Agent | 2025 | EMNLP | Method | one-pass 错误 thought 永久写入 trajectory | AlfWorld / WebShop 等 | Task success rate | 未处理 irreversible tool effect | **stepwise rollback 代表方法** | **9** |
| Why Retrying Fails: Context Contamination in LLM Agent Pipelines | 2026 | arXiv | Theory+Empirical | failed attempt 污染 retry（CCRM） | SWE-bench Verified | pass@K / ε1/ε0=7.1 | 理论假设 step IID | **直接形式化 context contamination** | **10** |
| ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore | 2026 | arXiv | Method | checkpoint-restore 导致 duplicate side-effect | Agent CR PoC | Attack / mitigation rate | 聚焦 security | **rollback ≠ undo 外部 world state** | **9** |
| Hell or High Water: Evaluating Agentic Recovery from External Failures | 2025 | arXiv | Benchmark | 外部 tool 失败时 backup plan 能力未知 | Hell-or-High-Water（830） | Success under failure | 非 self-caused contamination | recovery blind spot 广泛存在 | 7 |

---

## 初步空白判断

1. **已有**：context contamination 形式化（CCRM）、memory laundering（State Contamination）、stepwise rollback（GA-Rollback）、checkpoint 安全（ACRFence）。
2. **空白**：尚无 benchmark **同时**度量（a）长链路 tool state 污染程度、（b）clean-restart vs dirty-retry 差距、（c）外部 world state 与 context state 的不一致。
3. **可切入**：在 SWE-bench Verified / WebArena / τ-bench 上构造 **contamination-aware retry benchmark**，对比 pass@k vs pass^k vs clean-restart@k。
