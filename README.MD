Dataset – Data Card
🔹 1. Source of Data
The dataset was collected using the Yahoo Finance API through the Python library yfinance.
It contains historical stock price data for five companies listed on the NASDAQ:
Apple Inc. (AAPL)
NVIDIA Corporation (NVDA)
Tesla Inc. (TSLA)
Amazon.com Inc. (AMZN)
Microsoft Corporation (MSFT)
Each dataset was downloaded programmatically in Python and saved as separate .csv files.
To ensure variability in the dataset, each company was assigned a different time range (from 1 month to 1 year of historical data).
🔹 2. Dataset Description
The dataset consists of time-series financial data representing daily stock market activity.
Each CSV file contains the following features:
Date – trading day index
Open – opening price of the stock
High – highest price during the day
Low – lowest price during the day
Close – closing price of the stock
Volume – number of shares traded
The data is structured as daily observations and reflects real market fluctuations.
No heavy preprocessing was applied in order to preserve the raw nature of financial data for analysis and AI readiness evaluation.
🔹 3. Data Collection Process
Data was retrieved using the yfinance Python library
Historical stock data was downloaded for each ticker
Data was converted into tabular format (Pandas DataFrame)
Each dataset was saved as an individual .csv file
Data was later used for KPI evaluation and visualization
🔹 4. KPI (Key Performance Indicators) Assessment
The dataset was evaluated using four quality dimensions:
✅ (a) Completeness
The dataset is highly complete.
There are no significant missing values in key financial fields such as Open, High, Low, Close, or Volume.
Minor gaps may occur due to:
weekends (no trading days)
stock exchange holidays
These are expected characteristics of financial time-series data.
⏱ (b) Latency
The dataset demonstrates low latency (near real-time availability).
Data retrieved from Yahoo Finance reflects the most recent available trading sessions, making it suitable for:
time-sensitive analysis
financial modeling
machine learning applications
🎯 (c) Accuracy
The dataset is considered accurate based on the following checks:
no negative or invalid price values were found
price trends are consistent with real market behavior
data is sourced from a reputable financial provider (Yahoo Finance)
Although external validation was not performed, Yahoo Finance is widely used in academic and industry contexts.
🔄 (d) Consistency
The dataset is fully consistent across all files:
identical column structure
uniform data types
standardized time-series format
This ensures compatibility when merging datasets or using them in machine learning pipelines.
🔹 5. Exploratory Analysis & Visualization
Basic exploratory data analysis was performed, including:
descriptive statistics (mean, standard deviation, min, max)
time-series line plots of closing prices
comparison of stock trends across companies
These visualizations highlight:
market volatility differences
overall growth trends
variation in stock behavior across companies
🔹 6. Limitations
Missing values due to non-trading days (weekends and holidays)
Data depends on external API availability
No macroeconomic or external feature integration
Requires normalization for machine learning applications
🔹 7. Conclusion
The dataset is suitable for data analysis and AI model training due to its:
high completeness
strong consistency
near real-time updates
reliable financial source
Overall, the dataset provides a solid foundation for time-series analysis, financial forecasting, and machine learning experiments.
🔹 8. Repository Structure
stock-data-kpi-analysis/
│
├── data/
│   ├── AAPL.csv
│   ├── NVDA.csv
│   ├── TSLA.csv
│   ├── AMZN.csv
│   └── MSFT.csv
│
├── notebooks/
│   └── analysis_stock_kpi.ipynb
│
├── src/
│   └── pipeline.py
│
├── README.md
└── requirements.txt
<img width="855" height="374" alt="image" src="https://github.com/user-attachments/assets/214519c5-166c-490e-92bf-decd53f79823" />
<img width="830" height="374" alt="image" src="https://github.com/user-attachments/assets/8c513cf7-44ca-4038-870e-4151b6ef1f0e" />
<img width="835" height="374" alt="image" src="https://github.com/user-attachments/assets/5a81d2fe-9840-47d7-82be-560bc73a565f" />
<img width="831" height="374" alt="image" src="https://github.com/user-attachments/assets/507da687-9408-42ee-a099-c768f4ce3b13" />
<img width="831" height="374" alt="image" src="https://github.com/user-attachments/assets/2b243878-cf7d-404d-beee-3524f87a5d9d" />
