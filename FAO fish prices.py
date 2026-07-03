import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
# skiprows=3 skips the metadata rows, skipfooter=2 drops the footer note rows
df = pd.read_csv(
    'FAO_fish_price_index_May2026.csv',
    skiprows=3,
    skipfooter=2,
    engine='python'
)

# 2. Clean Data
df = df.dropna(subset=['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')
cols = ['Date', 'FAO Fish Price Index', 'Salmon', 'Whitefish']
df = df[cols]

# 3. Calculate Volatility (Year-on-Year Change)
# We set Date as index to calculate pct_change() easily
df_indexed = df.set_index('Date')
volatility = df_indexed.pct_change(periods=12) * 100 # Annualized % change

# 4. Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Trends
ax1.plot(df['Date'], df['FAO Fish Price Index'], label='Aggregate FPI', color='black', alpha=0.5)
ax1.plot(df['Date'], df['Salmon'], label='Salmon', color='blue')
ax1.plot(df['Date'], df['Whitefish'], label='Whitefish', color='green')
ax1.set_title('FAO Fish Price Index Trends (Focus: Salmon & Whitefish)')
ax1.legend()

# Plot 2: Volatility (The 'Jumpiness' of prices)
ax2.plot(volatility.index, volatility['Salmon'], label='Salmon Volatility (%)', color='blue', alpha=0.7)
ax2.plot(volatility.index, volatility['Whitefish'], label='Whitefish Volatility (%)', color='green', alpha=0.7)
ax2.axhline(0, color='red', linestyle='--')
ax2.set_title('Price Volatility (Year-on-Year % Change)')
ax2.legend()

plt.tight_layout()
plt.show()