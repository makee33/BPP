import pytest
import pandas as pd
from ejercicio_2 import gasto_mas
from ejercicio_2 import gasto_menos

# DATAFRAME A PELO, PARA TEST
df = pd.read_csv('finanzas2020.csv', sep="\t")

# DATAFRAME CON DATOS ARREGLADOS
df2 = pd.read_csv('finanzas2020.csv', sep="\t")
columnas_mal = ["Enero", "Julio","Septiembre", "Octubre","Noviembre"]
for columna in columnas_mal:
    df2[columna] = df2[columna].astype(str)
    df2[columna] = df2[columna].str.replace(r"[^0-9-]","", regex=True)
    for i in range(100):
            try:
                int(df2[columna][i])
            except ValueError:
                df2.loc[i,columna] = 0
    df2[columna] = df2[columna].astype(int)


# TESTS GASTOS
def test_gasto_mas():
    assert gasto_mas(df) == -18933

def test_gasto_mas_2():
    assert gasto_mas(df2) == -18933

def test_gasto_menos():
    assert gasto_menos(df) == 11523

def test_gasto_menos_2():
    assert gasto_menos(df2) == 11523