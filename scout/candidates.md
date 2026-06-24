# Candidate Directions: Agent Research Scout 2026-06-24

> **Phase**：Discovery
> **生成日期**：2026-06-24
> **扫描范围**：见 `scout/landscape_scan.md`
> **用途**：从广搜中提出 3–7 个候选方向，供人工选择 1 个进入 `topics/<topic>/` 深研

**candidate_id 规则**：本轮使用 C1–C5，与 `discovery_paper_table.csv` 的 `candidate_id` 列对齐。

**论据要求**：每个候选均至少有 3 篇 verified 来源支撑；每个候选的最大威胁 work 均为 verified。发现阶段不创建 `paper_cards/`，不做 Phase 3.5 targeted verification。

---

## 1. 扫描摘要

本轮广搜覆盖 agent trace diagnosis、memory agent、tool-use/security、software/app agents、多智能体协作与真实系统可靠性。总体空白不是“缺 benchmark”，而是缺少能把 agent 失败、工具副作用、记忆变化和多 agent 责任归因转成可操作诊断或修复协议的研究。最大撞车风险集中在 ACRFence、AgentDojo、MemBench/LongMemEval/Mem0、TRAIL/MAST/Who&When 和 AppWorld/TheAgentCompany。

---

## 2. 候选方向概览

| Rank | ID | 候选名称 | 一句话定义 | 贡献类型 | 支撑论文数 | 总分（/10） | 档位 | 最大威胁 | 推荐度 |
|------|----|----------|------------|----------|------------|-------------|------|----------|--------|
| 1 | C1 | Trace-Causal Failure Localization for Agent Workflows | 把 agent 轨迹失败定位到可解释的 causal step / component，并生成可复验的最小失败片段 | A/B/D | 6 | 8.3 | 可以做 | TRAIL；MAST；Who&When | ⭐⭐⭐ |
| 2 | C3 | Temporal Memory Conflict & Provenance for Long-Term Agents | 评估并缓解长期 agent memory 中过期事实、冲突更新和来源不明记忆导致的错误行为 | B/C/D | 6 | 8.1 | 可以做 | MemBench；LongMemEval；Mem0 | ⭐⭐⭐ |
| 3 | C4 | Collateral-Damage-Aware App and Coding Agents | 在 app/API/coding agent 中评估“任务成功但造成额外状态损坏”的隐藏失败 | A/D/C | 6 | 7.9 | 可以做 | AppWorld；TheAgentCompany；SWE-bench | ⭐⭐ |
| 4 | C2 | Policy-Consistent Tool Agents under Adversarial Evidence | 在工具输出不可信、政策约束复杂时，让 agent 同时保持任务效用、安全性和规则一致性 | C/D | 6 | 7.7 | 可以做 | AgentDojo；tau-bench；ToolEmu | ⭐⭐ |
| 5 | C5 | Failure Attribution and Protocol Selection in Multi-Agent Systems | 识别多 agent 失败由哪个 agent、哪一步、哪种协调协议造成，并建议协议切换 | A/D/C | 7 | 7.3 | 可以做但需收窄 | MultiAgentBench；MAST；Who&When | ⭐ |

**档位对照**（十维均分）：8.5–10 强烈值得做 · 7–8.4 可以做 · 5–6.9 谨慎 · 低于 5 不建议

---

## 3. 十维评分矩阵

与 `paper_research_skill.md` §三 对齐；每项 1–10 分，**风险可控**表示审稿/撞车风险越低分越高。

| ID | 重要性 | 新颖性 | 可形式化 | 可验证性 | 方法空间 | 泛化性 | 顶会匹配 | 工程可行 | Baseline清晰 | 风险可控 | 均分 |
|----|--------|--------|----------|----------|----------|--------|----------|----------|--------------|----------|------|
| C1 | 9 | 8 | 9 | 8 | 8 | 8 | 9 | 8 | 8 | 8 | 8.3 |
| C2 | 9 | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 6 | 7.7 |
| C3 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8.1 |
| C4 | 8 | 8 | 8 | 9 | 7 | 7 | 8 | 8 | 8 | 8 | 7.9 |
| C5 | 8 | 7 | 8 | 7 | 7 | 8 | 8 | 7 | 7 | 6 | 7.3 |

