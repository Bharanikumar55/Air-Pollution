import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

# ✅ Load realistic AQI prediction data
df = pd.read_csv("realistic_predicted_aqi_india.csv")

# ✅ Clean and rename columns
df.rename(columns={
    'City': 'City',
    'Latitude': 'Latitude',
    'Longitude': 'Longitude',
    'Predicted AQI': 'Predicted AQI'
}, inplace=True)

# ✅ Drop rows with missing coordinates or AQI
df = df.dropna(subset=['Predicted AQI', 'Latitude', 'Longitude'])

# ✅ Clean city names for dropdown
df['City'] = df['City'].astype(str).str.strip().str.title()

# ✅ Streamlit App
st.title("🌍 City-wise Air Quality Prediction (India)")

# ✅ Dropdown for city selection
city_list = sorted(df['City'].dropna().unique().tolist())
selected_city = st.selectbox("Select a City", city_list)

# ✅ Get selected city’s data
city_data = df[df['City'] == selected_city].iloc[0]

# ✅ Show predicted AQI
st.metric(label="Predicted AQI", value=int(city_data['Predicted AQI']))

# ✅ Show coordinates
st.write(f"📍 Latitude: {city_data['Latitude']}, Longitude: {city_data['Longitude']}")

# ✅ Show Map
if pd.notna(city_data['Latitude']) and pd.notna(city_data['Longitude']):
    m = folium.Map(location=[city_data['Latitude'], city_data['Longitude']], zoom_start=6)
    folium.Marker(
        location=[city_data['Latitude'], city_data['Longitude']],
        popup=f"{selected_city}<br>Predicted AQI: {int(city_data['Predicted AQI'])}",
        icon=folium.Icon(color='red')
    ).add_to(m)
    st_folium(m, width=700)
else:
    st.warning("⚠️ Coordinates not available for this city.")

# ℹ️ Optional placeholder for pollutants chart
st.subheader("Pollutant Breakdown")
st.info("Pollutant-level AQI data is not available for all cities. Only overall prediction shown.")
