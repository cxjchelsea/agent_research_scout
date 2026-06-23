# Agent / AI 顶会论文选题调研 Skill

## 目标

帮助我在 AI / LLM Agent 领域寻找一个有机会发展成顶会论文的研究课题。重点不是泛泛总结论文，而是识别一个可泛化、可复现、可实验验证的失败模式、机制问题、表示问题、评估问题或系统问题。

最终输出必须判断：这个课题是否值得做、是否已经有人做过、创新性是否足够、能否在公开数据集或可构造 benchmark 上验证、适合投哪些会议，以及我当前能力是否能推进。

**产出方式**：所有调研结果写入 `topics/<topic>/` 下的标准文件，而非只在对话里总结。模板见 `templates/`；workflow 见根目录 `README.md`。

------

## 一、调研对象

围绕以下方向进行系统调研：

1. LLM Agent 的失败模式
2. 长期个人 Agent / memory agent
3. workflow agent / tool-use agent / software engineering agent
4. 多智能体协作系统
5. agent evaluation / benchmark / trace diagnosis
6. agent 状态管理、回滚、恢复、状态污染
7. agent 个性化、长期适应、用户变化建模
8. agent 在真实工程系统中的可靠性问题

优先关注近三年论文，尤其是 ICLR、NeurIPS、ICML、ACL、EMNLP、COLM、CHI、WWW、KDD、ICSE、FSE、arXiv 高引用或高讨论论文。

------

## 二、调研时必须回答的问题

对每一个候选课题，必须回答以下问题。

### 1. 问题是否真实存在？

检查它是否属于以下至少一种类型：

- 现有方法没有覆盖的新问题；
- 已有问题进入了 agent / 长期交互 / 工具使用 / 真实任务后产生新困难；
- 现有系统反复出现但没有被形式化的工程问题；
- 现有 benchmark 看不到但真实部署中高频出现的问题；
- 现有方法在某些条件下系统性失败；
- 现有表示方式导致问题不可解或难以评估。

如果只是“感觉重要”，但没有论文、系统、benchmark、工程案例或可构造任务支撑，应判定为弱课题。

------

### 2. 是否已有相似工作？

必须检索并比较：

- 是否已有 benchmark；
- 是否已有 failure taxonomy；
- 是否已有 dataset；
- 是否已有方法论文；
- 是否已有 survey 明确总结该问题；
- 是否已有系统已经解决类似问题。

输出时不能只说“有人做过”。必须区分：

- 完全已做，创新空间小；
- 方向已做，但子问题仍有空白；
- benchmark 有了，但机制方法不足；
- 方法有了，但评估场景不真实；
- 工程里存在，但学术上尚未形式化；
- 只在某一领域做过，可以迁移到新场景。

------

### 3. 能否形成顶会级贡献？

从以下贡献类型中判断：

#### A. 问题贡献

提出一个以前没有被清楚定义、但真实重要的 agent 失败模式。

要求：

- 有清晰定义；
- 能构造正负样本；
- 能证明多个现有 agent 都会失败；
- 能说明为什么现有 benchmark 看不到它。

#### B. 表示贡献

提出一种新的表示方式，使 agent 的状态、记忆、任务轨迹、用户变化、工具调用或失败传播变得可建模。

要求：

- 表示不是换名字；
- 能带来可计算、可比较、可诊断或可优化的好处；
- 能接入训练、推理、检索、规划或评估流程。

#### C. 方法贡献

提出新的训练、推理、诊断、恢复、回滚、记忆更新、状态隔离或评估方法。

要求：

- 有明确 baseline；
- 有消融实验；
- 能在多个任务或多个模型上验证；
- 不是简单 prompt engineering。

#### D. Benchmark / Dataset 贡献

构建一个现有 benchmark 覆盖不到的新任务或新评估集。

要求：

