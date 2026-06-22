# src/analysis/data_inventory.py

import pandas as pd
import os

output_file = "reports/data_inventory_report.txt"

datasets = {
    "Climate Change": "data/raw/climate_change_dataset.csv",
    "Deforestation": "data/raw/global_deforestation_2000_2025.csv",
    "Air Pollution": "data/raw/global_environment_air_pollution_dataset.csv"
}

with open(output_file, "w", encoding="utf-8") as f:

    for name, path in datasets.items():

        df = pd.read_csv(path)

        f.write("\n" + "=" * 80 + "\n")
        f.write(f"DATASET: {name}\n")
        f.write("=" * 80 + "\n")

        f.write(f"Rows: {df.shape[0]}\n")
        f.write(f"Columns: {df.shape[1]}\n\n")

        f.write("Column Names:\n")
        f.write(str(df.columns.tolist()))
        f.write("\n\n")

        f.write("Data Types:\n")
        f.write(df.dtypes.to_string())
        f.write("\n\n")

        f.write("Missing Values:\n")
        f.write(df.isnull().sum().to_string())
        f.write("\n\n")

        f.write("First 5 Records:\n")
        f.write(df.head().to_string())
        f.write("\n\n")

print(f"Report saved to {output_file}")