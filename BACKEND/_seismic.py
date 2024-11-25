import matplotlib.pyplot as plt
from obspy.clients.fdsn import Client
import cartopy.crs as ccrs
import cartopy.feature as cfeat

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
client = Client("IRIS")

DATA = {}

def main():
    fetch()
    plot()

def fetch():
    limit = int(input("How many stations should be fetched? (number ^ = time ^)\n"))

    inventory = client.get_stations(network="IU", level="station")

    count = 0
    for network in inventory:
        for station in network.stations:
            if count >= limit:
                break
            name = station.code
            latitude = station.latitude
            longitude = station.longitude
            DATA[name] = [longitude, latitude]

            count += 1

def plot():
    plt.figure(figsize=(12, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.add_feature(cfeat.COASTLINE)
    ax.add_feature(cfeat.LAND)
    ax.add_feature(cfeat.OCEAN, alpha=0.5)
    ax.add_feature(cfeat.BORDERS, linestyle=':')
    ax.gridlines(draw_labels=True)

    for name, (lon, lat) in DATA.items():
        plt.plot(lon, lat, 'go', transform=ccrs.PlateCarree(), label=name)

    if len(DATA) <= 20:  # Avoid overcrowding if too many stations
        plt.legend(loc='lower left', fontsize='small')

    plt.title("World Map with Points: " + (', '.join([i for i in DATA])))
    plt.show()


if __name__ == "__main__":
    main()