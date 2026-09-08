# COF-ML-Tutorial

面向新入学研究生的 **计算材料机器学习入门教程**，重点服务于 COF（Covalent Organic Framework）相关科研。

课程设计原则：

- 从材料问题出发，而不是从神经网络公式出发；
- 优先 Google Colab，减少新生环境配置负担；
- 先做可靠 baseline，再进入 GNN；
- 明确区分“模型能运行”和“科研上可信”；
- 最终使用真实 COF 数据，而不是一直停留在无机 benchmark。

## 学习路线

| Notebook | 主题 | 核心能力 |
|---|---|---|
| 00 | Course map | 建立完整认知地图 |
| 01 | Python + ML | pandas / sklearn / regression / metrics |
| 02 | pymatgen | CIF 与周期结构 |
| 03 | descriptors | composition / structure / COF-specific features |
| 04 | real COF data | 读取 CURATED-COFs，数据审计 |
| 05 | COF prediction | baseline + grouped split |
| 06 | GNN | graph representation / message passing |
| 07 | MLFF | CHGNet energy/force 基础 |

## 推荐顺序

建议 6–8 周完成，每周 1–2 个 Notebook。

### 第 1 周
- `00_course_map.ipynb`
- `01_python_ml_basics.ipynb`

### 第 2 周
- `02_pymatgen_structure.ipynb`
- 熟悉 CIF / periodic structure

### 第 3 周
- `03_material_descriptors.ipynb`

### 第 4 周
- `04_real_cof_dataset.ipynb`
- 数据清洗、缺失值、metadata 与 feature 区分

### 第 5 周
- `05_cof_property_prediction.ipynb`
- random split vs family-aware split

### 第 6 周
- `06_gnn_for_materials.ipynb`

### 第 7–8 周
- `07_mlff_chgnet.ipynb`
- 再进入 MatGL / MACE / DeepMD

## COF 数据来源

课程真实 COF 数据部分使用：

- https://github.com/Wanteen/CURATED-COFs
- `cof-frameworks.csv`
- `cifs/`

课程内的 `data/cof_demo.csv` 仅用于机器学习教学，其 target 为人工构造，**不能作为科研数据使用**。

## Google Colab

仓库上传 GitHub 后，可在每个 notebook 页面中选择 **Open in Colab**，或使用：

`https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/<notebook>.ipynb`

例如：

`https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/01_python_ml_basics.ipynb`

## 新生完成标准

完成本教程后，应能够独立解释：

1. CIF 如何表示为可计算的结构对象；
2. feature / label / train / validation / test 的区别；
3. MAE、RMSE、R²；
4. overfitting 与 data leakage；
5. random split 为什么可能高估材料模型；
6. descriptor 与 GNN representation 的区别；
7. COF 中 geometric 与 chemical features 的互补性；
8. MLFF 的 energy / force 学习对象；
9. 为什么预训练 MLFF 对新 COF 需要验证。

## 建议科研进阶

基础完成后再进入：

- pore descriptors：Zeo++ / PoreBlazer 等；
- chemical descriptors：RDKit / functional-group encoding；
- COF topology / linkage classification；
- adsorption / diffusion labels；
- GNN：MatGL / ALIGNN；
- MLFF：CHGNet / MACE / DeepMD；
- uncertainty / active learning；
- scaffold / family-aware validation。

## 参考资源

- pymatgen: https://pymatgen.org/
- matminer: https://hackingmaterials.lbl.gov/matminer/
- MatGL: https://matgl.ai/
- CHGNet: https://github.com/CederGroupHub/chgnet
- Machine Learning for Materials: https://aronwalsh.github.io/MLforMaterials/

## License

MIT
