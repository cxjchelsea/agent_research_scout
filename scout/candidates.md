# Candidate Directions: agent_research_scout_2026_06_24

> **Phase**：Discovery
> **生成日期**：2026-06-24
> **扫描范围**：见 `scout/landscape_scan.md`
> **用途**：从广搜中提出 3–7 个候选方向，供人工选择 1 个进入 `topics/<topic>/` 深研

**candidate_id 规则**：本轮使用 C1–C5，与 `discovery_paper_table.csv` 的 `candidate_id` 列对齐。

**论据要求**：每个进入候选表的方向，至少在 `discovery_paper_table.csv` 中有 3 篇 verified 或 uncertain 来源支撑；最大威胁 work 必须 verified。

---

## 1. 扫描摘要

本轮广搜覆盖 Agent evaluation、SWE agents、tool-use/workflow、long-term memory、多智能体、security、state management 与 trace diagnosis，共写入 40 条发现阶段索引。最明显的趋势是：Agent 任务 benchmark 已经很多，但“失败为什么发生、状态如何污染、重试是否安全、结果是否可复现”仍没有被统一处理。候选方向因此不建议从“再做一个大而全 benchmark”切入，而应从可诊断、可验证、可构造 MVP 的失败机制切入。

---

## 2. 候选方向概览

| Rank | ID | 候选名称 | 一句话定义 | 贡献类型 | 支撑论文数 | 总分（/10） | 档位 | 最大威胁 | 推荐度 |
|------|----|----------|------------|----------|------------|-------------|------|----------|--------|
| 1 | C3 | Transaction-Safe Agent State Boundaries | 定义并验证 LLM agent 在 checkpoint/rollback/retry 后外部副作用与权限状态不一致导致的可恢复性失败 | A/B/C/D | 7 | 8.1 | 可做 | ACRFence | 首选 |
| 2 | C1 | Cross-Benchmark Trace Failure Diagnosis | 为 SWE/web/desktop/multi-agent traces 建立统一失败定位 schema 和最小诊断 benchmark | A/B/D | 9 | 7.8 | 可做 | AgentRx / TRAIL | 首选备选 |
| 3 | C4 | Policy-Consistent Tool-Use Reliability | 评估 tool-use agent 在同一任务多次运行中是否稳定遵守业务规则与状态约束 | A/D/C | 7 | 7.4 | 可做 | tau-bench / BFCL | 备选 |
| 4 | C2 | Preference Drift and Memory Hygiene for Personal Agents | 测试长期个人 agent 如何处理用户偏好变化、过期记忆与冲突记忆 | A/B/D | 7 | 7.0 | 可做 | MemoryCD / AI Persona | 谨慎 |
| 5 | C5 | SWE Agent Benchmark Integrity Diagnostics | 将 SWE agent 结果拆解为 model、harness、issue quality、oracle、contamination 等因素的诊断协议 | A/D | 7 | 6.8 | 谨慎 | SWE-bench Verified / SWE-smith / Agentless | 谨慎 |

**档位对照**（十维均分）：8.5–10 强烈值得做 · 7–8.4 可以做 · 5–6.9 谨慎 · 低于 5 不建议

---

## 3. 十维评分矩阵

与 `paper_research_skill.md` §三 对齐；每项 1–10 分，**风险可控**表示审稿/撞车风险越低分越高。

| ID | 重要性 | 新颖性 | 可形式化 | 可验证性 | 方法空间 | 泛化性 | 顶会匹配 | 工程可行 | Baseline清晰 | 风险可控 | 均分 |
|----|--------|--------|----------|----------|----------|--------|----------|----------|--------------|----------|------|
| C3 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8.1 |
| C1 | 9 | 7 | 8 | 8 | 7 | 9 | 8 | 7 | 8 | 7 | 7.8 |
| C4 | 8 | 7 | 8 | 8 | 7 | 7 | 7 | 8 | 8 | 6 | 7.4 |
| C2 | 8 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 6 | 7.0 |
| C5 | 8 | 6 | 7 | 8 | 6 | 7 | 7 | 7 | 8 | 4 | 6.8 |

**排序规则**：先按均分降序；均分接近时，优先 **可验证性 + Baseline清晰 + 风险可控** 更高的候选。

