# Agent / AI 顶会论文选题调研 Skill

## 目标

帮助我在 AI / LLM Agent 领域**发现**有潜力的研究创新点，并**快速判断**它是否值得继续投入。

本 skill 的定位是 **Research Scout**，不是论文写作助手。它服务的是：

```text
广搜发现 → 提出候选 → 选定一个方向 → 针对性深研 → 最小实验验证
```

重点不是泛泛总结论文，而是识别可泛化、可复现、可实验验证的失败模式、机制问题、表示问题、评估问题或系统问题。

最终必须回答：

1. 有哪些值得考虑的候选方向？
2. 选定方向后，创新点是否成立、是否只是换名、最大威胁是什么？
3. 能否用公开数据或可构造 benchmark 做 **MVP / pilot** 快速验证？
4. 我当前能力是否能在 **2–4 个月**内启动最小实验？

**不追求**：投稿级 Related Work 完整度、论文初稿审计、40–60 篇扩库。这些超出本 skill 范围。

**产出方式**：

- **发现阶段**写入 `scout/`（跨方向、多候选）
- **深研与验证阶段**写入 `topics/<topic>/`（单课题）
- 所有结论以 repo 文件为准，而非只在对话里总结。模板见 `templates/`；workflow 见根目录 `README.md`。

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

## 四、产出规范

### 4.1 发现阶段（`scout/`，跨方向）

在用户尚未选定单一课题，或需要重新发现方向时，先写 `scout/`，**不要**直接创建完整的 `topics/<topic>/` 深研文件。

| 文件 | 职责 | 模板 |
|------|------|------|
| `landscape_scan.md` | 跨方向文献地图：8 大类/sub-cluster 的覆盖与空白 | `templates/landscape_scan_template.md` |
| `discovery_paper_table.csv` | 发现阶段广搜索引，通常 30–50 篇，跨多个候选方向 | `templates/discovery_paper_table_template.csv`（无 `core_read` 列） |
| `candidates.md` | 3–7 个候选方向对比、评分、MVP 验证思路、推荐排序 | `templates/candidates_template.md` |
| `selection.md` | 用户最终选中的方向与 slug（Agent 不得替用户做最终选择） | 见 `candidates.md` §7 |

发现阶段 **不要求** `paper_cards/`。候选方向只需在 table 和 `candidates.md` 中有足够论据。

### 4.2 深研阶段（`topics/<topic>/`，单课题）

用户从 `scout/candidates.md` 选定 1 个方向后，创建 `topics/<topic>/` 并按以下顺序维护文件。**不得跳过 workflow 顺序**（见 §七）。

| 步骤 | 文件 | 职责 | 模板 |
|------|------|------|------|
| 1 | `topic_brief.md` | 当前版本课题定义（收窄后只保留一版） | `templates/topic_brief_template.md` |
| 2 | `paper_table.csv` | 针对该课题的论文索引 + 核验 | — |
| 3 | `paper_cards/` | 核心论文精读（`core_read=yes` 必须有 card） | `templates/paper_card_template.md` |
| 4 | `related_work.md` | 文献地图（按类总结，非流水账） | — |
| 5 | `gap_analysis.md` | 空白分析、换名判断、MVP 方向、收窄记录 | `templates/gap_analysis_template.md` |
| 6 | `adversarial_review.md` | 审稿人攻击：创新点是否站得住 | `templates/adversarial_review_template.md` |
| 7 | `file_consistency_check.md` | 全库一致性审计 | `templates/file_consistency_check_template.md` |
| 8 | `decision.md` | Promising / Narrow / Hold / No-Go | `templates/decision_template.md` |
| 9 | `experiment_plan.md` | MVP 实验设计（仅 decision 允许后） | `templates/experiment_plan_template.md` |
| 10 | `outputs/`、`scripts/`、`benchmarks/` | 该课题的最小验证实验产出 | 按课题自建 |

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

- **Promising / Narrow**：可写 **MVP / pilot**（明确 minimum evidence），目标是快速验证创新点
- **Hold / No-Go**：不写 experiment_plan，或只留一行说明暂停原因
- 不要求 full-scale 实验计划；本 skill 止于「快速证明值得做」

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

不要只是帮我找“有趣方向”，也不要直接跳到写论文。

本 skill 的成功标准是：

**发现阶段**

- 给出 3–7 个有论据的候选方向（`scout/candidates.md`）；
- 每个候选都能说明问题真实性、相似工作、MVP 验证思路；
- 用户能基于对比表做出选择（`scout/selection.md`）。

**深研阶段**

- 对选定方向给出清晰定义（`topic_brief.md`）；
- 说明创新点与最大威胁（`gap_analysis.md` + `adversarial_review.md`）；
- 判断不是换名、不是已被完整覆盖。

**验证阶段**

- 给出可执行的 MVP 实验（`experiment_plan.md`）；
- 有 baseline、指标、最小样本量；
- 通过 pilot / minimum evidence 判断：**这个创新点值得继续投入**。

若 MVP 不支持核心 claim，应 Hold / No-Go / 回到 `scout/` 重新发现，而不是硬写论文叙事。

------

## 七、Research Repo 结构与 Workflow

### 目录结构

```text
agent-research-scout/
├── README.md
├── skills/
│   └── paper_research_skill.md
├── templates/
├── scout/                         ← Phase 1–2：发现与候选（跨方向）
│   ├── landscape_scan.md
│   ├── discovery_paper_table.csv
│   ├── candidates.md
│   └── selection.md
├── topics/
│   └── <topic>/                   ← Phase 3–4：深研与快速验证（单课题）
│       ├── topic_brief.md
│       ├── paper_table.csv
│       ├── paper_cards/
│       ├── related_work.md
│       ├── gap_analysis.md
│       ├── adversarial_review.md
│       ├── file_consistency_check.md
│       ├── decision.md
│       └── experiment_plan.md
├── papers/
├── benchmarks/                    ← 选定课题后按需创建
├── scripts/
└── outputs/
```

### 总流程（四阶段）

```text
Phase 1  Discovery      广搜 → landscape_scan + discovery_paper_table + candidates
Phase 2  Selection      用户选定 1 个候选 → selection.md → 创建 topics/<topic>/
Phase 3  Deep Dive      针对选定方向做深研 → gap / adversarial / decision
Phase 4  Quick Proof    MVP 实验 → outputs/ → 更新 decision（值得继续 / 放弃）
```

每次执行 skill 时，必须先判断当前处于哪个 Phase，并在对应文件中写明。

| Phase | 名称 | 目标 | 最低完成标准 | 决策 |
|-------|------|------|--------------|------|
| 1 | Discovery | 在 Agent 领域内广搜，提出候选创新点 | `landscape_scan.md` + `discovery_paper_table.csv`（30–50 篇）+ `candidates.md`（3–7 个候选） | Continue / Hold |
| 2 | Selection | 从候选中选定 1 个方向 | `selection.md` 记录用户选择 + 创建 `topics/<topic>/` | Selected / Re-scan |
| 3 | Deep Dive | 验证选定方向是否真有创新点 | `paper_table.csv` ≥15 篇；`core_read=yes` 通常 8 篇；gap + adversarial + consistency + decision | Promising / Narrow / Hold / No-Go |
| 4 | Quick Proof | 用 MVP 快速证明该点值得做 | `experiment_plan.md` + `outputs/` 有 minimum evidence | **Go** / Hold / No-Go |

> **Go 的唯一含义**：创新点已通过最小实验或等价证据验证，**值得继续投入**（不等于可以投稿）。

### 用户输入三种模式

| 用户输入 | 从哪里开始 | 说明 |
|----------|------------|------|
| 无具体方向（「帮我找 Agent 课题」） | **Phase 1 Discovery** | 默认路径；必须先出候选，不可直接写 `topics/` 深研 |
| 有模糊偏好（「memory agent 相关」） | **Phase 1 Discovery**（带约束） | 扫描范围收窄，但仍应产出多个候选供比较 |
| 已有明确题目（「Dual-State Contamination in SWE agents」） | **Phase 3 Deep Dive** | 可跳过 Phase 1–2，但仍需写 `topic_brief.md` 并做撞车/换名检查；若发现已被覆盖，应建议回到 Phase 1 |

### Phase 1 — Discovery（广搜发现）

**默认起点**（当用户没有明确选定单一课题时）。

必须完成：