**排序规则**：先按均分降序；均分接近时，优先 **可验证性 + Baseline清晰 + 风险可控** 更高的候选。

---

## 4. 候选详情

### C1：Trace-Causal Failure Localization for Agent Workflows

- **问题是否真实**：真实。TRAIL 显示当前长上下文模型在 agent trace debugging 上表现很弱；MAST 和 Who&When 说明多 agent 失败归因仍很困难。SWE-bench / GAIA / AgentBench 等 benchmark 也普遍只给 final success，很难解释失败路径。
- **已有相似工作**：TRAIL 已有 trace reasoning 和 issue localization；MAST 已有 multi-agent failure taxonomy；Who&When 已有 multi-agent failure attribution。空白在于：把单/多 agent trace 中的失败归因为可复验的 causal slice，并把 slice 映射到修复建议或 regression test。
- **支撑论文**（≥3 篇，来自 `discovery_paper_table.csv`）：
  - TRAIL · verified
  - Why Do Multi-Agent LLM Systems Fail? · verified
  - Which Agent Causes Task Failures and When? · verified
  - SWE-bench · verified
  - GAIA · verified
  - AgentBench · verified
- **最大威胁 work**：TRAIL、MAST、Who&When（均 verified）。Phase 3 必须做 targeted verification：它们是否已覆盖 causal slice extraction、repair-target recommendation 和 cross-benchmark failure replay。
- **可能创新点**：定义 agent failure 的 causal slice 表示；构造 trace-to-minimal-failing-prefix / trace-to-component attribution benchmark；提出基于 span graph + state delta + tool outcome 的 failure localization 方法。
- **MVP 验证思路**（benchmark / baseline / metric）：从 TRAIL、SWE-bench Lite、GAIA 或小规模 WebArena traces 抽取 50–100 条失败轨迹；baseline 为 full-trace LLM judge、keyword taxonomy、last-error heuristic；指标为 responsible span F1、root-cause category accuracy、minimal prefix length、human audit time reduction。
- **最大风险**：容易被认为只是“trace summarization + LLM judge”。必须把贡献收窄成可计算 representation / benchmark，而不是通用日志分析工具。
- **为何进入 top-k**：问题真实、评测可构造、可复用现有 traces，且能连接 reliability、debugging、benchmark diagnosis，2–4 个月内可做 MVP。

### C2：Policy-Consistent Tool Agents under Adversarial Evidence

- **问题是否真实**：真实。AgentDojo 证明 tool outputs 可携带 prompt injection；tau-bench 证明工具、用户和政策一致性很难；ToolEmu 和 AgentPoison 证明 long-tail risk 与 memory/RAG poisoning 都会影响 agent 行为。
- **已有相似工作**：AgentDojo 强覆盖 indirect prompt injection；ToolEmu 覆盖 LM-emulated tool risk；tau-bench 覆盖 policy-following customer-service agents；BFCL 覆盖 function calling；AgentPoison 覆盖 RAG/memory poisoning。空白在于把“不可信证据 + policy constraints + tool side effects”统一到一个 runtime decision policy。
- **支撑论文**：
  - AgentDojo · verified
  - ToolEmu · verified
  - AgentPoison · verified
  - BFCL · verified
  - tau-bench · verified
  - ACRFence · verified
- **最大威胁 work**：AgentDojo、tau-bench、ToolEmu。ACRFence 是 2026 高威胁信号，若 topic 涉及 rollback/tool side effects，Phase 3 必须优先核验。
- **可能创新点**：把工具输出分为 trusted evidence、untrusted evidence、policy-critical evidence；在 agent tool runtime 中引入 evidence gating / policy conflict detector；同时优化 benign utility、policy compliance 和 attack resistance。
- **MVP 验证思路**：基于 AgentDojo 或 tau-bench 增加 policy-conflict cases；baseline 为 vanilla ReAct/function-calling、prompt-only safety instruction、AgentDojo defenses；指标为 benign utility、policy violation rate、targeted ASR、unnecessary refusal rate。
- **最大风险**：AgentDojo 和 tau-bench 已经覆盖核心问题，创新点必须避开“再做 prompt injection defense”或“再做 policy benchmark”。
- **为何进入 top-k**：现实部署价值高，benchmark 明确，但撞车风险较高，所以排在 C4 之后。

