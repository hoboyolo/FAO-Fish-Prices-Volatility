# FAO-Fish-Prices-Volatility

# FAO Fish Price Index Analysis 🐟

This project performs a comprehensive time-series analysis on the **FAO Fish Price Index (FPI)** dataset. The analysis aims to uncover historical price trends, identify market volatility, and explore the statistical relationship between different fish species.

## 🚀 Project Overview

Understanding commodity price behavior is critical for economic forecasting and supply chain management. This project utilizes Python to transform raw FAO index data into actionable insights, focusing on the price dynamics of **Salmon** and **Whitefish**.

## 🛠 Key Features

* **Data Cleaning:** Robust handling of metadata-heavy CSV files to extract usable time-series data.
* **Trend Visualization:** Visualizing the aggregate FPI compared to specific species trends to identify price divergence.
* **Volatility Analysis:** Calculating year-on-year percentage changes to understand market stability.
* **Correlation Mapping:** Statistical analysis to determine if **Salmon** and **Whitefish** prices move in lockstep or fluctuate independently.


## 📊 Analysis Highlights

* **Time-Series Alignment:** Correct parsing of monthly index data using `datetime` objects.
* **Statistical Rigor:** Utilization of rolling correlation windows to track changing relationships between species over a 36-year period.
* **Insightful Visualization:** Dual-axis plots and scatter matrices to interpret complex economic data effectively.

## 🔮 Future Scope

* **Macroeconomic Correlation:** Integrate inflation or fuel price data to determine the external drivers of fish price fluctuations.
* **Predictive Modeling:** Applying time-series forecasting (e.g., ARIMA or Prophet models) to predict future index trends based on historical performance.

---
