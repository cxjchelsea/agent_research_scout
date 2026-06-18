# Paper Card: ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore

## 1. 基本信息

- Title: ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore
- Year: 2026
- Venue: arXiv (2603.20625)
- Authors: Yusheng Zheng, Yiwei Yang, Wei Zhang, Andi Quinn
- Link: https://arxiv.org/abs/2603.20625
- Code: 论文 PoC（LangGraph/MCP 相关讨论）
- Benchmark / Dataset: Simulated Bank/Cloud/Approval services + agent CR testbed

## 2. 它研究什么问题？

Agent 框架 increasingly 提供 **checkpoint-restore** 做 error recovery，但 LLM restore 后会 **re-synthesize 语义不同但表面相似的 tool request**，服务器视为新请求 → duplicate payment、credential reuse 等 **semantic rollback attacks**。

## 3. 它的核心贡献是什么？

- 定义两类攻击：**Action Replay**、**Authority Resurrection**。
- 指出 root cause：CR 只 rollback **local process state**，无法 undo **external irreversible effects**。
- 提出 **ACRFence**：tool boundary proxy，记录 irreversible effects，enforce **replay-or-fork** semantics。

## 4. 它的方法是什么？

- 记录 irreversible tool effects。
- Restore 后用 Analyzer LLM 比较新 request 与 prior effect log。
- 三种动作：Replay（返回记录响应）/ Fork（显式分支）/ Credential reuse reject。

## 5. 它怎么实验？

### Task

Checkpoint-restore 后 agent 是否触发 duplicate irreversible side-effect。

### Dataset / Environment

Claude Code CLI + Qwen3-32B + simulated external services PoC。

### Baselines

Naive checkpoint-restore（无 fencing）。

### Metrics

Attack success rate；mitigation containment rate。

## 6. 它发现了什么失败模式？

- **Recovery blind spot**：rollback 本地 state ≠ undo world state。
- 即使 temperature=0，GPU 非确定性也可导致 restore 后不同 token → 不同 API call。
- Framework 社区已独立报告类似问题（LangGraph rewind、Vault token reuse 等）。

## 7. 它没有覆盖什么？

- 聚焦 **security / irreversible API**，非一般 reasoning error recovery。
- 不处理 context contamination 或 memory laundering。
- 不评 task success 提升，只评 attack mitigation。
- PoC 规模小，非大规模 agent benchmark。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| checkpoint | ✓ |
| rollback | ✓ semantic rollback |
| recovery blind spot | ✓ **核心** |
| tool-use | ✓ irreversible tools |
| error propagation | 间接 |
| contamination 术语 | ✗ 用 semantic rollback attack |

## 9. 它是否削弱我的创新性？

**部分覆盖，威胁「recovery 机制」叙事。**

- 已清晰论证 **recovery blind spot** 的一类实例（external state）。
- 我的课题可将其纳入 broader **dual-state contamination** 框架，而非重复 security PoC。
- 若我只讲 checkpoint 好 → 会被 ACRFence 反驳。

## 10. 我可以从它的 limitation 里切什么？

1. 从 security 扩展到 **task failure recovery**：错误 patch 已写入 repo，context rollback 不够。
2. 提出 **Unified Recovery Contract**：context clean + world snapshot + replay-or-fork。
3. 在 SWE-bench 上度量 restore 后 workspace drift。

## 11. 重要引用句

> "Checkpoint-restore saves and restores local process state but cannot undo actions already performed on external services."

> "LLM agents violate this assumption. Even under temperature=0 ... a restored agent generates requests that servers accept as new."

## 12. 我的判断

- 相关度：5 / 5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
