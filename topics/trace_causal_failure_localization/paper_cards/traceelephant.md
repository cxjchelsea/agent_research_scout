# Paper Card: Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems

> **card_status**：threat_verified
> **是否最大威胁 work**：是

## 1. 基本信息

- Title: Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems
- Year: 2026
- Venue: ACL
- Authors: Mengzhuo Chen et al.
- Link: https://aclanthology.org/2026.acl-long.912/
- Code: https://github.com/TraceElephant/TraceElephant
- Benchmark / Dataset: TraceElephant

## 2. 它研究什么问题？

TraceElephant 研究 multi-agent systems 中 failure attribution：识别 responsible agent/component 和 decisive failure step，并强调 full execution observability。

## 3. 它的核心贡献是什么？

1. 220 annotated failure traces。
2. 来自 Captain-Agent、Magentic-One、SWE-Agent 等系统。
3. 提供 full execution traces：inputs、outputs、inter-agent messages、tool invocations、raw logs、metadata。
4. 提供 reproducible execution environments。
5. 支持 dynamic failure attribution，例如 replay、controlled intervention、counterfactual execution。

## 4. 它的方法是什么？

收集完整执行轨迹与可复现环境，比较 partial observation 与 full trace observability 对 failure attribution 的影响。

## 5. 它怎么实验？

### Task

Responsible component and decisive step attribution。

### Dataset / Environment

220 failure traces from 3 agentic systems。

### Metrics

Attribution accuracy；full traces 对 partial-observation 的提升。

## 6. 它发现了什么失败模式？

缺少 inputs 和上下文会遮蔽失败原因；full execution observability 可显著提升 attribution。

## 7. 它没有覆盖什么？

它已覆盖 full execution trace attribution 和 counterfactual analysis 基础，但未必完整覆盖：

- 从 attribution 到具体修复 artifact；
- 自动生成 regression test；
- 单 agent / tool API workflow 的 constraint-based repair。

## 8. 它和我的课题有什么关系？

它覆盖“full trace + decisive step + responsible component”，对 C1 原始 claim 是强威胁。

## 9. 它是否削弱我的创新性？

强烈削弱，尤其是 multi-agent 方向和“完整 trace observability”方向。

## 10. 我可以从它的 limitation 里切什么？

- repair-target / regression-test generation；
- 从 attribution 到可执行 patch / prompt / tool schema changes；
- 对单 agent structured API workflows 的轻量化验证。

## 11. 重要引用句

- “failure attribution ... identifying the responsible agent and decisive step”
- “full execution traces and reproducible environments”
- “TraceElephant ... consists of 220 failure traces”
- “full traces improve attribution accuracy by up to 76.5%”

## 12. 我的判断

- 相关度：5
- 是否必须精读：是
- 是否作为 related work 核心论文：是

---

## 13. Targeted Verification

| Claim component | Covered by this paper? | Evidence | Implication |
|---|---|---|---|
| 核心问题定义 | yes | 负责 agent/component 与 decisive step attribution。 | C1 attribution claim 已覆盖。 |
| proposed mechanism | partial | 提供 benchmark/evaluation and full observability，不是 repair method。 | 方法 claim 仍可转向 repair/test。 |
| benchmark / evaluation setting | yes | 220 traces + reproducible environments。 | 新 benchmark 空间很小。 |
| baseline / comparison | yes | 比较 full vs partial observation，报告 76.5% 提升。 | 强 baseline。 |
| utility / risk trade-off | partial | 支持 counterfactual probing，但不主打修复收益。 | 可切 repair utility。 |

### Threat Verification Conclusion

- **是否覆盖本课题核心 claim**：yes
- **是否覆盖 proposed mechanism**：partial
- **是否覆盖 benchmark / evaluation setting**：yes
- **如果扩展该方法，是否自然得到本案方法**：partial
- **结论**：threat_verified；C1 必须从 attribution benchmark 收窄。
