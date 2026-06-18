# Paper Card: Why Retrying Fails: Context Contamination in LLM Agent Pipelines

## 1. 基本信息

- Title: Why Retrying Fails: Context Contamination in LLM Agent Pipelines
- Year: 2026
- Venue: arXiv (2605.08563)
- Authors: Zhanfu Yang
- Link: https://arxiv.org/abs/2605.08563
- Code: 未公开独立 repo（理论+实证论文）
- Benchmark / Dataset: SWE-bench Verified retry 轨迹；Monte Carlo 仿真

## 2. 它研究什么问题？

多步 tool-augmented agent 失败后，常见做法是 **in-context retry**，但失败 attempt 仍留在 context window 中，导致后续 attempt 的 per-step 错误率系统性升高——即 **context-contaminated restart**。该现象工程上常见，但此前缺乏形式化模型。

## 3. 它的核心贡献是什么？

提出 **Context-Contaminated Restart Model (CCRM)**，并给出五条理论结果：pass@K 闭式公式、cascade overhead、最优 budget 分配、Le Cam 下界、clean-restart dominance theorem。

## 4. 它的方法是什么？

- 将 pipeline 建模为长度 T 的 tool-call 链，基础错误率 ε₀，污染后错误率 ε₁ > ε₀。
- 对比 dirty-retry vs clean-restart 两种 restart 协议。
- 用 SWE-bench Verified 真实 retry 数据拟合 CCRM，估计 ε₁/ε₀ = 7.1。

## 5. 它怎么实验？

### Task

多步 agent pipeline 在 K 次 attempt 内成功概率；最优 depth T* 与 retry 预算分配。

### Dataset / Environment

SWE-bench Verified；Monte Carlo 验证理论预测。

### Baselines

IID step failure 模型（假设 retry 独立）。

### Metrics

pass@K；cascade ratio ε₁/ε₀；clean-restart vs CCRM 拟合误差。

## 6. 它发现了什么失败模式？

- **Context contamination**：失败轨迹留在 context 会放大后续错误（非独立 retry）。
- IID 模型 **高估 pass@3 17.4pp**（98.6% vs 81.2%）。
- Clean-restart 严格优于 contaminated retry（ dominance theorem）。

## 7. 它没有覆盖什么？

- 假设 step 级 IID（真实 agent 错误有结构依赖）。
- 未给出完整 agent 系统的 mitigation 实现。
- 未区分 context state vs external world state（文件/DB）的不一致。
- 未建 benchmark 专门测 contamination-aware recovery。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| 长链路 Agent | ✓ SWE 多步 tool pipeline |
| 工具使用 | ✓ tool-call chain |
| 状态管理 | ✓ context 即 agent state |
| rollback/recovery | ✓ clean-restart 协议 |
| error propagation | ✓ ε₁ > ε₀ 形式化 |
| 直接术语 | **context contamination** |

## 9. 它是否削弱我的创新性？

**部分覆盖，且高度威胁命名空间。**

- 已用与我课题几乎相同的术语 formalize 了 retry 污染。
- 但聚焦 **context window retry**，未覆盖 memory write-back laundering、executable world state、provenance tracking。
- 创新需从「CCRM 扩展」或「cross-state contamination benchmark」切入，不能重复 CCRM 理论。

## 10. 我可以从它的 limitation 里切什么？

1. 构建 **ContaminationBench**：同时测 context 污染 + workspace/DB 污染 + clean-restart@k。
2. 提出 **Dual-State CCRM**：分离 message state 与 world state 的污染通道。
3. 在 WebArena / τ-bench 上验证 CCRM 是否泛化出 SWE 之外。

## 11. 重要引用句

> "When an LLM agent fails a multi-step tool-augmented task and retries, the failed attempt typically remains in its context window—contaminating the next attempt and elevating the per-step error rate beyond the base level."

> "For any K≥2 and ε₁>ε₀: P_clean(E_K) > P_CCRM(E_K)."

## 12. 我的判断

- 相关度：5 / 5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
