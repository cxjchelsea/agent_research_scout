# Paper Card: State Contamination in Memory-Augmented LLM Agents

## 1. 基本信息

- Title: State Contamination in Memory-Augmented LLM Agents
- Year: 2026
- Venue: arXiv (2605.16746)
- Authors: Yian Wang, Agam Goyal, Yuen Chen, Hari Sundaram (UIUC)
- Link: https://arxiv.org/abs/2605.16746
- Code: 论文内实验（待查是否开源）
- Benchmark / Dataset: Multi-session memory-augmented agent 仿真环境

## 2. 它研究什么问题？

Memory-augmented agent 在跨 session 交互中，**污染内容在 memory 压缩/写回前未被拦截**，会以 laundered summary 形式进入 persistent memory，并在后续 session 持续 conditioning 行为——即 **state contamination / memory laundering**。

## 3. 它的核心贡献是什么？

- 正式定义 **state contamination** 与 **memory laundering** 机制。
- 识别三条 persistence channel（transcript → summary → retrieval）。
- 提出 read-side sanitization + write-gate + parameter debiasing 三通道 mitigation。
- 证明 **post-hoc summary 清洗太晚**（SPG 残留）。

## 4. 它的方法是什么？

- 在 memory 写回前做 transcript write-gating（redact/rewrite）。
- 读侧 sanitization + 参数级 debiasing 组合。
- 用 SPG、Δμ、P95_tox、downstream toxicity 度量污染残留。

## 5. 它怎么实验？

### Task

Multi-session agent 在 seed-level toxicity 注入后，后续 session 行为是否被污染。

### Dataset / Environment

Controlled multi-session memory agent 仿真。

### Baselines

Output filtering、DPO、post-hoc summary rewriting/gating。

### Metrics

SPG（Summary Persistence Gap）；Δμ；P95_tox；downstream toxicity。

## 6. 它发现了什么失败模式？

- **Memory laundering**：toxic framing 被压缩进 summary 后低于 classifier 阈值，但仍 behaviorally influential。
- Post-hoc sanitization 降 visible toxicity 但 **SPG 仍 0.086–0.103**。
- Write-gating before summarization 可将 SPG 降至 ~0.0004。

## 7. 它没有覆盖什么？

- 聚焦 **memory safety / toxicity**，非 general task-error state。
- 未覆盖 SWE/bash/file、web DOM、DB 等 **executable tool state**。
- 未研究 checkpoint-restore 与 irreversible side-effect。
- 未提供 tool-use agent 公开 benchmark。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| 长链路 Agent | ✓ multi-session |
| memory | ✓ 核心 |
| 状态管理 | ✓ write-gate / persistence channel |
| 直接术语 | **state contamination** |
| tool-use | ✗ 未覆盖 |
| rollback | ✗ 未覆盖 |

## 9. 它是否削弱我的创新性？

**部分覆盖，且直接占用核心术语。**

- 已用 "state contamination" 命名并度量 memory 通道污染。
- 我的课题若仅讨论 memory laundering → **高度重叠**。
- 若扩展到 **tool executable state + context retry + rollback blind spot** → 仍有空间，但需在 related work 中明确区分 memory-safety vs task-state contamination。

## 10. 我可以从它的 limitation 里切什么？

1. 定义 **Task-State Contamination**：错误 tool 结果/错误文件修改写入 agent state（非 toxicity）。
2. 将 write-gate 思想迁移到 **trajectory checkpoint** 与 **world state snapshot**。
3. 统一 memory laundering 与 CCRM context contamination 为 **multi-channel state contamination taxonomy**。

## 11. 重要引用句

> "The key design constraint is placement: controls must act before contaminated content is compressed into persistent memory."

> "For memory-augmented agents, robust safety therefore requires sanitizing the state before summarizing it."

## 12. 我的判断

- 相关度：5 / 5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
