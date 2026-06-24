# Experiment Plan: Repair-Test Generation from Agent Failure Traces

> **Experiment Plan Status**：draft
> **前置条件**：`gap_analysis.md` + `adversarial_review.md` + `file_consistency_check.md` 完成后方可填写。
> **决策联动**：见 `decision.md`

> 若最大威胁 work 尚未完成 Phase 3.5 targeted verification，本文件状态只能是 **draft**，不得进入 Phase 4 execution。

---

## 1. 任务定义

**目标**：给定已有 failure trace、critical step / root-cause evidence，生成可执行 regression test 或具体 repair target，并验证该 artifact 是否能复现或阻断失败。

**操作定义**：

| 概念 | 定义 |
|------|------|
| failure evidence | 已定位的 critical step、constraint violation、root-cause category 或 decisive error step |
| regression test | 能复现原失败或验证修复的最小可执行任务 / assertion / trace replay |
| repair target | 需要修改的 prompt、tool schema、policy rule、retrieval step、planner rule、handoff protocol |
| rerun validation | 对生成 artifact 进行 replay / counterfactual / patched rerun，确认失败是否被阻断 |

---

## 2. 数据与环境

| 项 | 规格 |
|----|------|
| 候选数据 | AgentRx / TraceElephant / TRAIL / AgentDebug traces |
| 当前状态 | 仅 draft；需确认数据许可、trace 可运行性和 artifact 标注成本 |

---

## 3. 实验条件（baselines）

| 条件 | 说明 |
|------|------|
| full-trace LLM repair suggestion | 让 LLM 直接生成自然语言修复建议 |
| AgentRx validation-log prompt | 基于 constraint violations 生成 repair/test |
| AgentDebug-style corrective feedback | 生成 corrective feedback，但不要求可执行 test |
| human-written test upper bound | 少量人工 regression tests 作为上界 |

---

## 4. 指标（≥3）

| 指标 | 定义 | 假设 |
|------|------|------|
| test validity | 生成的 regression test 是否可执行且与失败相关 | 本案方法应高于自然语言 repair suggestion |
| failure reproduction rate | test 是否能复现原失败 | 越高越好 |
| post-repair rerun success | repair target 被应用后是否阻断失败 | 越高越好 |
| human audit time reduction | 人工确认修复目标所需时间 | 本案方法应降低审计成本 |

---

## 5. 实验流程

### Pilot

- 暂不执行 Phase 4。
- Phase 3 后的候选 pilot：抽取 20–50 条已定位 failure traces，人工写 gold regression / repair target，与 LLM/AgentRx/AgentDebug baselines 比较。

### Full（pilot 通过后）

- 暂不设计 full-scale 实验。

---

## 6. 消融与泛化

| 实验 | 目的 |
|------|------|
| 只给自然语言 trace summary | 检查结构化 failure evidence 的必要性 |
| 只给 critical step 不给 validation log | 检查 AgentRx-style evidence 的增益 |
| 跨 benchmark 测试 | 检查是否泛化到 tau-bench / Magentic-One / SWE-Agent / GAIA traces |

---

## 7. 错误分析

- 待 Phase 4 pilot 后填写。

---

## 8. 资源与风险

| 风险 | 缓解 |
|------|------|
| AgentRx / AgentDebug 已覆盖 repair-test generation | No-Go |
| trace 数据难以运行 | 优先选择带 reproducible environment 的 TraceElephant 或 AgentRx examples |
| 人工标注成本高 | 先做 20 条小样本，明确 annotation schema |
| 生成内容不可执行 | 将成功标准设为 executable artifact，而非自然语言建议 |

---

## 9. 成功标准（pilot → Go）

| criterion | 阈值 |
|-----------|--------|
| targeted verification 完成 | AgentRx / TraceElephant / TRAIL / Who&When 均 `threat_verified` |
| test validity | 初步目标 ≥60% |
| failure reproduction rate | 初步目标 ≥50% |
| post-repair rerun success | 初步目标相对 baseline 有提升 |
| audit time reduction | 初步目标相对 full-trace LLM suggestion 降低人工确认时间 |