- 任务定义清晰；
- 数据来源可信；
- 标注或自动评估可靠；
- 有难度分层；
- 有 baseline 结果；
- 能揭示现有方法的系统性不足。

#### E. 系统贡献

构建一个真正运行的 agent 系统，并证明它解决真实问题。

要求：

- 系统不是简单集成；
- 有新的架构机制；
- 有真实任务或真实用户场景；
- 有端到端实验；
- 有失败分析、成本分析和泛化分析。

------

## 三、候选课题评分表

每个课题按 10 分制评分（写入 `decision.md`）：

1. 重要性：这个问题是否影响真实 agent 部署？
2. 新颖性：已有工作是否没有充分覆盖？
3. 可形式化程度：能否定义输入、输出、失败条件和评价指标？
4. 可验证性：能否用公开数据、模拟环境或可构造 benchmark 验证？
5. 方法空间：是否不只是发现问题，还能提出解决方法？
6. 泛化性：是否能跨模型、跨任务、跨 agent 框架验证？
7. 顶会匹配度：是否符合 ICLR / NeurIPS / ICML / ACL / EMNLP / CHI / ICSE 等会议兴趣？
8. 工程可行性：以我当前能力和资源，是否能在 2–4 个月内做出初版实验？
9. Baseline 清晰度：是否有可复现的现有方法可比较？
10. 风险：是否容易被审稿人认为只是工程问题、prompt trick、benchmark 小修小补或概念包装？

最后给出总评：

- 8.5–10：强烈值得做，有顶会潜力；
- 7–8.4：可以做，但需要找到更强贡献点；
- 5–6.9：适合作为项目或 workshop，不建议直接冲顶会；
- 5 以下：不建议投入。

------

## 四、Topic 目录产出规范

每个课题在 `topics/<topic>/` 下维护以下文件。**不得跳过 workflow 顺序**（见 §七）。

| 步骤 | 文件 | 职责 | 模板 |
|------|------|------|------|
| 1 | `topic_brief.md` | 当前版本课题定义（收窄后只保留一版） | `templates/topic_brief_template.md` |
| 2 | `paper_table.csv` | 论文索引 + 核验 | — |
| 3 | `paper_cards/` | 核心论文精读（`core_read=yes` 必须有 card） | `templates/paper_card_template.md` |
| 4 | `related_work.md` | 文献地图（按类总结，非流水账） | — |
| 5 | `gap_analysis.md` | 空白分析、换名判断、MVP 方向、收窄记录 | `templates/gap_analysis_template.md` |
| 6 | `adversarial_review.md` | 审稿人攻击：会不会被拒 | `templates/adversarial_review_template.md` |
| 7 | `file_consistency_check.md` | 全库一致性审计 | `templates/file_consistency_check_template.md` |
| 8 | `decision.md` | Go / Narrow / Hold / No-Go | `templates/decision_template.md` |
| 9 | `experiment_plan.md` | MVP 实验设计（仅 decision 允许后） | `templates/experiment_plan_template.md` |
| 10 | `outputs/` | pilot / 实验产出 | — |

### topic_brief.md 必须包含

- 一句话课题定义（不用空泛大词）
- 核心失败模式
- 为什么重要
- 研究边界（保留 / 删除）
- 研究问题（RQ1–3）
- 预期贡献
- 最危险 related work
- 当前最大风险

### related_work.md 必须包含

- 按 category 分组（非逐篇流水账）
- 每组：已覆盖什么、没覆盖什么、与本案关系
- 引用论文必须在 `paper_table.csv` 中有对应行

### gap_analysis.md 必须包含

- §二「是否已有相似工作」的分层判断
- §三「贡献类型」下的 MVP 选择
- 最危险 3 篇 related work 正面比较
- 是否只是换名
- 若收窄：完整收窄记录（原始题目 → 新题目 → 删除/保留/实验边界）
- **不得**嵌入 adversarial 或 consistency 全文（分别写入独立文件）

### adversarial_review.md 与 gap_analysis.md 的分工

