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


## Hypotheses

### Hypothesis 1

Starting grid position is more strongly correlated with final race position in modern Formula 1 than in older eras.

### Hypothesis 2

Top constructors do not only score more points; they also have a higher podium rate and better average position gain.


