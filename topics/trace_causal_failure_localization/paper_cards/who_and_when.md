# Paper Card: Which Agent Causes Task Failures and When?

> **card_status**：threat_verified
> **是否最大威胁 work**：是

## 1. 基本信息

- Title: Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems
- Year: 2025
- Venue: ICML
- Authors: Shaokun Zhang et al.
- Link: https://proceedings.mlr.press/v267/zhang25cq.html
- Code / Dataset: https://github.com/ag2ai/Agents_Failure_Attribution
- Benchmark / Dataset: Who&When

## 2. 它研究什么问题？

它正式提出 multi-agent systems 的 automated failure attribution：找出失败由哪个 agent 导致，以及 decisive error step 在哪里。

## 3. 它的核心贡献是什么？

1. 定义 automated failure attribution task。
2. 构造 Who&When dataset。
3. 失败日志来自 127 个 LLM multi-agent systems。
4. 标注 failure-responsible agent 和 decisive error step。
5. 评估 All-at-Once、Step-by-Step、Binary Search 等 attribution 方法。

## 4. 它的方法是什么？

让 LLM 或搜索式策略阅读失败日志，预测 responsible agent 和 decisive error step。

## 5. 它怎么实验？

### Task

Who failed and when。

### Dataset / Environment

Who&When；GAIA / AssistantBench 相关多 agent systems。

### Baselines

All-at-Once、Step-by-Step、Binary Search。

### Metrics

Responsible agent accuracy；decisive step accuracy。

## 6. 它发现了什么失败模式？

即使强 reasoning models，step-level attribution 仍很弱；最佳方法 agent accuracy 53.5%，step accuracy 14.2%。

## 7. 它没有覆盖什么？

主要聚焦 multi-agent systems，不覆盖单 agent tool workflows；也没有强调 repair-target 或 regression test generation。

## 8. 它和我的课题有什么关系？

它覆盖“responsible component / decisive step attribution”的 multi-agent 版本。

## 9. 它是否削弱我的创新性？

强覆盖 multi-agent attribution；若 C1 保留 multi-agent claim，必须明确与它不同。

## 10. 我可以从它的 limitation 里切什么？

转向单 agent + tool / API workflows，或从 attribution 转向 repair artifact generation。

## 11. 重要引用句

- “identifying the agent and step responsible for task failures”
- “failure logs from 127 LLM multi-agent systems”
- “53.5% accuracy in identifying failure-responsible agents but only 14.2% in pinpointing failure steps”

## 12. 我的判断

- 相关度：5
- 是否必须精读：是
- 是否作为 related work 核心论文：是

---

## 13. Targeted Verification

| Claim component | Covered by this paper? | Evidence | Implication |
|---|---|---|---|
| 核心问题定义 | yes | 明确提出 responsible agent + decisive step。 | C1 multi-agent attribution 被覆盖。 |
| proposed mechanism | partial | 提出初始 automated attribution methods。 | 仍可改进方法，但 novelty 风险高。 |
| benchmark / evaluation setting | yes | Who&When dataset from 127 MAS。 | 新 MAS attribution benchmark 空间小。 |
| baseline / comparison | yes | 三种 attribution baselines。 | 强 baseline。 |
| utility / risk trade-off | no | 不主打 repair/test generation。 | 下游修复是潜在空白。 |

### Threat Verification Conclusion

- **是否覆盖本课题核心 claim**：yes（multi-agent 版本）
- **是否覆盖 proposed mechanism**：partial
- **是否覆盖 benchmark / evaluation setting**：yes
- **如果扩展该方法，是否自然得到本案方法**：partial
- **结论**：threat_verified；C1 不能以 MAS attribution 作为核心创新。
