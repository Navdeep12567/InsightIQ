import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def generate_charts(df):

    # Create chart folder
    os.makedirs("static/images", exist_ok=True)

    df = df.copy()

    # Convert date
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    # =========================================================
    # 1. SALES BY CATEGORY
    # =========================================================

    sales_by_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(7, 4))

    sales_by_category.plot(
        kind="bar",
        width=0.55
    )

    plt.title("Sales by Category", fontsize=14, pad=10)
    plt.xlabel("")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "static/images/category_sales.png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()

    # =========================================================
    # 2. MONTHLY SALES TREND
    # =========================================================

    monthly_sales = (
        df.dropna(subset=["Order Date"])
        .set_index("Order Date")["Sales"]
        .resample("ME")
        .sum()
    )

    plt.figure(figsize=(8, 4))

    plt.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o",
        linewidth=2,
        markersize=4
    )

    plt.title("Monthly Sales Trend", fontsize=14, pad=10)
    plt.xlabel("")
    plt.ylabel("Sales ($)")

    ax = plt.gca()

    ax.xaxis.set_major_locator(
        mdates.MonthLocator(interval=3)
    )

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%b %Y")
    )

    plt.xticks(rotation=45, ha="right")
    plt.grid(alpha=0.25)

    plt.tight_layout()

    plt.savefig(
        "static/images/monthly_sales.png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()

    # =========================================================
    # 3. 6-MONTH SALES FORECAST
    # =========================================================

    if len(monthly_sales) >= 6:

        forecast_value = (
            monthly_sales
            .rolling(6)
            .mean()
            .iloc[-1]
        )

        last_date = monthly_sales.index[-1]

        forecast_dates = pd.date_range(
            start=last_date + pd.offsets.MonthEnd(1),
            periods=6,
            freq="ME"
        )

        forecast_values = [forecast_value] * 6

        plt.figure(figsize=(8, 4))

        plt.plot(
            monthly_sales.index,
            monthly_sales.values,
            marker="o",
            linewidth=2,
            label="Actual Sales"
        )

        plt.plot(
            forecast_dates,
            forecast_values,
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Forecast"
        )

        plt.title(
            "6-Month Sales Forecast",
            fontsize=14,
            pad=10
        )

        plt.xlabel("")
        plt.ylabel("Sales ($)")

        ax = plt.gca()

        ax.xaxis.set_major_locator(
            mdates.MonthLocator(interval=3)
        )

        ax.xaxis.set_major_formatter(
            mdates.DateFormatter("%b %Y")
        )

        plt.xticks(rotation=45, ha="right")

        plt.grid(alpha=0.25)
        plt.legend()

        plt.tight_layout()

        plt.savefig(
            "static/images/sales_forecast.png",
            dpi=130,
            bbox_inches="tight"
        )

        plt.close()

    else:

        plt.figure(figsize=(8, 4))

        plt.text(
            0.5,
            0.5,
            "Not enough data for forecast",
            ha="center",
            va="center",
            fontsize=14
        )

        plt.axis("off")

        plt.savefig(
            "static/images/sales_forecast.png",
            dpi=130,
            bbox_inches="tight"
        )

        plt.close()

    # =========================================================
    # 4. PROFIT BY REGION
    # =========================================================

    region_profit = (
        df.groupby("Region")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(7, 4))

    region_profit.plot(
        kind="bar",
        width=0.55
    )

    plt.title("Profit by Region", fontsize=14, pad=10)
    plt.xlabel("")
    plt.ylabel("Profit ($)")
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "static/images/profit_region.png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()

    # =========================================================
    # 5. TOP 10 STATES BY SALES
    # =========================================================

    state_sales = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(8, 4.5))

    state_sales.sort_values().plot(
        kind="barh",
        width=0.6
    )

    plt.title(
        "Top 10 States by Sales",
        fontsize=14,
        pad=10
    )

    plt.xlabel("Sales ($)")
    plt.ylabel("")
    plt.grid(axis="x", alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "static/images/top_states_sales.png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()

    # =========================================================
    # 6. TOP 10 PRODUCTS BY SALES
    # =========================================================

    product_sales = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(8, 5))

    product_sales.sort_values().plot(
        kind="barh",
        width=0.6
    )

    plt.title(
        "Top 10 Products by Sales",
        fontsize=14,
        pad=10
    )

    plt.xlabel("Sales ($)")
    plt.ylabel("")
    plt.grid(axis="x", alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "static/images/top_products_sales.png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()

    # =========================================================
    # 7. TOP 10 CUSTOMERS BY SALES
    # =========================================================

    customer_sales = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(8, 5))

    if not customer_sales.empty:

        customer_sales.sort_values().plot(
            kind="barh",
            width=0.6
        )

        plt.title(
            "Top 10 Customers by Sales",
            fontsize=14,
            pad=10
        )

        plt.xlabel("Sales ($)")
        plt.ylabel("")
        plt.grid(axis="x", alpha=0.3)

    else:

        plt.text(
            0.5,
            0.5,
            "No customer data available",
            ha="center",
            va="center",
            fontsize=14
        )

        plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        "static/images/top_customers_sales.png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()

    # =========================================================
    # 8. PROFIT BY CATEGORY
    # =========================================================

    profit_by_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(7, 4))

    profit_by_category.plot(
        kind="bar",
        width=0.55
    )

    plt.title(
        "Profit by Category",
        fontsize=14,
        pad=10
    )

    plt.xlabel("")
    plt.ylabel("Profit ($)")
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "static/images/profit_category.png",
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()