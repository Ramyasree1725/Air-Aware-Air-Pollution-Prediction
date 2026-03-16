# Milestone 2: AQI Forecasting using Prophet

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Step 1: Create Historical AQI Data
data = {
    "Date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "AQI": [
        120, 125, 130, 128, 135, 140, 138, 145, 150, 148,
        155, 160, 162, 158, 165, 170, 168, 175, 180, 178,
        185, 190, 192, 188, 195, 200, 198, 205, 210, 208
    ]
}

df = pd.DataFrame(data)

print("Historical AQI Data")
print(df.head())

# Step 2: Data Preprocessing
df = df.dropna()                     # Remove missing values
df["Date"] = pd.to_datetime(df["Date"])  # Convert date format

# Rename columns for Prophet
df = df.rename(columns={"Date": "ds", "AQI": "y"})

print("\nPreprocessed Data")
print(df.head())

# Step 3: Create and Train Prophet Model
model = Prophet()
model.fit(df)

# Step 4: Create Future Dates for Prediction
future = model.make_future_dataframe(periods=10)

print("\nFuture Dates")
print(future.tail())

# Step 5: Make Predictions
forecast = model.predict(future)

print("\nForecasted AQI")
print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())

# Step 6: Plot Forecast Graph
fig1 = model.plot(forecast)
plt.title("AQI Forecast")

# Step 7: Show Trend and Seasonal Components
fig2 = model.plot_components(forecast)

plt.show()