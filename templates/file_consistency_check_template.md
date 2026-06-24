# File Consistency Check: {{topic_name}}

> **目的**：检查 topic 目录内所有调研文件是否一致，并检查证据是否足够支持当前 decision。
> **审计日期**：

---

## 1. 文件状态总表

| File | Status | Required Update |
|------|--------|-----------------|
| topic_brief.md | consistent / outdated | |
| paper_table.csv | consistent / needs verification | |
| related_work.md | consistent / outdated | |
| paper_cards/ | complete / incomplete / stubs only | |
| gap_analysis.md | consistent / risky | |
| adversarial_review.md | consistent / missing | |
| experiment_plan.md | draft / ready / not ready / premature | |
| decision.md | ready / not ready | |
| file_consistency_check.md | — | 本文件 |

**Status 说明**：consistent = 与当前课题版本一致；outdated = 需同步；risky = 论据可能依赖 uncertain 论文。

---

## 2. Skill 一致性规则逐项检查

| # | 规则 | Pass? | 说明 |
|---|------|-------|------|
| 1 | uncertain 论文不作 gap 核心论据 | | |
| 2 | gap 收窄后 topic_brief 已同步 | | |
| 3 | gap 认为不能实验时，experiment_plan 未强行填写 | | |
| 4 | experiment_plan 有 MVP 时，decision 说明是否进入 pilot | | |
| 5 | related_work 引用论文均在 paper_table 中 | | |
| 6 | core_read=yes 均有 paper_card | | |
| 7 | remove 论文已从 related_work/gap 降级或删除 | | |
| 8 | venue/year/title 修正已全库同步 | | |
| 9 | 课题名称/范围以最新 gap_analysis 为准 | | |
| 10 | decision=Go 时 experiment_plan 有 data/baseline/metric/MVP | | |
| 11 | core_read=yes 的 paper card 均达到 close_read 或 threat_verified | | |
| 12 | 最大威胁 1–3 篇 work 均达到 threat_verified | | |
| 13 | gap_analysis 有 claim coverage matrix 且 Evidence 不为空 | | |
| 14 | targeted verification 未完成时 experiment_plan 仍为 draft | | |

---

## 3. 跨文件关键字段对齐

| 字段 | topic_brief | gap_analysis | decision | 是否一致 |
|------|-------------|--------------|----------|----------|
| 课题名称 | | | | |
| 核心 claim | | | | |
| MVP benchmark | | | | |
| 当前 Decision | — | — | | |

---

## 4. Evidence Readiness

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 8 篇核心论文 metadata_verified | pass / fail | |
| ≥5 篇核心论文 close_read 或 threat_verified | pass / fail | |
| 最大威胁 1–3 篇 threat_verified | pass / fail | |
| claim coverage matrix 完成 | pass / fail | |
| 最大威胁是否覆盖核心 claim | yes / partial / no / unknown | |
| experiment_plan status | draft / ready / premature | |
| 是否允许进入 Phase 4 execution | yes / no | |

---

## 5. 发现的问题与待办

1.
2.

---

## 6. 审计结论

- [ ] 全部 consistent → 可进入 decision 更新
- [ ] 存在 outdated → 先修复再 decision
- [ ] 存在 risky → 降级相关论据或标记 Hold
- [ ] evidence not ready → Phase 3 不得 complete，experiment_plan 保持 draft
