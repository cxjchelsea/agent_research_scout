# Gap Analysis: Dual-State Contamination in Software Engineering Agents

> **重调研版本**：2026-03-18（方案 A 增量审计）  
> 文献库：20 篇，verified 20 / uncertain 0 / remove 0（见 `paper_table.csv`）  
> 核心精读：8 篇（见 `paper_cards/`）  
> **审稿攻击** → `adversarial_review.md`  
> **文件一致性** → `file_consistency_check.md`  
> **阶段性决策** → `decision.md`

---

## 0. 课题收窄记录（Skill §九）

| 字段 | 内容 |
|------|------|
| **原始题目** | State Contamination in Long-Horizon Tool-Using Agents |
| **风险** | 与 CCRM（context contamination）、Wang et al.（state contamination）术语重叠；scope 过宽 |
| **建议新题目** | Dual-State Contamination in Software Engineering Agents |
| **一句话定义** | 评测 coding agent 在 SWE-bench Verified 上 ContextState 与 WorldState 的 retry 污染及 recovery blind spot |
| **删除** | 泛 web/memory agent、memory laundering、CCRM 理论、ACRFence security 复刻 |
| **保留** | dirty-retry vs clean-restart、workspace drift、SWE-bench Verified、三指标 |
| **实验边界** | MVP：Verified 10 题 pilot → 50–100 题 benchmark 子集 |

---

## 1. 已有工作已经覆盖什么？

### 1.1 问题定义与形式化

| 子问题 | 代表论文 | 已覆盖 | 本案 scope |
|--------|----------|--------|------------|
| Context retry 污染 | CCRM (Yang 2026, arXiv) | ε₁>ε₀；clean-restart dominance；Verified 拟合 | **子问题，需 cite + extend** |
| Memory state contamination | Wang et al. 2026 (arXiv) | laundering；write-gate；SPG | **不在本案 scope** |
| Error cascade | AgentDebug 2025 (arXiv, ICLR withdrawn) | 17 类 taxonomy；memory cascade | 相关，非核心论据 |
| Recovery blind spot (security) | ACRFence 2026 (arXiv) | local CR ≠ undo external effect | **叙事参照，非复刻** |

### 1.2 方法与 benchmark 边界

- **GA-Rollback**：trajectory rollback；无 world state（AlfWorld/WebShop）
- **Hell or High Water**：external failure recovery；非 self-caused contamination
- **SWE-bench**：end resolve only；CCRM 借用 retry 数据但未发布 contamination benchmark
- **MemoryAgentBench**：memory 四能力；无 executable workspace

### 1.3 本案可 claim 的空白

尚无公开 benchmark **同时**报告：

1. `pass@k` vs `clean-restart@k` vs `workspace-reset@k` on SWE-bench Verified  
2. ContextState 与 WorldState 的 **解耦污染** 度量  
3. Recovery Gap 与 World-State Drift 的 **系统性 baseline**

---

## 2. 是否只是换名？

| 提案 | 判断 |
|------|------|
| 只做 context retry 污染 | ❌ CCRM 换名 |
| 只做 memory laundering | ❌ Wang et al. 换名 |
| **Dual-state contamination + Verified eval protocol** | ✅ 非换名（扩展通道 + 评测） |

---

## 3. 最危险 related work 正面比较

### S1 — CCRM (Yang 2026)

| 维度 | CCRM | 本案 |
|------|------|------|
| 对象 | tool-call pipeline retry | mini-SWE-agent on Verified |
| 状态 | context only | context **+ workspace** |
| 贡献 | 理论 CCRM | **benchmark + dual-state metrics** |
| 关系 | 必须 cite；本案 = world-state extension + empirics |

### S1 — Wang et al. (2026)

| 维度 | Wang et al. | 本案 |
|------|-------------|------|
| 通道 | persistent memory / toxicity | executable repo state |
| 指标 | SPG, Δμ | Recovery Gap, World-State Drift |
| 关系 | 术语相近但 **问题域不同** |

### S2 — GA-Rollback (EMNLP 2025)

| 维度 | GA-Rollback | 本案 |
|------|-------------|------|
| 机制 | stepwise trajectory rollback | eval protocol + clean-restart |
| 环境 | AlfWorld/WebShop | SWE-bench Verified |
| 关系 | baseline 参照；不做 method 竞争 |

---

## 4. 最小可行创新点（MVP）

**贡献类型**：Problem (A) + Benchmark (D)

1. **Dual-State Contamination** 操作定义（ContextState / WorldState）  
2. **Eval protocol** on SWE-bench Verified（10 → 50–100 题）  
3. **Baselines**：dirty-retry / clean-restart@k / full-reset  
4. **Metrics**：Contamination Rate、Recovery Gap、World-State Drift  

---

## 5. 当前结论（gap 视角）

**方向可做，已收窄；空白在 dual-state eval protocol，不在 context 理论重推。**

- 主 claim：**dual-state contamination eval on SWE-bench Verified**
- 顶会路径：ICLR/NeurIPS（benchmark）或 ICSE/FSE（SE agent）
- 是否进入实验：见 `adversarial_review.md` 攻击结论 + `decision.md`

---

## 6. 核心论文（8 篇，verified + paper_card）

| # | 论文 | 角色 |
|---|------|------|
| 1 | CCRM | 最直接威胁 + context 子问题 |
| 2 | Wang et al. state contamination | 术语威胁 + scope 切割 |
| 3 | GA-Rollback | rollback method baseline |
| 4 | ACRFence | recovery blind spot 叙事 |
| 5 | AgentDebug | error propagation |
| 6 | MemoryAgentBench | memory eval 边界 |
| 7 | SWE-bench | 实验底座 |
| 8 | Hell or High Water | recovery eval 边界 |
