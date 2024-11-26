import _seismic as seis
import _weather as weat

def getSeismicPlot():
    seis.fetch()
    return seis.plot()

def seismicMain():
    seis.main()