| 文件 | 回答的问题 |
|------|------------|
| `gap_analysis.md` | 空白在哪里？还能做什么？ |
| `adversarial_review.md` | 这个空白站得住吗？审稿人会怎么拒？ |

### experiment_plan.md 填写条件

- **Go**：可写完整 MVP + pilot + full 计划
- **Narrow**：仅可写 **pilot / MVP**（明确 minimum evidence），不可写 full-scale claim
- **Hold / No-Go**：不写 experiment_plan，或只留一行说明暂停原因

### 对话输出 vs 文件

对话中可以摘要结论，但**必须以 repo 文件为准**。每轮调研结束应明确列出更新了哪些文件。

------

## 五、调研时的判断原则

不要迎合我的想法。
如果课题不够新，直接指出。
如果只是概念好听但不可验证，直接否定。
如果已有工作很多，必须说明我还能切哪里。
如果只能做成工程项目而不是论文，也要直接说明。
如果有机会，必须指出最小可行论文路径。

判断一个课题是否值得做时，优先考虑：

1. 是否能揭示现有 agent 的系统性失败；
2. 是否能提出新的问题定义或表示；
3. 是否能构造可靠 benchmark；
4. 是否能提出比 baseline 更稳的方法；
5. 是否能跨模型、跨任务、跨系统验证；
6. 是否能让审稿人相信这是一个领域需要认真对待的问题。

------

## 六、最终目标

不要只是帮我找“有趣方向”。
要帮我找到一个能够发展为论文的研究问题：

- 有问题定义（`topic_brief.md`）；
- 有相关工作边界（`related_work.md` + `paper_cards/`）；
- 有实验场景（`experiment_plan.md`）；
- 有 baseline；
- 有指标；
- 有方法空间；
- 有审稿人认可的贡献点（经 `adversarial_review.md` 检验）；
- 有我当前能力可以启动的最小版本。

------

## 七、Research Repo 结构与 Workflow

### 目录结构

```text
agent-research-scout/
├── README.md
├── skills/
│   └── paper_research_skill.md          ← 本文件
├── templates/                           ← 各产出文件模板
├── topics/
│   └── <topic>/
│       ├── topic_brief.md
│       ├── paper_table.csv
│       ├── paper_cards/
│       ├── related_work.md
│       ├── gap_analysis.md
│       ├── adversarial_review.md
│       ├── file_consistency_check.md
│       ├── decision.md
│       └── experiment_plan.md
├── papers/          ← 原始 PDF、笔记、bib
├── benchmarks/
├── scripts/
└── outputs/         ← pilot / 实验结果（按 topic 分子目录）
```

### Workflow（严格顺序）

```text
1. topic_brief.md           定义课题
2. paper_table.csv          收集并核验论文（≥15 篇广搜，标记 core_read）
3. paper_cards/             核心论文精读（core_read=yes，通常 ≥8 篇）
4. related_work.md          文献地图
5. gap_analysis.md          空白分析 + 必要时收窄
6. adversarial_review.md    审稿人攻击
7. file_consistency_check.md  一致性审计
8. decision.md              Go / Narrow / Hold / No-Go
9. experiment_plan.md       仅 decision 允许后
10. outputs/                执行 pilot / 实验
```

### 分阶段调研闭环（必须显式标注当前 Phase）

上面的 10 步是**文件写作顺序**，不是一次性投稿完成标准。每次执行本 skill 时，必须先判断当前课题处于哪个 Phase，并在 `decision.md` 与 `file_consistency_check.md` 中写明。

