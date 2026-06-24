# Decision: {{topic_name}}

> **审计日期**：  
> **Skill 版本**：paper_research_skill.md  
> **联动文件**：`gap_analysis.md` · `adversarial_review.md` · `file_consistency_check.md` · `experiment_plan.md`

---

## Decision: Promising / Narrow / Go / Hold / No-Go

> **Current Phase**：3（Deep Dive）/ 3.5（Targeted Verification）/ 4（Quick Proof）
> Go 仅用于 Phase 4：表示创新点已通过 MVP 验证，值得继续投入。

（一句话说明）

---

## Reason

### Phase 3 条件检查（深研后，尚未 Go）

| # | 条件 | 状态 |
|---|------|------|
| 1 | 至少 8 篇核心论文 metadata_verified | |
| 2 | 至少 5 篇核心论文 close_read 或 threat_verified | |
| 3 | 最大威胁 1–3 篇 work 均 threat_verified | |
| 4 | 最大威胁 work 有 claim coverage matrix，且 Evidence 不为空 | |
| 5 | gap_analysis 明确已有工作覆盖/未覆盖 | |
| 6 | adversarial_review 已完成且风险有回应 | |
| 7 | file_consistency_check 的 file consistency 与 evidence readiness 均通过 | |
| 8 | 最危险 related work 已正面比较 | |
| 9 | 课题已收窄到可实验场景 | |
| 10 | 有 benchmark / data、baseline 与 ≥3 个指标 | |
| 11 | uncertain 论文没有作为核心论据 | |

### Phase 3.5 Targeted Verification Gate

| Gate | 状态 |
|------|------|
| 最大威胁 work 是否覆盖核心 claim | yes / partial / no / unknown |
| 最大威胁 work 是否覆盖 proposed mechanism | yes / partial / no / unknown |
| 最大威胁 work 是否覆盖 benchmark / evaluation setting | yes / partial / no / unknown |
| 如果扩展最大威胁方法，是否自然得到本案方法 | yes / partial / no / unknown |
| 是否允许 experiment_plan 从 draft 升为 ready | yes / no |
| 是否允许进入 Phase 4 execution | yes / no |

### Phase 4 条件检查（Quick Proof 后，才可 Go）

| # | 条件 | 状态 |
|---|------|------|

### No-Go 条件检查

| 条件 | 是否触发 |
|------|----------|

---

## 课题收窄确认（如适用）

| 项 | 内容 |
|----|------|
| 旧题目 | |
| 新题目 | |

---

## Minimum next step

---

## What evidence would change this decision

| 证据 | 决策变化 |
|------|----------|

---

## 评分表（10 分制，可选）

| 维度 | 分 | 说明 |
|------|-----|------|

**总评**：

---

## 引用

- 空白分析 → `gap_analysis.md`
- 审稿攻击 → `adversarial_review.md`
- 一致性审计 → `file_consistency_check.md`
