# Formula 1 Performance Analytics

Data analysis project focused on Formula 1 race performance, starting grid position, constructor strength, race reliability and historical changes across different eras.

## Project overview

This project analyzes historical Formula 1 race data using Python and Jupyter Notebook. The main goal is to understand how starting grid position, constructors, circuits and racing eras are related to final race outcomes.

The analysis combines several raw relational CSV tables into one analytical dataset and includes data cleaning, feature engineering, exploratory data analysis, visualizations and hypothesis testing to identify performance patterns in Formula 1.

## Main research questions

The project focuses on the following questions:

1. Is starting grid position more strongly associated with final race position in modern Formula 1?
2. Do top constructors dominate across multiple performance metrics, not only total points?
3. Has the share of classified finishes increased over time, suggesting improved reliability in modern Formula 1?

## Dataset

The project uses a Formula 1 historical race dataset from Kaggle:

https://www.kaggle.com/datasets/jtrotman/formula-1-race-data?resource=download

The dataset is organized as a relational database exported into multiple CSV files. The main tables used in this project are:

* `results.csv`
* `races.csv`
* `drivers.csv`
* `constructors.csv`
* `circuits.csv`
* `status.csv`

The raw dataset contains hidden missing values encoded as `\N`, inconsistent data types in some columns and several tables that need to be merged before analysis. Therefore, data cleaning and preparation are important parts of this project.

The notebook automatically detects the maximum year available in the downloaded data and creates era groups based on the actual data range.

## Project structure

```text id="2m2xli"
formula-1-performance-analytics/
│
├── data/
│   ├── raw/                 # Original Kaggle CSV files, not tracked by Git
│   └── processed/           # Processed datasets generated locally
│
├── notebooks/
│   └── formula_1_project.ipynb
│
├── reports/
│   └── figures/             # Generated figures
│
├── src/
│   ├── build_dataset.py
│   ├── explore_dataset.py
│   ├── hypothesis_checks.py
│   └── inspect_data.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Tools and libraries

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## Data preparation

The project builds a main analytical dataset by merging several raw CSV tables:

```text id="o95h6u"
results
+ races
+ drivers
+ constructors
+ circuits
+ status
```

The data preparation process includes:

* loading multiple CSV files;
* detecting hidden missing values encoded as `\N`;
* replacing `\N` with proper missing values;
* selecting relevant columns;
* renaming columns to avoid conflicts after merge;
* converting numerical fields to proper data types;
* merging relational tables into one main analytical dataset;
* saving the processed dataset locally.

## Feature engineering

Several new features are created for analysis:

| Feature                | Description                                                       |
| ---------------------- | ----------------------------------------------------------------- |
| `driver_name`          | Full driver name                                                  |
| `position_gain`        | Difference between starting grid position and final race position |
| `is_podium`            | Whether the driver finished in the top 3                          |
| `is_points_finish`     | Whether the driver scored points                                  |
| `is_classified_finish` | Whether the driver was classified as finished                     |
| `era`                  | Historical Formula 1 era                                          |
| `grid_group`           | Starting grid group such as Top 5, P6-P10, P11-P15, P16+          |

## Exploratory data analysis

The project includes descriptive statistics and visual analysis for the main numerical fields:

* starting grid position;
* final race position;
* points;
* laps;
* season year;
* race round;
* position gain.

The visual analysis includes different plot types such as histograms, scatter plots, line plots, boxplots, bar plots and a correlation heatmap.

## Hypotheses

### Hypothesis 1

**Starting grid position is more strongly associated with final race position in modern Formula 1 than in earlier eras.**

The analysis compares the relationship between starting grid position and final race position across historical eras. Since both variables are rank-like, Spearman correlation is used as the main measure of association.

The results show that the relationship between starting position and final position is stronger in modern Formula 1, especially in the most recent era.

### Hypothesis 2

**Top constructors have higher average points and podium rates, but they do not necessarily have the highest average position gain.**

The analysis compares constructors using total points, average points, podium rate and average position gain.

The results show that dominant constructors perform strongly in points and podium rate, but average position gain captures a different aspect of race performance. Top constructors often start near the front of the grid, which gives them fewer opportunities to gain many positions during a race.

### Hypothesis 3

**The share of classified finishes increased over time, suggesting improved reliability in modern Formula 1.**

The analysis calculates classified finish rates by year and by era. A classified finish is defined as a result with status `Finished` or a status containing `Lap`, such as `+1 Lap` or `+2 Laps`.

The results show that classified finish rates increased substantially over time, especially from the 2000s onward. This pattern is consistent with improved reliability in modern Formula 1.

## Visualizations

The project includes the following visualizations:

* distribution of position gain;
* starting grid position vs final race position;
* average points by year;
* correlation matrix of numerical variables;
* position gain by era;
* podium rate by starting grid group;
* top constructors by total points;
* constructor podium rate;
* constructor average position gain;
* classified finish rate by era;
* classified finish rate by year.

## Key findings

* Starting grid position is more strongly related to final race position in modern Formula 1.
* Top constructors usually have higher points and podium rates, but not necessarily higher average position gain.
* Classified finish rates increased substantially over time, which is consistent with improved reliability in modern Formula 1.
* Position gain should be interpreted carefully because strong teams often start near the front and have fewer opportunities to gain many places.
* Raw Formula 1 data requires cleaning before analysis because missing values may be encoded as `\N` and some numerical columns may be loaded as strings.

## How to run the project

1. Clone the repository:

```bash id="tegtrr"
git clone https://github.com/FVMM6/formula-1-performance-analytics.git
cd formula-1-performance-analytics
```

2. Install dependencies:

```bash id="tobc0a"
pip install -r requirements.txt
```

3. Download the Kaggle dataset and place all CSV files into:

```text id="w3v1an"
data/raw/
```

4. Build the processed dataset:

```bash id="vmtagx"
python src/build_dataset.py
```

5. Run exploratory analysis:

```bash id="6v4p3r"
python src/explore_dataset.py
```

6. Run hypothesis checks:

```bash id="wgh3ht"
python src/hypothesis_checks.py
```

7. Open the final report notebook:

```text id="yn75tf"
notebooks/formula_1_project.ipynb
```

## Notes

The raw dataset files are not stored in this repository because they are downloaded from Kaggle and ignored by Git. To reproduce the analysis, download the dataset manually and place all CSV files into the `data/raw/` folder.

The processed dataset and figures can be regenerated locally by running the scripts in the `src/` folder or by running the Jupyter Notebook.

## Project status

Completed as a data analysis report in Jupyter Notebook and structured as a portfolio-ready Python data analytics project.
