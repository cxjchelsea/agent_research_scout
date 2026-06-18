# Gap Analysis: State Contamination in Long-Horizon Tool-Using Agents

> 基于 `paper_table.csv` 核验后的 20 篇论文（20/20 verified，0 remove）。  
> 精读核心集：8 篇（见 `paper_cards/`）。

---

## 1. 已有工作已经覆盖什么？

### 1.1 问题定义与形式化（已有人做，且用词高度重叠）

| 子问题 | 代表论文 | 已覆盖内容 |
|--------|----------|------------|
| **Context contamination（retry 污染）** | CCRM (Yang 2026) | 失败 attempt 留在 context → ε₁>ε₀；clean-restart dominance；SWE-bench Verified 拟合 |
| **State contamination（memory 通道）** | Wang et al. 2026 | memory laundering；write-gate before summarization；SPG 指标 |
| **Error propagation / cascade** | AgentDebug 2025 | 5 模块 17 类 taxonomy；memory/reflection 为 cascade 主源 |
| **Recovery blind spot（外部状态）** | ACRFence 2026 | checkpoint-restore ≠ undo irreversible tool effect；replay-or-fork |

### 1.2 方法与系统（部分覆盖）

| 方法 | 代表论文 | 覆盖边界 |
|------|----------|----------|
| Stepwise rollback | GA-Rollback (EMNLP 2025) | trajectory 内回滚；不处理 world state |
| Anticipatory reflection | Devil's Advocate (EMNLP 2024) | action 前反思；无 state isolation |
| Failure diagnosis | AgentRx, TRAIL, Who&When | 定位 critical step；无 rollback 协议 |
| Memory 评测 | MemoryAgentBench, LongMemEval | 四能力/五能力；无 executable tool state |

### 1.3 Benchmark 与实验平台（覆盖广，但缺口明显）

- **长链路 tool agent 环境**：WebArena, SWE-bench, OSWorld, τ-bench, OpenHands — 评 end success，**不评 contamination/recovery**。
- **Recovery 评测**：Hell or High Water (COLM 2025) — 仅 **external failure**，非 self-caused pollution。
- **CCRM 实证**：借用 SWE-bench Verified retry 数据，但 **未发布专用 benchmark**。

### 1.4 核验修正（影响文献边界）

- 「ADVOCATE」正式标题为 **Devil's Advocate**（EMNLP Findings 2024）。
- AgentDebug：**ICLR 2026 withdrawn**，以 arXiv 为准。
- AgentRx：原标 ICML 2026 **未获接受确认**，以 arXiv + Microsoft 发布为准。
- OpenHands：venue 应为 **ICLR 2025**（预印本 2024）。
- Hell or High Water：venue 应为 **COLM 2025**（非仅 arXiv）。

---

## 2. 我的 state contamination 课题是否只是已有工作的换名？

**不完全是，但存在「换名风险区」。**

| 若你的课题是… | 判断 |
|---------------|------|
| 「retry 失败后 context 污染导致性能下降」 | **基本是 CCRM 换名** → 不建议 |
| 「memory 写回导致 state contamination / laundering」 | **基本是 Wang et al. 2026 换名** → 不建议 |
| 「agent 需要 stepwise rollback」 | **与 GA-Rollback 高度重叠** → 需新场景或 dual-state |
| 「checkpoint 恢复有 blind spot」 | **与 ACRFence 重叠（security 角）** → 需 task-error 角 |

**尚未被充分覆盖、且与 topic_brief 一致的表述：**

> 长链路 **tool-using agent** 在 **context + executable world state + persistent memory** 三通道上发生 **state contamination**，现有系统存在 **recovery blind spot**——能 retry/rollback 本地 trajectory，却不能一致地 **检测、隔离、回滚** 已被污染的外部状态；且 **没有 benchmark** 同时度量 contamination 程度与 recovery 成功率。

这不是简单换名，而是 **跨通道统一问题 + 评测缺口**。

---

## 3. 如果不是，真正空白在哪里？

### 空白 A：Unified contamination taxonomy（跨通道）

现有工作各守一条通道：

- CCRM → context retry
- Wang et al. → memory safety
- ACRFence → irreversible API / security
- AgentDebug → modular errors（无 contamination 类）

**空白**：缺少把 **context / world / memory** 三类 state 污染统一定义，并标注 **pollution step vs failure step** 的 taxonomy。

### 空白 B：Contamination-aware benchmark（评测）

现有 benchmark 主流指标：pass@1, pass@k, pass^k, end-to-end success。

**空白**：缺少：

- `pass@k` vs **`clean-restart@k`** vs **`pass^k`** 三联对照；
- 注入可控 pollution 后的 **recovery rate**；
- **dual-state drift** 度量（message hash vs workspace/DB hash）。

### 空白 C：Recovery 机制（非 security PoC）

GA-Rollback 只做 trajectory；ACRFence 只做 irreversible API security；AgentDebug 只做 feedback。

**空白**：面向 **task failure** 的 **provenance-aware rollback**——知道哪一步污染了哪个 state substrate，并选择性 clean/fork/replay。

### 空白 D：Tool-agent 长链路实证

MemoryAgentBench / LongMemEval 不覆盖 bash/file/DB；SWE-bench 不评 intermediate state。

**空白**：在 **SWE-bench Verified / WebArena / τ-bench** 上系统测量 contamination 传播与 recovery blind spot。

---

