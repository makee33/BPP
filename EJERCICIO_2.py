from numpy import dtype
import pandas as pd

# SIMPLIFICAMOS INICIO DE LA ACTIVIDAD ANTERIOR
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
print(df.dtypes)

#MES QUE GASTA MAS
def gasto_mas(df):
    maximo_gasto = 0
    for col in df:
        suma_mes = df[col].sum()
        if (suma_mes <= maximo_gasto):
            maximo_gasto = suma_mes
    return maximo_gasto

#MES QUE GASTA MENOS
def gasto_menos(df):
    minimo_gasto = 0
    for col in df:
        suma_mes = df[col].sum()
        if (suma_mes >= minimo_gasto):
            minimo_gasto = suma_mes
    return minimo_gasto

# GASTO TOTAL ANUAL
def gasto_total(df):
    gasto_total = 0
    for col in df:
        suma_mes = df[col].sum()
        gasto_total = gasto_total + suma_mes
    return gasto_total

# MEDIA DE GASTOS ANUAL
def media_anual(gasto_total):
    media_anual = gasto_total/12
    return media_anual

# INGRESOS TOTALES A LO LARGO DEL AÑO
def ingresos_anuales(df):
    ingresos_anuales = 0
    for col in df:
        suma_positivos = df[col][df[col]>0].sum()
        ingresos_anuales = ingresos_anuales + suma_positivos
    return ingresos_anuales


print(ingresos_anuales(df))