import pandas as pd
import time
import requests

def general():
    descarga()

def descarga():
    url = "https://regiones.ine.cl/documentos/default-source/region-xv/estadisticas/generacion-y-distribucion-de-energia-electrica/cuadros-estadisticos/series-mensuales/series-mensuales-desde-2015-a-la-fecha.xlsx?sfvrsn=c19505b2_8"
    file = requests.get(url)

    open('text.xlsx', 'wb').write(file.content)


if __name__ == '__main__':
    general()