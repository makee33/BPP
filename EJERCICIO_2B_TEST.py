import pytest
import pandas as pd
from ejercicio_2 import gasto_total
from ejercicio_2 import media_anual
from ejercicio_2 import ingresos_anuales

# DATAFRAME CON DATOS ARREGLADOS
df = pd.read_csv('finanzas2020.csv', sep="\t")
columnas_mal = ["Enero", "Julio","Septiembre", "Octubre","Noviembre"]
for columna in columnas_mal:
    df[columna] = df[columna].astype(str)
    df[columna] = df[columna].str.replace(r"[^0-9-]","", regex=True)
    for i in range(100):
            try:
                int(df[columna][i])
            except ValueError:
                df.loc[i,columna] = 0
    df[columna] = df[columna].astype(int)


# TESTS GASTOS
def test_gasto_total():
    assert gasto_total(df) == -16973

def test_media_anual():
    assert media_anual(gasto_total(df)) == -1414.41

def test_ingresos_anuales():
    assert ingresos_anuales(df) == 280961


