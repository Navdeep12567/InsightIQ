from flask import Flask, render_template, request, send_file
import pandas as pd
from src.visualize import generate_charts
import io

app = Flask(__name__)

# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# Convert Order Date
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# Available years
available_years = sorted(
    df["Order Date"]
    .dt.year
    .dropna()
    .unique()
)


# =========================================================
# MAIN DASHBOARD
# =========================================================

@app.route("/")
def home():

    # Get selected filters
    selected_region = request.args.get(
        "region",
        "All"
    )

    selected_category = request.args.get(
        "category",
        "All"
    )

    selected_year = request.args.get(
        "year",
        "All"
    )

    # Start with complete dataset
    filtered_df = df.copy()

    # =====================================================
    # REGION FILTER
    # =====================================================

    if selected_region != "All":

        filtered_df = filtered_df[
            filtered_df["Region"] == selected_region
        ]

    # =====================================================
    # CATEGORY FILTER
    # =====================================================

    if selected_category != "All":

        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    # =====================================================
    # YEAR FILTER
    # =====================================================

    if selected_year != "All":

        filtered_df = filtered_df[
            filtered_df["Order Date"].dt.year
            == int(selected_year)
        ]

    # =====================================================
    # GENERATE CHARTS
    # =====================================================

    generate_charts(filtered_df)

    # =====================================================
    # KPIs
    # =====================================================

    total_sales = filtered_df["Sales"].sum()

    total_profit = filtered_df["Profit"].sum()

    total_customers = filtered_df[
        "Customer ID"
    ].nunique()

    profit_margin = (
        (total_profit / total_sales) * 100
        if total_sales != 0
        else 0
    )

    total_orders = filtered_df[
        "Order ID"
    ].nunique()

    average_order_value = (
        total_sales / total_orders
        if total_orders != 0
        else 0
    )

    # =====================================================
    # BUSINESS INSIGHTS
    # =====================================================

    # Best Category
    category_sales = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
    )

    if not category_sales.empty:

        best_category = category_sales.idxmax()

        best_category_sales = category_sales.max()

    else:

        best_category = "N/A"

        best_category_sales = 0


    # Most Profitable Region
    region_profit = (
        filtered_df
        .groupby("Region")["Profit"]
        .sum()
    )

    if not region_profit.empty:

        best_region = region_profit.idxmax()

        best_region_profit = region_profit.max()

    else:

        best_region = "N/A"

        best_region_profit = 0


    # Top State
    state_sales = (
        filtered_df
        .groupby("State")["Sales"]
        .sum()
    )

    if not state_sales.empty:

        best_state = state_sales.idxmax()

        best_state_sales = state_sales.max()

    else:

        best_state = "N/A"

        best_state_sales = 0


    # Best Sales Month
    monthly_sales = (
        filtered_df
        .dropna(subset=["Order Date"])
        .set_index("Order Date")["Sales"]
        .resample("ME")
        .sum()
    )

    if not monthly_sales.empty:

        best_month_date = monthly_sales.idxmax()

        best_month = best_month_date.strftime(
            "%Y-%m"
        )

        best_month_sales = monthly_sales.max()

    else:

        best_month = "N/A"

        best_month_sales = 0


    # =====================================================
    # RECOMMENDATION
    # =====================================================

    if profit_margin >= 20:

        recommendation = (
            "Profitability is excellent. "
            "Focus on increasing sales volume "
            "while maintaining current margins."
        )

    elif profit_margin >= 10:

        recommendation = (
            "Profitability is healthy. "
            "Focus on improving sales volume "
            "and reducing unnecessary costs."
        )

    else:

        recommendation = (
            "Profit margin is low. "
            "Review pricing, discounts and "
            "operational costs."
        )


    # =====================================================
    # RENDER DASHBOARD
    # =====================================================

    return render_template(

        "index.html",

        # KPIs
        total_sales=total_sales,
        total_profit=total_profit,
        total_customers=total_customers,
        profit_margin=profit_margin,
        total_orders=total_orders,
        average_order_value=average_order_value,

        # Filters
        selected_region=selected_region,
        selected_category=selected_category,
        selected_year=selected_year,
        available_years=available_years,

        # Business Insights
        best_category=best_category,
        best_category_sales=best_category_sales,

        best_region=best_region,
        best_region_profit=best_region_profit,

        best_state=best_state,
        best_state_sales=best_state_sales,

        best_month=best_month,
        best_month_sales=best_month_sales,

        # Recommendation
        recommendation=recommendation
    )


# =========================================================
# DOWNLOAD FILTERED CSV
# =========================================================

@app.route("/download")
def download():

    selected_region = request.args.get(
        "region",
        "All"
    )

    selected_category = request.args.get(
        "category",
        "All"
    )

    selected_year = request.args.get(
        "year",
        "All"
    )

    # Start with complete dataset
    filtered_df = df.copy()

    # Region filter
    if selected_region != "All":

        filtered_df = filtered_df[
            filtered_df["Region"] == selected_region
        ]

    # Category filter
    if selected_category != "All":

        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    # Year filter
    if selected_year != "All":

        filtered_df = filtered_df[
            filtered_df["Order Date"].dt.year
            == int(selected_year)
        ]

    # Convert dataframe to CSV
    output = io.StringIO()

    filtered_df.to_csv(
        output,
        index=False
    )

    output.seek(0)

    # Return downloadable file
    return send_file(

        io.BytesIO(
            output.getvalue().encode("utf-8")
        ),

        mimetype="text/csv",

        as_attachment=True,

        download_name="InsightIQ_Filtered_Data.csv"
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )