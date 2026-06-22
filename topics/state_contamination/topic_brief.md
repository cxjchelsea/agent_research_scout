# Topic Brief: Dual-State Contamination in Software Engineering Agents

> **版本**：v2（2026-03-18 重调研收窄）  
> 上一版题目「State Contamination in Long-Horizon Tool-Using Agents」过宽，与 CCRM / Wang et al. 2026 术语冲突；本版以 gap_analysis 为准。

---

## 1. 一句话课题定义

在 **software engineering agent**（如 mini-SWE-agent on SWE-bench Verified）的长链路 tool-use 中，失败 attempt 会同时污染 **ContextState**（message/history）与 **WorldState**（workspace/file edits）；本课题定义并评测这种 **dual-state contamination**，以及 **clean-restart** 相对 **dirty-retry** 的 recovery gap。

## 2. 核心失败模式

Agent 在中间步骤写入两类不可自动清除的错误状态：

| 状态通道 | 典型载体 | 污染表现 |
|----------|----------|----------|
| **ContextState** | message history、thought、tool output log | 失败 attempt 留在 context，retry 时 per-step 错误率升高（CCRM） |
| **WorldState** | repo 文件、workspace、test artifacts | 错误 edit 已落盘，仅清 context 无法恢复；rollback 本地 checkpoint ≠ undo 外部状态（ACRFence） |

**Recovery blind spot**：现有 agent 默认 dirty-retry（保留 context + workspace），缺少 contamination-aware clean-restart 协议与评测。

## 3. 为什么重要

- CCRM 已在 SWE-bench Verified 上证明 context retry 污染（ε₁/ε₀=7.1），但 **未度量 workspace drift**。
- SWE-bench 只评最终 patch pass，**看不到 intermediate state 污染与 recovery**。
- Wang et al. 2026 的 state contamination 限 **memory safety**，不覆盖 executable tool state。
- 真实 coding agent 部署中，retry 是默认行为；若 recovery blind spot 存在，pass@k 会系统性高估 agent 能力。

## 4. 研究边界（收窄后）

### 保留

- Software agent / SWE-bench Verified
- ContextState vs WorldState 双通道
- dirty-retry vs clean-restart@k vs workspace-reset
- Recovery Gap、Contamination Rate、World-State Drift 三指标

### 删除（本轮不做）

- 泛化「所有 tool agent / web agent / memory agent」
- Memory toxicity / SPG / laundering（Wang et al. 领地）
- CCRM 理论重推
- Security-focused semantic rollback（ACRFence 领地）
- 新方法 GA-Rollback 复刻

## 5. 研究问题

**RQ1**：在 SWE-bench Verified 上，dirty-retry 相对 clean-restart@k 的 Recovery Gap 有多大？能否复现 CCRM 方向并扩展到 WorldState？

**RQ2**：ContextState 污染与 WorldState drift 是否解耦（仅清 context 不够）？

**RQ3**：是否存在可操作的 **最小 recovery 协议**（workspace reset + clean context）显著优于默认 retry？

## 6. 预期贡献（Problem + Benchmark 路径）

1. **Dual-State Contamination** 操作化定义（ContextState / WorldState / pollution event / recovery blind spot）
2. **Contamination-aware eval protocol** on SWE-bench Verified 子集（50–100 题）
3. **三指标** baseline 结果：Contamination Rate、Recovery Gap、World-State Drift
4. （可选）轻量 PollutionDetector 触发 clean-restart

## 7. 最危险 related work（必须正面 differentiate）

| 论文 | 关系 |
|------|------|
| CCRM (Yang 2026) | 子集：我们只覆盖其 context 通道，扩展 world 通道 + benchmark |
| Wang et al. 2026 | 不同 scope：memory safety vs executable workspace |
| GA-Rollback / ACRFence | 方法参照，不做 security/trajectory-only 复刻 |

## 8. 当前最大风险

- 被审稿人判为 CCRM 增量或 retry 工程技巧
- SWE-bench 数据/评测争议
- Recovery Gap 效应量不足
- Benchmark 子集太小

## 9. 与旧版 topic_brief 的差异

| 维度 | 旧版 | 新版 v2 |
|------|------|---------|
| 题目 | 长链路工具型 Agent 状态污染（泛） | Dual-State Contamination in SE Agents（窄） |
| 场景 | web + memory + SWE + DB | **SWE-bench Verified only**（MVP） |
| 术语 | state contamination（与 Wang et al. 撞名） | **dual-state contamination** + recovery blind spot |
| 贡献 | 方法+系统+benchmark 全开 | **Problem + Benchmark 优先** |
