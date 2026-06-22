import pandas as pd

climate = pd.read_csv("data/raw/climate_change_dataset.csv")

print("Total Rows:", len(climate))

grouped = climate.groupby(["Country", "Year"]).size()

print("\nMax records per Country-Year:")
print(grouped.max())

print("\nSample:")
print(grouped.head(20))