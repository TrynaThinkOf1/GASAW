import _seismic as seis
import _weather as weat


def getSeismicPlot():
    return seis.main()
def getSeismicData():
    return list(seis.eventData.values())