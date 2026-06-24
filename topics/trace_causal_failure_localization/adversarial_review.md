# Adversarial Review: Trace-Causal Failure Localization for Agent Workflows

> **目的**：站在顶会审稿人角度攻击课题，判断会不会被拒。
> **与 gap_analysis 的区别**：gap 找空白；adversarial 攻击空白是否站得住。
> **审计日期**：2026-06-24

---

## 1. 八问自检

| # | 攻击问题 | 回应强度 | 回应要点 |
|---|----------|----------|----------|
| 1 | 这个问题是否已经被已有论文覆盖？ | 强攻击成立 | AgentRx / TraceElephant / TRAIL / Who&When 已覆盖 localization / attribution 主体。 |
| 2 | 这个课题是否只是已有工作的换名？ | 强攻击成立于原题 | 原题“trace-causal failure localization”近似已有 work 组合。 |
| 3 | 这个方法是否只是 prompt/retry/checkpoint 工程组合？ | 中 | 收窄后若只让 LLM 生成 repair suggestion，仍会被攻击。 |
| 4 | benchmark 是否太小、太人工、太依赖构造？ | 中 | 可复用 AgentRx / TraceElephant / TRAIL traces 缓解。 |
| 5 | 指标是否只是已有指标改名？ | 中 | 原有 responsible step accuracy 已拥挤；需改为 test validity / rerun success。 |
| 6 | baseline 是否足够强？ | 中高 | 必须包括 AgentRx、AgentDebug、TraceElephant-style attribution。 |
| 7 | 是否能跨模型、跨任务、跨环境验证？ | 中 | 可从 tau-bench / Magentic-One / SWE-Agent / SWE-bench 派生。 |
| 8 | 投 ICLR/NeurIPS/ACL/EMNLP 最可能被拒的理由？ | 高 | “AgentRx 已经定位 critical failure step，AgentDebug 已经给 corrective feedback；你只是在包装。” |

---

## 2. 必填输出

| 字段 | 内容 |
|------|------|
| **strongest rejection reason** | AgentRx 已经做 critical failure step localization，TraceElephant 已经做 full-trace attribution，TRAIL 已经做 trace issue localization；原题没有足够新颖性。 |
| **most dangerous related work** | AgentRx；TraceElephant；TRAIL；Who&When；AgentDebug |
| **novelty risk** | 高（原题）/ 中高（收窄题） |
| **evaluation risk** | 中：可复用现有 traces，但 repair-test ground truth 需要新增标注。 |
| **engineering-only risk** | 中高：如果只是生成建议而非可执行 tests / rerun validation，会被认为是工程 glue。 |
| **minimum evidence needed to continue** | 证明 AgentRx / AgentDebug 未覆盖 executable regression-test generation；至少构造 20–50 个 failure-to-test examples。 |

---

## 3. 攻击表（按强度）

| 攻击 | 强度 | 预备回应 |
|------|------|----------|
| AgentRx 已覆盖 critical failure step + root-cause attribution | 高 | 原题 No-Go；只能转向 repair-test generation。 |
| TraceElephant 已覆盖 full execution traces + decisive step attribution | 高 | 不能做 full-trace attribution benchmark。 |
| TRAIL 已经是 trace reasoning 和 issue localization benchmark | 高 | 不能做泛化 issue localization。 |
| AgentDebug 已覆盖 root-cause + corrective feedback | 中高 | 收窄题必须输出可执行 regression tests，而不是自然语言 feedback。 |
| 数据集太小，靠人工标注不可扩展 | 中 | MVP 需基于现有 traces 派生，并定义可验证 test artifact。 |

---

## 4. 攻击结论

攻击结论：原始 C1 题目基本不应继续，因核心 claim 已被 AgentRx / TraceElephant / TRAIL / Who&When 强覆盖。可考虑收窄为 **Repair-Test Generation from Agent Failure Traces**，但该收窄题仍需继续核验 AgentDebug 和 AgentRx 是否已经自然覆盖。

---

## 5. 与 decision 的联动

| 若… | 建议 decision |
|-----|----------------|
| 坚持原始 trace-causal localization claim | No-Go |
| 收窄到 executable regression-test / repair-target generation | Narrow |
| 无法证明 AgentDebug / AgentRx 未覆盖收窄题 | No-Go |
| 收窄题有 20–50 个可构造 examples 且 baseline 清晰 | Narrow → Promising（后续） |
