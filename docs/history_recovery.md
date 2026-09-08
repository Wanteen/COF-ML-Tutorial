# 历史内容恢复记录 / History recovery

本轮以 `0e82dbbb8b7a950429df86833d5a03f7c603bb7e` 为基线，保留当前 `01A–04C → 05 → 06` 的课程主线与 A/B/C 掌握度。

## 历史依据与落点

| 历史来源 | 恢复内容 | 当前落点 |
|---|---|---|
| [`9dc9507`](https://github.com/Wanteen/COF-ML-Tutorial/commit/9dc9507) README | ML for Materials、pymatgen、matminer、JARVIS、MatGL、CHGNet、ALIGNN、Matbench | 双语首页及 [数据资源](data_resources.md) |
| [`78c6121`](https://github.com/Wanteen/COF-ML-Tutorial/commit/78c6121) README / 05D | Materials Cloud、ReDD-COFFEE、甲烷储存数据库、第二套吸附表、HTS results | 首页、04A、04C |
| 同版本 02 / 03 | 分数坐标、PBC 邻居、术语、描述符局限与练习 | 02A / 02B |
| 同版本 05B | CIF 下载、解析失败记录、QC、ID 合并、密度管线基线 | 04B |
| 同版本 05C | 教学 surrogate、候选排序、适用域、验证队列 | 04C |
| 同版本 06 / 07 | GNN message passing、cutoff 局限、MLFF 势能面、适用域、术语和思考题 | 05 / 06 |

[`493f828`](https://github.com/Wanteen/COF-ML-Tutorial/commit/493f828) 是将这些旧章节替换为当前短版主线的主要重构点。本轮把历史内容重新编排进现有知识块，并修正旧例子中的弱点。

## 一并修正的运行与教学问题

- 03A/03B/04A 的缺失值填补进入训练折内的 Pipeline；03C 只在训练部分拟合填补器。
- 分类阈值只从训练部分计算；03A 加入均值与多数类基线。
- 英文 03A/03B/04A 补齐训练、调参与 CV 执行代码；英文标题和掌握度与当前主线对齐。
- 04A 增加空键、重复键、外连接覆盖率及 target 单位检查。
- 04B 解释密度可以直接计算、晶格参数仍编码体积，避免把教学回归包装成独立科研发现。
- 04C 恢复完整机制实验，并增加真实预测表 Top-20 导出和作者固定划分审计。模拟标签、公开预测和人工教学 target 明确区分。
- matminer 的三个教学样本使用单进程，避免 Windows 多进程开销和启动问题。

## 验证范围

2026-09-09 本地验证：

- 30 个笔记本通过 JSON/nbformat、代码语法、编号、掌握度和 notebook 内链接检查。
- 中英文 01A–05 共 24 个教学笔记本，代码单元按顺序在独立命名空间运行；下载数据用本次真实 CSV 快照缓存，CIF 和固定 split lists 实际读取上游。
- matminer 与 SHAP 中英文单元另行执行通过。绘图使用非交互后端；未进行 Colab 浏览器端运行。
- 中英文 04B 各读取 80 个 CIF，解析 80、失败 0，按 ID 合并 80 行。
- HTS 固定划分为 10000 train / 5000 test，互不重叠；results 缺少其中 9 个 train ID 和 2 个 test ID，教程显示该差异。
- 06 的可选 CHGNet 模型下载/推理未执行，只检查语法和结构；未运行 MLFF 训练或 MD。
- `git diff --check` 通过。可再次运行 `python scripts/check_notebooks.py` 检查课程结构。

这些检查验证教程执行与数据约定，不等于复现原论文的科学性能。笔记本保持清空 outputs，避免提交庞大或易过期的输出；运行时打印的数据行数、指标与失败记录可供学生核验。

English: the current course structure is retained. Historical explanations, datasets and exercises are redistributed into the existing lessons. All 24 non-MLFF teaching notebooks were executed in isolated namespaces; matminer and SHAP were checked separately. The optional CHGNet download/inference and browser-based Colab execution were not run. This is tutorial validation, not a reproduction of published scientific benchmarks.
