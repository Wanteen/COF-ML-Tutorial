# COF-ML-Tutorial 教学审计 / Teaching Audit

审计日期：2026-09

## 结论

仓库原有 00–07 已覆盖 Python/ML 基础、pymatgen、描述符、真实数据库、baseline、GNN 与 MLFF，但主线存在一个关键断点：学生没有真正完成过一次“真实 COF CIF → 结构解析 → 特征表 → target 对齐 → ML → 筛选”的闭环。

原有主线更接近：

```text
02 了解 CIF
03 用手工表格/组成描述符理解 feature
04 查看真实 COF metadata
05 用人工 CO2_uptake_demo 训练模型
```

因此，学生可能会理解 sklearn API，却仍不清楚真实结构数据如何进入机器学习表格，也不清楚训练好的模型如何用于材料筛选。

## 本轮修改

### 新增 05B：Real COF CIF → ML

目标：第一次真正从 CURATED-COFs 的 CIF 出发建立机器学习数据管线。

新增内容：

- 批量下载/解析真实 COF CIF；
- 从 pymatgen `Structure` 提取晶格、组成、体积、密度等基础结构信息；
- 显式区分“CIF 可直接得到的结构描述符”和“需要 Zeo++ / PoreBlazer 等额外计算的 pore descriptors”；
- 建立 `COF_ID` 主键；
- 将 feature table 与 target table 拆开再通过 `COF_ID` 合并；
- 讨论 target leakage / shortcut learning；
- 完成 train/test、Random Forest、parity plot 和 feature importance；
- 明确说明本章 target 为真实结构性质，只用于学习数据管线，不冒充实验 CO2 吸附数据。

### 新增 05C：High-throughput screening

目标：回答“训练模型以后材料 ML 用来做什么”。

路线借鉴：

- `jsdvos/SupportingInformation_CO2captureHTS_2024`
- `CURATED-COFs`
- `CoRE-COF Database`
- `mofdscribe`

新增内容：

- reference subset → surrogate model → candidate library；
- 训练后对未计算 COF 进行预测和排序；
- applicability-domain 的最基础检查；
- feature importance → SHAP 的升级路线；
- top candidates 必须回到 CIF 并进行高精度模拟/实验验证；
- 建议真实项目目录：`cifs/`, `features/`, `targets/`, `splits/`, `models/`, `predictions/`。

## 对现有章节的审计

| Chapter | 当前作用 | 主要不足 | 处理 |
|---|---|---|---|
| 00 | 课程地图 | 原路线把 01–05 称为完整 workflow | 需要把 05B/05C 纳入 Level A |
| 01 | ML 基础 | 合理 | 保留 |
| 02 | CIF / pymatgen | 真实 CIF 只停留在示例代码 | 由 05B 承接批量真实 CIF |
| 03 | descriptors | 主要是手工表格和 composition descriptor | 由 05B 增加真正 structure-derived descriptors，并强调 pore descriptors 需专门软件 |
| 04 | real COF data | 只做 metadata / missing-value audit | 保留，作为数据质量与 provenance 章节 |
| 05 | baseline prediction | target 为人工构造，和真实 CIF 未连接 | 保留其 split / leakage 教学价值，并由 05B/05C 完成真实结构闭环 |
| 06 | GNN | 与 descriptor-based ML 之间跳跃较大 | 05B/05C 现在提供 representation → screening 的过渡 |
| 07 | MLFF | 属于进阶补充 | 保留 |

## 后续优先级

下一轮最值得补的不是更多模型，而是数据层：

1. 加入一个可公开再分发的小型真实 COF property benchmark；
2. 为真实 CIF 批量计算 PLD/LCD/ASA/void fraction，并提供可追溯脚本；
3. 增加 structure/family/topology-aware split；
4. 增加 SHAP 与 uncertainty / ensemble disagreement；
5. 为 05B/05C 增加固定版本的小型数据快照，减少外部仓库变化对教学运行的影响；
6. 添加自动 notebook smoke test，至少验证 import、数据下载和主要代码单元。

## 新的 Level A 完成标准

完成 Level A 后，学生应该能够解释并执行：

```text
真实 CIF
→ 结构解析与质量检查
→ descriptor 构建
→ target 定义
→ COF_ID 对齐
→ split
→ baseline model
→ validation
→ candidate screening
→ applicability domain
→ 回到 CIF / simulation / experiment 验证
```

只有做到这一点，才能称为完成了一个基础 COF machine-learning workflow。
