import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import plotly.express as px

st.set_page_config(page_title="Indian AQI Map", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("aqi_india_pollutants.csv", low_memory=False)
    df['City'] = df['City'].str.strip().str.title()
    return df

df = load_data()

st.title("AQI Map of Indian Cities")

# Folium map
m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)
marker_cluster = MarkerCluster().add_to(m)

def get_color(aqi):
    try:
        aqi = float(aqi)
        if aqi <= 50: return 'green'
        elif aqi <= 100: return 'lightgreen'
        elif aqi <= 200: return 'orange'
        elif aqi <= 300: return 'red'
        elif aqi <= 400: return 'purple'
        else: return 'darkred'
    except:
        return 'gray'

# Add all city markers
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['City']} - AQI: {row['AQI Value']}",
        icon=folium.Icon(color=get_color(row['AQI Value']))
    ).add_to(marker_cluster)

# Select city
city_list = sorted(df['City'].unique())
selected_city = st.selectbox("Choose a city:", city_list)
city_data = df[df['City'] == selected_city].iloc[0]

# Mark selected city
folium.Marker(
    location=[city_data['Latitude'], city_data['Longitude']],
    popup=f"{selected_city} - AQI: {city_data['AQI Value']}",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(m)

st_folium(m, width=700, height=500)

# Pollutants bar chart
pollutants = ['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']
pollutant_df = pd.DataFrame({
    "Pollutant": pollutants,
    "Value": [city_data[p] for p in pollutants]
})
fig = px.bar(pollutant_df, x="Pollutant", y="Value", title=f"Pollutants in {selected_city}")
st.plotly_chart(fig)

# Pie chart for AQI category distribution
category_counts = df['AQI Category'].value_counts().reset_index()
category_counts.columns = ['AQI Category', 'Count']
fig_pie = px.pie(category_counts, values='Count', names='AQI Category', title="AQI Category Distribution")
st.plotly_chart(fig_pie)
