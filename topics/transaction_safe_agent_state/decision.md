# Decision: Recovery-Safe Memory Provenance for Tool-Using Agents

> **审计日期**：2026-06-24
> **Skill 版本**：paper_research_skill.md
> **联动文件**：`gap_analysis.md` · `adversarial_review.md` · `file_consistency_check.md` · `experiment_plan.md`

---

## Decision: Narrow

> **Current Phase**：3（Deep Dive）
> Go 仅用于 Phase 4：表示创新点已通过 MVP 验证，值得继续投入。

原始 C3 方向过宽，ACRFence 已强覆盖 external side-effect rollback。当前收窄为 **Recovery-Safe Memory Provenance for Tool-Using Agents**：研究 recovery / rollback / branch 后长期 memory 写入的 provenance、validity 与 quarantine。方向可继续，但 claim 必须围绕 memory provenance，而不是泛化 transaction-safe state boundary。

---

## Reason

### Phase 3 条件检查（深研后，尚未 Go）

| # | 条件 | 状态 |
|---|------|------|
| 1 | 至少 8 篇核心论文已核验 | 满足；8 篇 core_read=yes 且 verified |
| 2 | 至少 5 篇核心论文已有 paper card | 满足；8 篇 paper cards |
| 3 | gap_analysis 明确指出已有工作覆盖/未覆盖 | 满足 |
| 4 | adversarial_review 已完成且风险有回应 | 满足；仍有中等 novelty 风险 |
| 5 | file_consistency_check 通过 | 待最终更新 |
| 6 | 最危险 3 篇 related work 正面比较 | 满足；ACRFence、AgentDojo、ASB、AgentPoison 已比较 |
| 7 | 课题已收窄到可实验场景 | 满足；recovery-safe memory provenance |
| 8 | 有明确 benchmark 或可构造数据 | 满足；mock tool + memory scenarios |
| 9 | 有 baseline 与至少 3 个可量化指标 | 满足 |
| 10 | uncertain 论文没有作为核心论据 | 满足 |

### Phase 4 条件检查（Quick Proof 后，才可 Go）

| # | 条件 | 状态 |
|---|------|------|
| 1 | experiment_plan.md + outputs/ 有 minimum evidence | 未开始 |
| 2 | MVP / pilot 支持核心创新点 | 未开始 |

### No-Go 条件检查

| 条件 | 是否触发 |
|------|----------|
| 核心问题已被已有论文完整覆盖 | 未触发；ACRFence 覆盖 rollback side effects 但未确认覆盖 memory provenance |
| 只能通过换术语制造新颖性 | 未触发但有风险；已收窄并定义 recovery / branch 变量 |
| 没有可复现实验路径 | 未触发 |
| 没有强 baseline | 未触发 |
| MVP 成本超出 2–4 个月 | 未触发 |
| 主要论据依赖 uncertain 论文 | 未触发 |

---

## 课题收窄确认（如适用）

| 项 | 内容 |
|----|------|
| 旧题目 | Transaction-Safe Agent State Boundaries |
| 新题目 | Recovery-Safe Memory Provenance for Tool-Using Agents |

---

## Minimum next step

进入 Phase 4 Quick Proof 前，先实现 5 个 pilot scenarios：tool observation 写入 memory → rollback/fork/retry → later retrieval。最小比较 B1 Naive persistent memory、B3 ACRFence-like tool-effect log、Ours provenance-filtered memory。

---

## What evidence would change this decision

| 证据 | 决策变化 |
|------|----------|
| ACRFence 已完整覆盖 memory provenance / store rollback / branch-aware retrieval | No-Go |
| Pilot 显示 B1/B3 都没有 contaminated memory reuse 问题 | No-Go |
| Ours 降低污染复用但 benign memory utility 下降过大 | Hold |
| Ours 比 B1/B3 降低 ≥50% contaminated memory reuse 且 utility 下降 ≤10% | Promising / Phase 4 Go 候选 |

---

## 评分表（10 分制，可选）

| 维度 | 分 | 说明 |
|------|-----|------|
| 重要性 | 9 | recovery + long-term memory 是真实 agent 部署问题 |
| 新颖性 | 7 | ACRFence / AgentPoison 很强，需靠交界问题成立 |
| 可形式化 | 8 | provenance、branch、checkpoint、validity 可形式化 |
| 可验证性 | 8 | mock tool + memory MVP 可构造 |
| 方法空间 | 7 | quarantine / provenance-filtered retrieval |
| 泛化性 | 7 | 可跨工具类型，模型泛化待验证 |
| 顶会匹配 | 7 | agent reliability / security / memory |
| 工程可行 | 8 | 2–4 个月内可做 MVP |
| Baseline 清晰 | 8 | B1/B2/B3/Ours 明确 |
| 风险可控 | 6 | novelty 和 toy benchmark 风险仍在 |

**总评**：7.5，**Narrow**。方向可做，但必须围绕 recovery-safe memory provenance，不宜继续使用 broad transaction-safe state boundary claim。

---

## 引用

- 空白分析 → `gap_analysis.md`
- 审稿攻击 → `adversarial_review.md`
- 一致性审计 → `file_consistency_check.md`
