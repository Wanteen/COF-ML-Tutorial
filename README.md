# COF-ML-Tutorial

> 面向计算材料 / COF 方向新入学研究生的机器学习入门教程。  
> **GitHub 直接阅读 + Google Colab 运行 + COF 真实数据实践。**

本教程不以“尽快训练一个神经网络”为目标，而是建立一条可用于科研的路线：

**materials question → data → representation → baseline → validation → GNN / MLFF → scientific interpretation**

## Course map

| Chapter | Topic | 你需要掌握什么 | GitHub | Colab |
|---|---|---|---|---|
| 00 | Course map | 建立材料 ML 全局认知 | [View](notebooks/00_course_map.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/00_course_map.ipynb) |
| 01 | Python + ML | regression、split、metrics、overfitting | [View](notebooks/01_python_ml_basics.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/01_python_ml_basics.ipynb) |
| 02 | pymatgen | CIF、lattice、PBC、neighbors | [View](notebooks/02_pymatgen_structure.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/02_pymatgen_structure.ipynb) |
| 03 | Descriptors | composition / pore / chemistry / topology | [View](notebooks/03_material_descriptors.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/03_material_descriptors.ipynb) |
| 04 | Real COF data | 数据审计、缺失、重复、leakage | [View](notebooks/04_real_cof_dataset.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/04_real_cof_dataset.ipynb) |
| 05 | COF prediction | baseline、Pipeline、family-aware split | [View](notebooks/05_cof_property_prediction.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/05_cof_property_prediction.ipynb) |
| 06 | GNN | graph、message passing、cutoff | [View](notebooks/06_gnn_for_materials.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/06_gnn_for_materials.ipynb) |
| 07 | MLFF | energy/force、pretrained potential、validation | [View](notebooks/07_mlff_chgnet.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/07_mlff_chgnet.ipynb) |

## 推荐学习节奏

**Week 1 — Python & supervised learning**  
完成 00–01。重点不是语法，而是 feature/target、train/test、MAE/RMSE/R²、overfitting 和 data leakage。

**Week 2 — Materials structures**  
完成 02。能用 pymatgen 读取 CIF，并理解 periodic structure 与普通分子表格数据的区别。

**Week 3 — Representation**  
完成 03。理解为什么 composition descriptors 无法描述 COF 孔道、stacking 和 functional-group position。

**Week 4 — Real data**  
完成 04。直接分析 [Wanteen/CURATED-COFs](https://github.com/Wanteen/CURATED-COFs)，完成数据审计。

**Week 5 — Reliable prediction**  
完成 05。比较 random split 与 family-aware split，开始建立“适用域”意识。

**Week 6 — GNN**  
完成 06。理解 atomic graph 和 message passing，再运行成熟的 MatGL / ALIGNN 教程。

**Week 7–8 — MLFF**  
完成 07。理解 energy/force learning、pretrained model 的适用域和 validation，再进入 CHGNet / MACE / DeepMD。

## 为什么专门针对 COF？

通用材料 ML 教程通常以无机晶体或小型 benchmark 为主。COF 还有一些必须单独考虑的问题：

- pore size、limiting pore diameter、surface area、void fraction；
- linker / node / linkage / topology；
- functional-group identity 与位置；
- 2D COF stacking、interlayer distance、slip；
- framework flexibility；
- guest loading、hydration、temperature / pressure 等工作条件；
- 同系列 COF 高度相似导致的 train/test leakage。

因此教程坚持一个原则：**先做物理上可解释的 COF baseline，再决定是否需要更复杂的 GNN。**

## 数据

真实 COF 数据来自 [Wanteen/CURATED-COFs](https://github.com/Wanteen/CURATED-COFs)。

`data/cof_demo.csv` 仅用于教学。`CO2_uptake_demo` 是人工构造 target，**不得用于科研结论或论文数据**。

## 推荐外部教材

这些资源不是要求从头到尾全部学习，而是作为本教程对应章节的扩展阅读：

| Resource | 推荐用途 |
|---|---|
| [Machine Learning for Materials](https://aronwalsh.github.io/MLforMaterials/) | 系统理解材料 ML、representation、model 与 optimization |
| [pymatgen](https://pymatgen.org/) | 周期结构与材料数据处理 |
| [matminer](https://hackingmaterials.lbl.gov/matminer/) | composition / structure featurization |
| [JARVIS notebooks](https://github.com/atomgptlab/jarvis-tools-notebooks) | Colab 化材料 AI 示例、ALIGNN 与材料数据 |
| [MatGL tutorials](https://matgl.ai/tutorials.html) | 图神经网络和材料势的官方 notebook |
| [CHGNet](https://github.com/CederGroupHub/chgnet) | pretrained universal ML potential 入门 |
| [ALIGNN](https://github.com/usnistgov/alignn) | atomistic line-graph neural network |
| [Matbench](https://github.com/materialsproject/matbench) | benchmark 与可比较的模型评价思维 |

## 新生完成标准

完成后应能够独立回答：

1. CIF 如何变成 Python 中的周期结构对象？
2. feature、label、training/validation/test 分别是什么？
3. MAE、RMSE、R² 应该怎样解释？
4. data leakage 为什么会制造虚假的高精度？
5. random split 为什么可能高估 COF screening 能力？
6. composition、pore descriptors 与 atomic graph 各自包含什么信息？
7. 为什么 GNN 不一定自动优于合理的 descriptor baseline？
8. MLFF 的 energy / force 数据从哪里来？
9. 为什么 pretrained MLFF 在新 COF 上必须重新验证？
10. 如何设计一个能够支持科研结论的独立 test set？

## 下一阶段计划

后续适合继续增加四个进阶模块：

- `08_pore_descriptors`：从 CIF 批量构建 COF pore/geometric descriptors；
- `09_cof_screening_project`：真实 COF property/screening workflow；
- `10_gnn_training`：在标准数据上训练一个完整 GNN，再迁移到 COF；
- `11_mlff_validation`：DFT reference → force/energy test → fine-tuning / active learning。

最终结课项目建议做成：

**COF CIF → structure cleaning → descriptors → exploratory analysis → baseline → family-aware validation → candidate screening → uncertainty / applicability-domain analysis**

## Environment

Google Colab 为推荐环境。本地运行可使用：

```bash
pip install -r requirements.txt
```

## License

MIT
