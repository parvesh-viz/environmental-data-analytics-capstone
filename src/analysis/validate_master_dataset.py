import pandas as pd

master = pd.read_csv(
    "data/processed/master_environment_dataset.csv"
)

print("\nShape:")
print(master.shape)

print("\nColumns:")
print(master.columns.tolist())

print("\nMissing Values:")
print(master.isnull().sum())

print("\nCountries:")
print(master["Country"].nunique())

print("\nYears:")
print(master["Year"].min(), "-", master["Year"].max())