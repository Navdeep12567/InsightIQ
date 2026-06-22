import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chart style
sns.set_theme(style="whitegrid")

# Read dataset
file_path = "data/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

print("Dataset Loaded Successfully!")
print(df.head())

# ==========================================================
# SALES BY CATEGORY
# ==========================================================

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Sales by Category", fontsize=16, fontweight="bold")
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig("reports/sales_by_category.png", dpi=300)

plt.show()

# ==========================================================
# PROFIT BY CATEGORY
# ==========================================================

category_profit = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_profit.index,
    y=category_profit.values
)

plt.title("Profit by Category", fontsize=16, fontweight="bold")
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Profit ($)", fontsize=12)

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig("reports/profit_by_category.png", dpi=300)

plt.show()

# ==========================================================
# TOP 10 STATES BY SALES
# ==========================================================

state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=state_sales.values,
    y=state_sales.index
)

plt.title("Top 10 States by Sales", fontsize=16, fontweight="bold")
plt.xlabel("Total Sales ($)", fontsize=12)
plt.ylabel("State", fontsize=12)

plt.grid(axis="x", alpha=0.3)

plt.tight_layout()

plt.savefig("reports/top10_states_sales.png", dpi=300)

plt.show()

# ==========================================================
# SALES BY REGION
# ==========================================================

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Sales by Region", fontsize=16, fontweight="bold")
plt.xlabel("Region", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig("reports/sales_by_region.png", dpi=300)

plt.show()

# ==========================================================
# TOP 10 PRODUCTS BY SALES
# ==========================================================

product_sales = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=product_sales.values,
    y=product_sales.index
)

plt.title("Top 10 Products by Sales", fontsize=16, fontweight="bold")
plt.xlabel("Total Sales ($)", fontsize=12)
plt.ylabel("Product", fontsize=12)

plt.grid(axis="x", alpha=0.3)

plt.tight_layout()

plt.savefig("reports/top10_products_sales.png", dpi=300)

plt.show()