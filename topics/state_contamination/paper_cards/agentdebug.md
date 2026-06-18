# Paper Card: AgentDebug — Where LLM Agents Fail and How They Can Learn From Failures

## 1. 基本信息

- Title: Where LLM Agents Fail and How They Can Learn From Failures (AgentDebug)
- Year: 2025
- Venue: arXiv (2509.25370)；ICLR 2026 withdrawn
- Authors: Kunlun Zhu, Zijia Liu, Bingxuan Li, Muxin Tian, et al. (UIUC 等)
- Link: https://arxiv.org/abs/2509.25370
- Code: https://github.com/ulab-uiuc/AgentDebug
- Benchmark / Dataset: AgentErrorBench（ALFWorld, GAIA, WebShop 失败轨迹）

## 2. 它研究什么问题？

模块化 LLM agent（planning/memory/reflection/action/system）中，**单一 root-cause error 通过 cascade 传播**导致任务失败；现有系统缺乏 modular failure understanding 与 actionable recovery。

## 3. 它的核心贡献是什么？

1. **AgentErrorTaxonomy**：17 类错误，5 模块。
2. **AgentErrorBench**：首个系统化标注失败轨迹 benchmark。
3. **AgentDebug**：定位 root-cause step + 生成 corrective feedback → 迭代恢复。

## 4. 它的方法是什么？

- 分解 trajectory 为 decision steps。
- 标注每步 error type；找 **earliest critical error**。
- 向 responsible state/action 提供 targeted feedback，非 fix 所有 surface errors。

## 5. 它怎么实验？

### Task

Failure detection + step localization + recovery via feedback。

### Dataset / Environment

AgentErrorBench；下游 ALFWorld / GAIA / WebShop。

### Baselines

Strongest LLM judge baselines。

### Metrics

All-correct accuracy；step accuracy；task success improvement（+26% relative）。

## 6. 它发现了什么失败模式？

- **Memory/reflection errors** 是最常见 cascade 源（step 5–15）。
- Planning errors 导致 constraint ignorance 级联。
- Action errors 有时可恢复；system errors 常直接终止。
- 一旦 cascade 开始，**难以 reverse**（与 early detection 重要性一致）。

## 7. 它没有覆盖什么？

- Recovery 是 **feedback/reprompt**，非 explicit state rollback 或 clean-restart。
- Taxonomy **未单独定义 state contamination**。
- 未度量 retry 污染或 world state inconsistency。
- ICLR 2026  withdrawn，peer review 状态弱。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| error propagation | ✓ 核心 |
| failure diagnosis | ✓ |
| recovery | 部分（feedback-based） |
| rollback | ✗ |
| contamination | 未形式化 |
| tool-use | ✓ GAIA 等 |

## 9. 它是否削弱我的创新性？

**部分覆盖。**

- 已覆盖 error cascade + taxonomy + recovery feedback。
- 我的差异点：**state-level contamination 定义/度量 + clean-restart/rollback 协议**，而非 debug feedback alone。

## 10. 我可以从它的 limitation 里切什么？

1. 在 AgentErrorTaxonomy 上增加 **StateContamination** 子类（context/world/memory）。
2. 对比 AgentDebug feedback vs clean-restart@k vs GA-Rollback。
3. 用 AgentErrorBench 标注 **pollution step** 而非仅 failure step。

## 11. 重要引用句

> "Memory and reflection errors are the most common sources of propagation, typically arising in early or mid-trajectory steps."

> "Once cascades begin, they are difficult to reverse."

## 12. 我的判断

- 相关度：4 / 5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
