# COF 数据入口与使用约定 / Data sources and contracts

课程仍按 `01 → 02 → 03 → 04 → 05 → 06` 学习。这里集中保存历史版本中的数据入口和扩展教材；不要求初学者一次下载所有数据库。

Follow the existing course order. These resources support the lessons; large archives are optional.

## 按任务选择数据 / Choose data by task

| 章节 / Lesson | 数据入口 / Source | 内容与使用边界 / Contract |
|---|---|---|
| 02C–04A | [COFSpace](https://github.com/gokhanonderaksu/COFSpace) · [CO₂ 1 bar table](https://raw.githubusercontent.com/gokhanonderaksu/COFSpace/main/OnlyCoRECOF%20-%20Feature%20Sets/CoRECOF%20-%20CO2%20-%201%20BAR.csv) | 本次读取 1060 行、13 列。Target 为 `CO2-1 bar (mol/kg)`；孔结构和元素比例作基线输入。此表不含材料 ID，不可假设行号能跨数据库对齐。1060 rows, 13 columns; no material-ID column. |
| 04A 拓展 | [nachatz/cof-data](https://github.com/nachatz/cof-data) · [properties](https://raw.githubusercontent.com/nachatz/cof-data/main/properties.csv) · [simple features](https://raw.githubusercontent.com/nachatz/cof-data/main/simple_features.csv) | CURATED/Materials Cloud 的派生表；`cof` ↔ `name` 合并。读取时分别为 572 个 feature 行、566 个 property 行；先检查 unmatched IDs。CO₂ target 单位列为 `mol/kg`。Derived tables: audit join coverage before fitting. |
| 02A / 04B | [CURATED-COFs 原库](https://github.com/danieleongari/CURATED-COFs) · [Wanteen mirror](https://github.com/Wanteen/CURATED-COFs) · [metadata CSV](https://raw.githubusercontent.com/Wanteen/CURATED-COFs/master/cof-frameworks.csv) | CIF、稳定 ID、结构修正记录。本次清单 874 行；下载和解析失败单独记录。CIF 来源真实不代表密度教学回归能用于吸附结论。Real CIFs and curation records; density regression is a pipeline exercise. |
| 04A / 04B | [Materials Cloud 2021.100](https://archive.materialscloud.org/record/2021.100) · [data DOI](https://doi.org/10.24435/materialscloud:z6-jn) | 原始数据记录：*Building a consistent and reproducible database for adsorption evaluation in Covalent-Organic Frameworks*. 追溯温度、模拟协议、结构版本和引用。Original record for provenance and conditions. |
| 02A / 04B | [CoRE-COF Database](https://github.com/core-cof/CoRE-COF-Database) | 实验报道 COF 的结构来源；版本、清理规则和 ID 与 CURATED 不应默认一致。Check version and identifier mapping. |
| 04C | [ReDD-COFFEE 2023](https://github.com/jsdvos/SupportingInformation_ReDD-COFFEE_2023) | hypothetical COF 化学空间、几何与 RAC 描述符；结构库规模不等于有 reference labels 的训练集规模。Structure-library size is not labelled-set size. |
| 04C | [CO₂ capture HTS 2024](https://github.com/jsdvos/SupportingInformation_CO2captureHTS_2024) · [ML inputs](https://github.com/jsdvos/SupportingInformation_CO2captureHTS_2024/tree/master/Step2_MachineLearning/data/input) · [results.csv](https://raw.githubusercontent.com/jsdvos/SupportingInformation_CO2captureHTS_2024/master/Step2_MachineLearning/data/input/results.csv) | `sep=';'`；本次 results 为 14989 行、7 列，主键 `struct`，吸附量为 `mg/g`。从原库获取 features、固定 train/test lists 与训练脚本；不重新随机划分来声称复现原论文。Use author splits for reproduction. |
| 04C | [COFSpace hypothetical predictions](https://raw.githubusercontent.com/gokhanonderaksu/COFSpace/main/68724HypoCOFs-ML_Predicted%20Data-1bar.csv) | 68724 行预测表，列名带 `- ML`。它是候选排名输入，不能充当独立 GCMC 标签验证模型。Published predictions are not reference labels. |
| 04C 拓展 | [Hypothetical COFs for methane storage](https://www.materialscloud.org/discover/cofs) | 甲烷储存候选结构与计算结果；deliverable capacity 与单点 CO₂ uptake 是不同任务。Methane deliverable capacity is a distinct target. |

表中行数来自本次下载快照，不是对未来上游版本的保证。温度若未出现在 CSV 列名中，不要凭压力或论文标题猜测；从原始记录确认后填入数据卡。

Counts describe the checked snapshot. Verify temperature and simulation protocol from the original record; pressure alone does not define the task.

## 训练前的数据卡 / Dataset card

每个实验保存一份，未知字段明确写 `unverified`，不要补猜测值。

```python
dataset_card = {
    'source_url': '...',
    'source_commit_or_doi': '...',
    'download_date': 'YYYY-MM-DD',
    'sha256': '...',
    'structure_origin': 'experimental report / hypothetical',
    'label_origin': 'simulation / experiment / ML prediction / synthetic',
    'material_key': '...',
    'gas': 'CO2',
    'temperature_K': 'unverified',
    'pressure_bar': 1,
    'target_column': 'CO2-1 bar (mol/kg)',
    'target_unit': 'mol/kg',
    'simulation_protocol': 'unverified',
    'features_and_units': {},
    'excluded_rows_and_reason': [],
    'split_method_and_indices': '...',
    'preprocessing_fit_scope': 'training fold only',
    'model_and_library_versions': {},
    'license_and_citation': 'original source',
}
```

合并时先看外连接覆盖率，再决定保留哪些行；使用 `validate='one_to_one'` 检测重复键。跨库需要显式 ID 对照及结构核验。训练前统一单位，但单位统一不等于计算协议一致。数据 DOI、Git commit 和下载文件的 SHA256 比只记录可变的 `main` 链接更利于复现。

Audit outer-join coverage, validate key uniqueness, and verify cross-database structures. Unit conversion does not harmonize simulation protocols. Preserve DOI/commit and file hashes alongside the mutable download URL.

`KCO2` 是需要额外计算的吸附亲和力相关输入。若目标是在没有相关模拟的情况下低成本预测，先排除它；若研究设置允许该计算，单独报告包含它的实验及计算成本。不同压力实验先分别验证，不能把不同条件的标签直接拼接。

Treat Henry-coefficient availability as part of the deployment setting. Compare with/without it on the same development splits and report its computational cost.

## 教材与软件 / Learning resources

| 章节 | 官方资源 | 重点 / Focus |
|---|---|---|
| 01–04 | [ML for Materials](https://aronwalsh.github.io/MLforMaterials/) | 表示、模型与材料问题 / representation and models |
| 02A / 04B | [pymatgen](https://pymatgen.org/) | 晶胞、周期邻居、CIF / periodic structures |
| 02B | [matminer](https://hackingmaterials.lbl.gov/matminer/) | 自动描述符及局限 / featurization limits |
| 03B | [Matbench](https://github.com/materialsproject/matbench) | 一致的评估与 benchmark / comparable evaluation |
| 05 | [JARVIS notebooks](https://github.com/atomgptlab/jarvis-tools-notebooks) · [ALIGNN](https://github.com/usnistgov/alignn) | 原子图与键角图 / atom and line graphs |
| 05–06 | [MatGL tutorials](https://matgl.ai/tutorials.html) | 成熟图模型工作流 / graph-model workflows |
| 06 | [CHGNet](https://github.com/CederGroupHub/chgnet) | 预训练势、独立验证 / pretrained potentials |

扩展资料按需阅读。05 保持 Level B，06 保持 Level C；恢复资料不增加主线的神经网络训练或生产 MD 考核。

Further reading is optional. GNN remains Level B and MLFF remains Level C.
