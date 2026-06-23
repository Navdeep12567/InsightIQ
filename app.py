from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

@app.route("/")
def home():
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_customers = df["Customer ID"].nunique()   

    return render_template(
        "index.html",
        total_sales=total_sales,
        total_profit=total_profit,
        total_customers=total_customers
    )

if __name__ == "__main__":
    app.run(debug=True)