---

## 4. 候选详情

### C3：Transaction-Safe Agent State Boundaries

- **问题是否真实**：真实。Agent 框架越来越支持 checkpoint、rollback、human-in-the-loop recovery 和重试，但 agent local state 与外部服务状态不可同时回滚。ACRFence 已明确指出 semantic rollback attacks，AgentDojo/ASB 说明工具与 memory 是安全边界。
- **已有相似工作**：ACRFence 已覆盖 checkpoint-restore 下的 Action Replay 和 Authority Resurrection；AgentDojo/ASB 覆盖 prompt injection、memory poisoning、tool attacks；OpenHands/SWE-agent 提供实际 agent runtime 和 ACI 场景。空白在于：把 rollback、memory contamination、credential scope、tool effect log 统一为可测试的 state boundary hygiene，而不是只处理单一 rollback 攻击。
- **支撑论文**（≥3 篇，来自 `discovery_paper_table.csv`）：
  - ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore · verified
  - AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents · verified
  - Agent Security Bench ASB · verified
  - OpenHands · verified
  - SWE-agent · verified
- **最大威胁 work**：ACRFence · verified。若 Phase 3 发现它已经完整覆盖“transaction-safe state boundary”，本候选必须收窄到 memory/tool side-effect interaction 或放弃。
- **可能创新点**：
  - A. 问题贡献：定义 agent state boundary failure taxonomy，包括 local rollback / external side effect / credential resurrection / memory laundering / branch confusion。
  - B. 表示贡献：提出 tool-effect ledger + memory provenance + branch semantics 的统一 trace 表示。
  - C. 方法贡献：最小实现可做 replay-or-fork、credential invalidation、memory quarantine。
  - D. Benchmark：构造 30–80 个跨 email/payment/file/GitHub issue 的 reversible vs irreversible tool scenarios。
- **MVP 验证思路**（benchmark / baseline / metric）：
  - benchmark：自建 20–30 个 mock tool scenarios，含可逆读操作、不可逆写操作、一次性 token、memory update。
  - baseline：普通 checkpoint retry、idempotency-key-only、ACRFence-like replay。
  - metric：duplicate side-effect rate、credential resurrection rate、benign recovery success、false block rate、token/cost overhead。
- **最大风险**：ACRFence 过强，容易被认为只是 follow-up；需要找出 ACRFence 没覆盖的 memory/tool provenance 或 multi-branch workflow 场景。
- **为何进入 top-k**：问题真实、MVP 可构造、工程范围可控，并且直接贴近 agent 系统可靠性和安全边界。

### C1：Cross-Benchmark Trace Failure Diagnosis

- **问题是否真实**：真实。WebArena、OSWorld、SWE-bench、MultiAgentBench 等 benchmark 都能告诉我们成功/失败，但很少给出跨环境可复用的“关键失败步”和 failure taxonomy。AgentRx/TRAIL 说明研究社区已经开始需要 trace-level diagnosis。
- **已有相似工作**：AgentRx 有 115 failed trajectories 与 10 类 taxonomy；TRAIL 有结构化 traces 与 issue localization；ErrorProbe 面向 multi-agent diagnosis。空白在于跨 benchmark 的统一 trace schema、低标注协议，以及从 diagnosis 到 repair/retry policy 的闭环。
- **支撑论文**（≥3 篇，来自 `discovery_paper_table.csv`）：
  - AgentRx · verified
  - TRAIL · verified
  - AgentBench · verified
  - WebArena · verified
  - OSWorld · verified
  - MultiAgentBench · verified
- **最大威胁 work**：AgentRx / TRAIL · verified。Phase 3 必须正面比较 taxonomy、trace format、annotation granularity、domains。
- **可能创新点**：
  - A. 问题贡献：将 agent failure 从 final outcome 推进到 cross-domain critical step localization。
  - B. 表示贡献：统一 SWE/web/desktop/multi-agent trace events：observation、intent、tool call、state delta、constraint violation。
  - D. Benchmark：选取少量公开失败 traces 或重新运行任务，标注 critical step + failure type。
- **MVP 验证思路**（benchmark / baseline / metric）：
  - benchmark：每类 10–20 条失败 trace，覆盖 SWE-bench Lite、WebArena/VisualWebArena、OSWorld、multi-agent toy workflow。
  - baseline：final-outcome-only judge、LLM full-trace judge、TRAIL-style structured judge、constraint-based judge。
  - metric：critical-step accuracy、failure-category F1、explanation faithfulness、annotation cost。
- **最大风险**：标注成本可能上升；AgentRx 已经很接近，必须找跨 domain schema 或诊断后可恢复性作为差异点。
- **为何进入 top-k**：文献支撑强，问题横跨多个 agent benchmark，容易形成可验证 MVP。

### C4：Policy-Consistent Tool-Use Reliability

- **问题是否真实**：真实。BFCL 测函数调用准确率，tau-bench 测多轮 agent-user-tool interaction 的 pass^k，但现实 workflow 还关心同一任务多次运行是否稳定遵守 policy、是否在 partial failure 后保持数据库状态一致。
- **已有相似工作**：BFCL 是函数调用标准；tau-bench 已引入 pass^k 和数据库终态比较；ToolBench/APIBank/ToolLLM 覆盖广泛工具调用；WorkArena/WebShop 提供 workflow 环境。空白在于“policy-consistent across retries/runs”的细粒度 failure modes。
- **支撑论文**（≥3 篇，来自 `discovery_paper_table.csv`）：
  - BFCL · verified
  - tau-bench · verified
  - ToolBench / ToolLLM · verified
  - WebShop · verified
  - VisualWebArena · verified
- **最大威胁 work**：tau-bench · verified。Phase 3 需要正面比较 pass^k、database-state evaluation 与本候选的 invariant violation / retry consistency 是否有实质差异。
- **可能创新点**：
  - A. 问题贡献：定义 policy drift、state drift、retry drift、tool-argument drift。
  - D. Benchmark：在 airline/retail/finance/GitHub issue 等小型 API 环境中构造 multi-run consistency tasks。
  - C. 方法贡献：policy-state checker、run-to-run invariant validator、tool-call repair。
- **MVP 验证思路**（benchmark / baseline / metric）：
  - benchmark：20–40 个 API workflow，每个运行 k=5 次。
  - baseline：普通 ReAct/tool-calling agent、strict JSON/function calling、policy reminder prompt、state checker。
  - metric：pass^k、policy violation rate、database invariant violation rate、variance across runs。
- **最大风险**：容易被认为是 tau-bench 的小扩展；必须强调 retry/multi-run consistency 与 invariant violation，而不是只加 domain。
- **为何进入 top-k**：实验可控，baseline 清晰，2–4 个月可做一个小型 benchmark。

### C2：Preference Drift and Memory Hygiene for Personal Agents

- **问题是否真实**：真实。长期个人 agent 必须处理用户偏好随时间变化、旧记忆失效、冲突偏好与跨域迁移。AI Persona、MemoryCD、LoCoMo 等说明该方向正在快速上升。
- **已有相似工作**：AI Persona 构造 PersonaBench；MemoryCD 用真实 Amazon Review 跨域行为；Preference-Aware Memory Update 直接处理偏好更新；LoCoMo/MemGPT/MemoryBank 是长期记忆基础。空白可能在 memory hygiene：什么时候更新、什么时候遗忘、什么时候隔离不可信记忆。
- **支撑论文**（≥3 篇，来自 `discovery_paper_table.csv`）：
  - AI Persona · verified
  - MemoryCD · verified
  - Preference-Aware Memory Update · verified
  - LoCoMo · verified
  - MemGPT · verified
- **最大威胁 work**：MemoryCD / AI Persona · verified。Phase 3 必须检查它们是否已覆盖偏好漂移、跨域迁移与过期记忆。
- **可能创新点**：
  - A. 问题贡献：定义 preference drift 与 stale memory harm。
  - B. 表示贡献：为 memory item 增加 temporal validity、confidence、domain、contradiction relation。
  - D. Benchmark：构造用户偏好变化任务，测 agent 是否更新、遗忘或询问澄清。
- **MVP 验证思路**（benchmark / baseline / metric）：
  - benchmark：合成 20–50 个用户 trajectory，包含偏好反转、上下文限定偏好、恶意/错误记忆注入。
  - baseline：full-history prompting、RAG memory、profile summary、preference-aware update。
  - metric：current-preference accuracy、stale-memory usage rate、clarification rate、user satisfaction proxy。
