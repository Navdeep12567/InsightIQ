import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Sales by Category
sales_by_category = df.groupby("Category")["Sales"].sum()

# Create Bar Chart
plt.figure(figsize=(6,4))
sales_by_category.plot(kind="bar")


plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.xlabel("")
plt.ylabel("Sales")

plt.tight_layout(pad=0.5)


# Save Chart
plt.savefig(
    "static/images/category_sales.png",
    dpi=180,
    bbox_inches="tight",
    pad_inches=0.1
)

print("Chart Saved Successfully!")

# Monthly Sales Trend

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(8,4))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2.5,
    color="#4F46E5"
)

plt.title("Monthly Sales Trend")
plt.xlabel("")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "static/images/monthly_sales.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("Monthly Sales Chart Saved!")

# Profit by Region

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(7,4))

region_profit.plot(
    kind="bar",
    color=["#2563EB", "#10B981", "#F59E0B", "#EF4444"]
)

plt.title("Profit by Region")
plt.xlabel("")
plt.ylabel("Profit ($)")
plt.xticks(rotation=0)

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "static/images/profit_region.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("Profit by Region Chart Saved!")

# Top 10 States by Sales

state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(8,5))

state_sales.plot(
    kind="bar",
    color="#14B8A6"
)

plt.title("Top 10 States by Sales")
plt.xlabel("")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "static/images/top_states_sales.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("Top States Chart Saved!")