# Paper Card: Hell or High Water — Evaluating Agentic Recovery from External Failures

## 1. 基本信息

- Title: Hell or High Water: Evaluating Agentic Recovery from External Failures
- Year: 2025
- Venue: COLM 2025
- Authors: Andrew Wang, Sophia Hager, Adi Asija, Daniel Khashabi, Nicholas Andrews (JHU CLSP)
- Link: https://arxiv.org/abs/2508.11027
- Code: https://github.com/JHU-CLSP/hell-or-high-water
- Benchmark / Dataset: Hell-or-High-Water（830 questions，4450 functions）

## 2. 它研究什么问题？

当 agent 计划中的 function/tool **因外部原因不可用**（非 agent 自身 reasoning error）时，agent 能否发现 backup plan 并完成任务？即 **fault-tolerant planning / external failure recovery**。

## 3. 它的核心贡献是什么？

- 首个专门测 **external failure recovery** 的 agent planning benchmark。
- 保证每题至少两条 distinct solution path，注入 failure 后仍 solvable。
- 系统分析 search failure / ID failure / ordering failure / tool failure taxonomy。

## 4. 它的方法是什么？

- 从 text-to-SQL 数据集自动构造 QA + tool library（4000+ functions）。
- Agent 需 search + retrieve + compose function calls。
- Adversary 注入 function unavailability；对比 restricted vs full search space。

## 5. 它怎么实验？

### Task

Multi-step function-call planning under injected failures。

### Dataset / Environment

830 questions；4450 functions；CodeAct agent framework。

### Baselines

多种 open/commercial LLMs（GPT-4o, Claude, Qwen, Llama 等）。

### Metrics

Task success rate with/without failure injection；recovery rate drop。

## 6. 它发现了什么失败模式？

- Agent **不能可靠 incorporate environment feedback** 找 backup。
- 即使 restricted search space，SOTA 在 failure 下仍 ~45% success（大幅下降）。
- 常见错误：search failure（找不到 tool）、ID failure、ordering failure、tool execution failure。
- **Recovery blind spot**：能识别正确 function，但不会 alternate course。

## 7. 它没有覆盖什么？

- 测 **external** failure，非 **self-caused state contamination**（错误写入 context/memory）。
- 无 checkpoint/rollback；无 world state snapshot。
- 非真实 SWE/web env（synthetic SQL-derived tools）。
- 不形式化 retry contamination（CCRM 问题）。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| recovery | ✓ |
| tool-use | ✓ function calling |
| recovery blind spot | ✓ 互补视角 |
| state contamination | ✗ 非 self-caused |
| rollback | ✗ |

## 9. 它是否削弱我的创新性？

**相关但不直接威胁。**

- 占住 "agent recovery benchmark" 部分空间，但是 **external failure** 角度。
- 我的 **self-caused contamination + dual-state rollback** 可并存。

## 10. 我可以从它的 limitation 里切什么？

1. 扩展 benchmark：同时注入 **external failure + prior attempt contamination**。
2. 报告 recovery rate conditional on clean-restart vs dirty-retry。
3. 借用 failure taxonomy，增加 **state pollution failure** 类。

## 11. 重要引用句

> "Language agents struggle to formulate and execute backup plans in response to environment feedback."

> "Ideally, an agent's performance on the planning task should not be affected by the presence of external failures."

## 12. 我的判断

- 相关度：4 / 5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