| Phase | 名称 | 目标 | 最低完成标准 | 允许的决策 |
|-------|------|------|--------------|------------|
| 0 | Intake / Scope | 把用户的模糊方向变成可调研课题 | `topic_brief.md` 有一句话定义、边界、最危险相邻方向 | Hold / Continue |
| 1 | Scouting | 判断方向是否值得进入 MVP / pilot | `paper_table.csv` ≥15 篇 verified/uncertain 分明；`core_read=yes` 通常 8 篇；完成 gap + adversarial + consistency | Narrow / Hold / No-Go |
| 2 | Expansion | 把选题侦察扩成论文级 related work 地图 | `paper_table.csv` 通常 40–60+ 篇；`core_read=yes` 通常 12–20 篇；补齐 survey、引用链、同期 work、强 baseline | Narrow / Go / Hold |
| 3 | Validation | 用 pilot 或 minimum evidence 验证核心效应 | `outputs/` 有可审计日志/指标；`decision.md` 根据实验更新；失败时回到 Phase 1/2 收窄 | Go / Narrow / Hold / No-Go |
| 4 | Paper-ready Audit | 投稿前完整性审计 | related work 覆盖主要簇；最危险 5–8 篇正面比较；claims 与 evidence 对齐；实验计划可扩到 full study | Go / Hold |

#### Phase 1 — Scouting（默认起点）

当用户只给出一个想调研的方向时，默认先做 Phase 1，而不是承诺完成投稿级调研。Phase 1 的产物用于回答：

- 这个方向是否真实、重要、可验证？
- 是否已有工作完整覆盖？
- 是否能收窄到一个 MVP benchmark / baseline / metric？
- 是否值得投入 pilot？

Phase 1 完成后，如果 `decision.md` 是 **Narrow**，不能声称“完整调研完成”，只能说“选题侦察完成，可进入 pilot 或扩库”。

#### Phase 2 — Expansion（论文级扩库）

进入 Phase 2 的触发条件：

- Phase 1 为 Narrow / Go，且用户希望继续推进成论文；
- 或 adversarial_review 指出 related work 覆盖不足；
- 或 pilot 前需要补强 baseline / benchmark / method 线索。

Phase 2 必须使用增量方式，不删除 Phase 1 产物：

1. 从核心 8 篇做 backward / forward snowball（参考文献 + citing papers）。
2. 补 survey / taxonomy / benchmark / method / system / evaluation 五类文献。
3. 将 `paper_table.csv` 扩到通常 40–60+ 篇；少于 40 篇时必须解释领域过窄或检索边界。
4. 将 `core_read=yes` 扩到通常 12–20 篇；新增 card 优先给最危险竞品、强 baseline、实验底座、定义/术语威胁。
5. 重写或增补 `related_work.md`，按问题簇组织，而不是按检索顺序堆论文。
6. 更新 `gap_analysis.md` 中“已覆盖/未覆盖”的判断，重新做最危险 5–8 篇正面比较。
7. 重新运行 `adversarial_review.md` 与 `file_consistency_check.md`，并更新 `decision.md`。

Phase 2 的目标是论文级文献地图，不要求所有 40–60 篇都有 paper card；`core_read=no` 可只在 table 和 related_work 中作为背景或相邻工作引用。

#### Phase 3 — Validation（实验验证）

Phase 3 不能只写计划，必须产生或合并 evidence：

- pilot / smoke / mock 必须在 `outputs/` 中可区分，mock 只能验证管道，不能作为研究证据；
- 必须先通过 state-control 验证：dirty-retry 保留 context+world，clean-restart 重置 context 但保留 world，full-reset 同时重置 context+world；
- 合并 SWE-bench resolved 标签时，必须精确匹配 `instance_id + condition + attempt`；缺少 condition 或 attempt 的结果不得宽松合并；
- `decision.md` 必须说明实验是否满足 adversarial_review 中的 minimum evidence；
- 10 题 pilot 只能作为 infrastructure pilot；若要支持 Go，至少需要 signal pilot（20–30 题）或等价 minimum evidence；
- WSD 不能只报告 hash drift；必须区分 WSD-basic、source/residual drift、harmful drift 或说明为何暂不可计算；
- CR 如果依赖 `first_step_error`，必须说明 judge / 人工校验方式；缺失 step-level evidence 时不得把 CR 当核心指标；
- 如果 pilot 不支持核心效应，应优先 Narrow / Hold，而不是继续扩大 claims；
- 如果实验暴露新的 baseline 或 failure mode，应回到 Phase 2 扩库并更新 related work。

