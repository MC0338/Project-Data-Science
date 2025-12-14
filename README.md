# Welzijnsmonitor Data Science Project

Analyzing the student wellbeing monitor survey by AM and BIM students.

## Project Organization

```
├── data
│   ├── processed          <- The final, canonical data sets for modeling.
│   │   ├── Welzijnsmonitor2024_scaled_normalised_UTF8.csv
│   │   └── Welzijnsmonitor2025_scaled_normalised_UTF8.csv
│   └── raw                <- The original, immutable data dump.
│       ├── Welzijnsmonitor2025_prep_dataGroepen.xlsx
│       └── Welzijnsmonitor2025_prep.xlsx
├── data-analysis          <- Trained models, and model summaries.
│   └── DataAnalysis.ipynb
├── data-preprocessing
│   ├── Kolommen.py
│   ├── Mapping.py
│   └── Normalisering.py
├── docs                   <- A default mkdocs project; see www.mkdocs.org for details
├── output
│   ├── data_with_normalized_latent_variables.csv
│   ├── descriptive_statistics.csv
│   ├── latent_variable_scores.csv
│   ├── model_coefficients.csv
│   └── model_coefficients.xlsx
├── paths.py
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting
│       ├── correlation_matrix.png
│       ├── pd
│       ├── pd.png
│       ├── pd2
│       ├── pd2.png
│       ├── pd3
│       └── pd3.png
├── .gitignore              <- Remove redudant or irrelevant files/folders from git commit.
├── paths.py                <- Relative path configuration (prevent absolute path problem).
├── README.md               <- The top-level README for developers using this project.
├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
```

## Getting started

### IMPORTANT: Python 3.12 is not compatible with semopy>=2.4, so do not use 3.12

These are the steps to create the enviroment in your local machine, follow these steps in your terminal/command prompt (cmd):
- Instead, create a fresh venv (or conda env) with Python 3.10/3.11:
```
# macOS/Linux
python3.11 -m venv swm_env

# Windows
py -3.11 -m venv swm_env
```

- Activate the environment:
```
# Mac/Linux
source swm_env/bin/activate

# Windows
swm_env\Scripts\activate
```

- Run:
```
pip install -r requirements.txt
```
--------

