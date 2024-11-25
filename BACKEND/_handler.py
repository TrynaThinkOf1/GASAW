import meteostat as ms
import numpy as np
import matplotlib.pyplot as plt
import obspy as obs
from datetime import datetime as dt
import cartopy.crs as ccrs
import cartopy.feature as cfeat

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

names = []
DATA = {}

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

def main():
    while True:
        city = input("Enter city name and coords(or done): ")

        if city.lower() == "done":
            break

        city_data = city.split(',')

        if len(city_data) == 3:
            city_name = city_data[0].strip()
            try:
                lon = float(city_data[1].strip())
                lat = float(city_data[2].strip())
                names.append(city_name)
                DATA[city_name] = [lon, lat]
            except ValueError:
                print("Invalid coordinates")
                continue

        else:
            print("please enter the city name and coords in the format: 'City Name, Longitude, Latitude'")

    plt.figure(figsize=(12, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cfeat.COASTLINE)
    ax.add_feature(cfeat.BORDERS, linestyle=':')
    ax.gridlines(draw_labels=True)

    for lon, lat in DATA.values():
        plt.plot(lon, lat, 'go', transform=ccrs.PlateCarree())

    plt.title("World Map with Points: " + (', '.join([i for i in names])))
    plt.show()

if __name__ == "__main__":
    main()