#### Phase 4 — Paper-ready Audit（投稿前审计）

Phase 4 用于检查是否接近论文初稿，而不是继续堆论文数量。必须确认：

- Related Work 覆盖直接竞品、相邻 benchmark、方法 baseline、failure taxonomy、survey；
- 最危险 5–8 篇都有正面比较，不只是一句 limitation；
- claims、metrics、baseline、dataset、pilot/full experiment 证据完全一致；
- `decision.md` 的 Go 不是只基于 Phase 1 的 15+8 下限；
- 仍未解决的威胁写入 limitation / future work，而不是藏在文件外。

**关键约束**：

- `experiment_plan.md` **不得**早于 `gap_analysis.md` 和 `adversarial_review.md`
- `decision.md` **不得**早于 `file_consistency_check.md`
- `gap_analysis` 收窄后，**必须同步** `topic_brief.md`
- 重调研、扩库或 Phase 回退时：**保留**旧文件，增量审计更新，不整库删除

### 新开课题

1. 创建 `topics/<topic>/`
2. 从 `templates/` 复制各模板并重命名
3. 按 workflow 顺序填写

------

## 八、真实性核验要求

所有论文、benchmark、数据集、代码库、会议接收信息都必须经过核验，写入 `paper_table.csv`。

### paper_table.csv 必填列

- title, year, venue, category, type
- problem, benchmark, metrics, limitation
- relevance_to_<topic>, relevance_score
- url, authors, source_type, verified_status, verification_note
- **core_read**（yes / no）

### source_type 只能是

- arXiv
- OpenReview
- ACL Anthology
- PMLR
- ACM / IEEE / Springer official page
- official project page
- author homepage
- GitHub official repository
- uncertain

### verified_status 只能是

- verified
- uncertain
- remove

### 判定规则

1. 如果找不到可靠来源，必须标记为 uncertain。
2. 如果标题、作者、年份、venue 任一关键字段无法核验，不能标记 verified。
3. 如果论文看起来合理但无法找到来源，必须标记 uncertain 或 remove。
4. 不能为了保持方向成立而强行保留论文。
5. arXiv 论文不能随意写成顶会接收论文。
6. under review 不能写成 accepted。
7. withdrawn 论文必须注明 withdrawn。
8. 如果某篇论文是 gap_analysis 的核心论据，必须有可靠来源，否则不能作为核心论据。
9. 如果一个事实只来自模型记忆而没有来源，必须降级为 uncertain。
10. 如果检索结果之间互相矛盾，优先使用官方论文页、会议 proceedings、arXiv/OpenReview/PMLR/ACL Anthology，并在 verification_note 中写明冲突。

### core_read 规则

- `core_read=yes` 的论文：**必须**有 `paper_cards/<slug>.md`
- Phase 1 通常选 8 篇：最直接威胁 + 实验底座 + 方法/benchmark 边界
- Phase 2 通常扩到 12–20 篇：新增最危险竞品、强 baseline、survey / taxonomy、同期 work、可复现实验底座
- uncertain / remove 论文：**不得**设 core_read=yes

------

## 九、Adversarial Review 要求

在判断任何课题是否值得继续前，必须先站在顶会审稿人角度攻击该课题。

**产出文件**：`topics/<topic>/adversarial_review.md`（模板：`templates/adversarial_review_template.md`）。**不得**只嵌入 `gap_analysis.md`。

必须回答：