## 4. 哪些已有论文最威胁我的创新性？

按威胁等级排序：

| 优先级 | 论文 | 威胁点 | 应对策略 |
|--------|------|--------|----------|
| **S1** | CCRM (2026) | 已用 **context contamination** + 理论 + SWE 实证 | 扩展到 dual-state + benchmark； cite 并 differentiate |
| **S1** | State Contamination in Memory-Augmented LLM Agents (2026) | 已用 **state contamination** 术语 + mitigation | 明确 scope：tool executable state，非 toxicity |
| **S2** | GA-Rollback (2025) | rollback 方法已有 | 组合 world-state consistency + provenance trigger |
| **S2** | ACRFence (2026) | recovery blind spot 叙事已有 | 从 security 扩展到 task-error + 评测 |
| **S3** | AgentDebug (2025) | cascade + recovery feedback | 增加 state-level 操作而非仅 feedback |
| **S3** | MemoryAgentBench (2026) | memory 评测 + selective forgetting | 不做 pure memory bench；做 tool-agent extension |

---

## 5. 最小可行创新点是什么？

**推荐 MVP（2–4 个月可启动）：**

### 贡献组合：Problem + Benchmark（最小顶会路径）

1. **问题定义**：**Dual-State Contamination** — 区分 `ContextState`（message/history）与 `WorldState`（workspace/DB/file），定义 pollution event 与 recovery blind spot。
2. **Benchmark 子集**：在 **SWE-bench Verified**（50–100 题）上构造：
   - 条件 A：dirty retry（默认 agent）
   - 条件 B：clean-restart@k
   - 条件 C：workspace reset + clean context
   - 报告 Δresolve = resolve(B) − resolve(A)，复现 CCRM 方向并扩展到 workspace drift。
3. **指标**（3 个即可）：
   - Contamination Rate（retry 后第一步错误率提升）
   - Recovery Gap（clean-restart@k − pass@k）
   - World-State Drift（patch/file hash 与 gold path 偏离度）

**可选 +Method 增量（若时间允许）：**

- 轻量 **PollutionDetector**：基于 constraint violation（借鉴 AgentRx）触发 clean-restart，而非 full AgentDebug stack。

**刻意不做（避免重叠）：**

- 不重推 CCRM 理论；
- 不做 memory toxicity / SPG；
- 不做 security-focused ACRFence 复刻。

---

## 6. 审稿人最可能如何攻击？

| 攻击点 | 强度 | 预备回应 |
|--------|------|----------|
| 「CCRM 已经 formalize context contamination」 | 高 | 我们覆盖 world state + benchmark；CCRM 是子模块 |
| 「Wang et al. 已定义 state contamination」 | 高 | 他们限 memory safety；我们是 tool-agent task state |
| 「只是 retry / checkpoint 工程技巧」 | 高 | 提供 formal dual-state definition + 系统性 benchmark 结果 |
| 「benchmark 太小或人工注入」 | 中 | 基于 Verified 真实 trajectories + 公开 protocol |
| 「GA-Rollback / ACRFence 已有 recovery」 | 中 | 对比实验：trajectory rollback vs dual-state clean |
| 「AgentDebug 已做 failure analysis」 | 中 | 我们评 recovery rate，不是 detection accuracy |
| 「SWE-bench contamination 争议」 | 中 | 使用 third-party eval + 固定 mini-SWE-agent scaffold |

---

## 7. 当前结论

### 结论：**继续 — 但必须缩小 scope**

| 维度 | 判断 |
|------|------|
| 值不值得做 | **值得**，但不能再泛谈「state contamination」 |
| 是否换名 | **若只做 retry 或 memory → 是换名；若做 dual-state tool-agent → 不是** |
| 顶会潜力 | **Problem + Benchmark 路径** 有潜力；纯 method 需显著超过 GA-Rollback |
| 适合会议 | ACL/EMNLP（agent eval）、ICLR/NeurIPS（benchmark+analysis）、ICSE/FSE（SWE angle） |
| 建议动作 | **缩小**为 Dual-State Contamination on SWE-bench Verified |

### 不建议

- **暂停**：问题真实，且 CCRM/Wang/ACRFence 三角证明缺口存在。
- **换方向**：除非放弃 tool-agent 角度转 pure memory safety（会与 Wang et al. 正面撞车）。

### 下一步 7 天

1. 精读 8 篇 core papers（paper_cards 已就绪）。
2. 用 mini-SWE-agent 在 Verified 10 题上跑 pass@3 vs clean-restart@3 试点。
3. 写 1 页 Dual-State Contamination 定义（context/world/memory 三通道表）。
4. 更新 `topic_brief.md` 术语，避免与 CCRM / Wang et al. 撞名。
5. 起草 benchmark protocol 文档（可放 `experiment_plan.md`）。

---

## 附录：8 篇精读核心论文

| # | 论文 | 选入理由 |
|---|------|----------|
| 1 | CCRM | 直接 context contamination 理论 + SWE 实证 |
| 2 | State Contamination (Wang et al.) | 直接 state contamination 术语 |
| 3 | GA-Rollback | rollback 方法代表 |
| 4 | ACRFence | recovery blind spot（world state） |
| 5 | AgentDebug | error propagation taxonomy |
| 6 | MemoryAgentBench | memory/forgetting 评测框架 |
| 7 | SWE-bench | 实验底座 + CCRM 验证来源 |
| 8 | Hell or High Water | recovery benchmark 互补 |