### C3：Temporal Memory Conflict & Provenance for Long-Term Agents

- **问题是否真实**：真实。LoCoMo、LongMemEval、MemBench 证明长期记忆、temporal reasoning、knowledge update、reflective/factual memory 仍然困难；AgentPoison 说明持久记忆可成为攻击面。
- **已有相似工作**：LoCoMo / LongMemEval 覆盖长期对话记忆和知识更新；MemBench 覆盖多层级、多场景 memory evaluation；Mem0 覆盖 production memory system；Letta critique 指出现有 benchmark 可能只测 retrieval。空白在于 memory item 的来源、时间、有效期、冲突状态和任务上下文如何影响后续 tool-using 行为。
- **支撑论文**：
  - LoCoMo · verified
  - LongMemEval · verified
  - MemBench · verified
  - Mem0 · verified
  - Letta Memory Benchmark critique · verified
  - AgentPoison · verified
- **最大威胁 work**：MemBench、LongMemEval、Mem0（均 verified）。Phase 3 必须核验它们是否已覆盖 memory provenance、expired-memory quarantine、conflict resolution、tool-use downstream impact。
- **可能创新点**：提出 memory provenance schema（source / timestamp / validity / conflict / task scope）；构造 memory conflict benchmark；提出 retrieval quarantine 或 validity-aware memory update 方法。
- **MVP 验证思路**：从 LoCoMo / LongMemEval 派生 100 个“用户事实更新/冲突/过期”任务，并增加 tool decision outcome；baseline 为 full context、RAG、Mem0-like selective memory、time-aware retrieval；指标为 conflict resolution accuracy、stale-memory usage rate、downstream task success、token/latency。
- **最大风险**：容易被 MemBench 或 Mem0 认为已覆盖 memory evaluation / architecture。必须强调“provenance + conflict validity + downstream agent action”，不是再做记忆检索。
- **为何进入 top-k**：问题重要、MVP 可构造、与长期个人 agent 需求强相关；比 C2 更有可控的新颖性。

### C4：Collateral-Damage-Aware App and Coding Agents

- **问题是否真实**：真实。AppWorld 已经显式检查 unexpected changes / collateral damage；TheAgentCompany、OSWorld、WebArena、SWE-bench 说明 agent 进入真实 app/desktop/codebase 后，final success 远不足以刻画可靠性。
- **已有相似工作**：AppWorld 是最大威胁，因为它已经有 state-based unit tests 和 collateral damage 检查；TheAgentCompany 覆盖真实办公任务；SWE-bench 覆盖 patch test；OSWorld/WebArena/VisualWebArena 覆盖 desktop/web execution。空白在于统一“目标状态达成 + 非目标状态保持”的 side-effect ledger 和 damage taxonomy。
- **支撑论文**：
  - AppWorld · verified
  - OSWorld · verified
  - WebArena · verified
  - VisualWebArena · verified
  - TheAgentCompany · verified
  - SWE-bench · verified
- **最大威胁 work**：AppWorld、TheAgentCompany、SWE-bench。Phase 3 必须核验 AppWorld collateral damage 是否已经足够覆盖本案。
- **可能创新点**：定义 collateral damage taxonomy；为 app/coding agents 构造 target-state vs protected-state 双通道评估；提出 side-effect-aware planning 或 verification wrapper。
- **MVP 验证思路**：在 AppWorld 或小型模拟 app 中增加 protected fields；baseline 为 vanilla agent、retry/self-reflection、unit-test-only judge；指标为 task success、protected-state violation rate、damage severity、repair cost。
- **最大风险**：如果 AppWorld 已经完整覆盖 collateral damage，本方向需要进一步收窄到 coding patch hidden regressions、cross-app irreversible side effects 或 policy-protected state。
- **为何进入 top-k**：可验证性很强，MVP 工程可控；但新颖性依赖对 AppWorld 的 claim-level 核验。

