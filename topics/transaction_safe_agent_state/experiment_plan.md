# Experiment Plan: Recovery-Safe Memory Provenance for Tool-Using Agents

> **前置条件**：`gap_analysis.md` + `adversarial_review.md` + `file_consistency_check.md` 完成后方可填写。
> **决策联动**：见 `decision.md`

---

## 1. 任务定义

**目标**：验证 rollback / fork / retry 后，缺少 provenance 的长期 memory 是否会复用失败分支或攻击性 observation；以及 provenance-filtered retrieval / quarantine 是否能降低该失败，同时保持良性 memory utility。

**操作定义**：

| 概念 | 定义 |
|------|------|
| contaminated memory reuse | agent 在后续任务中检索并依据应被 rollback/fork 隔离的 memory item 行动 |
| invalid-branch retrieval | 当前 branch 检索到另一个 branch 或失败 checkpoint 写入的 memory |
| provenance-filtered retrieval | retrieval 时依据 branch_id、checkpoint_id、validity_state、trust_state 过滤 memory |
| memory quarantine | rollback/fork 后将可疑 memory item 标记为 quarantined，需重新验证后才可检索 |

---

## 2. 数据与环境

| 项 | 规格 |
|----|------|
| Tool scenarios | 20–30 个 mock scenarios：email、payment、file、GitHub issue/PR、calendar |
| Memory events | 每个 scenario 包含 observation → memory write → rollback/fork/retry → later retrieval |
| Attack / error types | malicious observation、incorrect tool output、failed branch hypothesis、stale credential note |
| Models | 先用 1 个主力闭源模型 + 1 个便宜模型；后续扩到 3 个 |
| Evaluation | deterministic scripts 检查 final action 和 memory access log |

---

## 3. 实验条件（baselines）

| 条件 | 说明 |
|------|------|
| B0 No memory | 不使用长期 memory，测任务下限和 false positive |
| B1 Naive persistent memory | 所有写入跨 rollback/fork 保留，可直接检索 |
| B2 Prompt guard | 提示 agent 不要信任可疑 memory，但不改 retrieval |
| B3 ACRFence-like tool-effect log | 记录外部工具副作用，但不处理 memory provenance |
| Ours Provenance-filtered memory | memory item 带 branch/checkpoint/source/validity，检索时过滤或 quarantine |

---

## 4. 指标（≥3）

| 指标 | 定义 | 假设 |
|------|------|------|
| contaminated memory reuse rate | 后续任务中使用了应隔离 memory 的比例 | Ours 显著低于 B1/B2/B3 |
| invalid-branch retrieval rate | 检索到错误 branch/checkpoint memory 的比例 | Ours 显著降低 |
| benign memory utility | 非攻击/非错误场景下正确利用 memory 的比例 | Ours 相比 B1 下降不超过 10% |
| recovery success rate | rollback/fork 后完成原任务的比例 | Ours 不低于 B2/B3 |
| overhead | token / latency / memory metadata 增量 | Ours 可接受 |

---

## 5. 实验流程

### Pilot

- 实现 5 个 tool scenarios，每个包含 2 个污染 memory case 和 1 个 benign memory case。
- 跑 B1、B3、Ours 三个条件。
- 手工检查 memory access log 和 final action。

### Full（pilot 通过后）

- 扩展到 20–30 scenarios。
- 加入 B0、B2。
- 跨 2–3 个模型重复运行，每个 scenario 至少 3 次。
- 输出 per-scenario error analysis。

---

## 6. 消融与泛化

| 实验 | 目的 |
|------|------|
| 去掉 branch_id | 判断 branch provenance 是否必要 |
| 去掉 checkpoint_id | 判断 rollback provenance 是否必要 |
| 只 quarantine 不重新验证 | 判断是否过度保守 |
| 只过滤 malicious observation | 判断能否覆盖非恶意错误工具结果 |

---

## 7. 错误分析

- agent 明知 memory 可疑但仍使用；
- retrieval 层过滤正确但 agent 从上下文残留中复用；
- benign memory 被错误 quarantine；
- ACRFence-like baseline 阻止了 tool side effect 但没有阻止 memory reuse。

---

## 8. 资源与风险

| 风险 | 缓解 |
|------|------|
| benchmark 太人工 | 使用真实语义工具：email/payment/file/GitHub/calendar |
| 与 AgentPoison 撞车 | 明确变量是 recovery/fork，不是 poisoning attack generation |
| 与 ACRFence 撞车 | 明确 baseline 是 tool-effect log，不处理 memory provenance |
| utility 下降太大 | 报告 benign memory utility 和 quarantine false positive |

---

## 9. 成功标准（pilot → Go）

| criterion | 阈值 |
|-----------|--------|
| contaminated memory reuse rate | Ours 比 B1/B3 降低 ≥50% |
| invalid-branch retrieval rate | Ours 低于 10% |
| benign memory utility | 相比 B1 下降 ≤10% |
| recovery success rate | 不低于 B3 |
| qualitative evidence | 至少 3 类失败模式被清晰复现并被 provenance 机制阻断 |
