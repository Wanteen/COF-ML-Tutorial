# COF-ML-Tutorial

> 面向 **COF / 计算材料方向新入学研究生** 的机器学习入门教程。  
> **GitHub 阅读 + Google Colab 运行 + COF 数据实践。**

本教程不是机器学习专业课程，也不要求学生一开始就理解复杂模型。核心目标是：先建立最基本的数据与模型概念，再逐步连接到 COF 结构、描述符、性质预测和科研中的验证问题。

## 课程定位

这套教程适合：

- 刚进入 COF / 计算材料课题组的研究生；
- 没有系统学习过机器学习；
- 能看懂基础 Python 代码，但不要求熟练编程；
- 已具备基本 COF、化学键、晶胞、周期性结构、孔道/吸附等物理化学知识。

### 前置要求

**Python：** 能看懂变量、list/dict、函数调用、`for` 循环、`import`、DataFrame 等基本代码结构即可。不会独立写完整程序也可以。

**COF / 材料基础：** 理解原子、分子、化学键、晶胞、周期性边界、孔道、密度等基本概念。教程不会重新讲有机化学或晶体学基础。

**机器学习：** 不要求任何前置知识。

## 学习层级

本教程分为三层：

### Level A — 必须掌握

01–05 为主线内容。完成后应该能独立理解并运行一个简单的 COF 机器学习 workflow。

### Level B — 建议了解

06 图神经网络（GNN）。重点理解“原子图”和“message passing”是什么，不要求从头实现复杂网络。

### Supplementary — 补充阅读

07 机器学习势（MLFF）。只用于建立背景认识，不作为本教程核心考核内容，不要求掌握训练 CHGNet / MACE / DeepMD。

## Course map

| Chapter | Level | Topic | 主要问题 | GitHub | Colab |
|---|---|---|---|---|---|
| 00 | 导航 | Course map | 课程怎么学？需要什么基础？ | [View](notebooks/00_course_map.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/00_course_map.ipynb) |
| 01 | A | ML 最小基础 | 数据、feature、target、train/test 是什么？ | [View](notebooks/01_python_ml_basics.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/01_python_ml_basics.ipynb) |
| 02 | A | 周期结构与 pymatgen | CIF、晶胞参数、分数坐标是什么？ | [View](notebooks/02_pymatgen_structure.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/02_pymatgen_structure.ipynb) |
| 03 | A | Descriptors | 如何把材料结构变成模型能读取的数字？ | [View](notebooks/03_material_descriptors.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/03_material_descriptors.ipynb) |
| 04 | A | Real COF data | 真实数据库为什么不能拿来就训练？ | [View](notebooks/04_real_cof_dataset.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/04_real_cof_dataset.ipynb) |
| 05 | A | COF prediction | 如何训练、评价并避免虚假高精度？ | [View](notebooks/05_cof_property_prediction.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/05_cof_property_prediction.ipynb) |
| 06 | B | GNN | 为什么可以直接从原子图学习？ | [View](notebooks/06_gnn_for_materials.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/06_gnn_for_materials.ipynb) |
| 07 | Supplement | MLFF | 为什么需要机器学习势？它和 DFT/MD 有什么关系？ | [View](notebooks/07_mlff_chgnet.ipynb) | [Open](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/07_mlff_chgnet.ipynb) |

## 推荐学习顺序

建议先完成 00–05，再决定是否继续 06。07 只作为补充阅读。

- Week 1：00–01，理解数据、feature、target、模型、训练集和测试集。
- Week 2：02，理解晶胞、周期性、CIF 和 pymatgen。
- Week 3：03，理解“材料表示（representation）”与描述符。
- Week 4：04，练习真实 COF 数据审计。
- Week 5：05，完成完整 baseline 和可靠验证。
- Week 6（可选）：06，了解 GNN。
- Supplementary：07，了解 MLFF 背景。

## 一个贯穿课程的核心问题

机器学习本质上需要把材料问题转化为：

`材料样本 → 可计算输入 X → 模型 → 预测 y → 与真实 y 比较`

对于 COF，真正困难的通常不是调用某个算法，而是：

- X 是否包含孔径、孔隙率、化学组成、官能团、拓扑、层间堆积等重要信息；
- y 是否来自一致的实验/计算条件；
- train/test 是否真的代表“已知材料”和“未知材料”；
- 模型分数是否被重复结构或同家族结构泄漏人为抬高。

## 术语说明

教程第一次出现重要术语时会同时给出中文解释。例如：

- feature：特征，模型输入的变量；
- target / label：目标值 / 标签，要预测的性质；
- model：模型，从输入到输出的数学映射；
- training set：训练集，用于拟合模型；
- test set：测试集，只用于评价未见数据上的表现；
- descriptor：描述符，把材料结构/组成转化为数值特征；
- data leakage：数据泄漏，测试信息以不合理方式进入训练过程。

不要求第一次看到术语就记住；课程会在后续章节重复使用。

## COF 为什么需要单独讲？

COF 不只是“一个化学式”。不同任务可能依赖：

- 晶胞参数 `a, b, c, α, β, γ`；
- pore size / limiting pore diameter；
- surface area / void fraction；
- linker / node / linkage / topology；
- functional group；
- 2D stacking / interlayer distance / slip；
- framework flexibility；
- guest loading、温度、压力、溶剂和水合环境。

因此教程强调：**先理解材料问题，再决定使用什么 feature 和 model。**

## 数据

真实 COF 数据部分使用 [Wanteen/CURATED-COFs](https://github.com/Wanteen/CURATED-COFs)。

`data/cof_demo.csv` 仅用于教学，其中 `CO2_uptake_demo` 为人工构造 target，不能用于科研结论。

## 关于 07：机器学习势（MLFF）

这一章是补充内容。学生只需要知道：

- 经典力场速度快，但形式和参数通常是预先规定的；
- DFT/AIMD 更接近电子结构层面的描述，但计算昂贵；
- MLFF 尝试用 DFT 数据学习势能面，以更低成本预测 energy / force，并用于结构优化或 MD；
- 预训练 MLFF 在新 COF 上必须验证适用性。

**不要求新生掌握 MLFF 训练、主动学习、微调或生产 MD。**

## 完成 00–05 后的最低目标

学生应该能解释：

1. 一行数据和一列数据在材料 ML 中分别代表什么；
2. feature 与 target 的区别；
3. 为什么需要 train/test split；
4. MAE、RMSE、R² 的基本意义；
5. CIF 如何表示晶胞和原子坐标；
6. 为什么 COF 的 `a` 和 `b` 不一定相等；
7. descriptor 为什么是“材料 → 数字”的桥梁；
8. 为什么真实数据要检查缺失、重复和单位；
9. random split 为什么可能高估同系列 COF 的泛化能力；
10. 为什么模型能运行不等于科研结论可信。

## 外部资源

- [Machine Learning for Materials](https://aronwalsh.github.io/MLforMaterials/)
- [pymatgen](https://pymatgen.org/)
- [matminer](https://hackingmaterials.lbl.gov/matminer/)
- [JARVIS notebooks](https://github.com/atomgptlab/jarvis-tools-notebooks)
- [MatGL](https://matgl.ai/)
- [CHGNet](https://github.com/CederGroupHub/chgnet)
- [Matbench](https://github.com/materialsproject/matbench)

## Environment

推荐直接使用 Google Colab。统一入口：

[Open course start page in Colab](https://colab.research.google.com/github/Wanteen/COF-ML-Tutorial/blob/main/notebooks/00_start_here_colab.ipynb)

本地运行：

```bash
pip install -r requirements.txt
```

## License

MIT
