# 📊 InsightIQ

### Business Intelligence & Data Analytics Dashboard

InsightIQ is a Python-based Business Intelligence and Data Analytics project that transforms raw business sales data into meaningful insights through data preprocessing, analysis, visualization, forecasting, and an interactive Flask dashboard.

---

## 🚀 Project Overview

InsightIQ provides a centralized dashboard for analyzing business performance through key performance indicators, interactive filters, business insights, data visualizations, sales forecasting, and filtered data export.

The project follows a structured analytics workflow:

**Raw Data → Preprocessing → Analysis → Visualization → Forecasting → Business Insights → Dashboard**

---

## ✨ Features

- 📊 Interactive Business Intelligence Dashboard
- 💰 Sales and Profit Analysis
- 👥 Customer Performance Analysis
- 📦 Product Performance Analysis
- 🌎 Regional and State-wise Analysis
- 📅 Year and Monthly Sales Analysis
- 🔎 Dynamic filtering by Region, Category, and Year
- 💡 Automated Business Insights
- 🎯 Data-driven Business Recommendations
- 📈 Monthly Sales Trend Analysis
- 🔮 6-Month Sales Forecast
- 📥 Filtered CSV Data Download
- 📊 Multiple Business Visualizations
- 📌 KPI-based Business Performance Monitoring

---

## 📌 Key Performance Indicators

The dashboard provides the following KPIs:

- Total Sales
- Total Profit
- Total Customers
- Profit Margin
- Total Orders
- Average Order Value

These metrics update dynamically according to the selected dashboard filters.

---

## 💡 Business Insights

InsightIQ automatically identifies important business performance indicators such as:

- 🏆 Best Performing Category
- 💰 Most Profitable Region
- 📍 Top Performing State
- 📅 Best Sales Month
- 🎯 Data-driven Business Recommendations

These insights help users understand business performance and support better decision-making.

---

## 📈 Data Visualizations

The dashboard includes:

- Sales by Category
- Monthly Sales Trend
- 6-Month Sales Forecast
- Profit by Region
- Top 10 States by Sales
- Top 10 Products by Sales
- Top 10 Customers by Sales
- Profit by Category

---

## 🔎 Interactive Filtering

Users can dynamically filter the dashboard based on:

- Region
- Product Category
- Year

The dashboard automatically updates the displayed KPIs, business insights, and analysis according to the selected filters.

---

## 🔮 Sales Forecasting

InsightIQ includes a 6-month sales forecasting component based on historical monthly sales data.

The forecasting module helps identify expected sales trends and provides additional information for business planning and decision-making.

---

## 📥 Data Export

Users can download filtered business data directly from the dashboard in **CSV format**.

This allows the analyzed data to be reused for:

- Further analysis
- Reporting
- Data processing
- Business documentation

---

## 🛠️ Technologies Used

### Programming & Data Analysis
- Python
- Pandas
- Matplotlib

### Web Development
- Flask
- HTML5
- CSS3
- Jinja2

### Development & Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
InsightIQ/
│
├── reports/
│
├── src/
│   ├── analytics/
│   ├── cleaning/
│   ├── forecasting/
│   ├── preprocessing/
│   ├── reports/
│   ├── sql/
│   ├── utils/
│   ├── visualization/
│   ├── read_data.py
│   └── visualize.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
├── templates/
│   └── index.html
│
├── tests/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore