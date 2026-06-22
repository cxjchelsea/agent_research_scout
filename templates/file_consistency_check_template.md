# File Consistency Check: {{topic_name}}

> **目的**：检查 topic 目录内所有调研文件是否一致，防止 topic_brief / gap / experiment 相互矛盾。  
> **审计日期**：

---

## 1. 文件状态总表

| File | Status | Required Update |
|------|--------|-----------------|
| topic_brief.md | consistent / outdated | |
| paper_table.csv | consistent / needs verification | |
| related_work.md | consistent / outdated | |
| paper_cards/ | complete / incomplete | |
| gap_analysis.md | consistent / risky | |
| adversarial_review.md | consistent / missing | |
| experiment_plan.md | ready / not ready / premature | |
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

---

## 3. 跨文件关键字段对齐

| 字段 | topic_brief | gap_analysis | decision | 是否一致 |
|------|-------------|--------------|----------|----------|
| 课题名称 | | | | |
| 核心 claim | | | | |
| MVP benchmark | | | | |
| 当前 Decision | — | — | | |

---

## 4. 发现的问题与待办

1.
2.

---

## 5. 审计结论

- [ ] 全部 consistent → 可进入 decision 更新
- [ ] 存在 outdated → 先修复再 decision
- [ ] 存在 risky → 降级相关论据或标记 Hold
