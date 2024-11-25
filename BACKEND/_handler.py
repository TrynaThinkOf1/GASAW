import meteostat as ms
import numpy as np
import matplotlib.pyplot as plt
import obspy as obs
from datetime import datetime as dt
import cartopy.crs as ccrs
import cartopy.feature as cfeat

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_data(type=0):
    data_combinations = [
        (seis, temp, prec),
        (seis, temp),
        (seis, prec),
        (seis,),
        (temp, prec),
        (temp,),
        (temp, prec),
        (prec,)
    ]

    if 0 <= type < len(data_combinations):
        return data_combinations[type]
    else:
        raise ValueError("Invalid type")

atl_lat, atl_lon = 33.749, -84.388
mos_lat, mos_lon = 55.756, 37.617
syd_lat, syd_lon = -33.869, 151.209

# Create a figure
plt.figure(figsize=(12, 8))

# Define the projection (Plate Carrée is commonly used for global maps)
ax = plt.axes(projection=ccrs.PlateCarree())

# Add features to the map
ax.add_feature(cfeat.COASTLINE)
ax.add_feature(cfeat.BORDERS, linestyle=':')

# Add a grid for reference
ax.gridlines(draw_labels=True)

# Plot Atlanta
plt.plot(atl_lon, atl_lat, 'ro', transform=ccrs.PlateCarree(), label="Atlanta (33.749, -84.388)")
plt.plot(mos_lon, mos_lat, 'bo', transform=ccrs.PlateCarree(), label="Moscow (55.756, 37.617)")
plt.plot(syd_lon, syd_lat, 'go', transform=ccrs.PlateCarree(), label="Sydney (-33.869, 151.209)")

# Show the map
plt.title("World Map with Points: Atlanta, Moscow, Syndey")
plt.show()