1. 扫描 §一 中 8 个方向（或用户指定子域），形成 `landscape_scan.md`。
2. 建立 `discovery_paper_table.csv`，通常 **30–50 篇**，verified/uncertain 分明。
3. 提出 **3–7 个候选方向**，写入 `candidates.md`；每个候选必须：
   - 有一句话定义；
   - 说明问题是否真实；
   - 指出最大威胁 work；
   - 给出 MVP 验证思路（benchmark / baseline / metric）；
   - 用 §三 评分表做横向比较。
4. 明确排除 1–3 个看似热门但不应继续的方向（已被覆盖 / 换名 / 不可验证）。

**本阶段不做**：`paper_cards/`、完整 `gap_analysis.md`、针对单题的 15+8 深研。

Phase 1 完成后，必须等待用户选择，或写入 `selection.md` 记录用户确认，再进入 Phase 3。

### Phase 2 — Selection（人工选定）

Agent **不得**替用户做最终选题。必须：

1. 在 `candidates.md` 给出推荐排序和理由；
2. 等用户确认后，写入 `scout/selection.md`；
3. 创建 `topics/<slug>/`，从 `templates/` 复制深研模板。

若用户否决全部候选，回到 Phase 1 重新扫描，而不是硬选一个。

### Phase 3 — Deep Dive（针对性深研）

针对 **已选定** 的单一方向，在 `topics/<topic>/` 完成：

```text
1. topic_brief.md
2. paper_table.csv          （≥15 篇，针对该题）
3. paper_cards/             （core_read=yes，通常 8 篇）
4. related_work.md
5. gap_analysis.md
6. adversarial_review.md
7. file_consistency_check.md
8. decision.md
9. experiment_plan.md       （Promising / Narrow 时写 MVP）
```

本阶段要回答：

- 这个方向是否只是换名？
- 最危险的 3 篇 work 是否已被正面比较？
- 能否收窄到一个可执行的 MVP？
- 是否值得进入 Phase 4 做快速验证？

Phase 3 完成后：

- **Promising / Narrow**：可以写 MVP，进入 Phase 4；
- **Hold / No-Go**：停止或回到 `scout/` 重新发现。

### Phase 4 — Quick Proof（快速验证）

目标不是论文级完整实验，而是 **minimum evidence**：

- `experiment_plan.md` 只写 MVP：最小 benchmark、baseline、指标、样本量；
- 在 `outputs/<topic>/`（及按需的 `scripts/<topic>/`）运行 pilot；
- mock/smoke 只能验证管道，不能作为创新点成立的证据；
- 根据结果更新 `decision.md`：
  - **Go**：核心效应有信号，值得继续投入；
  - **Hold**：有微弱信号，需调整 MVP 或扩样本；
  - **No-Go**：效应不成立，回到 Phase 1 或换候选。

Phase 4 不要求：大规模实验、置信区间、论文级 error analysis、40–60 篇扩库。

### 关键约束

- 没有 `scout/selection.md`，**不得**对未经选定的方向写完整 `topics/<topic>/` 深研（除非用户明确跳过 Phase 1–2）
- `experiment_plan.md` **不得**早于 `gap_analysis.md` 和 `adversarial_review.md`
- `decision.md` **不得**早于 `file_consistency_check.md`
- `gap_analysis` 收窄后，**必须同步** `topic_brief.md`
- 重调研时：**保留**旧文件，增量更新；若方向错误，回到 `scout/` 而不是在原 topic 上硬改

### 新开一轮发现

1. 在 `scout/` 写入或更新 `landscape_scan.md`、`discovery_paper_table.csv`、`candidates.md`
2. 用户选定后写 `selection.md`，创建 `topics/<topic>/`
3. 从 `templates/` 复制深研模板，进入 Phase 3

------

## 八、真实性核验要求

所有论文、benchmark、数据集、代码库、会议接收信息都必须经过核验，写入 `discovery_paper_table.csv`（Phase 1）或 `topics/<topic>/paper_table.csv`（Phase 3）。

### discovery_paper_table.csv 必填列（Phase 1）

模板：`templates/discovery_paper_table_template.csv`

- title, year, venue, category, type
- problem, benchmark, metrics, limitation
- **relevance_to_candidate**, relevance_score（说明与哪个候选方向相关）
- url, authors, source_type, verified_status, verification_note

**不设** `core_read` 列；发现阶段不要求 `paper_cards/`。

### paper_table.csv 必填列（Phase 3）

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
- **仅适用于 Phase 3 Deep Dive** 的 `topics/<topic>/paper_table.csv`；发现阶段的 `discovery_paper_table.csv` **不设** core_read
- Phase 3 通常选 8 篇：最直接威胁 + 实验底座 + 方法/benchmark 边界
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

## 十二、决策规则

**产出文件**：`topics/<topic>/decision.md`（模板：`templates/decision_template.md`）。

### Phase 3 决策（深研后，尚未跑 MVP）

满足以下**全部**条件，才可标 **Promising** 或 **Narrow**（可写 MVP，但还不是 Go）：

1. 至少 8 篇核心论文已核验（verified）。
2. 至少 5 篇核心论文已有 paper card（通常 8/8）。
3. gap_analysis 明确指出已有工作覆盖了什么、没有覆盖什么。
4. adversarial_review 已完成，且 novelty / evaluation 风险有预备回应。
5. file_consistency_check 通过（无 outdated / risky）。
6. 最危险的 3 篇 related work 已经被正面比较。
7. 课题已经收窄到一个可实验场景。
8. 有明确 benchmark 或可构造数据。
9. 有 baseline 与至少 3 个可量化指标。
10. uncertain 论文没有被当作核心论据。

- **Promising**：创新点清晰，撞车风险可控，建议进入 Phase 4。
- **Narrow**：方向可做但 claim 需收窄，或 MVP 方案仍需细化。
- **Hold**：证据不足，先补文献或重新定义问题。
- **No-Go**：已被覆盖、只是换名、或无法验证。

### Phase 4 决策（Quick Proof 后）

只有 Phase 4 完成后，才使用 **Go**：

- **Go**：MVP / pilot 提供了 minimum evidence，支持核心创新点，**值得继续投入**（扩实验、做方法、或写论文）。
- **Hold**：有微弱信号但不足以确认；可调整 MVP 后再试。
- **No-Go**：实验不支持核心 claim；应放弃该方向或回到 `scout/` 重新发现。

**Go 不意味着**可以投稿；只意味着这个创新点通过了快速验证。

### No-Go 条件（任一阶段）

1. 核心问题已被已有论文完整覆盖。
2. 只能通过换术语制造新颖性。
3. 没有可复现实验路径。
4. 没有强 baseline。
5. MVP 无法构造或成本明显超出 2–4 个月能力范围。
6. 主要论据依赖 uncertain 论文。

### 决策输出格式（decision.md）

- **Decision**: Promising / Narrow / Go / Hold / No-Go
- **Current Phase**: 3 或 4
- **Reason**（含条件检查表）
- **Minimum next step**
- **What evidence would change this decision**
- **评分表**（§三 10 分制，可选）

说明：

- **Promising / Narrow**：Phase 3 结论，可进入 Phase 4 Quick Proof。
- **Go**：仅 Phase 4 结论，表示创新点值得继续投入。
- **Hold**：暂缓，补文献、改 MVP 或重扫候选。
- **No-Go**：不建议继续投入。

------

## 十三、最终使用原则

这个 skill 用于 **发现创新点并快速验证**，也用于 **审计** 各阶段产出是否一致。

使用时必须遵守：

1. **先发现，后深研**：没有 `scout/candidates.md` 和 `selection.md`，不要直接做完整 `topics/` 深研（除非用户明确给出题目并跳过发现阶段）。
2. **先核验，再判断**（`discovery_paper_table.csv` / `paper_table.csv`）。
3. **先攻击，再支持**（`adversarial_review.md`）。
4. **先收窄，再实验**（`gap_analysis.md` → `topic_brief.md`）。
5. **先 MVP，再声称 Go**（Go 只属于 Phase 4，且只表示值得继续投入）。
6. 不把 uncertain 论文当核心证据。
7. 不为了保留课题而降低判断标准。
8. 不把工程集成包装成研究贡献。
9. 每轮调研结束必须更新对应阶段文件；Phase 3 结束时更新 `file_consistency_check.md` 和 `decision.md`。
10. 所有结论以 repo 文件为准；对话摘要不得与文件矛盾。
11. **不做投稿审计**：40–60 篇扩库、论文级 Related Work 完整性不在本 skill 范围内。
