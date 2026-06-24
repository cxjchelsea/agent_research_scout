# File Consistency Check: Recovery-Safe Memory Provenance for Tool-Using Agents

> **目的**：检查 topic 目录内所有调研文件是否一致，防止 topic_brief / gap / experiment 相互矛盾。
> **审计日期**：2026-06-24

---

## 1. 文件状态总表

| File | Status | Required Update |
|------|--------|-----------------|
| topic_brief.md | consistent | 已同步收窄到 Recovery-Safe Memory Provenance |
| paper_table.csv | consistent | 16 篇；8 篇 core_read=yes；uncertain 不作核心论据 |
| related_work.md | consistent | 已按 rollback/tool security/memory poisoning/memory evaluation/runtime 分组 |
| paper_cards/ | complete | 8 篇 core_read 均有 card |
| gap_analysis.md | consistent | 已给出 Narrow 结论 |
| adversarial_review.md | consistent | 已更新收窄后的攻击与回应 |
| experiment_plan.md | ready | MVP 已填写；进入 Phase 4 前仍需用户确认 |
| decision.md | ready | 当前为 Narrow |
| file_consistency_check.md | — | 本文件 |

**Status 说明**：consistent = 与当前课题版本一致；outdated = 需同步；risky = 论据可能依赖 uncertain 论文。

---

## 2. Skill 一致性规则逐项检查

| # | 规则 | Pass? | 说明 |
|---|------|-------|------|
| 1 | uncertain 论文不作 gap 核心论据 | Pass | MPBench / MINJA / InjecAgent / MemoryBank 仅作背景或待核验线索 |
| 2 | gap 收窄后 topic_brief 已同步 | Pass | topic_brief v2 已同步新题目 |
| 3 | gap 认为不能实验时，experiment_plan 未强行填写 | Pass | 当前 gap 允许 Narrow 后写 MVP |
| 4 | experiment_plan 有 MVP 时，decision 说明是否进入 pilot | Pass | decision 给出 Minimum next step，但尚未进入 Phase 4 Go |
| 5 | related_work 引用论文均在 paper_table 中 | Pass | 当前引用均来自 paper_table |
| 6 | core_read=yes 均有 paper_card | Pass | 8/8 cards 已创建 |
| 7 | remove 论文已从 related_work/gap 降级或删除 | N/A | 当前无 remove |
| 8 | venue/year/title 修正已全库同步 | Pass | paper_table 与 cards 对齐 |
| 9 | 课题名称/范围以最新 gap_analysis 为准 | Pass | topic_brief / gap / decision 均为新 scope |
| 10 | decision=Go 时 experiment_plan 有 data/baseline/metric/MVP | N/A | 当前不是 Go |

---

## 3. 跨文件关键字段对齐

| 字段 | topic_brief | gap_analysis | decision | 是否一致 |
|------|-------------|--------------|----------|----------|
| 课题名称 | Recovery-Safe Memory Provenance for Tool-Using Agents | Recovery-Safe Memory Provenance for Tool-Using Agents | Narrow | 是 |
| 核心 claim | recovery 后 memory provenance / validity / quarantine | recovery-induced memory contamination | Narrow | 是 |
| MVP benchmark | mock tool + memory scenarios | tool observation → memory write → rollback/fork → later retrieval | Narrow | 是 |
| 当前 Decision | — | Narrow | Narrow | 是 |

---

## 4. 发现的问题与待办

1. Phase 4 前需要用户确认是否按 `experiment_plan.md` 启动 pilot。
2. 若继续深研，可补充 MPBench / MINJA 作者信息并决定是否升级为 verified core。
3. 实验实现时需要避免 benchmark 太人工，优先选 email/payment/file/GitHub-like 场景。

---

## 5. 审计结论

- [x] 全部 consistent → 可进入 decision 更新
- [ ] 存在 outdated → 先修复再 decision
- [ ] 存在 risky → 降级相关论据或标记 Hold
