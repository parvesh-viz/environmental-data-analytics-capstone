import pandas as pd

# ---------------------------------
# Load datasets
# ---------------------------------

climate = pd.read_csv(
    "data/processed/climate_change_cleaned.csv"
)

deforestation = pd.read_csv(
    "data/processed/deforestation_cleaned.csv"
)

pollution = pd.read_csv(
    "data/processed/air_pollution_cleaned.csv"
)

# ---------------------------------
# Common countries
# ---------------------------------

common_countries = [
    "Germany",
    "China",
    "India",
    "Brazil",
    "France",
    "Australia",
    "USA",
    "Canada",
    "Japan"
]

# ---------------------------------
# Climate aggregation
# ---------------------------------

climate_agg = (
    climate
    .query("Country in @common_countries")
    .groupby(["Country", "Year"], as_index=False)
    .mean(numeric_only=True)
)

# ---------------------------------
# Deforestation filter
# ---------------------------------

deforestation_filtered = (
    deforestation[
        deforestation["Country"].isin(common_countries)
    ]
)

# ---------------------------------
# Pollution aggregation
# ---------------------------------

pollution_agg = (
    pollution[
        pollution["country"].isin(common_countries)
    ]
    .groupby(
        ["country", "year"],
        as_index=False
    )
    .mean(numeric_only=True)
)

pollution_agg.rename(
    columns={
        "country": "Country",
        "year": "Year"
    },
    inplace=True
)

# ---------------------------------
# Merge datasets
# ---------------------------------

master = pd.merge(
    climate_agg,
    deforestation_filtered,
    on=["Country", "Year"],
    how="inner"
)

master = pd.merge(
    master,
    pollution_agg,
    on=["Country", "Year"],
    how="inner"
)

# ---------------------------------
# Keep common year range
# ---------------------------------

master = master[
    (master["Year"] >= 2000)
    &
    (master["Year"] <= 2023)
]

# ---------------------------------
# Remove unnecessary columns
# ---------------------------------

master = master.drop(
    columns=["month"]
)

# ---------------------------------
# Save master dataset
# ---------------------------------

master.to_csv(
    "data/processed/master_environment_dataset.csv",
    index=False
)

print("\nShape:")
print(master.shape)

print("\nColumns:")
print(master.columns.tolist())

print("\nFirst 5 Rows:")
print(master.head())

print("\nMaster dataset created successfully.")