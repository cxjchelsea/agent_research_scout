# Paper Card: {{paper_title}}

> **card_status**：stub / metadata_verified / close_read / threat_verified
> **是否最大威胁 work**：是 / 否
> **状态规则**：只有 `close_read` / `threat_verified` 可计入核心精读；最大威胁 work 必须达到 `threat_verified`。

## 1. 基本信息

- Title:
- Year:
- Venue:
- Authors:
- Link:
- Code:
- Benchmark / Dataset:

## 2. 它研究什么问题？

## 3. 它的核心贡献是什么？

## 4. 它的方法是什么？

## 5. 它怎么实验？

### Task

### Dataset / Environment

### Baselines

### Metrics

## 6. 它发现了什么失败模式？

## 7. 它没有覆盖什么？

## 8. 它和我的课题有什么关系？

重点判断它是否涉及：

- 长链路 Agent；
- 工具使用；
- 状态管理；
- memory；
- checkpoint；
- rollback；
- recovery；
- error propagation；
- trajectory evaluation；
- failure diagnosis。

## 9. 它是否削弱我的创新性？

判断：

- 完全覆盖；
- 部分覆盖；
- 只是相关；
- 几乎无关。

## 10. 我可以从它的 limitation 里切什么？

## 11. 重要引用句

（`close_read` 必填。必须是原文关键句或可定位的方法/实验边界，不得只写总结。）

## 12. 我的判断

- 相关度：1 / 2 / 3 / 4 / 5
- 是否必须精读：是 / 否
- 是否作为 related work 核心论文：是 / 否

---

## 13. Targeted Verification（仅最大威胁 work 必填）

| Claim component | Covered by this paper? | Evidence | Implication |
|---|---|---|---|
| 核心问题定义 | yes / partial / no | | |
| proposed mechanism | yes / partial / no | | |
| benchmark / evaluation setting | yes / partial / no | | |
| baseline / comparison | yes / partial / no | | |
| utility / risk trade-off | yes / partial / no | | |

### Threat Verification Conclusion

- **是否覆盖本课题核心 claim**：yes / partial / no
- **是否覆盖 proposed mechanism**：yes / partial / no
- **是否覆盖 benchmark / evaluation setting**：yes / partial / no
- **如果扩展该方法，是否自然得到本案方法**：yes / partial / no
- **结论**：threat_verified / 仍需补证据 / 应降级为 No-Go 或 Narrow