### C5：Failure Attribution and Protocol Selection in Multi-Agent Systems

- **问题是否真实**：真实。MultiAgentBench 证明 multi-agent 协作/竞争需要独立评估；MAST 和 Who&When 显示失败归因困难；AgentVerse、MetaGPT、ChatDev 展示多 agent 框架在协作中有 emergent behavior、SOP、角色分工等机制。
- **已有相似工作**：MultiAgentBench 已覆盖多 agent benchmark 和 protocol/topology；MAST 已覆盖 failure taxonomy；Who&When 已覆盖 agent/step attribution；MetaGPT/AgentVerse/ChatDev 是强框架基线。空白在于：失败后自动建议是换 topology、换角色、减少 agent、增加 verifier，还是修复某个 agent prompt/tool。
- **支撑论文**：
  - MultiAgentBench · verified
  - AgentVerse · verified
  - MetaGPT · verified
  - ChatDev · verified
  - Code in Harmony · verified
  - MAST · verified
  - Who&When · verified
- **最大威胁 work**：MultiAgentBench、MAST、Who&When。Phase 3 必须核验它们是否已覆盖 protocol selection / intervention recommendation。
- **可能创新点**：构造 failure-to-intervention benchmark；定义 coordination protocol selection task；提出基于 trace features 的 protocol repair recommender。
- **MVP 验证思路**：复用 MultiAgentBench / ChatDev / MetaGPT traces，标注 50 个失败案例的 intervention；baseline 为 static protocol、LLM judge、majority discussion；指标为 recommended intervention accuracy、rerun success lift、cost overhead。
- **最大风险**：多 agent 方向容易变成框架拼装或 prompt workflow，对深研和实验资源要求更高。
- **为何进入 top-k**：问题重要，但比 C1 更窄的可验证 MVP 需要更多 trace/框架控制，因此排序靠后。

---

## 5. 不建议继续的方向（可选）

| 方向 | 为何排除 |
|------|----------|
| 再做一个通用 Agent benchmark | AgentBench、GAIA、WebArena、OSWorld、TheAgentCompany 已覆盖多个维度；除非有明确新 failure mode，否则容易只是拼盘。 |
| 泛泛的 multi-agent 框架优化 | MetaGPT、AgentVerse、ChatDev 已经是强威胁；如果没有 failure attribution 或 protocol selection 的可计算目标，容易被认为只是工程组合。 |
| 纯 memory retrieval 分数提升 | LoCoMo、LongMemEval、MemBench、Mem0 已覆盖大量 memory retrieval/evaluation；必须转向 provenance、conflict、validity 或 downstream tool action。 |
| checkpoint-restore semantic rollback 本体 | ACRFence 已经非常直接地定义 semantic rollback attack 和 replay-or-fork mitigation；不建议继续做同名或相近主 claim。 |

---

## 6. 推荐进入深研的 1–2 个方向

| 推荐 | ID | 理由 | 建议 topic 目录名 |
|------|----|------|-------------------|
| 首选 | C1 | 真实痛点强，已有 benchmark 可复用，最大威胁虽多但仍可能留下 causal slice / repair-target 空白；MVP 可在 2–4 个月内启动。 | `topics/trace_causal_failure_localization/` |
| 备选 | C3 | 长期 memory 仍快速增长，provenance/conflict/downstream action 的切口比纯 retrieval 更稳；适合后续做 Phase 3.5 核验 MemBench/LongMemEval/Mem0。 | `topics/memory_conflict_provenance/` |

---

## 7. 人工选择（Selection）

> 用户确认后，Agent 写入 `scout/selection.md`（模板：`templates/selection_template.md`）；**不得**自行替用户做最终选择。

- **待选 ID**：C1 / C2 / C3 / C4 / C5
- **下一步**：用户确认 → 填写 `scout/selection.md` → 创建 `topics/<slug>/` → Phase 3 Deep Dive
