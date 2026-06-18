# Paper Card: SWE-bench

## 1. 基本信息

- Title: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- Year: 2024
- Venue: ICLR 2024
- Authors: Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik R. Narasimhan
- Link: https://arxiv.org/abs/2310.06770
- Code: https://github.com/SWE-bench/SWE-bench
- Benchmark / Dataset: SWE-bench（2294 issues）；SWE-bench Verified（500 人工校验）

## 2. 它研究什么问题？

LLM / agent 能否像工程师一样读真实 GitHub issue、修改 codebase、产出通过 hidden tests 的 patch——即 **real-world software engineering** 能力评估。

## 3. 它的核心贡献是什么？

- 从 12 个 Python repo 收集 2294 真实 issue-PR 对。
- 可执行 verifier：apply patch + run tests。
- SWE-bench Verified：500 人工过滤的高质量子集。
- 成为 coding agent 事实标准 benchmark。

## 4. 它的方法是什么？

- 给定 issue description + codebase snapshot。
- Agent 生成 unified diff patch。
- 自动运行 repo test suite 判定 resolved。

## 5. 它怎么实验？

### Task

Issue resolution（generate patch）。

### Dataset / Environment

Real GitHub repos in Docker sandbox。

### Baselines

Non-interactive LLM；SWE-agent；OpenHands；mini-SWE-agent 等。

### Metrics

pass@1 / resolve rate；Verified leaderboard。

## 6. 它发现了什么失败模式？

- 长链路 bash/edit/search 轨迹中 **错误假设累积**。
- Agent scaffold 对性能影响极大（非纯 LLM 能力）。
- **CCRM 论文揭示**：retry 污染在此 benchmark 上显著（ε₁/ε₀=7.1）——虽非 SWE-bench 原文贡献，但是关键衍生发现。

## 7. 它没有覆盖什么？

- 只评 **最终 patch 是否 pass tests**。
- 不追踪 intermediate workspace pollution、dirty retry、rollback 成功率。
- 无 failure step annotation（TRAIL/AgentDebug 补此空白）。
- 数据 contamination 争议（OpenAI 停止自报 Verified 分数）。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| 长链路 tool agent | ✓ 典型 |
| 状态污染场景 | ✓ bash history + file state |
| recovery 评测 | ✗ |
| 实验 substrate | ✓ CCRM 验证平台 |

## 9. 它是否削弱我的创新性？

**几乎无关（作为方法论文），但作为实验平台高度相关。**

- SWE-bench 本身不解决 contamination；是我建 **ContaminationBench extension** 的理想底座。

## 10. 我可以从它的 limitation 里切什么？

1. 在 Verified 上报告 **pass@k vs clean-restart@k vs pass^k**。
2. 记录 workspace hash + message hash 测 **dual-state drift**。
3. 标注 pollution step 子集（人工或 heuristic）。

## 11. 重要引用句

> "Can Language Models Resolve Real-World Github Issues?" — 任务定义即长链路 tool-use。

（CCRM 引用句）> "We validate CCRM on real SWE-bench Verified data ... cascade ratio ε₁/ε₀ = 7.1."

## 12. 我的判断

- 相关度：4 / 5（实验平台价值）
- 是否必须精读：是（实验设计必读）
- 是否作为 related work 核心论文：是（作 benchmark 底座）
