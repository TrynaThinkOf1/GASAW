import _seismic as seis
import _weather as weat


def getSeismicPlot(min_magnitude, measure_period):
    return seis.main(min_magnitude, measure_period)

def getSeismicData():
    return seis.eventData