from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "f1_main_dataset.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

grid_df = df[
    (df["grid"].notna()) &
    (df["grid"] > 0) &
    (df["positionOrder"].notna()) &
    (df["positionOrder"] > 0)
    ].copy()

era_order = [
    "1950-1979",
    "1980-1999",
    "2000-2013",
    "2014-2026",
]

correlation_rows = []

for era, group in grid_df.groupby("era"):
    pearson_corr = group["grid"].corr(group["positionOrder"])
    spearman_corr = group[["grid", "positionOrder"]].corr(method="spearman").iloc[0, 1]

    correlation_rows.append(
        {
            "era": era,
            "race_results": len(group),
            "pearson_correlation": pearson_corr,
            "spearman_correlation": spearman_corr,
            "avg_position_gain": group["position_gain"].mean(),
            "median_position_gain": group["position_gain"].median(),
        }
    )

era_correlation = pd.DataFrame(correlation_rows)

era_correlation["era"] = pd.Categorical(
    era_correlation["era"],
    categories=era_order,
    ordered=True
)

era_correlation = era_correlation.sort_values("era")

print("HYPOTHESIS 1: GRID POSITION AND FINAL POSITION BY ERA")

print("\nCorrelation by era:")
print(era_correlation)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=era_correlation,
    x="era",
    y="spearman_correlation"
)

plt.title("Correlation Between Starting Grid and Final Position by Era")
plt.xlabel("Era")
plt.ylabel("Spearman Correlation")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "h1_grid_final_position_correlation_by_era.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(
    data=grid_df,
    x="era",
    y="position_gain",
    order=era_order
)

plt.title("Position Gain by Formula 1 Era")
plt.xlabel("Era")
plt.ylabel("Position Gain")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "h1_position_gain_by_era.png", dpi=300)
plt.show()

# 2 гипотеза
print("HYPOTHESIS 2: CONSTRUCTOR PERFORMANCE")

constructor_df = df[
    (df["constructor_name"].notna()) &
    (df["grid"].notna()) &
    (df["grid"] > 0) &
    (df["positionOrder"].notna()) &
    (df["positionOrder"] > 0)
    ].copy()

constructor_summary = (
    constructor_df
    .groupby("constructor_name")
    .agg(
        race_results=("resultId", "count"),
        total_points=("points", "sum"),
        avg_points=("points", "mean"),
        podium_rate=("is_podium", "mean"),
        avg_position_gain=("position_gain", "mean"),
        median_position_gain=("position_gain", "median"),
    )
    .reset_index()
)

constructor_summary = constructor_summary[
    constructor_summary["race_results"] >= 100
    ].copy()

top_constructors = (
    constructor_summary
    .sort_values("total_points", ascending=False)
    .head(10)
    .copy()
)

print("\nTop constructors by total points:")
print(
    top_constructors[
        [
            "constructor_name",
            "race_results",
            "total_points",
            "avg_points",
            "podium_rate",
            "avg_position_gain",
            "median_position_gain",
        ]
    ]
)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_constructors,
    x="total_points",
    y="constructor_name"
)

plt.title("Top 10 Constructors by Total Points")
plt.xlabel("Total Points")
plt.ylabel("Constructor")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "h2_top_constructors_total_points.png", dpi=300)
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_constructors.sort_values("podium_rate", ascending=False),
    x="podium_rate",
    y="constructor_name"
)

plt.title("Podium Rate of Top Constructors")
plt.xlabel("Podium Rate")
plt.ylabel("Constructor")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "h2_top_constructors_podium_rate.png", dpi=300)
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_constructors.sort_values("avg_position_gain", ascending=False),
    x="avg_position_gain",
    y="constructor_name"
)
plt.axvline(0, color="black", linewidth=1)
plt.title("Average Position Gain of Top Constructors")
plt.xlabel("Average Position Gain")
plt.ylabel("Constructor")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "h2_top_constructors_position_gain.png", dpi=300)
plt.show()

#3 гипотеза
print("HYPOTHESIS 3: CLASSIFIED FINISH RATE OVER TIME")


reliability_df = df[
    df["status"].notna()
].copy()


finish_rate_by_era = (
    reliability_df
    .groupby("era")
    .agg(
        race_results=("resultId", "count"),
        classified_finishes=("is_classified_finish", "sum"),
        classified_finish_rate=("is_classified_finish", "mean"),
    )
    .reset_index()
)


finish_rate_by_era["era"] = pd.Categorical(
    finish_rate_by_era["era"],
    categories=era_order,
    ordered=True
)

finish_rate_by_era = finish_rate_by_era.sort_values("era")


print("\nClassified finish rate by era:")
print(finish_rate_by_era)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=finish_rate_by_era,
    x="era",
    y="classified_finish_rate"
)

plt.title("Classified Finish Rate by Formula 1 Era")
plt.xlabel("Era")
plt.ylabel("Classified Finish Rate")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "h3_classified_finish_rate_by_era.png", dpi=300)
plt.show()

finish_rate_by_year = (
    reliability_df
    .groupby("year")
    .agg(
        race_results=("resultId", "count"),
        classified_finishes=("is_classified_finish", "sum"),
        classified_finish_rate=("is_classified_finish", "mean"),
    )
    .reset_index()
)


plt.figure(figsize=(12, 6))
sns.lineplot(
    data=finish_rate_by_year,
    x="year",
    y="classified_finish_rate"
)

plt.title("Classified Finish Rate by Year")
plt.xlabel("Year")
plt.ylabel("Classified Finish Rate")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "h3_classified_finish_rate_by_year.png", dpi=300)
plt.show()