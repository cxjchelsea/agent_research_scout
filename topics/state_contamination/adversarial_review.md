# Adversarial Review: Dual-State Contamination in Software Engineering Agents

> **审计日期**：2026-03-18（方案 A 重调研）  
> **课题版本**：v2（收窄后）  
> **与 gap_analysis 的区别**：gap 找空白；本文件攻击空白是否站得住。

---

## 1. 八问自检

| # | 攻击问题 | 回应强度 | 回应要点 |
|---|----------|----------|----------|
| 1 | 这个问题是否已经被已有论文覆盖？ | 中-高 | CCRM 覆盖 context retry；Wang et al. 覆盖 memory；world+eval 未覆盖 |
| 2 | 这个课题是否只是已有工作的换名？ | 中 | dual-state + Verified 三联指标非换名；需 pilot 数据支撑 |
| 3 | 这个方法是否只是 prompt/retry/checkpoint 工程组合？ | **高** | 必须有 formal dual-state definition + 系统 baseline；否则拒 |
| 4 | benchmark 是否太小、太人工、太依赖构造？ | 中 | 从 Verified 真实 issue 采样；pilot 10 题 → full 50–100 题 |
| 5 | 指标是否只是已有指标改名？ | 中 | Recovery Gap ≠ pass@k；World-State Drift 用 workspace hash |
| 6 | baseline 是否足够强？ | 中 | dirty-retry / clean-restart / full-reset 三联；可选 GA-Rollback |
| 7 | 是否能跨模型、跨任务、跨环境验证？ | 中-低 | MVP 限 Verified + 1–2 模型；WebArena/τ-bench 为 future |
| 8 | 投 ICLR/ICSE 最可能被拒的理由？ | **高** | 「CCRM 已足够，world state 只是 obvious extension」 |

---

## 2. 必填输出

| 字段 | 内容 |
|------|------|
| **strongest rejection reason** | CCRM 已在 SWE-bench Verified 上 formalize context contamination 并拟合 ε₁/ε₀=7.1；ACRFence 已论述 recovery blind spot。审稿人会认为本文只是把两者拼成 benchmark，增量不足。 |
| **most dangerous related work** | **Why Retrying Fails: Context Contamination in LLM Agent Pipelines** (Yang 2026, arXiv 2605.08563) — 同数据集、同 retry 设定、同 clean-restart 叙事 |
| **novelty risk** | **中高** — context contamination 与 state contamination 术语已被占用 |
| **evaluation risk** | **中** — SWE-bench 数据/评测争议；pilot 效应量未知 |
| **engineering-only risk** | **高** — 若无 formalism，clean-restart 会被判为工程技巧而非 research contribution |
| **minimum evidence needed to continue** | Verified **10 题 pilot**：Recovery Gap ≥ **5pp**；且条件 C（full-reset）resolve > 条件 B（clean-restart）在 **≥2/10** 题可观测 |

---

## 3. 攻击表（按强度）

| 攻击 | 强度 | 预备回应 |
|------|------|----------|
| CCRM 已 formalize context contamination | 高 | 我们扩展 world channel + 发布 eval protocol；CCRM 是子模块非全文 |
| Wang et al. 已定义 state contamination | 高 | scope 切割：executable workspace vs memory safety / toxicity |
| 只是 retry / checkpoint 工程 | 高 | Dual-State 操作定义 + 三条件 baseline + 公开 trajectories |
| benchmark 太小 | 中 | pilot → 50–100 题；报告置信区间 |
| SWE-bench contamination 争议 | 中 | 固定 mini-SWE-agent scaffold；第三方可复现 |
| GA-Rollback 已有 rollback 方法 | 中 | 我们评 recovery rate 非 trajectory rollback method |
| 指标 Recovery Gap 可由 pass@k 推导 | 低-中 | 报告 dirty vs clean 差分；与 CCRM 理论对照 |

---

## 4. 攻击结论

**攻击部分成立**，但不构成 immediate No-Go：

- Context 通道：CCRM 已占住 → 本案 **不能** 以 context-only 为主 claim
- World 通道 + eval protocol：**尚未被同一 benchmark 系统报告** → 仍有空间
- 关键分水岭：**pilot 数据** — 若 workspace reset 无额外收益 → 降级为 **No-Go**（CCRM 复述）

**若无法有效回应「incremental extension」攻击**，应 Hold 或 Narrow 到更窄子问题（例如仅 World-State Drift metric）。

---

## 5. 与 decision 的联动

| 条件 | 建议 decision |
|------|----------------|
| Pilot RG ≥ 5pp 且 C > B 可观测 | **Narrow → Go** |
| Pilot RG 3–5pp | **Hold**（扩样本） |
| Pilot RG < 3pp | **No-Go** |
| 发现 CCRM 已发 dual-state benchmark | **No-Go**（立即 pivot） |
| 当前（无 pilot 数据） | **Narrow** |
