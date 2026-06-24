# Adversarial Review: Transaction-Safe Agent State Boundaries

> **目的**：站在顶会审稿人角度攻击课题，判断会不会被拒。
> **与 gap_analysis 的区别**：gap 找空白；adversarial 攻击空白是否站得住。
> **审计日期**：2026-06-24

---

## 1. 八问自检

| # | 攻击问题 | 回应强度 | 回应要点 |
|---|----------|----------|----------|
| 1 | 这个问题是否已经被已有论文覆盖？ | 弱 | ACRFence 是最大威胁，尚未完成正面比较。 |
| 2 | 这个课题是否只是已有工作的换名？ | 弱 | “semantic rollback attack” 不能直接复用，必须收窄或扩展到 memory/tool provenance。 |
| 3 | 这个方法是否只是 prompt/retry/checkpoint 工程组合？ | 中弱 | 需要证明 state boundary 表示和 replay/fork/quarantine 不是普通工程拼接。 |
| 4 | benchmark 是否太小、太人工、太依赖构造？ | 中弱 | MVP 可用 mock tools，但 Phase 3 需设计贴近真实 email/payment/file/GitHub 语义。 |
| 5 | 指标是否只是已有指标改名？ | 中 | duplicate side-effect rate、credential resurrection rate、memory contamination reuse rate 需要清晰定义。 |
| 6 | baseline 是否足够强？ | 中弱 | 至少需要 ordinary retry、idempotency key、ACRFence-like replay、prompt guard / tool guard。 |
| 7 | 是否能跨模型、跨任务、跨环境验证？ | 中 | 可先跨工具类型验证，模型跨 GPT/Claude/open model 留到后续。 |
| 8 | 投 ICLR/NeurIPS/ACL/EMNLP 最可能被拒的理由？ | 强攻击 | “ACRFence already did this; your benchmark is toy; this is engineering.” |

---

## 2. 必填输出

| 字段 | 内容 |
|------|------|
| **strongest rejection reason** | ACRFence 已经覆盖 checkpoint-restore 下的 semantic rollback attack，本案可能只是换名或小扩展。 |
| **most dangerous related work** | ACRFence |
| **novelty risk** | 中高 |
| **evaluation risk** | mock tool benchmark 可能被认为太人工，必须覆盖真实语义约束。 |
| **engineering-only risk** | 中高 |
| **minimum evidence needed to continue** | 证明 ACRFence 未覆盖 memory provenance / credential scope / branch contamination 中至少一个核心维度，并构造可复现实验显示普通 retry 和 ACRFence-like baseline 仍失败。 |

---

## 3. 攻击表（按强度）

| 攻击 | 强度 | 预备回应 |
|------|------|----------|
| ACRFence 已经提出 replay-or-fork 语义 | 高 | Phase 3 必须逐节比较，只有找到 memory/tool provenance 或 branch contamination 空白才继续。 |
| benchmark 只是 toy tool | 高 | 任务需绑定真实工具语义：email send、payment transfer、file delete、GitHub issue/PR action。 |
| 方法只是 idempotency key + logging | 中高 | 需要定义 LLM-specific semantic equivalence、branch id、memory quarantine，不只是记录请求 ID。 |
| 安全 benchmark 已有 AgentDojo / ASB | 中 | 本案不做泛化安全攻击，而做 recovery 后 state consistency。 |

---

## 4. 攻击结论

当前攻击 **部分成立**。C3 值得进入 Phase 3，但必须先深研 ACRFence；若 ACRFence 已覆盖 memory/tool provenance 或 branch-aware recovery，本方向应 Narrow 或 No-Go。当前不能标 Go，也不能标 Promising。

---

## 5. 与 decision 的联动

| 若… | 建议 decision |
|-----|----------------|
| ACRFence 完整覆盖核心 claim | No-Go |
| ACRFence 覆盖 rollback 但不覆盖 memory provenance / branch contamination | Narrow |
| 需要补充 memory / security 文献才能判断 | Hold |
| 攻击可回应且有 pilot 路径 | Promising（Phase 3 后）；Go 只能等 Phase 4 |
