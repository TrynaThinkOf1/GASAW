import _seismic as seis
import _weather as weat

def getSeismicPlot():
    seis.fetch(min_mag=5.0)
    return seis.plot()