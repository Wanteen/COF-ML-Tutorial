# COF-ML-Tutorial

<p align="center">
  <img src="https://img.shields.io/badge/Level-Beginner-2ea44f" alt="Beginner">
  <img src="https://img.shields.io/badge/Field-COF%20%2F%20Materials-blueviolet" alt="COF Materials">
  <img src="https://img.shields.io/badge/Run-Google%20Colab-F9AB00" alt="Google Colab">
  <img src="https://img.shields.io/badge/Language-Chinese%20%7C%20English-1f6feb" alt="Bilingual">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="MIT">
</p>

Short tutorials are grouped by **knowledge density and difficulty**. Tutorials inside one knowledge block use A/B/C numbering instead of consuming a full chapter number.

## Mastery levels
- 🟢 **Level A · Must master**
- 🔵 **Level B · Recommended**
- 🟣 **Level C · Awareness only**

| Course ID | Level | Topic |
|---|---|---|
| 01A | 🟢 | Python & data basics |
| 01B | 🟢 | First regression + classification |
| 02A | 🟢 | COF structure & CIF |
| 02B | 🟢 | COF descriptors |
| 02C | 🟢 | Data preparation & feature engineering |
| 03A | 🟢 | Multi-model comparison |
| 03B | 🟢 | Validation & tuning |
| 03C | 🟢 | Feature importance & interpretation |
| 04A | 🟢 | Real COF ML case study |
| 04B | 🔵 | Real CIF → ML |
| 04C | 🔵 | High-throughput screening |
| 05 | 🔵 | GNN |
| 06 | 🟣 | MLFF |

Milestones: finish 01 for your first successful ML loop; 02 for ML-ready materials data; 03 for trustworthy model comparison and interpretation; 04 for a complete real COF workflow.

Public data include COFSpace, CURATED-COFs, CoRE-COF Database and ReDD-COFFEE CO₂-capture HTS supporting information.

`data/cof_demo.csv` is used only for the low-barrier introductory tutorials. Its `CO2_uptake_demo` target is synthetic and must not be used for scientific conclusions.

## Real COF datasets

| Source | Contents | Teaching use |
|---|---|---|
| [CURATED-COFs](https://github.com/danieleongari/CURATED-COFs) + [Materials Cloud](https://archive.materialscloud.org/record/2021.100) | experimentally reported COFs, optimized structures, pore properties and CO₂/N₂ adsorption data | CIF ↔ ID ↔ property, small-data ML, carbon capture |
| [COFSpace](https://github.com/gokhanonderaksu/COFSpace) | simulated CO₂/CH₄/H₂/N₂/O₂ adsorption for 1060 CoRE COFs, structural/chemical/energy features, plus hypothetical-COF predictions | multi-gas regression, pressure dependence, feature importance, external prediction |
| [ReDD-COFFEE](https://github.com/jsdvos/SupportingInformation_ReDD-COFFEE_2023) | large hypothetical-COF space, pore geometry and RAC descriptors | representation, diversity and large chemical spaces |
| [CO₂ capture HTS](https://github.com/jsdvos/SupportingInformation_CO2captureHTS_2024) | ReDD-COFFEE features, GCMC results, fixed train/test splits, ML and SHAP | high-throughput screening, feature reduction and interpretability |
| [Hypothetical COFs for methane storage](https://www.materialscloud.org/discover/cofs) | 69,840 hypothetical 2D/3D COFs with GCMC methane deliverable capacities | large-scale screening and structure–property relationships |

04A includes the second adsorption dataset; 04B restores the CIF-to-table pipeline; 04C connects screening practice to published results and predictions. Keep dataset conditions and provenance separate.


Additional ready-to-read tables: [nachatz/cof-data](https://github.com/nachatz/cof-data) · [properties.csv](https://raw.githubusercontent.com/nachatz/cof-data/main/properties.csv) · [simple_features.csv](https://raw.githubusercontent.com/nachatz/cof-data/main/simple_features.csv)

## Further reading by chapter

| Chapter | Resource | Purpose |
|---|---|---|
| 01–04 | [Machine Learning for Materials](https://aronwalsh.github.io/MLforMaterials/) | Materials ML concepts |
| 02A / 04B | [pymatgen](https://pymatgen.org/) | Cells, CIF and PBC |
| 02B | [matminer](https://hackingmaterials.lbl.gov/matminer/) | Composition and structure descriptors |
| 05 | [JARVIS notebooks](https://github.com/atomgptlab/jarvis-tools-notebooks) | Materials graphs and notebooks |
| 05–06 | [MatGL tutorials](https://matgl.ai/tutorials.html) | Graph models and potentials |
| 06 | [CHGNet](https://github.com/CederGroupHub/chgnet) | Pretrained potentials and validation |
| 05 | [ALIGNN](https://github.com/usnistgov/alignn) | Atom and bond-angle graphs |
| 03B | [Matbench](https://github.com/materialsproject/matbench) | Comparable benchmarks |

[Data contracts and source links](docs/data_resources.md). Cite original papers/data records and record version, units, conditions and splits.

## Author
Tutorial developed by [Wanteen](https://github.com/Wanteen), Guo Group, Department of Macromolecular Science, Fudan University.  
wantingshieh@gmail.com · wantingshieh@outlook.com

## License
[MIT License](LICENSE)
