import pandas as pd

climate = pd.read_csv("data/raw/climate_change_dataset.csv")
deforestation = pd.read_csv("data/raw/global_deforestation_2000_2025.csv")
pollution = pd.read_csv("data/raw/global_environment_air_pollution_dataset.csv")

climate_countries = set(climate["Country"].unique())
deforestation_countries = set(deforestation["Country"].unique())
pollution_countries = set(pollution["country"].unique())

print("Climate Countries:", len(climate_countries))
print("Deforestation Countries:", len(deforestation_countries))
print("Pollution Countries:", len(pollution_countries))

print("\nCommon Countries:")
print(
    climate_countries
    & deforestation_countries
    & pollution_countries
)