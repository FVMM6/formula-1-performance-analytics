# Formula 1 Performance Analytics

Data analysis project on Formula 1 race performance using Python and Jupyter Notebook.

## Project Idea

The project studies how Formula 1 race results are related to starting grid position, constructor, driver, season, and circuit.

Main analysis direction:

- descriptive statistics for race result fields;
- relationship between grid position and final position;
- constructor and driver performance comparisons;
- position gains and podium finishes;
- hypothesis testing across seasons and constructors.

## Dataset

Planned dataset: Formula 1 Dataset (1950-2023) [Cleaned] from Kaggle:

https://www.kaggle.com/datasets/suletanmay/formula-1-dataset-1950-2023-cleaned

Download the dataset manually from Kaggle and put the extracted CSV files into `data/raw/`.

The dataset itself is not stored in this repository because CSV/ZIP data files can be large and are ignored by `.gitignore`.

Expected files may include:

- `results.csv` or `cleaned_results.csv`
- `races.csv` or `cleaned_races.csv`
- `drivers.csv` or `cleaned_drivers.csv`
- `constructors.csv` or `cleaned_constructors.csv`
- `circuits.csv` or `cleaned_circuits.csv`
- `qualifying.csv` or `cleaned_qualifying.csv`

## Repository Structure

```text
formula-1-performance-analytics/
├── data/
│   ├── raw/              # downloaded Kaggle CSV files
│   └── processed/        # optional cleaned/merged outputs
├── notebooks/            # Jupyter notebooks
├── reports/
│   └── figures/          # exported plots, if needed
├── .gitignore
├── README.md
└── requirements.txt
```

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the notebook:

```bash
jupyter notebook notebooks/formula_1_project.ipynb
```

## Working With Google Colab

Google Colab is the easiest option if Jupyter Notebook is not installed locally.

Recommended workflow:

1. Upload `notebooks/formula_1_project.ipynb` to Google Drive.
2. Open it with Google Colab.
3. Upload the dataset CSV files into the Colab session or mount Google Drive.
4. Make sure the notebook can find files in a `data/raw/` folder.
5. Download the finished notebook and commit it back to GitHub.

Important: Colab runtime files disappear after the session ends, so keep the dataset in Google Drive or download it again when needed.

## Working With PyCharm

PyCharm Professional supports Jupyter notebooks directly.

If you use PyCharm Community, it is usually better to use Google Colab or run Jupyter Notebook in the browser.

## Hypotheses

### Hypothesis 1

Starting grid position is more strongly correlated with final race position in modern Formula 1 than in older eras.

### Hypothesis 2

Top constructors do not only score more points; they also have a higher podium rate and better average position gain.

## Collaboration

Suggested teamwork:

- one person works on data loading, cleaning, and transformations;
- one person works on plots, hypotheses, and written explanations;
- commit changes often with clear messages;
- before editing the notebook, pull the latest version from GitHub.
