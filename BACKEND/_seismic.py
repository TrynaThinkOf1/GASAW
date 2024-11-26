import time

import matplotlib.pyplot as plt
from obspy.clients.fdsn import Client
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from datetime import date
from io import BytesIO
from threading import Thread

from time import sleep
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
client = Client("IRIS")

eventData = {}

def main():
    while True:
        fetch()
        img = plot()

        Thread(target=this_is_a_stupid_function, daemon=True).start()

        return img

def this_is_a_stupid_function():
    while True:
        sleep(30)
        fetch()
        plot()

def fetch(min_mag=3.0):
    global eventData

    try:
        catalog = client.get_events(starttime=date.today(), minmagnitude=min_mag)
        for event in catalog:
            origin = event.origins[0]
            magnitude = event.magnitudes[0].mag
            latitude = origin.latitude
            longitude = origin.longitude

            event_id = event.resource_id.id
            if event_id not in eventData:
                eventData[event_id] = {
                    "latitude": latitude,
                    "longitude": longitude,
                    "magnitude": magnitude,
                }
    except Exception as e:
        raise Exception(e)

def plot():
    plt.figure(figsize=(12, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.add_feature(cfeat.COASTLINE)
    ax.add_feature(cfeat.LAND)
    ax.add_feature(cfeat.OCEAN, alpha=0.5)
    ax.add_feature(cfeat.BORDERS, linestyle=':')
    ax.gridlines(draw_labels=True)

    ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

    for event_id, event in eventData.items():
        lat, lon, mag = event["latitude"], event["longitude"], event["magnitude"]
        plt.plot(lon, lat, 'ro', transform=ccrs.PlateCarree())
        plt.text(lon + 1, lat + 1, f"Mag {mag:.1f}", color="red", fontsize=9,
                 transform=ccrs.PlateCarree())

    plt.title("Seismic Activity Map")

    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    return img


if __name__ == "__main__":
    main()