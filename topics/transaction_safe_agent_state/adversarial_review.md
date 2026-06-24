# Adversarial Review: Recovery-Safe Memory Provenance for Tool-Using Agents

> **目的**：站在顶会审稿人角度攻击课题，判断会不会被拒。
> **与 gap_analysis 的区别**：gap 找空白；adversarial 攻击空白是否站得住。
> **审计日期**：2026-06-24

---

## 1. 八问自检

| # | 攻击问题 | 回应强度 | 回应要点 |
|---|----------|----------|----------|
| 1 | 这个问题是否已经被已有论文覆盖？ | 中 | ACRFence 覆盖 external side-effect rollback；AgentPoison/ASB 覆盖 memory poisoning。本案必须证明 recovery-induced memory contamination 是交界空白。 |
| 2 | 这个课题是否只是已有工作的换名？ | 中 | 原题过宽，已收窄到 memory provenance；仍需避免把 memory poisoning 换名成 provenance。 |
| 3 | 这个方法是否只是 prompt/retry/checkpoint 工程组合？ | 中 | 预备回应是 provenance schema + branch-aware retrieval/quarantine，而非 prompt guard。 |
| 4 | benchmark 是否太小、太人工、太依赖构造？ | 中 | MVP 可用 mock tools，但任务必须绑定 email/payment/file/GitHub-like memory write 和 recovery semantics。 |
| 5 | 指标是否只是已有指标改名？ | 中 | 需要定义 contaminated memory reuse rate、invalid-branch retrieval rate、benign memory utility。 |
| 6 | baseline 是否足够强？ | 中 | 需包含 ordinary persistent memory、prompt guard、ACRFence-like tool-effect logging、Mem0-like update/retrieval。 |
| 7 | 是否能跨模型、跨任务、跨环境验证？ | 中 | 先跨工具类型和 memory policies；模型泛化可用 2–3 个 LLM。 |
| 8 | 投 ICLR/NeurIPS/ACL/EMNLP 最可能被拒的理由？ | 强攻击 | “ACRFence handles recovery; AgentPoison handles memory poisoning; this is just metadata engineering.” |

---

## 2. 必填输出

| 字段 | 内容 |
|------|------|
| **strongest rejection reason** | ACRFence + AgentPoison/ASB 的组合可能被认为已覆盖 recovery 和 memory poisoning，本案只是把二者拼起来。 |
| **most dangerous related work** | ACRFence；AgentPoison；ASB |
| **novelty risk** | 中 |
| **evaluation risk** | mock benchmark 如果没有 recovery / branch 变量，会退化成普通 memory poisoning benchmark。 |
| **engineering-only risk** | 中 |
| **minimum evidence needed to continue** | 展示至少一种现有 baseline 无法处理的 failure：rollback/fork 后 contaminated memory 被检索复用；provenance-filtered retrieval 能降低该失败且不显著损伤 benign memory utility。 |

---

## 3. 攻击表（按强度）

| 攻击 | 强度 | 预备回应 |
|------|------|----------|
| ACRFence 已经提出 replay-or-fork 语义 | 高 | 删除 external side-effect 主 claim；只保留 ACRFence 未直接处理的 memory write/retrieval provenance。 |
| AgentPoison 已证明 memory poisoning | 高 | 不 claim poisoning attack；claim recovery/fork 后污染 memory 的状态边界与隔离策略。 |
| benchmark 只是 toy tool | 中高 | 任务需绑定真实工具语义，并显式包含 checkpoint、fork、memory write、later retrieval。 |
| 方法只是 metadata logging | 中高 | 必须让 provenance 改变 retrieval/quarantine 行为，并报告 utility trade-off。 |
| 安全 benchmark 已有 AgentDojo / ASB | 中 | 本案不做泛化安全攻击，而做 recovery 后 persistent memory consistency。 |

---

## 4. 攻击结论

当前攻击 **部分成立但可回应**。原题过宽，已经收窄为 Recovery-Safe Memory Provenance。当前最合适的 decision 是 **Narrow**：方向可做，但必须用 MVP 证明 recovery / fork 变量带来区别于 ACRFence 和 AgentPoison 的新失败模式。

---

## 5. 与 decision 的联动

| 若… | 建议 decision |
|-----|----------------|
| ACRFence 完整覆盖 memory provenance / store rollback | No-Go |
| ACRFence 覆盖 rollback 但不覆盖 memory provenance / branch contamination | Narrow |
| MVP 显示 provenance-filtered retrieval 明显降低污染复用 | Promising |
| Pilot 有 minimum evidence | Go（仅 Phase 4） |
