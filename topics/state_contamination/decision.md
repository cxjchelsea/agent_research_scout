# Decision: Dual-State Contamination in Software Engineering Agents

> **审计日期**：2026-03-18（方案 A 重调研 + 结构升级）  
> **Skill 版本**：paper_research_skill.md v2（§七–§十二）  
> **联动文件**：`gap_analysis.md` · `adversarial_review.md` · `file_consistency_check.md` · `experiment_plan.md`

---

## Decision: **Narrow**

方向可做且已收窄；**尚未执行 pilot**，暂不能标 Go。完成 10 题 pilot 并达到 `adversarial_review.md` 中的 minimum evidence 后，升级为 **Go**。

---

## Reason

### Go 条件检查

| # | 条件 | 状态 |
|---|------|------|
| 1 | ≥8 篇核心论文已核验 | ✅ 8/8 verified |
| 2 | ≥5 篇有 paper card | ✅ 8/8 |
| 3 | gap_analysis 明确覆盖/空白 | ✅ 见 `gap_analysis.md` |
| 4 | 最危险 3 篇已正面比较 | ✅ CCRM, Wang et al., GA-Rollback |
| 5 | 课题收窄到可实验场景 | ✅ SWE-bench Verified |
| 6 | 有明确 benchmark | ✅ Verified 子集 |
| 7 | 有 baseline | ✅ dirty / clean-restart / full-reset |
| 8 | ≥3 可量化指标 | ✅ CR, RG, WSD |
| 9 | 有最小实验方案 | ✅ `experiment_plan.md` pilot |
| 10 | uncertain 论文不作核心论据 | ✅ 0 uncertain |
| 11 | adversarial_review 已完成 | ✅ 见 `adversarial_review.md` |
| 12 | file_consistency_check 通过 | ✅ 见 `file_consistency_check.md` |
| 13 | **pilot 数据验证效应量** | ❌ **未完成** → 不能 Go |

### No-Go 条件检查

| 条件 | 是否触发 |
|------|----------|
| 核心问题已被完整覆盖 | ⚠️ 部分（CCRM 覆盖 context） |
| 只能换术语 | ⚠️ 风险存在；靠 dual-state benchmark 化解 |
| 无复现实验 | ❌ 未触发（plan 已有） |
| 无强 baseline | ❌ 未触发 |
| 纯工程拼装 | ⚠️ 见 `adversarial_review.md` engineering-only risk = 高 |
| benchmark 完全人工 | ❌ 基于 Verified 真实 issue |
| 指标无法说服审稿人 | ⚠️ 待 pilot |
| 核心论据依赖 uncertain | ❌ 未触发 |

**结论**：无硬性 No-Go → **Narrow**（非 Hold，因 gap + adversarial 已闭环）

---

## 课题收窄确认

| 项 | 内容 |
|----|------|
| 旧题目 | State Contamination in Long-Horizon Tool-Using Agents |
| 新题目 | **Dual-State Contamination in Software Engineering Agents** |
| 删除 | 泛 agent、memory laundering、CCRM 理论、ACRFence 复刻 |
| 保留 | Verified eval、dual-state metrics、recovery blind spot |

---

## Minimum next step

**执行 pilot** — 按 `outputs/pilot/checklist.md`：

```powershell
cd scripts/pilot
pip install -r requirements.txt
python sample_instances.py
python run_pilot.py --dry-run    # 检查命令
python run_pilot.py --execute    # 真实运行（Docker + API）
python analyze_pilot.py
python update_decision_draft.py  # 合并进本文件
```

---

## What evidence would change this decision

| 证据 | 决策变化 |
|------|----------|
| Pilot RG ≥ 5pp + C > B on ≥2 题 | **Narrow → Go** |
| Pilot RG < 3pp | **Narrow → No-Go** |
| Pilot RG 3–5pp | **Hold** |
| CCRM 发布 dual-state benchmark | **No-Go** |

---

## 评分表（10 分制）

| 维度 | 分 | 说明 |
|------|-----|------|
| 1. 重要性 | 8 | retry 是生产默认行为 |
| 2. 新颖性 | 6 | CCRM/Wang 占术语；dual-state eval 有空间 |
| 3. 可形式化 | 8 | Context/World 可操作定义 |
| 4. 可验证性 | 8 | Verified + mini-SWE-agent |
| 5. 方法空间 | 6 | MVP 偏 benchmark |
| 6. 泛化性 | 5 | MVP 限 Verified |
| 7. 顶会匹配 | 7 | ICLR/ICSE benchmark 角 |
| 8. 工程可行性 | 8 | 10 题 pilot 可行 |
| 9. Baseline 清晰度 | 9 | 三条件清晰 |
| 10. 风险 | 4 | incremental / 工程技巧风险高 |
| **总分** | **6.9 / 10** | 符合 **Narrow** |

---

## 引用（详情见独立文件）

| 主题 | 文件 |
|------|------|
| 空白与换名判断 | `gap_analysis.md` |
| 审稿攻击与 minimum evidence | `adversarial_review.md` |
| 文件一致性审计 | `file_consistency_check.md` |
| MVP 实验设计 | `experiment_plan.md` |
