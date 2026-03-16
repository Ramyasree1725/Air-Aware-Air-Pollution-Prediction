# Milestone 3: AQI Calculations, Alerts and Analysis

import pandas as pd

# Step 1: Predicted AQI Data for different states
data = {
    "State": ["Andhra Pradesh", "Telangana", "Tamil Nadu", "Karnataka", "Kerala"],
    "Predicted_AQI": [85, 120, 165, 220, 310]
}

df = pd.DataFrame(data)

print("Predicted AQI Data:")
print(df)

# Step 2: Function to classify AQI category
def classify_aqi(aqi):

    if aqi <= 50:
        return "Good"
    
    elif aqi <= 100:
        return "Moderate"
    
    elif aqi <= 200:
        return "Unhealthy"
    
    elif aqi <= 300:
        return "Very Unhealthy"
    
    else:
        return "Hazardous"


# Step 3: Apply AQI category function
df["AQI_Category"] = df["Predicted_AQI"].apply(classify_aqi)

# Step 4: Function to generate alerts
def generate_alert(category):

    if category == "Good":
        return "Air quality is safe."
    
    elif category == "Moderate":
        return "Sensitive people should be careful."
    
    elif category == "Unhealthy":
        return "Limit outdoor activities."
    
    elif category == "Very Unhealthy":
        return "Wear mask and avoid outdoor exposure."
    
    else:
        return "Health Alert! Stay indoors."


# Step 5: Apply alert function
df["Health_Alert"] = df["AQI_Category"].apply(generate_alert)

# Step 6: Final Analysis
print("\nAQI Analysis with Categories and Alerts:")
print(df)