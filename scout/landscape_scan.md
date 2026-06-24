# Landscape Scan: agent_research_scout_2026_06_24

> **Phase**：Discovery
> **生成日期**：2026-06-24

---

## 1. 扫描边界

- **领域**：AI / LLM Agent，覆盖 benchmark/evaluation、memory/personalization、tool-use/workflow、software engineering agent、多智能体、安全与状态管理、trace diagnosis。
- **时间范围**：优先 2023–2026；早于 2023 的工作仅作为背景，不进入本轮候选支撑。
- **是否受用户偏好约束**：无。默认从 Agent 研究创新点发现开始。
- **排除范围**：不做投稿级 related work 完整审计；不创建 `topics/`；不跑实验；不替用户做最终选题。

---

## 2. 方向地图（按 §一 八大类或子簇）

| 类别 / 子方向 | 代表性工作（verified） | 已覆盖什么 | 明显空白 | 是否值得出候选 |
|---------------|------------------------|------------|----------|----------------|
| Agent evaluation / benchmark | AgentBench, WebArena, OSWorld, GAIA, VisualWebArena, MultiAgentBench | 已有多环境、多模态、Web/desktop/多智能体任务成功率评测 | 多数仍停留在 end-to-end success，缺少跨 benchmark 的可复用 failure attribution 与 trace-level causal diagnosis | 是，形成 C1 |
| Trace diagnosis / failure localization | AgentRx, TRAIL, ErrorProbe | 已开始做关键失败步定位、结构化 trace reasoning、失败分类 | 仍缺少可迁移到 SWE/web/desktop/多智能体的统一 trace schema 与低标注成本诊断协议 | 是，形成 C1 |
| Long-term memory / personalization | AI Persona, MemoryCD, Preference-Aware Memory Update, LoCoMo, MemGPT, MemoryBank | 已有长期对话记忆、用户画像、跨域 personalization benchmark | 偏好漂移、过期记忆、冲突记忆与 tool/action memory 的联合评测不足 | 是，形成 C2 |
| Tool-use / workflow agents | BFCL, tau-bench, ToolBench, APIBank, ToolLLM, WorkArena, WebShop | 已覆盖函数调用准确率、多轮 API 使用、用户模拟、状态核验 | 真实 workflow 中的多次运行一致性、policy compliance、recoverability 与 partial failure 处理仍弱 | 是，形成 C4 |
| Software engineering agents | SWE-bench, SWE-bench Verified, SWE-agent, Agentless, OpenHands, SWE-smith, SWE-bench Multimodal | 已有真实 issue resolution、ACI、平台、数据生成与 multimodal extension | 结果同时受 model、harness、issue quality、contamination、validation oracle 影响，缺少系统化 benchmark integrity 诊断 | 是，形成 C5 |
| Agent 状态管理 / 回滚 / 恢复 | ACRFence, OpenHands, SWE-agent, AutoGen | ACRFence 已明确 semantic rollback attack；平台工作已有 sandbox / agent runtime | 除 rollback 外，长期 memory、external side effects、credential scope、branch/fork semantics 的统一状态隔离仍缺口明显 | 是，形成 C3 |
| Agent security / memory poisoning | AgentDojo, Agent Security Bench, ToolEmu, InjecAgent | prompt injection、memory poisoning、tool attacks、security-utility trade-off 已有强 benchmark | 安全 benchmark 与可靠性 benchmark 分离；攻击后的状态清理、可恢复性、污染传播仍缺少实验协议 | 是，主要支撑 C3 |
| Multi-agent collaboration | MultiAgentBench, MetaGPT, AgentVerse, AutoGen, Magentic-One | 已有协作协议、SOP、多代理框架与多场景 benchmark | 失败归因很难区分 agent-level、protocol-level、tool-level、memory-level，适合并入 trace diagnosis | 是，作为 C1 子场景 |

---

## 3. 跨方向观察

- **重复出现的 failure mode**：长链路中早期错误被后续步骤放大；工具调用参数看似合法但语义偏离；benchmark 只记录最终失败而不记录可操作原因；agent 恢复/重试时外部状态无法回滚；记忆系统把过期、恶意或低置信信息固化到后续行为中。
- **被多个方向共同忽略的问题**：多数 benchmark 关注成功率，不关心失败是否可诊断、可恢复、可防止复发；memory、安全、tool-use、SWE agent 的状态边界各自为政，缺少统一的 state hygiene / trace hygiene 概念。
- **术语/撞车风险**：`trace diagnosis` 已有 AgentRx/TRAIL/ErrorProbe；`rollback attack` 已有 ACRFence；`memory poisoning` 已有 ASB/AgentDojo 相关工作；`SWE benchmark integrity` 容易与 SWE-bench Verified、SWE-smith、Agentless 撞车，必须收窄。
- **近期高威胁论文**（可能直接否决候选）：AgentRx、TRAIL、ACRFence、MemoryCD、tau-bench、Agent Security Bench、SWE-smith、Agentless。

---

## 4. 发现阶段论文索引说明

- 广搜索引文件：`scout/discovery_paper_table.csv`
- 目标规模：本轮写入 **40 篇**，覆盖 5 个候选方向（C1–C5）
- 本阶段 **不要求** `paper_cards/`；精读留给选中课题之后
- verified / uncertain 说明：核心威胁 work 尽量使用 arXiv、OpenReview、ACL Anthology、official project page；少数未在本轮直接抓取官方页但有明确线索的条目标为 uncertain，不作为核心否定依据
