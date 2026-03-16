import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from prophet import Prophet

st.set_page_config(page_title="AirAware Smart Dashboard", layout="wide")

st.title("🌫️ AirAware Smart Dashboard")
st.markdown("### India Air Quality Monitoring & Prediction System")


# Sidebar Filters


st.sidebar.header("Dashboard Filters")

states = {
"Maharashtra":["Mumbai","Pune","Nagpur"],
"Delhi":["New Delhi"],
"Karnataka":["Bangalore","Mysore"],
"Telangana":["Hyderabad","Warangal"],
"Tamil Nadu":["Chennai","Coimbatore"]
}

state = st.sidebar.selectbox("Select State", list(states.keys()))
city = st.sidebar.selectbox("Select City", states[state])


# Real-time AQI API


API_KEY = "demo"
url = f"https://api.waqi.info/feed/{city}/?token={API_KEY}"

response = requests.get(url)
data = response.json()

if data["status"] == "ok":

    aqi = data["data"]["aqi"]
    iaqi = data["data"]["iaqi"]

    pm25 = iaqi.get("pm25", {}).get("v", 0)
    pm10 = iaqi.get("pm10", {}).get("v", 0)

else:

    aqi = 120
    pm25 = 60
    pm10 = 80


# Dashboard Cards


col1, col2, col3 = st.columns(3)

col1.metric("City", city)
col2.metric("Current AQI", aqi)
col3.metric("State", state)

# AQI Category

if aqi <= 50:
    st.success("Good Air Quality 🟢")
elif aqi <= 100:
    st.info("Moderate Air Quality 🟡")
elif aqi <= 200:
    st.warning("Poor Air Quality 🟠")
else:
    st.error("Very Poor Air Quality 🔴")


# PM Chart


st.subheader("Pollution Levels")

pollution = pd.DataFrame({
"Pollutant":["PM2.5","PM10"],
"Value":[pm25,pm10]
})

fig1 = px.bar(pollution, x="Pollutant", y="Value", color="Pollutant")

st.plotly_chart(fig1, use_container_width=True)


# India AQI Heatmap


st.subheader("India AQI Heatmap")

heatmap_data = pd.DataFrame({
"City":["Mumbai","Delhi","Hyderabad","Chennai","Bangalore"],
"Lat":[19.0760,28.7041,17.3850,13.0827,12.9716],
"Lon":[72.8777,77.1025,78.4867,80.2707,77.5946],
"AQI":[180,220,170,130,110]
})

fig2 = px.scatter_mapbox(
heatmap_data,
lat="Lat",
lon="Lon",
color="AQI",
size="AQI",
hover_name="City",
zoom=4,
color_continuous_scale="RdYlGn_r"
)

fig2.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig2, use_container_width=True)


# AQI Trend Analysis


st.subheader("AQI Trend Analysis (Last 30 Days)")

trend_data = pd.DataFrame({
"Date": pd.date_range(end=pd.Timestamp.today(), periods=30),
"AQI":[aqi + i for i in range(30)]
})

fig3 = px.line(trend_data, x="Date", y="AQI")

st.plotly_chart(fig3, use_container_width=True)


# AI Prediction

st.subheader("7 Day AQI Prediction")

history = pd.DataFrame({
"ds": pd.date_range(end=pd.Timestamp.today(), periods=30),
"y":[aqi + i for i in range(30)]
})

model = Prophet()
model.fit(history)

future = model.make_future_dataframe(periods=7)

forecast = model.predict(future)

fig4 = px.line(forecast, x="ds", y="yhat")

st.plotly_chart(fig4, use_container_width=True)


# Pollution Alert


st.subheader("Health Advisory")

if aqi > 200:
    st.error("⚠️ Severe Pollution Alert! Avoid outdoor activities")
elif aqi > 150:
    st.warning("Air quality unhealthy. Wear masks outdoors.")
else:
    st.success("Air quality acceptable.")