- **最大风险**：Memory/personalization 论文增长很快，2025–2026 可能已有很接近的 benchmark；真实用户数据获取难。
- **为何进入 top-k**：问题重要且可构造，但撞车风险高于 C1/C3。

### C5：SWE Agent Benchmark Integrity Diagnostics

- **问题是否真实**：真实。SWE-bench 生态非常活跃，Verified、Multimodal、SWE-smith、Agentless、SWE-agent、OpenHands 都说明 benchmark 结果受任务质量、数据生成、harness、oracle 与模型能力共同影响。
- **已有相似工作**：SWE-bench Verified 已人工筛选 500 个任务；Agentless 质疑复杂 agent 必要性；SWE-smith 生成大量训练数据；SWE-agent/OpenHands 展示 harness 影响。空白在于系统化诊断 benchmark score 的来源，而不是只报告 resolved %。
- **支撑论文**（≥3 篇，来自 `discovery_paper_table.csv`）：
  - SWE-bench · verified
  - SWE-bench Verified · verified
  - SWE-smith · verified
  - Agentless · verified
  - SWE-agent · verified
  - OpenHands · verified
- **最大威胁 work**：SWE-bench Verified / SWE-smith / Agentless · verified。这些可能已经覆盖 task quality、data generation 或 baseline reset。
- **可能创新点**：
  - A. 问题贡献：将 SWE agent score 拆成 issue ambiguity、oracle weakness、harness affordance、context leakage、contamination risk。
  - D. Benchmark：抽样 SWE-bench Lite/Verified，人工或半自动标注 integrity risk。
  - C. 方法贡献：score diagnostic report，不直接提升 agent，而是解释 score。
- **MVP 验证思路**（benchmark / baseline / metric）：
  - benchmark：抽 30–50 个 SWE-bench Lite/Verified 任务，标注 issue quality、test oracle、localization difficulty、harness dependence。
  - baseline：SWE-agent、Agentless、mini-SWE-agent/OpenHands style harness。
  - metric：risk label agreement、score delta under harness changes、oracle fragility rate。
- **最大风险**：容易成为 benchmark audit 而非新研究贡献；也可能超出当前 skill“不做投稿级审计”的范围。
- **为何进入 top-k**：实际价值高，但作为论文方向需要非常收窄，当前只建议作为备选或后续工程分析。

---

## 5. 不建议继续的方向（可选）

| 方向 | 为何排除 |
|------|----------|
| 再做一个通用 AgentBench/WebArena 风格大 benchmark | 已有 AgentBench、WebArena、OSWorld、GAIA、VisualWebArena、MultiAgentBench，若没有新的 failure mechanism 或 evaluation lens，容易只是规模扩展 |
| 只做 prompt injection defense | AgentDojo 和 ASB 已经很强；单纯 prompt/filter/guardrail 方法容易被认为是已有防御组合 |
| 只做多智能体 SOP/role 框架 | MetaGPT、AgentVerse、AutoGen、Magentic-One 已覆盖很多系统设计；如果没有 failure diagnosis 或可量化机制，工程-only 风险高 |

---

## 6. 推荐进入深研的 1–2 个方向

| 推荐 | ID | 理由 | 建议 topic 目录名 |
|------|----|------|-------------------|
| 首选 | C3 | 问题真实、MVP 可构造、工程边界清晰；最大威胁 ACRFence 明确，Phase 3 能快速判断是否还有可切空白 | `topics/transaction_safe_agent_state/` |
| 备选 | C1 | 横跨多个 benchmark，trace diagnosis 需求强；但必须正面避开 AgentRx/TRAIL 的已有贡献 | `topics/cross_benchmark_trace_diagnosis/` |

---

## 7. 人工选择（Selection）

> 用户确认后，Agent 写入 `scout/selection.md`（模板：`templates/selection_template.md`）；**不得**自行替用户做最终选择。

- **待选 ID**：C3 / C1 / C4 / C2 / C5
- **下一步**：用户确认 → 填写 `scout/selection.md` → 创建 `topics/<slug>/` → Phase 3 Deep Dive
