# 🌍 Air Pollution Visualizer (AQI Viewer)

This project is a web-based Air Quality Index (AQI) visualization tool built using **Python**, **Flask**, and **Folium**, allowing users to explore air quality data interactively.

## 🚀 Features

### ✅ Indian Cities AQI Viewer
- Displays AQI data for major Indian cities.
- Color-coded markers based on AQI categories (Good, Moderate, Unhealthy, etc.).
- Uses coordinates from official datasets.
- Clean, minimal UI for easy exploration.

### 🌐 Global AQI Viewer (In Progress)
- Visualizes AQI for cities around the world.
- Dropdown-based city selector to highlight location and show details.
- Pie chart for AQI category distribution.
- Currently under development to support dynamic graphs and better zoom/categorization.

---

## 🗂️ Project Structure

air_project/
├── templates/
│ ├── index.html # Indian AQI Viewer UI
│ └── global_index.html # Global AQI Viewer UI
├── static/
│ └── pie_chart.png # Dynamically generated pie chart image
├── indian_aqi_app.py # Flask app for India-specific data
├── global_aqi_app.py # Flask app for worldwide data
├── global_air_pollution_dataset.csv
├── air_pollution_with_coords_final.csv
└── README.md


---

## 📊 Data Sources

- **India**: Filtered city data with coordinates and AQI values.
- **Global**: Air quality statistics from worldwide sources (limited coordinate coverage).
- Coordinates for global cities have been auto-merged using city-country matching.

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Flask**
- **Pandas**
- **Folium** (Map rendering)
- **Matplotlib** (for pie charts)
- HTML + Jinja2 templates

---

## 🧩 To-Do / In Progress

- [x] Basic global AQI visualization
- [ ] Improve global map marker spacing and clustering
- [ ] Add dynamic bar/pie charts for both city and country views
- [ ] Add filtering by pollutant (PM2.5, NO₂, Ozone, CO)
- [ ] Deploy on a live server (Render, Heroku, etc.)
- [ ] Add search functionality for cities

---

## 📸 Preview

**Indian Cities AQI Viewer**

![India AQI](static/sample_india_map.png) <!-- Replace with your actual screenshots -->

**Global Cities AQI Viewer**

![Global AQI](static/sample_global_map.png)

---

## 📦 How to Run

Make sure you have Python and required packages installed.

```bash
# Install dependencies
pip install pandas flask folium matplotlib

# Run Indian AQI App
python indian_aqi_app.py

# OR run Global AQI App
python global_aqi_app.py


