# Experiment Plan: Agentic Regression Scenarios for Tool-Using Agent Failures

> **Experiment Plan Status**：draft
> **前置条件**：`gap_analysis.md` + `adversarial_review.md` + `file_consistency_check.md` 完成后方可填写。
> **决策联动**：见 `decision.md`

> 若最大威胁 work 尚未完成 Phase 3.5 targeted verification，本文件状态只能是 **draft**，不得进入 Phase 4 execution。

---

## 1. 任务定义

**目标**：给定已有 tool-using agent failure trace、critical step / root-cause evidence，生成可重放 agentic regression scenario，并验证该 scenario 是否能复现失败或验证 agent-level 修复。

**操作定义**：

| 概念 | 定义 |
|------|------|
| failure evidence | 已定位的 critical step、constraint violation、root-cause category 或 decisive error step |
| agentic regression scenario | 可重放的 agent 任务场景，包括 user goal、initial environment/tool state、policy/memory context、mock backend、oracle |
| repair target | 需要修改的 prompt、tool schema、policy rule、retrieval step、planner rule、handoff protocol |
| rerun validation | 对生成 scenario 进行 replay / counterfactual / patched rerun，确认失败是否被阻断 |

---

## 2. 数据与环境

| 项 | 规格 |
|----|------|
| 候选数据 | AgentRx / TraceElephant / TRAIL / AgentDebug traces |
| 当前状态 | 仅 draft；需确认数据许可、trace 可运行性、mock state 可恢复性和 scenario 标注成本 |

---

## 3. 实验条件（baselines）

| 条件 | 说明 |
|------|------|
| full-trace LLM repair suggestion | 让 LLM 直接生成自然语言修复建议 |
| AgentRx validation-log prompt | 基于 constraint violations 生成 scenario/oracle |
| AgentDebug-style corrective feedback | 生成 corrective feedback，但不要求可重放 scenario |
| Issue2Test-style software test generator | 传统 issue-to-test baseline，验证是否退化为软件测试问题 |
| human-written scenario upper bound | 少量人工 agentic scenarios 作为上界 |

---

## 4. 指标（≥3）

| 指标 | 定义 | 假设 |
|------|------|------|
| scenario validity | 生成的 scenario 是否包含可运行 user goal / tool state / oracle | 本案方法应高于自然语言 repair suggestion |
| failure reproduction rate | scenario 是否能复现原 agent failure | 越高越好 |
| post-repair rerun success | repair target 被应用后是否阻断失败 | 越高越好 |
| human audit time reduction | 人工确认修复目标所需时间 | 本案方法应降低审计成本 |

---

## 5. 实验流程

### Pilot

- 暂不执行 Phase 4。
- Phase 3.5b 后的候选 feasibility check：抽取 10–20 条已定位 tool-using agent failure traces，人工写 gold agentic regression scenarios，与 LLM/AgentRx/AgentDebug/Issue2Test-style baselines 比较。

### Full（pilot 通过后）

- 暂不设计 full-scale 实验。

---

## 6. 消融与泛化

| 实验 | 目的 |
|------|------|
| 只给自然语言 trace summary | 检查结构化 failure evidence 的必要性 |
| 只给 critical step 不给 validation log | 检查 AgentRx-style evidence 的增益 |
| 去掉 tool/policy/mock state | 检查 agentic scenario 是否区别于普通软件 test |
| 跨 benchmark 测试 | 检查是否泛化到 tau-bench / Magentic-One / SWE-Agent / GAIA traces |

---

## 7. 错误分析

- 待 Phase 4 pilot 后填写。

---

## 8. 资源与风险

| 风险 | 缓解 |
|------|------|
| 任务退化为传统 software test generation | No-Go 或再次回到 scout |
| trace 数据难以运行 | 优先选择带 reproducible environment 的 TraceElephant 或 AgentRx examples |
| 人工标注成本高 | 先做 20 条小样本，明确 annotation schema |
| 生成内容不可执行 | 将成功标准设为 replayable agentic scenario，而非自然语言建议 |

---

## 9. 成功标准（pilot → Go）

| criterion | 阈值 |
|-----------|--------|
| Phase 3.5b 完成 | AgentDebug / AgentRx / software testing 三点已核验 |
| scenario validity | 初步目标 ≥60% |
| failure reproduction rate | 初步目标 ≥50% |
| post-repair rerun success | 初步目标相对 baseline 有提升 |
| audit time reduction | 初步目标相对 full-trace LLM suggestion 降低人工确认时间 |
