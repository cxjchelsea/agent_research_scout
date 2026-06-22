# File Consistency Check: Dual-State Contamination

> **审计日期**：2026-03-18  
> **课题版本**：v2（Dual-State Contamination in Software Engineering Agents）  
> **触发原因**：skill 升级 + 方案 A 重调研 + 新增独立 adversarial / consistency 文件

---

## 1. 文件状态总表

| File | Status | Required Update |
|------|--------|-----------------|
| topic_brief.md | **consistent** | v2 已与 gap 收窄同步 |
| paper_table.csv | **consistent** | 20/20 verified；已含 source_type |
| related_work.md | **consistent** | venue/标题/verified 列已对齐 |
| paper_cards/ | **complete** | 8/8 core_read=yes 均有 card |
| gap_analysis.md | **consistent** | 已拆出 adversarial / consistency 至独立文件 |
| adversarial_review.md | **consistent** | 本轮回新建并填充 |
| experiment_plan.md | **ready** | MVP pilot 已写；待 pilot 执行后更新结果 |
| decision.md | **consistent** | Narrow；与 adversarial 结论一致 |
| file_consistency_check.md | **consistent** | 本文件 |

---

## 2. Skill 一致性规则逐项检查

| # | 规则 | Pass? | 说明 |
|---|------|-------|------|
| 1 | uncertain 论文不作 gap 核心论据 | ✅ | paper_table 0 uncertain；gap/adversarial 核心论据均为 verified |
| 2 | gap 收窄后 topic_brief 已同步 | ✅ | topic_brief v2 标题与 Dual-State 定义一致 |
| 3 | gap 认为不能实验时 experiment_plan 未强行填写 | ✅ | gap 结论为「待 pilot」；plan 为 MVP pilot 非 full claim |
| 4 | experiment_plan 有 MVP 时 decision 说明是否进入 pilot | ✅ | decision.md：Minimum next step = 10 题 pilot |
| 5 | related_work 引用论文均在 paper_table 中 | ✅ | 20 篇一一对应 |
| 6 | core_read=yes 均有 paper_card | ✅ | 8/8 卡片存在 |
| 7 | remove 论文已从 related_work/gap 降级 | ✅ | 0 remove |
| 8 | venue/year/title 修正已全库同步 | ✅ | Devil's Advocate、COLM、ICLR 2025 OpenHands、AgentRx arXiv 等已修正 |
| 9 | 课题名称/范围以最新 gap_analysis 为准 | ✅ | 三文件统一为 Dual-State / SWE-bench Verified |
| 10 | decision=Go 时 plan 有 data/baseline/metric/MVP | ✅（N/A） | 当前 decision=**Narrow** 非 Go；plan 已具备 MVP 要素 |

---

## 3. 跨文件关键字段对齐

| 字段 | topic_brief | gap_analysis | adversarial_review | decision | 一致？ |
|------|-------------|--------------|-------------------|----------|--------|
| 课题名称 | Dual-State Contamination in SE Agents | 同左 | 同左 | 同左 | ✅ |
| 核心 claim | context + world dual-state eval | dual-state contamination eval | 非 context-only | dual-state metrics | ✅ |
| MVP benchmark | SWE-bench Verified | Verified 10→50–100 | Verified 10 题 pilot | Verified pilot | ✅ |
| 当前 Decision | — | 待 pilot | Narrow | **Narrow** | ✅ |
| 最大威胁 | CCRM, Wang et al. | CCRM S1 | CCRM arXiv 2605.08563 | CCRM | ✅ |

---

## 4. core_read 与 paper_cards 映射

| paper_table title (short) | core_read | paper_card 文件 | 存在？ |
|---------------------------|-----------|-----------------|--------|
| CCRM | yes | ccrm_context_contamination.md | ✅ |
| Wang et al. state contamination | yes | state_contamination_memory_agents.md | ✅ |
| GA-Rollback | yes | ga_rollback.md | ✅ |
| ACRFence | yes | acrfence.md | ✅ |
| AgentDebug | yes | agentdebug.md | ✅ |
| MemoryAgentBench | yes | memoryagentbench.md | ✅ |
| SWE-bench | yes | swe_bench.md | ✅ |
| Hell or High Water | yes | hell_or_high_water.md | ✅ |

---

## 5. 发现的问题与待办

| # | 问题 | 状态 | 待办 |
|---|------|------|------|
| 1 | adversarial / consistency 曾嵌入 gap/decision | **已修复** | 已拆为独立文件 |
| 2 | README 未反映新 workflow | **已修复** | README 已更新 9 步 workflow |
| 3 | skill §十 未列新文件名 | **已修复** | paper_research_skill.md 已同步 |
| 4 | pilot 未执行 | **开放** | 执行 experiment_plan Phase 1 后重跑本检查 |

---

## 6. 审计结论

- [x] 调研文件全部 **consistent**（无 outdated / risky）
- [x] 可维持 **decision = Narrow**
- [ ] pilot 完成后需 **重跑本检查** 并更新 decision（Go / Hold / No-Go）

**下一步**：执行 `experiment_plan.md` 10 题 pilot → 更新 `outputs/pilot/` → 重跑 `file_consistency_check.md` + `decision.md`
