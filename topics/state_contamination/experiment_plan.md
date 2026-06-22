# Experiment Plan: Dual-State Contamination on SWE-bench Verified

> **状态**：MVP pilot 就绪（待执行）  
> **决策联动**：见 `decision.md` — 当前 **Narrow**；pilot 通过后升为 **Go**

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
| Pilot 规模 | **10 题**（随机 seed，stratified by difficulty if available） |
| Full 规模 | 50–100 题（pilot 效应量 ≥ 5pp Recovery Gap 后扩展） |

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
| **World-State Drift (WSD)** | 失败 attempt 结束时 workspace 文件 hash 相对初始 snapshot 的偏离度 | WSD > 0 且 C 优于 B 表示 world 通道独立 |
| （辅助）pass@k / clean-restart@k | 与 CCRM 对齐报告 | 复现方向即可 |

---

## 5. 实验流程（Pilot 7 天）

### Day 1–2：环境搭建
- [ ] 安装 mini-SWE-agent + SWE-bench Verified Docker（见 `outputs/pilot/checklist.md`）
- [ ] `cd scripts/pilot && pip install -r requirements.txt`
- [ ] `python sample_instances.py` → `outputs/pilot/instances.json`
- [ ] 三条件 wrapper：`scripts/pilot/run_pilot.py`（dirty / clean-context / full-reset）
- [ ] 日志格式：`outputs/pilot/run_log.jsonl`（见 `scripts/pilot/trajectory_schema.py`）

### Day 3–5：10 题 pilot
- [ ] `python run_pilot.py --execute`（或先 `--dry-run` / `--mock` 测管道）
- [ ] 每题 3 条件 × k=3
- [ ] 导出 trajectories 到 `outputs/pilot/trajectories/`

### Day 6：分析
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
| Docker/GPU 成本 | pilot 仅 10 题 × 3 条件 |
| SWE-bench 争议 | 固定 scaffold + 公开 trajectories |
| 效应量不足 | 提前定义 No-Go 阈值（RG < 3pp） |
| CCRM 已报告类似结论 | 必须报告 WSD；否则无增量 |

---

## 9. 成功标准（pilot → Go）

|  criterion | 阈值 |
|-----------|--------|
| Recovery Gap | ≥ **5pp** on 10-question pilot |
| World-State Drift | 条件 C resolve > 条件 B resolve（≥ 2/10 题可观测） |
| 可复现 | 脚本 + 日志公开 |

满足 → `decision.md` 升级为 **Go（full benchmark）**  
不满足 → **No-Go** 或 pivot 到纯 CCRM replication study
