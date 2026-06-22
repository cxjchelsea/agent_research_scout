# Related Work: Dual-State Contamination in Software Engineering Agents

> 重调研版本：2026-03-18 | 20 篇 verified | 详见 `paper_table.csv`  
> 课题已收窄：不再以泛化「长链路 tool agent 状态污染」为主叙事

---

## 核心 related work（与本案直接相关）

| 论文 | year | venue | verified | 做到了什么 | 没做到什么 | 与本案关系 |
|------|------|-------|----------|------------|------------|------------|
| Why Retrying Fails (CCRM) | 2026 | arXiv | ✓ | context contamination 形式化；Verified 拟合 | 无 world state；无 benchmark | **最大威胁**；context 子问题 |
| State Contamination in Memory-Augmented LLM Agents | 2026 | arXiv | ✓ | state contamination 定义；memory laundering | 非 executable tool state | 术语威胁；scope 不同 |
| GA-Rollback | 2025 | EMNLP | ✓ | stepwise trajectory rollback | 无 SWE/world state | method baseline |
| ACRFence | 2026 | arXiv | ✓ | CR ≠ undo external effect | security 角；无 task benchmark | blind spot 叙事 |
| AgentDebug | 2025 | arXiv (ICLR withdrawn) | ✓ | error cascade taxonomy | 无 state rollback | failure analysis 参照 |
| SWE-bench | 2024 | ICLR | ✓ | 真实 issue resolve eval | 无 contamination/recovery 指标 | **实验底座** |
| Hell or High Water | 2025 | COLM | ✓ | external failure recovery bench | 非 self-caused pollution | recovery 边界 |
| MemoryAgentBench | 2026 | ICLR | ✓ | memory 四能力 eval | 无 tool workspace | memory 边界 |

---

## 1. Agent Benchmark（4 篇）

| title | year | venue | verified | limitation（污染/recovery） | relevance |
|-------|------|-------|----------|----------------------------|-----------|
| WebArena | 2024 | ICLR | ✓ | 不追踪中间状态污染 | 6 — 未来扩展 |
| GAIA | 2024 | ICLR | ✓ | 不暴露 retry 污染 | 5 — 背景 |
| **SWE-bench** | 2024 | ICLR | ✓ | 不度量 dirty workspace / retry | 6 — **MVP 底座** |
| OSWorld | 2024 | NeurIPS D&B | ✓ | 不区分状态漂移与恢复 | 6 — 未来扩展 |

---

## 2. Tool-use / Software Agent（4 篇）

| title | year | venue | verified | limitation | relevance |
|-------|------|-------|----------|------------|-----------|
| SWE-agent | 2024 | NeurIPS | ✓ | 线性 history，无 rollback | 7 |
| τ-bench | 2024 | arXiv (under review) | ✓ | 不研究 retry 污染 | 7 — 未来 |
| **Devil's Advocate** | 2024 | EMNLP Findings | ✓ | 无 state isolation | 7 |
| OpenHands | 2025 | ICLR | ✓ | append-only 轨迹 | 6 — scaffold 参照 |

> 注：旧版「ADVOCATE」已更正为 **Devil's Advocate**（ACL Anthology 2024.findings-emnlp.53）

---

## 3. Memory / Long-Horizon（4 篇）

| title | year | venue | verified | limitation | relevance |
|-------|------|-------|----------|------------|-----------|
| MemGPT | 2023 | arXiv | ✓ | 错误 summary 可持久化 | 7 — 机制背景 |
| LongMemEval | 2025 | ICLR | ✓ | 无 executable state | 7 |
| MemoryAgentBench | 2026 | ICLR | ✓ | 无 tool side-effect | 8 — 边界 |
| **State Contamination (Wang et al.)** | 2026 | arXiv | ✓ | memory safety only | **10 — 术语威胁** |

---

## 4. Failure Analysis（4 篇）

| title | year | venue | verified | limitation | relevance |
|-------|------|-------|----------|------------|-----------|
| AgentDebug | 2025 | arXiv | ✓ | feedback recovery，无 rollback | 8 |
| TRAIL | 2025 | arXiv | ✓ | 不评 clean restart | 7 |
| Who&When | 2025 | ICML | ✓ | multi-agent attribution | 6 |
| AgentRx | 2026 | arXiv | ✓ | 无 rollback 协议 | 6 |

> 注：AgentRx venue 为 arXiv，**非 ICML 2026 accepted**

---

## 5. Recovery / Rollback（4 篇）

| title | year | venue | verified | limitation | relevance |
|-------|------|-------|----------|------------|-----------|
| **GA-Rollback** | 2025 | EMNLP | ✓ | 无 irreversible tool effect | **9** |
| **CCRM** | 2026 | arXiv | ✓ | context only | **10** |
| **ACRFence** | 2026 | arXiv | ✓ | security PoC | **9** |
| Hell or High Water | 2025 | COLM | ✓ | external failure only | 7 |

---

## 空白总结（同步 gap_analysis）

1. **已有**：CCRM（context）、Wang et al.（memory）、GA-Rollback（trajectory）、ACRFence（CR security）
2. **空白**：SWE-bench Verified 上 **dual-state contamination eval protocol** 缺失
3. **本案切口**：Problem + Benchmark，非 CCRM 理论重推
