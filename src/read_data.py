import pandas as pd

file_path = "data/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("="*60)
print("INSIGHTIQ - DATASET SUMMARY")
print("="*60)

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())