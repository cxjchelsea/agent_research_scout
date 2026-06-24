# File Consistency Check: Transaction-Safe Agent State Boundaries

> **目的**：检查 topic 目录内所有调研文件是否一致，防止 topic_brief / gap / experiment 相互矛盾。
> **审计日期**：2026-06-24

---

## 1. 文件状态总表

| File | Status | Required Update |
|------|--------|-----------------|
| topic_brief.md | consistent | Phase 3 深研后若收窄需同步 |
| paper_table.csv | needs verification | 当前 8 篇种子论文，未达到 ≥15；uncertain 条目不能作为核心论据 |
| related_work.md | outdated | 仅占位，需按 category 完成 |
| paper_cards/ | incomplete | 当前未设置 core_read=yes，也未完成 cards |
| gap_analysis.md | risky | 初步 gap，依赖后续深研 ACRFence |
| adversarial_review.md | consistent | 初步攻击已指出最大风险 |
| experiment_plan.md | not ready | Phase 3 未完成，不填写 MVP |
| decision.md | ready | 当前为 Hold：证据不足，需补 Phase 3 深研 |
| file_consistency_check.md | — | 本文件 |

**Status 说明**：consistent = 与当前课题版本一致；outdated = 需同步；risky = 论据可能依赖 uncertain 论文。

---

## 2. Skill 一致性规则逐项检查

| # | 规则 | Pass? | 说明 |
|---|------|-------|------|
| 1 | uncertain 论文不作 gap 核心论据 | Pass | ToolEmu / InjecAgent 仅作待核验线索 |
| 2 | gap 收窄后 topic_brief 已同步 | Pass | 当前尚未正式收窄 |
| 3 | gap 认为不能实验时，experiment_plan 未强行填写 | Pass | experiment_plan 仅说明未满足前置条件 |
| 4 | experiment_plan 有 MVP 时，decision 说明是否进入 pilot | N/A | 尚未写 MVP |
| 5 | related_work 引用论文均在 paper_table 中 | Pass | 当前引用均来自 paper_table |
| 6 | core_read=yes 均有 paper_card | Pass | 当前无 core_read=yes |
| 7 | remove 论文已从 related_work/gap 降级或删除 | N/A | 当前无 remove |
| 8 | venue/year/title 修正已全库同步 | Pass | 当前按 discovery seed 初始化 |
| 9 | 课题名称/范围以最新 gap_analysis 为准 | Pass | 当前与 topic_brief v1 一致 |
| 10 | decision=Go 时 experiment_plan 有 data/baseline/metric/MVP | N/A | 当前不是 Go |

---

## 3. 跨文件关键字段对齐

| 字段 | topic_brief | gap_analysis | decision | 是否一致 |
|------|-------------|--------------|----------|----------|
| 课题名称 | Transaction-Safe Agent State Boundaries | Transaction-Safe Agent State Boundaries | Hold | 是 |
| 核心 claim | agent state boundary consistency | tool/memory/credential/branch boundary | Hold | 暂一致 |
| MVP benchmark | mock tool scenarios | email/payment/file/GitHub-like tasks | Hold | 暂一致 |
| 当前 Decision | — | 继续进入 Phase 3 深研 | Hold | 是 |

---

## 4. 发现的问题与待办

1. `paper_table.csv` 需要扩展到 ≥15 篇，并核验 ToolEmu / InjecAgent。
2. 需要完成 ACRFence、AgentDojo、ASB 等核心 paper cards 后再更新 gap / decision。
3. 需要补充 memory provenance、stale memory、credential scope 相关论文。
4. `related_work.md` 需要按 category 完成，不能停留在占位。

---

## 5. 审计结论

- [ ] 全部 consistent → 可进入 decision 更新
- [x] 存在 outdated → 先修复再 decision
- [x] 存在 risky → 降级相关论据或标记 Hold
