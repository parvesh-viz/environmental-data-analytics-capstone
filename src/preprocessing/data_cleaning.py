import pandas as pd

# Load datasets
climate_df = pd.read_csv("data/raw/climate_change_dataset.csv")
deforestation_df = pd.read_csv("data/raw/global_deforestation_2000_2025.csv")
pollution_df = pd.read_csv("data/raw/global_environment_air_pollution_dataset.csv")

print("Before Cleaning")
print("Climate:", climate_df.shape)
print("Deforestation:", deforestation_df.shape)
print("Pollution:", pollution_df.shape)

# Handle missing values
deforestation_df["Primary_Driver_of_Change"] = (
    deforestation_df["Primary_Driver_of_Change"]
    .fillna("Unknown")
)

# Remove duplicates
climate_df = climate_df.drop_duplicates()
deforestation_df = deforestation_df.drop_duplicates()
pollution_df = pollution_df.drop_duplicates()

print("\nAfter Cleaning")
print("Climate:", climate_df.shape)
print("Deforestation:", deforestation_df.shape)
print("Pollution:", pollution_df.shape)

# Save cleaned datasets
climate_df.to_csv(
    "data/processed/climate_change_cleaned.csv",
    index=False
)

deforestation_df.to_csv(
    "data/processed/deforestation_cleaned.csv",
    index=False
)

pollution_df.to_csv(
    "data/processed/air_pollution_cleaned.csv",
    index=False
)

print("\nCleaned datasets saved successfully.")