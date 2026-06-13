import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

results = pd.read_csv(RAW_DATA_DIR / "results.csv")
races = pd.read_csv(RAW_DATA_DIR / "races.csv")
drivers = pd.read_csv(RAW_DATA_DIR / "drivers.csv")
constructors = pd.read_csv(RAW_DATA_DIR / "constructors.csv")
circuits = pd.read_csv(RAW_DATA_DIR / "circuits.csv")
status = pd.read_csv(RAW_DATA_DIR / "status.csv")

print("results:", results.shape)
print("races:", races.shape)
print("drivers:", drivers.shape)
print("constructors:", constructors.shape)
print("circuits:", circuits.shape)
print("status:", status.shape)

tables = [results, races, drivers, constructors, circuits, status]

for table in tables:
    table.replace("\\N", pd.NA, inplace=True)

print(results.isna().sum().sort_values(ascending=False))

results = results[
    ["resultId", "raceId", "driverId", "constructorId", "grid", "positionOrder", "points", "laps", "statusId", ]
]

races = races[
    [
        "raceId",
        "year",
        "round",
        "circuitId",
        "name",
        "date",
    ]
].rename(columns={"name": "race_name"})

drivers = drivers[
    [
        "driverId",
        "forename",
        "surname",
        "dob",
        "nationality",
    ]
].rename(columns={"nationality": "driver_nationality"})

constructors = constructors[
    [
        "constructorId",
        "name",
        "nationality",
    ]
].rename(columns={"name": "constructor_name", "nationality": "constructor_nationality"})

circuits = circuits[
    [
        "circuitId",
        "name",
        "location",
        "country",
        "lat",
        "lng",
        "alt",
    ]
].rename(columns={"name": "circuit_name", "country": "circuit_country"})

status = status[
    [
        "statusId",
        "status", ]
]


results_numeric_columns = [
    "grid",
    "positionOrder",
    "points",
    "laps",
]

for column in results_numeric_columns:
    results[column] = pd.to_numeric(results[column], errors="coerce")

races_numeric_columns = [
    "year",
    "round",
]

for column in races_numeric_columns:
    races[column] = pd.to_numeric(races[column], errors="coerce")

print(results.dtypes)
print(races.dtypes)

main_df = (
    results
    .merge(races, on="raceId", how="left")
    .merge(drivers, on="driverId", how="left")
    .merge(constructors, on="constructorId", how="left")
    .merge(circuits, on="circuitId", how="left")
    .merge(status, on="statusId", how="left")
)


key_columns = [
    "race_name",
    "driver_nationality",
    "constructor_name",
    "circuit_name",
    "status",
]

print("\nMissing values in key merged columns:")
print(main_df[key_columns].isna().sum())

main_df["driver_name"] = main_df["forename"] + " " + main_df["surname"]

main_df["position_gain"] = main_df["grid"] - main_df["positionOrder"]

main_df["is_podium"] = main_df["positionOrder"] <= 3

main_df["is_points_finish"] = main_df["points"] > 0


def assign_era(year):
    if year <= 1979:
        return "1950-1979"
    elif year <= 1999:
        return "1980-1999"
    elif year <= 2013:
        return "2000-2013"
    else:
        return "2014-2026"


main_df["era"] = main_df["year"].apply(assign_era)


def assign_grid_group(grid):
    if pd.isna(grid):
        return pd.NA
    elif grid <= 5:
        return "Top 5"
    elif grid <= 10:
        return "P6-P10"
    elif grid <= 15:
        return "P11-P15"
    else:
        return "P16+"


main_df["grid_group"] = main_df["grid"].apply(assign_grid_group)
main_df["is_classified_finish"] = (
    (main_df["status"] == "Finished") |
    (main_df["status"].str.contains("Lap", na=False))
)
new_columns = [
    "driver_name",
    "position_gain",
    "is_podium",
    "is_points_finish",
    "era",
    "grid_group",
    "is_classified_finish",
]

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

output_path = PROCESSED_DATA_DIR / "f1_main_dataset.csv"

main_df.to_csv(output_path, index=False)

print(f"\nSaved main dataset to: {output_path}")
print(f"Final dataset shape: {main_df.shape}")
