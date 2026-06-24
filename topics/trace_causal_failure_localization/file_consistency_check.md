# File Consistency Check: Repair-Test Generation from Agent Failure Traces

> **目的**：检查 topic 目录内所有调研文件是否一致，并检查证据是否足够支持当前 decision。
> **审计日期**：2026-06-24

---

## 1. 文件状态总表

| File | Status | Required Update |
|------|--------|-----------------|
| topic_brief.md | consistent | 已同步收窄题 |
| paper_table.csv | consistent | 17 篇，8 篇 core_read |
| related_work.md | consistent | 已按强威胁更新 |
| paper_cards/ | complete | 8 张 core cards；最大威胁 cards 已 threat_verified |
| gap_analysis.md | consistent | 已含 claim coverage matrix |
| adversarial_review.md | consistent | 已记录原题 No-Go / 收窄 Narrow |
| experiment_plan.md | draft | targeted verification 未完成，不得 ready |
| decision.md | ready | Narrow |
| file_consistency_check.md | — | 本文件 |

**Status 说明**：consistent = 与当前课题版本一致；outdated = 需同步；risky = 论据可能依赖未完成的 claim-level verification。

---

## 2. Skill 一致性规则逐项检查

| # | 规则 | Pass? | 说明 |
|---|------|-------|------|
| 1 | uncertain 论文不作 gap 核心论据 | Pass | 当前还未进入 topic-level 论据使用。 |
| 2 | gap 收窄后 topic_brief 已同步 | Pass | 已同步为 Repair-Test Generation from Agent Failure Traces。 |
| 3 | gap 认为不能实验时，experiment_plan 未强行填写 | Pass | experiment_plan 保持 draft。 |
| 4 | experiment_plan 有 MVP 时，decision 说明是否进入 pilot | Pass | decision 明确不得进入 Phase 4。 |
| 5 | related_work 引用论文均在 paper_table 中 | Pass | 相关核心论文均在 paper_table。 |
| 6 | core_read=yes 均有 paper_card | Pass | 8 篇 core_read 均有 card。 |
| 7 | remove 论文已从 related_work/gap 降级或删除 | Pass | 暂无 remove。 |
| 8 | venue/year/title 修正已全库同步 | Pass | 暂无修正。 |
| 9 | 课题名称/范围以最新 gap_analysis 为准 | Pass | 当前一致。 |
| 10 | decision=Go 时 experiment_plan 有 data/baseline/metric/MVP | Pass | decision 不是 Go。 |
| 11 | core_read=yes 的 paper card 均达到 close_read 或 threat_verified | Pass | 4 张 threat_verified，4 张 close_read。 |
| 12 | 最大威胁 1–3 篇 work 均达到 threat_verified | Pass | TRAIL / AgentRx / TraceElephant / Who&When 已 threat_verified。 |
| 13 | gap_analysis 有 claim coverage matrix 且 Evidence 不为空 | Pass | matrix 已填入 evidence 和 implication。 |
| 14 | targeted verification 未完成时 experiment_plan 仍为 draft | Pass | experiment_plan 为 draft。 |

---

## 3. 跨文件关键字段对齐

| 字段 | topic_brief | gap_analysis | decision | 是否一致 |
|------|-------------|--------------|----------|----------|
| 课题名称 | Repair-Test Generation from Agent Failure Traces | Repair-Test Generation from Agent Failure Traces | Repair-Test Generation from Agent Failure Traces | 是 |
| 核心 claim | failure trace → executable regression test / repair target | repair-test artifact generation | Narrow | 是 |
| MVP benchmark | AgentRx / TraceElephant / TRAIL traces | 20–50 examples | draft | 是 |
| 当前 Decision | — | 原题 No-Go；收窄题 Narrow | Narrow | 是 |

---

## 4. Evidence Readiness

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 8 篇核心论文 metadata_verified | pass | 8 篇 core_read 均 verified。 |
| ≥5 篇核心论文 close_read 或 threat_verified | pass | 8/8 cards 达到 close_read 或 threat_verified。 |
| 最大威胁 1–3 篇 threat_verified | pass | TRAIL / AgentRx / TraceElephant / Who&When 已 threat_verified。 |
| claim coverage matrix 完成 | pass | Evidence 已填写。 |
| 最大威胁是否覆盖核心 claim | partial / yes | 原始 localization claim 基本覆盖；收窄 repair-test claim 未完全覆盖。 |
| experiment_plan status | draft | 符合 skill。 |
| 是否允许进入 Phase 4 execution | no | Narrow 题仍需确认数据和 artifact 标注，不进入 execution。 |

---

## 5. 发现的问题与待办

1. 若继续，下一步核验 AgentDebug / AgentRx 是否已覆盖 executable regression-test generation。
2. 设计 20–50 条 failure-to-test 标注样例。
3. 明确 test validity / reproduction / post-repair rerun success 的可执行评估协议。
4. 不得以原始 trace localization claim 继续。

---

## 6. 审计结论

- [x] 全部 consistent → 可进入 decision 更新
- [ ] 存在 outdated → 先修复再 decision
- [ ] 存在 risky → 降级相关论据或标记 Hold
- [ ] evidence not ready → Phase 3 不得 complete，experiment_plan 保持 draft

审计结论：Phase 3.5 targeted verification 对原题给出负面结果。原题应 No-Go；收窄题可 Narrow，但 experiment_plan 仍保持 draft，不进入 Phase 4 execution。
