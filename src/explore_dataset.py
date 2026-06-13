from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

DATA_PATH = PROCESSED_DATA_DIR / "f1_main_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("MAIN DATASET OVERVIEW")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

print("MISSING VALUES")

missing_values = df.isna().sum().sort_values(ascending=False)
print(missing_values[missing_values > 0])

print("DESCRIPTIVE STATISTICS")

numeric_columns = [
    "grid",
    "positionOrder",
    "points",
    "laps",
    "year",
    "round",
    "position_gain",
]

descriptive_stats = df[numeric_columns].agg(["mean", "median", "std"]).T
print(descriptive_stats)

print("CATEGORY DISTRIBUTIONS")

print("\nEra distribution:")
print(df["era"].value_counts())

print("\nGrid group distribution:")
print(df["grid_group"].value_counts(dropna=False))

print("\nClassified finish distribution:")
print(df["is_classified_finish"].value_counts())

print("\nPodium finish distribution:")
print(df["is_podium"].value_counts())

print("\nPoints finish distribution:")
print(df["is_points_finish"].value_counts())

FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


plt.figure(figsize=(10, 6))
sns.histplot(df["position_gain"].dropna(), bins=40, kde=True)
plt.title("Distribution of Position Gain")
plt.xlabel("Position Gain")
plt.ylabel("Number of Race Results")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "position_gain_distribution.png", dpi=300)
plt.show()


grid_df = df[
    (df["grid"].notna()) &
    (df["grid"] > 0) &
    (df["positionOrder"].notna()) &
    (df["positionOrder"] > 0)
]

sample_df = grid_df.sample(min(5000, len(grid_df)), random_state=42)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=sample_df,
    x="grid",
    y="positionOrder",
    alpha=0.4
)
plt.title("Starting Grid Position vs Final Race Position")
plt.xlabel("Starting Grid Position")
plt.ylabel("Final Race Position")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "grid_vs_final_position.png", dpi=300)
plt.show()


avg_points_by_year = (
    df.groupby("year")["points"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=avg_points_by_year,
    x="year",
    y="points"
)
plt.title("Average Points per Race Result by Year")
plt.xlabel("Year")
plt.ylabel("Average Points")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "average_points_by_year.png", dpi=300)
plt.show()


corr_columns = [
    "grid",
    "positionOrder",
    "points",
    "laps",
    "year",
    "round",
    "position_gain",
]

plt.figure(figsize=(10, 7))
sns.heatmap(
    df[corr_columns].corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)
plt.title("Correlation Matrix of Numerical Variables")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "correlation_matrix.png", dpi=300)
plt.show()
