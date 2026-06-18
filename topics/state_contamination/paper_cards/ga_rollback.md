# Paper Card: GA-Rollback (Generator-Assistant Stepwise Rollback Framework)

## 1. 基本信息

- Title: Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent
- Year: 2025
- Venue: EMNLP 2025
- Authors: Xingzuo Li, Kehai Chen, Yunfei Long, Xuefeng Bai, Yong Xu, Min Zhang
- Link: https://aclanthology.org/2025.emnlp-main.892/
- Code: https://github.com/12933/GA-Rollback
- Benchmark / Dataset: AlfWorld, WebShop, HotpotQA

## 2. 它研究什么问题？

ReAct 式 agent 的 **one-pass issue**：每个 intermediate thought/action 无论对错都 append 到 trajectory，导致 **irreversible error propagation**。需要 step-level 检测错误并 rollback。

## 3. 它的核心贡献是什么？

提出 **GA-Rollback**：Generator 与环境交互，Assistant 审查每步 action，检测错误时触发 **stepwise rollback**；并有两项 rollback 专用增强策略。

## 4. 它的方法是什么？

- 双角色：Generator（actor）+ Assistant（critic/rollback trigger）。
- 错误 action  detected → 回滚到 prior correct state，重新生成。
- 可 plug-and-play 接入其他 agent 方法。

## 5. 它怎么实验？

### Task

多步 reasoning + acting（QA、embodied、web shopping）。

### Dataset / Environment

HotpotQA, AlfWorld, WebShop。

### Baselines

ReAct 及 EMNLP 同期 strong baselines。

### Metrics

Task success rate。

## 6. 它发现了什么失败模式？

- **One-pass trajectory pollution**：错误 intermediate state 永久进入 history。
- Stepwise rollback 可显著降低 error propagation（相对 baseline 明显提升）。

## 7. 它没有覆盖什么？

- Rollback 仅限 **trajectory/context**，不 undo **external tool side-effects**。
- Assistant 判错可能误 rollback；无 provenance 或 typed state。
- 未形式化 contamination 度量；未评 clean-restart vs dirty-retry。
- 环境相对短链路（非 SWE 级长 horizon）。

## 8. 它和我的课题有什么关系？

| 维度 | 关系 |
|------|------|
| 长链路 Agent | 部分（AlfWorld/WebShop） |
| rollback | ✓ 核心方法 |
| error propagation | ✓ one-pass issue |
| recovery | ✓ stepwise |
| tool irreversible effect | ✗ 未处理 |
| benchmark | ✗ 用现有 env |

## 9. 它是否削弱我的创新性？

**部分覆盖。**

- 已有 stepwise rollback **方法**；若我只做 rollback prompt → 创新不足。
- 空白在于：**rollback + world state consistency**（结合 ACRFence 问题）与 **contamination-aware evaluation**。

## 10. 我可以从它的 limitation 里切什么？

1. **Semantic rollback**：结合 ACRFence 的 replay-or-fork，处理 irreversible tools。
2. **Rollback trigger from provenance**：不只 assistant 判错，还用 constraint violation（AgentRx 思路）。
3. 在 SWE-bench Verified 上对比 GA-Rollback vs clean-restart@k。

## 11. 重要引用句

> "This paradigm faces a deep rooted one-pass issue whereby each generated intermediate thought is plugged into the trajectory regardless of its correctness, which can cause irreversible error propagation."

## 12. 我的判断

- 相关度：5 / 5
- 是否必须精读：是
- 是否作为 related work 核心论文：是
