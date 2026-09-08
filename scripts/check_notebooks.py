"""Check course IDs, notebook syntax, local links and obsolete notebook paths.

Run from any directory: python scripts/check_notebooks.py
This is a structural check, not a substitute for executing scientific examples.
"""
import ast
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
IDS = {
    '01A_python_ml_basics': '01A',
    '01B_first_ml_regression_classification': '01B',
    '02A_cof_structure_cif': '02A',
    '02B_cof_descriptors': '02B',
    '02C_data_preparation_feature_engineering': '02C',
    '03A_model_comparison': '03A',
    '03B_validation_tuning': '03B',
    '03C_feature_importance_interpretation': '03C',
    '04A_real_cof_ml_case_study': '04A',
    '04B_real_cif_to_ml': '04B',
    '04C_high_throughput_screening': '04C',
    '05_gnn_for_cofs': '05',
    '06_mlff': '06',
}
errors = []
notebooks = sorted(ROOT.glob('notebooks/**/*.ipynb'))
for path in notebooks:
    nb = json.loads(path.read_text(encoding='utf-8'))
    if nb.get('nbformat') != 4:
        errors.append(f'{path.name}: expected notebook format 4')
    text = '\n'.join(''.join(c['source']) for c in nb['cells'])
    if path.stem in IDS:
        heading = ''.join(nb['cells'][0]['source'])
        if not heading.startswith('# ' + IDS[path.stem] + ' '):
            errors.append(f'{path}: course ID changed')
        level = 'C' if path.stem == '06_mlff' else 'B' if path.stem in {
            '04B_real_cif_to_ml', '04C_high_throughput_screening', '05_gnn_for_cofs'
        } else 'A'
        if 'Level ' + level not in heading:
            errors.append(f'{path}: mastery level changed')
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            code = '\n'.join(line for line in ''.join(cell['source']).splitlines()
                             if not line.lstrip().startswith(('!', '%')))
            try:
                ast.parse(code)
            except SyntaxError as exc:
                errors.append(f'{path}: cell {i}: {exc}')
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if '://' in link or link.startswith('#'):
            continue
        target = unquote(link.split('#', 1)[0])
        if not (path.parent / target).exists():
            errors.append(f'{path}: missing link {link}')
    for link in re.findall(r'https://[^\s)]+\.ipynb', text):
        if '/COF-ML-Tutorial/blob/main/' in link:
            rel = link.split('/blob/main/', 1)[1]
            if not (ROOT / unquote(rel)).exists():
                errors.append(f'{path}: obsolete Colab link {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Checked {len(notebooks)} notebooks: course IDs, levels, syntax and notebook links OK.')
