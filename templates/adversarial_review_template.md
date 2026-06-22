# Adversarial Review: {{topic_name}}

> **目的**：站在顶会审稿人角度攻击课题，判断会不会被拒。  
> **与 gap_analysis 的区别**：gap 找空白；adversarial 攻击空白是否站得住。  
> **审计日期**：

---

## 1. 八问自检

| # | 攻击问题 | 回应强度 | 回应要点 |
|---|----------|----------|----------|
| 1 | 这个问题是否已经被已有论文覆盖？ | | |
| 2 | 这个课题是否只是已有工作的换名？ | | |
| 3 | 这个方法是否只是 prompt/retry/checkpoint 工程组合？ | | |
| 4 | benchmark 是否太小、太人工、太依赖构造？ | | |
| 5 | 指标是否只是已有指标改名？ | | |
| 6 | baseline 是否足够强？ | | |
| 7 | 是否能跨模型、跨任务、跨环境验证？ | | |
| 8 | 投 ICLR/NeurIPS/ACL/EMNLP 最可能被拒的理由？ | | |

---

## 2. 必填输出

| 字段 | 内容 |
|------|------|
| **strongest rejection reason** | |
| **most dangerous related work** | |
| **novelty risk** | 高 / 中高 / 中 / 低 |
| **evaluation risk** | |
| **engineering-only risk** | |
| **minimum evidence needed to continue** | |

---

## 3. 攻击表（按强度）

| 攻击 | 强度 | 预备回应 |
|------|------|----------|

---

## 4. 攻击结论

（攻击是否部分/全部成立？若无法回应核心拒稿理由 → 建议 Hold / No-Go / 收窄）

---

## 5. 与 decision 的联动

| 若… | 建议 decision |
|-----|----------------|
| 攻击全部成立 | No-Go |
| 部分成立，可收窄 | Narrow |
| 需补证据 | Hold |
| 攻击可回应且有 pilot 路径 | Go（待证据） |
