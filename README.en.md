# COF-ML-Tutorial

A bilingual beginner course on machine learning for covalent organic frameworks, progressing from first regression/classification models to real COF data, CIF parsing, interpretation and screening.

Learning path: `Python/data → first regression & classification → CIF → descriptors → cleaning/feature engineering → multiple models → validation/tuning → interpretation → real COF case study → CIF-to-ML → screening → GNN/MLFF`.

## Course structure

| Chapter | Topic | Focus |
|---|---|---|
| 00 | Course map | learning path |
| 01 | Python & data basics | DataFrame, X/y |
| 02 | First ML | first regression + classification |
| 03 | COF structure & CIF | unit cells, PBC, pymatgen, QC |
| 04 | COF descriptors | composition, crystal, pore, learned features |
| 05 | Data preparation | cleaning, feature engineering, selection |
| 06 | Model comparison | multiple regression/classification models |
| 07 | Validation & tuning | CV, overfitting, leakage, tuning |
| 08 | Interpretation | correlation, permutation, SHAP |
| 09 | Real COF case study | real CO₂ adsorption workflow |
| 10 | CIF → ML | build feature tables from real CIFs |
| 11 | High-throughput screening | surrogate, ranking, domain checks |
| 12 | GNN | atomic graphs and learned representations |
| 13 | MLFF | machine-learned interatomic potentials |

Public data resources used include COFSpace, CURATED-COFs, CoRE-COF Database and SupportingInformation_CO2captureHTS_2024. `data/cof_demo.csv` is introductory teaching data only; `CO2_uptake_demo` is synthetic.

Tutorial developed by Wanteen, Guo Group, Department of Macromolecular Science, Fudan University.  
wantingshieh@gmail.com · wantingshieh@outlook.com

[MIT License](LICENSE)
