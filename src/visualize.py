import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Sales by Category
sales_by_category = df.groupby("Category")["Sales"].sum()

# Create Bar Chart
plt.figure(figsize=(8,5))
sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

# Save Chart
plt.savefig("static/images/category_sales.png")

print("Chart Saved Successfully!")