1. 这个问题是否已经被已有论文覆盖？
2. 这个课题是否只是已有工作的换名？
3. 这个方法是否只是 prompt / retry / checkpoint / workflow 工程组合？
4. benchmark 是否太小、太人工、太依赖构造？
5. 指标是否只是已有指标改名？
6. baseline 是否足够强？
7. 是否能跨模型、跨任务、跨环境验证？
8. 如果投 ICLR / NeurIPS / ACL / EMNLP，最可能被拒的理由是什么？

输出必须包含：

- strongest rejection reason
- most dangerous related work
- novelty risk（高 / 中高 / 中 / 低）
- evaluation risk
- engineering-only risk
- minimum evidence needed to continue

若无法有效回应核心拒稿理由 → 建议 Hold、Narrow 或 No-Go（写入 `decision.md`）。

------

## 十、课题收窄与重命名规则

如果调研发现原始课题过宽、已有工作覆盖过多、术语与已有论文重叠，必须主动提出收窄或重命名。

**产出位置**：`gap_analysis.md` §0 收窄记录 + 同步更新 `topic_brief.md`（只保留当前版本）。

必须检查：

1. 原始课题名是否与已有论文术语冲突？
2. 原始问题定义是否太宽？
3. 是否需要限定场景？
4. 是否需要限定状态类型？
5. 是否需要限定 benchmark？
6. 是否需要从 general agent 缩小到 software agent / web agent / memory agent？
7. 是否需要从 method paper 改成 benchmark paper？
8. 是否需要从系统贡献改成问题贡献？

收窄记录格式：

- 原始题目
- 风险
- 建议新题目
- 新题目的一句话定义
- 删除哪些过宽内容
- 保留哪些核心内容
- 下一步实验边界

如果 gap_analysis 已经收窄课题，**必须**同步更新 topic_brief.md、related_work.md 中的 scope 描述，并在下一轮 `file_consistency_check.md` 中验证。

------

## 十一、Research Repo 文件一致性要求

每次完成调研、审计、gap analysis 或实验计划后，必须运行一致性检查。

**产出文件**：`topics/<topic>/file_consistency_check.md`（模板：`templates/file_consistency_check_template.md`）。**不得**只嵌入 `gap_analysis.md` 或 `decision.md`。

检查范围：

- topic_brief.md
- paper_table.csv
- related_work.md
- paper_cards/
- gap_analysis.md
- adversarial_review.md
- experiment_plan.md
- decision.md
- file_consistency_check.md（本文件自身）

### 一致性规则

1. 如果 paper_table 中某论文被标记 uncertain，则 gap_analysis 不能把它作为核心论据。
2. 如果 gap_analysis 收窄课题，topic_brief 必须同步更新。
3. 如果 gap_analysis 认为当前还不能实验，experiment_plan.md 不应强行填写 full 计划。
4. 如果 experiment_plan.md 已经写出 MVP，decision.md 必须说明当前是否进入 pilot experiment。
5. 如果 related_work 中引用了论文，paper_table 必须有对应条目。
6. 如果某论文 core_read=yes，则必须有对应 paper_card。
7. 如果某论文被标记 remove，related_work 和 gap_analysis 必须删除或降级其论据地位。
8. 如果 venue、year、title 被修正，所有相关文件必须同步修正。
9. 如果 topic_brief、gap_analysis、experiment_plan 对课题名称或范围的描述不一致，必须优先以最新 gap_analysis 为准并同步更新其他文件。
10. 如果 decision.md 给出 Go，但 experiment_plan.md 没有明确 data、baseline、指标和 MVP，则 decision 必须降级为 Narrow 或 Hold。

### file_consistency_check.md 必须包含

1. 文件状态总表（consistent / outdated / risky）
2. 上述 10 条规则逐项 Pass/Fail
3. 跨文件关键字段对齐表（课题名称、核心 claim、MVP benchmark、Decision）
4. 发现的问题与待办
5. 审计结论

------

## 十二、Go / No-Go 决策规则

任何课题进入实验前，必须通过以下检查。

**产出文件**：`topics/<topic>/decision.md`（模板：`templates/decision_template.md`）。

