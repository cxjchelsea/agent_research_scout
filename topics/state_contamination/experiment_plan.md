# Experiment Plan: Dual-State Contamination on SWE-bench Verified

> **状态**：MVP pilot 就绪（待执行）  
> **决策联动**：见 `decision.md` — 当前 **Narrow**；10 题 infrastructure pilot 只能决定是否扩样，不能单独升为论文级 **Go**

---

## 1. 任务定义

**目标**：度量 software engineering agent 在失败 retry 时，ContextState 与 WorldState 的污染程度，以及 clean-restart 相对 dirty-retry 的 Recovery Gap。

**Dual-State 操作定义**：

| 概念 | 定义 |
|------|------|
| ContextState | agent message history + tool I/O log（含 failed attempt） |
| WorldState | Docker workspace 内 repo 文件树 + 测试产物 |
| Pollution event | 失败 attempt 结束后，ContextState 或 WorldState 仍保留错误信息且被后续 attempt conditioning |
| Recovery blind spot | 仅 dirty-retry（默认）无法恢复；需 clean-restart 和/或 workspace reset |

---

## 2. 数据与环境

| 项 | 规格 |
|----|------|
| Benchmark | SWE-bench Verified |
| Agent scaffold | mini-SWE-agent（bash-only，与 Verified leaderboard 对齐） |
| 模型 | 至少 1 个开源模型（如 Qwen2.5-Coder-32B）+ 可选 1 个强闭源作 upper bound |
| Infrastructure pilot | **10 题**（验证状态控制、日志、merge、指标是否可计算） |
| Signal pilot | 20–30 题（观察 full-reset 是否稳定优于 clean-restart） |
| Full / paper-scale | 50–100 题（报告效应量、置信区间和错误分析） |

---

## 3. 实验条件（3 baselines）

| 条件 | ContextState | WorldState | 说明 |
|------|--------------|------------|------|
| **A: dirty-retry** | 保留 failed attempt | 保留 edits | 默认 agent 行为 |
| **B: clean-restart@k** | 每次 retry 清空 history | 保留 edits | 隔离 context 污染（CCRM clean-restart） |
| **C: full-reset@k** | 清空 history | **reset workspace 到初始 snapshot** | 隔离 world 污染 |

每题最多 **k=3** attempts；记录每 attempt 的 resolve 与否。

---

## 4. 指标（≥3，Skill 要求）

| 指标 | 定义 | 假设 |
|------|------|------|
| **Contamination Rate (CR)** | retry 后第 1 step 错误率 − 首次 attempt 第 1 step 错误率 | CR > 0 表示污染 |
| **Recovery Gap (RG)** | resolve(clean-restart@k) − resolve(dirty-retry@k) | RG > 0 表示 blind spot |
| **World-State Drift (WSD-basic)** | 失败 attempt 结束时 workspace hash 相对初始 snapshot 的偏离度 | 只能说明 workspace 变化，不能单独证明污染 |
| **WSD-source / WSD-residual** | git diff 文件列表、源码/测试文件变化、失败 attempt 残留 patch | 用于区分测试产物、合理 edit、残留错误 edit |
| **WSD-harmful** | retry 前残留 workspace state 导致后续 attempt 偏航或失败 | 最接近论文 claim 的 world contamination 证据 |
| （辅助）pass@k / clean-restart@k | 与 CCRM 对齐报告 | 复现方向即可 |

---

## 5. 实验流程（Pilot 7 天）

### Day 1–2：环境搭建
- [ ] 安装 mini-SWE-agent + SWE-bench Verified Docker（见 `outputs/pilot/checklist.md`）
- [ ] `cd scripts/pilot && pip install -r requirements.txt`
- [ ] `python sample_instances.py` → `outputs/pilot/instances.json`
- [ ] 三条件 wrapper：`scripts/pilot/run_pilot.py`（dirty / clean-context / full-reset）
- [ ] `python validate_pilot_setup.py` 验证配置与日志不是 mock/未解析状态
- [ ] `python state_control_validation.py` 验证 context/world state-control 证据
- [ ] 日志格式：`outputs/pilot/run_log.jsonl`（见 `scripts/pilot/trajectory_schema.py`）

### Day 3–5：10 题 infrastructure pilot
- [ ] `python run_pilot.py --mock --reset-log` 测试管道（不可作为研究证据）
- [ ] `python run_pilot.py --dry-run` 检查真实命令（不应含 `--exit-immediately`）
- [ ] `python run_pilot.py --smoke-test` 做单题基础设施检查
- [ ] `python run_pilot.py --execute --reset-log` 真实执行（清空 mock 日志）
- [ ] 每题 3 条件 × k=3
- [ ] 导出 trajectories 到 `outputs/pilot/trajectories/`
- [ ] 严格合并评测结果：每条 resolved 必须对应 `instance_id + condition + attempt`

### Day 6：分析
- [ ] `python validate_pilot_setup.py` 确认真实日志可分析
- [ ] `python state_control_validation.py` 确认状态控制证据可审计
- [ ] `python analyze_pilot.py` → `outputs/pilot/metrics/pilot_summary.json`
- [ ] `python update_decision_draft.py` → 合并进 `decision.md`

### Day 7：文档
- [ ] 更新 gap_analysis / decision.md
- [ ] 起草 benchmark protocol README（放 `outputs/` 或 `benchmarks/`）

---

## 6. 消融与泛化（Full 阶段，pilot 后）

| 实验 | 目的 |
|------|------|
| k=1 vs k=3 | 污染是否随 retry 次数累积 |
| 第二模型 | 跨模型泛化 |
| 错误类型分层 | edit-heavy vs search-heavy issues |
| （可选）GA-Rollback 接入 | 对比 trajectory rollback vs clean-restart |

---

## 7. 错误分析

- 抽样 5 条 trajectories：标注 pollution step（context / world / both）
- 对比 AgentDebug taxonomy：是否落在 memory/planning/action
- 报告：full-reset 救回但 clean-restart 未救回的比例（证明 world 通道）

---

## 8. 资源与风险

| 风险 | 缓解 |
|------|------|
| Docker/GPU 成本 | 先跑 10 题 infrastructure pilot，再决定是否扩到 20–30 / 50–100 |
| SWE-bench 争议 | 固定 scaffold + 公开 trajectories；报告模型、seed、实例列表、评测命令；后续可迁移到新 issue 或替代 SWE benchmark |
| test oracle / public benchmark overfitting | 保留完整 trajectories 与 predictions；按 repo / issue 类型分层；必要时人工抽样检查 plausible patch |
| 效应量不足 | 10 题只看非零信号；20–30 题看稳定性；50–100 题报告 CI / paired analysis |
| CCRM 已报告类似结论 | 必须报告 WSD；否则无增量 |

---

## 9. 成功标准（分层证据）

| 层级 | 标准 | 决策 |
|------|------|------|
| 10 题 infrastructure | state control 验证通过；strict merge 通过；CR/WSD/RG 至少可计算；观察到非零 world-reset signal | **Hold / scale**，不能直接 Go |
| 20–30 题 signal | full-reset 相对 clean-restart 有稳定优势；RG / world-reset wins 不只来自单个异常实例 | 可考虑 **Go / Hold** |
| 50–100 题 paper-scale | paired analysis、CI、WSD-harmful case study、人工抽样错误分析齐全 | 支撑论文级 claim |

若 10 题基础设施失败 → 先修脚本/状态控制，不更新 decision。
若 20–30 题仍无 full-reset 增量 → **No-Go** 或 pivot 到纯 CCRM replication study。
