# Paper Card: AgentRx: Diagnosing AI Agent Failures from Execution Trajectories

> **card_status**：threat_verified
> **是否最大威胁 work**：是

## 1. 基本信息

- Title: AgentRx: Diagnosing AI Agent Failures from Execution Trajectories
- Year: 2026
- Venue: arXiv / Microsoft Research
- Authors: Shraddha Barke, Arnav Goyal, Alind Khare, Avaljot Singh, Suman Nath, Chetan Bansal
- Link: https://arxiv.org/abs/2602.02475v1
- Code: https://github.com/microsoft/AgentRx
- Benchmark / Dataset: AgentRx Benchmark

## 2. 它研究什么问题？

AgentRx 研究如何从失败的 agent execution trajectories 中自动定位 first unrecoverable critical failure step，并给出 root-cause category。

## 3. 它的核心贡献是什么？

1. 115 条 manually annotated failed trajectories。
2. 涵盖 structured API workflows、incident management、open-ended web/file tasks。
3. 用 tool schemas 和 domain policies 合成 executable constraints。
4. 逐步检查 constraint violations，并生成 auditable validation log。
5. LLM judge 使用 validation log 定位 critical step 和 failure category。

## 4. 它的方法是什么？

Normalize raw logs 为 trajectory IR，然后生成 static / dynamic invariants，逐步检查约束，最后用 LLM judge 根据 evidence-backed violations 做定位和分类。

## 5. 它怎么实验？

### Task

Critical failure step localization and root-cause attribution。

### Dataset / Environment

Tau-bench、Flash、Magentic-One。

### Baselines

现有 trajectory diagnosis baselines。

### Metrics

Step localization accuracy；root-cause attribution accuracy。

## 6. 它发现了什么失败模式？

Agent 失败与 instruction adherence、invalid invocation、tool output misinterpretation、intent-plan misalignment、guardrails、system failure 等类别相关。

## 7. 它没有覆盖什么？

从摘要看，它非常接近本案，但仍可能未完整覆盖：

- 从 critical step 到具体 code/prompt/tool schema repair patch；
- 自动生成可运行 regression test；
- benchmark 中 counterfactual intervention 的标准协议。

## 8. 它和我的课题有什么关系？

它比发现阶段预期的 TRAIL 更危险，直接覆盖“critical failure step”和“root-cause attribution”。

## 9. 它是否削弱我的创新性？

强烈削弱。原始 C1 如果主张“定位 causal failure step / component”，AgentRx 基本已覆盖。

## 10. 我可以从它的 limitation 里切什么？

只能考虑更下游的 repair-target grounding、regression-test generation、或 counterfactual intervention evaluation。

## 11. 重要引用句

- “pinpoints the critical failure step in a failed agent trajectory”
- “synthesizes constraints, evaluates them step-by-step, and produces an auditable validation log”
- “115 failed trajectories spanning structured API workflows, incident management, and open-ended web/file tasks”

## 12. 我的判断

- 相关度：5
- 是否必须精读：是
- 是否作为 related work 核心论文：是

---

## 13. Targeted Verification

| Claim component | Covered by this paper? | Evidence | Implication |
|---|---|---|---|
| 核心问题定义 | yes | 明确定位 failed agent trajectory 的 critical failure step。 | 原始 C1 核心被覆盖。 |
| proposed mechanism | yes | trajectory IR + constraints + validation log + LLM judge。 | 方法空间被强占。 |
| benchmark / evaluation setting | yes | 115 failed trajectories across three domains。 | 本案若做数据集必须显著不同。 |
| baseline / comparison | yes | 报告 step localization 和 attribution 改进。 | 可作为强 baseline。 |
| utility / risk trade-off | partial | 有 auditable logs，但不以 repair/test generation 为主。 | 下游修复仍可能有空白。 |

### Threat Verification Conclusion

- **是否覆盖本课题核心 claim**：yes
- **是否覆盖 proposed mechanism**：yes
- **是否覆盖 benchmark / evaluation setting**：yes
- **如果扩展该方法，是否自然得到本案方法**：partial
- **结论**：threat_verified；原始 C1 应 No-Go，除非收窄到 AgentRx 未覆盖的 repair/test generation。
