# COF-ML-Tutorial

<p align="center"><b>从真实 COF 结构和公开数据出发，学习机器学习、性质预测与材料筛选。</b><br><b>Machine learning for COFs: from first models to real structures and screening.</b></p>

<p align="center"><b>复旦大学高分子科学系 · 郭佳课题组</b><br>Guo Group, Department of Macromolecular Science, Fudan University<br><sub>教程开发：Wanteen · Tutorial developed by Wanteen</sub></p>

<p align="center"><a href="README.md">中文</a> · <a href="README.en.md">English</a> · <a href="https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/00_start_here_colab.ipynb">Open in Colab</a></p>

面向 COF / 计算材料方向新生的双语机器学习教程。课程强调阶段性完成：先快速完成第一次回归和分类，再逐步学习结构、描述符、数据清洗、多模型训练、验证、解释和真实 COF 工作流。

## COF 背景

[![COF 背景知识总览](assets/cof_background.jpg)](assets/cof_background.jpg)

COF 是由有机构筑单元通过共价键形成的晶态多孔网络。连接化学、拓扑、孔结构和层间堆积会共同影响吸附、传输和电子性质。

## 学习路线

`Python/data → first regression & classification → CIF → descriptors → cleaning/feature engineering → multiple models → validation/tuning → feature importance/SHAP → real COF case study → CIF-to-ML → screening → GNN/MLFF`

## 课程目录

| Chapter | Topic | 核心内容 |
|---|---|---|
| 00 | Course map | 课程路线与完成标准 |
| 01 | Python & data basics | DataFrame、X/y、基础数据操作 |
| 02 | First ML | 第一次回归 + 分类，建立成就感 |
| 03 | COF structure & CIF | 晶胞、PBC、pymatgen、结构 QC |
| 04 | COF descriptors | composition / crystal / pore / learned features |
| 05 | Data preparation | 清洗、特征构造、选择、scaling |
| 06 | Model comparison | 多种回归与分类模型 |
| 07 | Validation & tuning | CV、overfitting、leakage、调参 |
| 08 | Interpretation | correlation、permutation、SHAP |
| 09 | Real COF case study | 真实 CO₂ adsorption 综合项目 |
| 10 | CIF → ML | 真实 CIF 自动构建 feature table |
| 11 | High-throughput screening | surrogate、ranking、适用域、验证 |
| 12 | GNN | atomic graph 与 learned representation |
| 13 | MLFF | 机器学习势与原子模拟 |

### 课程分层
- **00–02 快速入门**：尽快完成第一次机器学习。
- **03–08 核心方法**：把 ML 做正确、做可解释。
- **09–11 COF 项目实践**：真实 adsorption 数据、真实 CIF、高通量筛选。
- **12–13 进阶专题**：GNN 与 MLFF。

## 公开 COF 数据
- [COFSpace](https://github.com/gokhanonderaksu/COFSpace)：06–09 使用其 CoRE-COF CO₂ 1 bar 数据，并在 11 使用大型 hypothetical-COF predictions。
- [CURATED-COFs](https://github.com/danieleongari/CURATED-COFs) / [Wanteen mirror](https://github.com/Wanteen/CURATED-COFs)：10 用于真实 CIF 解析。
- [CoRE-COF Database](https://github.com/core-cof/CoRE-COF-Database)：实验 COF 结构集合。
- [SupportingInformation_CO2captureHTS_2024](https://github.com/jsdvos/SupportingInformation_CO2captureHTS_2024)：CO₂ capture HTS、固定 train/test、SHAP 与 screening workflow。

`data/cof_demo.csv` 只用于 01–02 教学演示，其中 `CO2_uptake_demo` 为人工 target，不能用于科研结论。

## 作者与联系
**教程开发:** [Wanteen](https://github.com/Wanteen)  
**所属:** 复旦大学高分子科学系 · 郭佳课题组  
wantingshieh@gmail.com · wantingshieh@outlook.com

## License
[MIT License](LICENSE)
