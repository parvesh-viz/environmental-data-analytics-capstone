import pandas as pd

climate = pd.read_csv("data/raw/climate_change_dataset.csv")
deforestation = pd.read_csv("data/raw/global_deforestation_2000_2025.csv")
pollution = pd.read_csv("data/raw/global_environment_air_pollution_dataset.csv")

print("Climate")
print("Min Year:", climate["Year"].min())
print("Max Year:", climate["Year"].max())

print("\nDeforestation")
print("Min Year:", deforestation["Year"].min())
print("Max Year:", deforestation["Year"].max())

print("\nPollution")
print("Min Year:", pollution["year"].min())
print("Max Year:", pollution["year"].max())