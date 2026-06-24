# Paper Card: AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

## 1. 基本信息

- Title: AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents
- Year: 2024
- Venue: NeurIPS
- Authors: Edoardo Debenedetti; others
- Link: https://arxiv.org/abs/2406.13352
- Code: 未核验
- Benchmark / Dataset: AgentDojo

## 2. 它研究什么问题？

工具增强 agent 会从外部工具读取不可信数据，这些 observation 可以包含间接 prompt injection，劫持 agent 后续行为。

## 3. 它的核心贡献是什么？

构造动态 agent security 环境，包含现实任务、安全测试用例、攻击与防御评估，并同时衡量 utility 和 attack success。

## 4. 它的方法是什么？

让 agent 在多工具环境中完成正常任务，同时在工具返回数据中注入攻击内容，检查 agent 是否保持任务能力并抵御攻击。

## 5. 它怎么实验？

### Task

银行、Slack、旅行、workspace 等工具任务。

### Dataset / Environment

97 realistic tasks 和 629 security test cases。

### Baselines

多种 prompt injection attacks 与 defenses。

### Metrics

benign utility、utility under attack、attack success rate。

## 6. 它发现了什么失败模式？

Agent 在读取工具结果时会把外部不可信内容混入决策上下文，导致目标偏移或恶意行为。

## 7. 它没有覆盖什么？

它主要覆盖攻击时的工具 observation，不直接研究 checkpoint/rollback 后的状态恢复，也不强调 persistent memory 写入后的恢复清理。

## 8. 它和我的课题有什么关系？

它证明 tool boundary 是安全边界。本课题可以把“工具返回污染”扩展到“恢复后状态边界是否干净”。

## 9. 它是否削弱我的创新性？

部分覆盖。它会削弱通用 tool-security claim，但不直接否定 transaction-safe recovery。

## 10. 我可以从它的 limitation 里切什么？

攻击后的状态清理、污染 observation 是否写入 memory、恢复后是否继续使用被污染状态。

## 11. 重要引用句

待后续精读原文摘录。

## 12. 我的判断

- 相关度：4
- 是否必须精读：是
- 是否作为 related work 核心论文：是
