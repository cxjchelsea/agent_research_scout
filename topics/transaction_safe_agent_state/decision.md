# Decision: Transaction-Safe Agent State Boundaries

> **审计日期**：2026-06-24
> **Skill 版本**：paper_research_skill.md
> **联动文件**：`gap_analysis.md` · `adversarial_review.md` · `file_consistency_check.md` · `experiment_plan.md`

---

## Decision: Hold

> **Current Phase**：3（Deep Dive）
> Go 仅用于 Phase 4：表示创新点已通过 MVP 验证，值得继续投入。

用户已选择 C3，当前仅完成 Phase 2 selection 与 Phase 3 初始化；尚未完成 15+8 深研、paper cards、正式 gap analysis 和完整一致性审计，因此暂标 **Hold**。这里的 Hold 表示证据不足、需要补 Phase 3 深研，不是否定方向。

---

## Reason

### Phase 3 条件检查（深研后，尚未 Go）

| # | 条件 | 状态 |
|---|------|------|
| 1 | 至少 8 篇核心论文已核验 | 未满足；当前仅种子表 |
| 2 | 至少 5 篇核心论文已有 paper card | 未满足 |
| 3 | gap_analysis 明确指出已有工作覆盖/未覆盖 | 未满足；当前为初步假设 |
| 4 | adversarial_review 已完成且风险有回应 | 部分满足；已有初步攻击，未完成深研回应 |
| 5 | file_consistency_check 通过 | 未满足；存在 outdated / risky |
| 6 | 最危险 3 篇 related work 正面比较 | 未满足 |
| 7 | 课题已收窄到可实验场景 | 部分满足；mock tool boundary 初步可行 |
| 8 | 有明确 benchmark 或可构造数据 | 部分满足；需正式 experiment_plan |
| 9 | 有 baseline 与至少 3 个指标 | 部分满足；来自候选阶段假设 |
| 10 | uncertain 论文没有作为核心论据 | 满足 |

### Phase 4 条件检查（Quick Proof 后，才可 Go）

| # | 条件 | 状态 |
|---|------|------|
| 1 | experiment_plan.md + outputs/ 有 minimum evidence | 未开始 |
| 2 | MVP / pilot 支持核心创新点 | 未开始 |

### No-Go 条件检查

| 条件 | 是否触发 |
|------|----------|
| 核心问题已被已有论文完整覆盖 | 未知；ACRFence 需优先核验 |
| 只能通过换术语制造新颖性 | 未知；当前存在风险 |
| 没有可复现实验路径 | 暂未触发 |
| 没有强 baseline | 暂未触发 |
| MVP 成本超出 2–4 个月 | 暂未触发 |
| 主要论据依赖 uncertain 论文 | 未触发 |

---

## 课题收窄确认（如适用）

| 项 | 内容 |
|----|------|
| 旧题目 | Transaction-Safe Agent State Boundaries |
| 新题目 | 待 Phase 3 深研后决定 |

---

## Minimum next step

扩展 `paper_table.csv` 至 ≥15 篇，优先精读并创建 paper cards：ACRFence、AgentDojo、ASB、ToolEmu、OpenHands、SWE-agent、AutoGen，以及 memory provenance / stale memory / memory poisoning 相关工作。

---

## What evidence would change this decision

| 证据 | 决策变化 |
|------|----------|
| ACRFence 已完整覆盖 tool effect + credential + memory provenance + branch semantics | No-Go |
| ACRFence 只覆盖 rollback/external side effects，不覆盖 memory provenance 或 branch contamination | Narrow / Promising |
| 找不到可复现实验场景或强 baseline | Hold / No-Go |
| 能构造 20–30 个 mock tool tasks 且普通 retry / ACRFence-like baseline 仍失败 | Promising（Phase 3 后） |

---

## 评分表（10 分制，可选）

| 维度 | 分 | 说明 |
|------|-----|------|
| 重要性 | 9 | 影响真实 agent recovery / retry / safety |
| 新颖性 | 8 | 候选阶段评分，需经 ACRFence 深研验证 |
| 可形式化 | 8 | tool effect / memory provenance / branch semantics 可形式化 |
| 可验证性 | 8 | mock tool MVP 可构造 |
| 方法空间 | 8 | replay-or-fork、quarantine、credential invalidation |
| 泛化性 | 8 | 可跨工具类型 |
| 顶会匹配 | 8 | agent reliability / security / systems |
| 工程可行 | 8 | 2–4 个月内可做 MVP |
| Baseline 清晰 | 8 | ordinary retry、idempotency key、ACRFence-like |
| 风险可控 | 8 | 候选阶段估计；当前需下调审慎看待 |

**总评**：候选阶段 8.1；Phase 3 尚未完成，当前不作为正式 decision。

---

## 引用

- 空白分析 → `gap_analysis.md`
- 审稿攻击 → `adversarial_review.md`
- 一致性审计 → `file_consistency_check.md`
