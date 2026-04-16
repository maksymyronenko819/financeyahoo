# =========================
# 1. IMPORTS
# =========================
import yfinance as yf
import pandas as pd

# =========================
# 2. DATA COLLECTION
# =========================
def collect_data():
    companies = {
        "AAPL": "1y",
        "NVDA": "6mo",
        "TSLA": "3mo",
        "AMZN": "9mo",
        "MSFT": "1mo"
    }

    data = {}

    for ticker, period in companies.items():
        df = yf.Ticker(ticker).history(period=period)
        df.reset_index(inplace=True)
        
        filename = f"data/{ticker}.csv"
        df.to_csv(filename, index=False)
        
        data[ticker] = df

    return data

# =========================
# 3. KPI ANALYSIS
# =========================
def kpi_analysis(data):
    for ticker, df in data.items():
        print(f"\n===== {ticker} KPI REPORT =====")

        # Completeness
        print("Missing values:\n", df.isnull().sum())

        # Latency
        print("Latest date:", df["Date"].max())

        # Accuracy check
        if (df["Close"] < 0).any():
            print("❌ Negative values found")
        else:
            print("✅ Accuracy OK")

        # Consistency
        print("Columns:", list(df.columns))

# =========================
# 4. MAIN PIPELINE
# =========================
if __name__ == "__main__":
    data = collect_data()
    kpi_analysis(data)
