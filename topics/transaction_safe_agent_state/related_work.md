# Related Work: Transaction-Safe Agent State Boundaries

> **状态**：Phase 3 Deep Dive 初始化，占位文件。
> **文献库**：见 `paper_table.csv`。
> **要求**：正式深研时按 category 分组总结，引用论文必须在 `paper_table.csv` 中有对应行。

---

## 1. Checkpoint / Rollback / Recovery Semantics

待深研。核心威胁：ACRFence。

## 2. Tool-Boundary Security and Prompt Injection

待深研。核心工作：AgentDojo、ASB、ToolEmu、InjecAgent。

## 3. Software Agent Runtime and Agent-Computer Interfaces

待深研。核心工作：OpenHands、SWE-agent、AutoGen。

## 4. Memory Provenance and Persistent State Hygiene

待补充检索。当前 `paper_table.csv` 尚未覆盖足够 memory provenance / stale memory / memory poisoning 专门工作，Phase 3 需要扩展。

## 5. 初步空白假设

当前假设：已有工作分别覆盖 rollback attack、prompt injection / memory poisoning benchmark、agent runtime，但还没有统一处理 tool side effect、credential lifetime、memory provenance 与 branch/replay semantics 的 transaction-safe state boundary。
