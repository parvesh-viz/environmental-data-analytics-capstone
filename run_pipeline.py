import subprocess

print("Starting Data Pipeline...\n")

subprocess.run(["python", "src/preprocessing/data_cleaning.py"], check=True)
subprocess.run(["python", "src/preprocessing/feature_engineering.py"], check=True)
subprocess.run(["python", "src/preprocessing/create_master_dataset.py"], check=True)

print("\nPipeline completed successfully!")