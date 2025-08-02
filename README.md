# 🌫️ Air Pollution Prediction and Visualization App

A Streamlit-based web application to **predict AQI (Air Quality Index)** for Indian cities using machine learning, and visualize the data interactively with maps and pollutant breakdown.

---

## 🚀 Features

- 🔍 **City-wise AQI prediction** using Random Forest + KNN
- 🗺️ **Interactive Map** using Folium
- 📍 **Dropdown** to select Indian cities/towns
- 📊 **Pie chart** showing contribution of pollutants
- 💾 Built using cleaned global AQI data and GeoNames cities

---

## 🧠 Model Summary

- **Algorithms Used:**
  - `RandomForestRegressor` (for training on available AQI)
  - `KNeighborsRegressor` (to predict AQI for missing cities)
- **Input Features:**
  - `PM2.5 AQI Value`
  - `CO AQI Value`
  - `NO2 AQI Value`
  - `Ozone AQI Value`

---
## 🗂️ Project Structure

air_project/
├── aqi_app.py # Streamlit app code
├── airpollutionpredict.ipynb # Jupyter notebook for preprocessing + model
├── realistic_predicted_aqi_india.csv # Final dataset with predicted AQI and coords
├── .gitignore # Excludes large files from git
└── requirements.txt # Dependencies

📡 Data Sources
📊 Global Air Pollution Dataset
🧭 GeoNames.org – Indian cities from IN.txt

🛑 Disclaimer
AQI values are approximate predictions based on available pollutant data. This tool is meant for demonstration and educational use only.


## 🗂️ Project Structure

