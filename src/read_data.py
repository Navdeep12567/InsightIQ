import os
import pandas as pd


file_path = "data/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")
file_size = os.path.getsize(file_path) / (1024 * 1024)
memory_usage = df.memory_usage(deep=True).sum() / (1024 * 1024)
duplicate_rows = df.duplicated().sum()

print("="*60)
print("INSIGHTIQ - DATASET SUMMARY")
print("="*60)

print("\nFirst 5 Rows")
print(df.head())    

print("\nDataset Shape")
print(df.shape)

print("\nFile Size")
print(f"{file_size:.2f} MB")

print("\nColumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\n" + "="*60)
print("BUSINESS KPIs")
print("="*60)

print(f"Total Sales      : ${df['Sales'].sum():,.2f}")
print(f"Total Profit     : ${df['Profit'].sum():,.2f}")
print(f"Total Orders     : {df['Order ID'].nunique()}")
print(f"Total Customers  : {df['Customer ID'].nunique()}")
print(f"Total Products   : {df['Product ID'].nunique()}")
print(f"Total Quantity   : {df['Quantity'].sum()}")


print("\n" + "="*60)
print("TOP 10 STATES BY SALES")
print("="*60)

state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(state_sales)
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales.sort_values(ascending=False))

print("\n" + "="*60)
print("TOP 10 CITIES BY SALES")
print("="*60)

city_sales = (
    df.groupby("City")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(city_sales)

print("\n" + "="*60)
print("SALES BY CATEGORY")
print("="*60)

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(category_sales)

print("\n" + "="*60)
print("PROFIT BY CATEGORY")
print("="*60)

category_profit = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print(category_profit)

print("\n" + "="*60)
print("TOP 10 PRODUCTS BY SALES")
print("="*60)

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)