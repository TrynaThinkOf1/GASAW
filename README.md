# Global Analysis for Weather And Seismic Activity

This is a Python-based web application that displays **global weather data** (temperature and precipitation) alongside **seismic activity** (earthquakes) on a dynamic, real-time map. 

The application uses a **Flask backend** to process data and generate interactive maps using **Matplotlib** and **Cartopy**, which are then served to the frontend for visualization.

---

## Features

### Weather Data
- Displays global **temperature** and **precipitation** data.
- Automatically updates the map at regular intervals to reflect recent weather conditions.
- Fetches weather data using APIs or libraries like **Meteostat**.

### Seismic Activity
- Displays earthquake data, including:
  - **Magnitude** of seismic events.
  - **Coordinates** (latitude, longitude) of the epicenters.
- Automatically refreshes to show the latest seismic activity.

### Dynamic Visualization
- Maps are generated dynamically and displayed on the frontend.
- Real-time auto-refresh every 30 seconds.
- Fully responsive map that fits the screen size.

---

## Technologies Used

### Backend
- **Python 3**: Core language for the backend.
- **Flask**: Web framework to serve data and generate map images.
- **Matplotlib**: For creating the map visualizations.
- **Cartopy**: For rendering global maps and handling geographic projections.
- **ObsPy**: For fetching seismic data.
- **Meteostat**: For retrieving weather data (temperature and precipitation).

### Frontend
- **HTML5**: Structure of the web page.
- **CSS3**: Styling the webpage for a responsive design.
- **JavaScript**: For auto-refreshing the map image every 30 seconds.

---

## Installation
1. Enter Virtual Environment:
   ```bash
   python3 -m venv GASAWA
   source GASAWA/bin/activate
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/TrynaThinkOf1/GASAWA
   ```
3. Install dependancies:
    ```bash
   pip install -r requirements.txt
    ```
4. Run the server:
    ```bash
   python3 BACKEND/server.py
   ```
5. Navigate to `http://127.0.0.1:5000/`