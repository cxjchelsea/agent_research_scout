# Selection: Agent Research Scout 2026-06-24

> **Phase**：Selection
> **生成日期**：2026-06-24
> **来源**：`scout/candidates.md`
> **用途**：记录用户最终选定的方向，作为创建 `topics/<slug>/` 的依据

> Agent 不得自行替用户做最终选择；本文件依据用户确认“选择 C1”填写。

---

## 1. 选定方向

- **Selected topic**：Trace-Causal Failure Localization for Agent Workflows
- **Selected slug**：`trace_causal_failure_localization`
- **candidate_id**：C1

---

## 2. 选择理由

C1 的问题真实性强：现有 agent benchmark 越来越多，但大量任务只给 final success，不能稳定回答“哪一步错、为什么错、应修哪个 agent/component”。TRAIL、MAST、Who&When 已经证明 trace debugging 和 failure attribution 是明确痛点，同时也提供了可复用的 benchmark / taxonomy / annotation 起点。

该方向适合进入 Phase 3，因为它具备较清晰的 MVP 路径：从 TRAIL、SWE-bench Lite、GAIA 或小规模 WebArena traces 中抽取失败轨迹，比较 full-trace LLM judge、last-error heuristic、taxonomy classifier 等 baseline，并用 responsible span F1、root-cause category accuracy、minimal failing prefix 等指标验证。

---

## 3. 为什么没有选择其他候选

| 未选候选 | candidate_id | 主要放弃原因 |
|----------|--------------|--------------|
| Policy-Consistent Tool Agents under Adversarial Evidence | C2 | AgentDojo、tau-bench、ToolEmu 已覆盖较多核心问题；需要更强收窄才能避免变成 prompt injection / policy benchmark 增量。 |
| Temporal Memory Conflict & Provenance for Long-Term Agents | C3 | 仍是强备选，但 MemBench、LongMemEval、Mem0 威胁较强；本轮优先选择 trace diagnosis 方向。 |
| Collateral-Damage-Aware App and Coding Agents | C4 | MVP 可行，但 AppWorld 已显式覆盖 collateral damage，需要先核验是否还有足够新空间。 |
| Failure Attribution and Protocol Selection in Multi-Agent Systems | C5 | 问题重要，但多 agent 框架和 trace 控制成本更高；适合作为 C1 的后续子场景，而非首选起点。 |

---

## 4. 进入 Phase 3 的初始问题定义

- **一句话定义**：把 agent workflow 的失败轨迹定位到可复验的 causal step / component，并生成最小失败片段或修复目标。
- **核心失败模式 / 机制问题**：现有 benchmark 常能判定任务失败，却不能可靠指出失败由哪个 reasoning / planning / tool / memory / agent-handoff span 触发，导致调试、回归测试和方法改进缺乏可操作目标。
- **预期贡献类型**（A/B/C/D/E）：A（问题贡献）+ B（表示贡献）+ D（Benchmark / Dataset 贡献），后续可扩展 C（方法贡献）。
- **研究边界**（保留 / 删除）：
  - 保留：trace causal slice、minimal failing prefix、root-cause category、repair-target recommendation、跨单/多 agent 的失败定位。
  - 删除：通用日志可视化工具、无人工标注的纯总结、只做 multi-agent 框架性能比较、只预测 final success。

---

## 5. 需要重点核验的 related work

| 论文 | verified_status | 为何必须深研阶段核验 |
|------|-----------------|----------------------|
| TRAIL: Trace Reasoning and Agentic Issue Localization | verified | 最大威胁；必须核验是否已覆盖 causal slice extraction、minimal failing prefix 和 repair-target recommendation。 |
| Why Do Multi-Agent LLM Systems Fail? | verified | 最大威胁；必须核验 MAST taxonomy 是否已足够覆盖本案 root-cause categories。 |
| Which Agent Causes Task Failures and When? | verified | 最大威胁；必须核验 Who&When 是否已覆盖 step-level causal attribution，尤其是否只限 multi-agent。 |
| SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | verified | 可能作为失败轨迹来源或应用场景；需核验 trace 可获得性和评价可复现性。 |
| GAIA: A Benchmark for General AI Assistants | verified | 可能作为 general assistant traces 来源；需核验任务答案和轨迹可获取性。 |

---

## 6. 下一步

- [x] 创建 `topics/trace_causal_failure_localization/`
- [x] 从 `templates/` 复制深研模板
- [ ] 进入 Phase 3 Deep Dive
