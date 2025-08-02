from flask import Flask, render_template, request
import pandas as pd
import folium
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load the merged global dataset (with latitude and longitude)
df = pd.read_csv("global_aqi_with_coords.csv")

# Clean
df = df.dropna(subset=["Latitude", "Longitude", "AQI Value"])
df["City"] = df["City"].astype(str).str.strip().str.title()
df["Country"] = df["Country"].astype(str).str.strip().str.title()

# Sort cities alphabetically
cities = sorted(df["City"].unique())

@app.route("/", methods=["GET", "POST"])
def index():
    selected_city = request.form.get("city")
    city_df = df[df["City"] == selected_city] if selected_city else pd.DataFrame()

    # Create map
    m = folium.Map(location=[20, 0], zoom_start=2)
    for _, row in df.iterrows():
        color = get_color(row["AQI Category"])
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=5,
            popup=f"{row['City']}, {row['Country']}<br>AQI: {row['AQI Value']}",
            color=color,
            fill=True,
            fill_color=color
        ).add_to(m)

    map_html = m._repr_html_()

    # Generate pie chart if city selected
    if not city_df.empty:
        city_data = city_df.iloc[0].to_dict()
        category_counts = {
            "CO": city_df["CO AQI Category"].values[0],
            "Ozone": city_df["Ozone AQI Category"].values[0],
            "NO2": city_df["NO2 AQI Category"].values[0],
            "PM2.5": city_df["PM2.5 AQI Category"].values[0],
        }

        plt.figure(figsize=(6, 6))
        plt.pie(
            [1] * len(category_counts),
            labels=[f"{k}: {v}" for k, v in category_counts.items()],
            colors=["lightblue", "orange", "gray", "lightgreen"],
            startangle=90,
            autopct='%1.1f%%'
        )
        plt.title("Pollutant AQI Categories")
        plt.tight_layout()
        plt.savefig("static/pie_chart.png")
        plt.close()
    else:
        city_data = None

    return render_template("global_index.html",
                           cities=cities,
                           selected_city=selected_city,
                           map_html=map_html,
                           city_info=city_data)

def get_color(category):
    return {
        "Good": "green",
        "Moderate": "yellow",
        "Unhealthy for Sensitive Groups": "orange",
        "Unhealthy": "red",
        "Very Unhealthy": "purple",
        "Hazardous": "maroon"
    }.get(category, "gray")

if __name__ == "__main__":
    app.run(debug=True)
