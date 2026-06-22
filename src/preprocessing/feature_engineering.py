import pandas as pd

# Load cleaned datasets
climate_df = pd.read_csv(
    "data/processed/climate_change_cleaned.csv"
)

deforestation_df = pd.read_csv(
    "data/processed/deforestation_cleaned.csv"
)

pollution_df = pd.read_csv(
    "data/processed/air_pollution_cleaned.csv"
)

# -----------------------------
# Climate Features
# -----------------------------

climate_df["Temp_CO2_Ratio"] = (
    climate_df["Avg Temperature (°C)"] /
    climate_df["CO2 Emissions (Tons/Capita)"]
)

# -----------------------------
# Deforestation Features
# -----------------------------

deforestation_df["Net_Forest_Change"] = (
    deforestation_df["Annual_Afforestation_Rate"]
    -
    deforestation_df["Annual_Deforestation_Rate"]
)

# -----------------------------
# Pollution Features
# -----------------------------

pollution_df["Pollution_Index"] = (
    pollution_df["pm2_5"] +
    pollution_df["pm10"] +
    pollution_df["no2"]
)

pollution_df["AQI_Category"] = pd.cut(
    pollution_df["aqi"],
    bins=[0, 50, 100, 150, 200, 300, 500],
    labels=[
        "Good",
        "Moderate",
        "Unhealthy-SG",
        "Unhealthy",
        "Very Unhealthy",
        "Hazardous"
    ]
)

# Save feature datasets

climate_df.to_csv(
    "data/processed/climate_features.csv",
    index=False
)

deforestation_df.to_csv(
    "data/processed/deforestation_features.csv",
    index=False
)

pollution_df.to_csv(
    "data/processed/pollution_features.csv",
    index=False
)

print("Feature engineering completed.")