### Pilot-ready / Pilot Go 条件（Phase 1 / 3）

Phase 1 满足第 1–12 条但尚未跑 pilot 时，最高只能标 **Narrow**，含义是“可进入 pilot / 最小实验”。Phase 3 跑完 pilot 或取得 minimum evidence，并满足第 13 条后，才可以标 **Go**：

1. 至少 8 篇核心论文已核验（verified）。
2. 至少 5 篇核心论文已有 paper card（通常 8/8）。
3. gap_analysis 明确指出已有工作覆盖了什么、没有覆盖什么。
4. adversarial_review 已完成，且 novelty / evaluation 风险有预备回应。
5. file_consistency_check 通过（无 outdated / risky）。
6. 最危险的 3 篇 related work 已经被正面比较。
7. 课题已经收窄到一个可实验场景。
8. 有明确 benchmark 或可构造数据。
9. 有 baseline。
10. 有至少 3 个可量化指标。
11. 有最小实验方案（experiment_plan MVP 段）。
12. uncertain 论文没有被当作核心论据。
13. **pilot 或 minimum evidence 已满足** adversarial_review 中的阈值（若尚未跑 pilot → 最高只能 **Narrow**，不能 Go）。

### Paper-ready Go 条件（Phase 2 / 4）

如果目标是投稿级调研或论文初稿，不能只满足 Pilot Go。还必须满足：

1. `paper_table.csv` 通常达到 40–60+ 篇 verified / uncertain 分明；少于 40 篇必须说明检索边界。
2. `core_read=yes` 通常达到 12–20 篇，且全部有 paper card。
3. 至少覆盖 direct competitors、benchmarks、methods/baselines、failure taxonomy、survey/position work、同期 arXiv 六类中的相关类别。
4. 最危险 5–8 篇 related work 已经正面比较，不能只比较 3 篇。
5. `related_work.md` 已重写为论文级叙事：按问题簇组织，说明本案相对每一簇的增量。
6. Phase 3 的 pilot / minimum evidence 已支持核心 claim，或已明确降级 claim。
7. `file_consistency_check.md` 明确标注当前为 Phase 4，并通过 paper-ready audit。

### No-Go 条件

出现以下情况，应暂停或换方向：

1. 核心问题已被已有论文完整覆盖。
2. 只能通过换术语制造新颖性。
3. 没有可复现实验。
4. 没有强 baseline。
5. 方法只是工程拼装。
6. benchmark 完全人工且缺乏真实任务支撑。
7. 指标无法说服审稿人。
8. 主要论据依赖 uncertain 论文。

### 决策输出格式（decision.md）

- **Decision**: Go / Narrow / Hold / No-Go
- **Reason**（含 Go / No-Go 条件检查表）
- **Minimum next step**
- **What evidence would change this decision**
- **评分表**（§三 10 分制，可选）

说明：

- **Go**：可以进入 pilot / 最小实验。
- **Narrow**：方向可做，已收窄或待 pilot；可写 MVP plan，不可标 full Go。
- **Hold**：暂缓，先补文献核验、gap 或 pilot 数据。
- **No-Go**：不建议继续投入。

------

## 十三、最终使用原则

这个 skill 不只用于生成调研结果，还用于**审计**调研结果。

使用时必须遵守：

1. 先核验，再判断（`paper_table.csv`）。
2. 先攻击，再支持（`adversarial_review.md`）。
3. 先收窄，再实验（`gap_analysis.md` → `topic_brief.md`）。
4. 先形成 benchmark / baseline / metric，再讨论方法创新。
5. 不把 uncertain 论文当核心证据。
6. 不为了保留课题而降低判断标准。
7. 不把工程集成包装成研究贡献。
8. 每轮调研结束必须更新 `file_consistency_check.md` 和 `decision.md`。
9. 所有结论以 repo 文件为准；对话摘要不得与文件矛盾。
