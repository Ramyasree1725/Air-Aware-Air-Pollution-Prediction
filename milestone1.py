# Milestone 1: Data Collection, Cleaning, and Pattern Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Collected Data (Sample Air Quality Data)
data = {
    "State": ["Andhra Pradesh", "Telangana", "Tamil Nadu", "Karnataka", "Kerala"],
    "PM25": [120, 150, 90, 110, 80],
    "PM10": [200, 220, 150, 180, 130],
    "AQI": [180, 210, 140, 170, 120]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

print("Collected Air Quality Data:")
print(df)

# Step 2: Data Cleaning
# (Remove missing values if any)
df = df.dropna()

print("\nCleaned Dataset:")
print(df)

# Step 3: Understanding Data Patterns
print("\nSummary Statistics:")
print(df.describe())

# Step 4: Visualization to understand pattern
plt.figure()

plt.bar(df["State"], df["AQI"])

plt.title("AQI Pattern Across States")
plt.xlabel("State")
plt.ylabel("AQI")

plt.show()