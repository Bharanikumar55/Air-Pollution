from flask import Flask, render_template
import pandas as pd
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

@app.route('/')
def index():
    # ✅ Load data
    df = pd.read_csv("predicted_aqi_all_cities.csv")

    # ✅ Drop rows with missing required fields
    df = df.dropna(subset=['City', 'AQI Value', 'Latitude', 'Longitude'])

    # ✅ Limit to top 500 cities with highest AQI for speed
    df = df.sort_values(by='AQI Value', ascending=False).head(500)

    # ✅ Function to choose color based on AQI
    def get_color(aqi):
        try:
            aqi = float(aqi)
            if aqi <= 50:
                return 'green'
            elif aqi <= 100:
                return 'lightgreen'
            elif aqi <= 200:
                return 'orange'
            elif aqi <= 300:
                return 'red'
            elif aqi <= 400:
                return 'purple'
            else:
                return 'darkred'
        except:
            return 'gray'

    # ✅ Create folium map centered on India
    m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)

    # ✅ Add marker cluster
    marker_cluster = MarkerCluster().add_to(m)

    # ✅ Add markers
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{str(row['City']).title()} - AQI: {int(row['AQI Value'])}",
            icon=folium.Icon(color=get_color(row['AQI Value']))
        ).add_to(marker_cluster)

    # ✅ Render map
    map_html = m._repr_html_()
    return render_template("index.html", map_html=map_html)

if __name__ == "__main__":
    app.run(debug=True)
