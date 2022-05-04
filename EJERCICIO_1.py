from ast import Try
from sre_constants import ASSERT
from numpy import dtype
import pandas as pd
import matplotlib.pyplot as plt

# UNA CLASE PARA LOS ERRORES
class Error(Exception):
    pass
class NumeroColumnasErroneo(Error):
    pass
class ColumnaVacia(Error):
    pass


# LEEMOS EL ARCHIVO CSV Y LO PONEMOS EN UN DATAFRAME
try:
    df = pd.read_csv('finanzas2020.csv', sep="\t")
except IOError as e:
    print(f"No se encuentra el fichero o no se puede leer. Error:{e}")
else:
    print(f"El fichero ha sido leido")


# COMPROBAMOS QUE TENGA 12 COLUMNAS EL DATAFRAME
try:
    columnas = len(df.columns)
    if(columnas != 12):
        raise NumeroColumnasErroneo
except NumeroColumnasErroneo:
    print(f"El archivo debe tener 12 columnas de informacion y tiene {columnas}")
else:
    print(f"El archivo tiene {columnas} columnas")


# QUE TODAS LAS COLUMNAS TENGAN INFORMACIÓN:
columnas_lista = list(df.columns)
for columna in columnas_lista:
    try:
        prueba = df[columna].empty
        if (prueba == True):
            raise ColumnaVacia
    except ColumnaVacia:
        print(f"La columna {columna} esta vacia")
    else:
        print(f"La columna {columna} contiene datos")

print(df.dtypes)
# COLUMNAS QUE NO SON NUMEROS PROBAMOS CON ASSERT
lista_col_malas = []
for col in df:
    try:
        if (df[col].dtypes != "int64"):
            raise AssertionError()
    except AssertionError:
            print(f"la columna {col} no tiene el tipo de datos correctos")
            lista_col_malas.append(col)

 
# LAS RECORREMOS PARA CAMBIAR LOS DATOS
for columna in lista_col_malas:
    df[columna] = df[columna].astype(str)
    df[columna] = df[columna].str.replace(r"[^0-9-]","", regex=True)
    for i in range(100):
        try:
            int(df[columna][i])
        except ValueError:
            df.loc[i,columna] = 0
            int(df[columna][i])
    
    df[columna] = df[columna].astype(int)

print("\n")
print(df.dtypes)
print("\n")

# QUE MES SE HA GASTADO MÁS Y CUAL MENOS
gasto_mas = 0
ahorro_mas = 0
for col in df:
    suma_mes = df[col].sum()
    print(f"GASTO EN {col}:\n{suma_mes}")
    if (suma_mes <= gasto_mas):
        gasto_mas = suma_mes
        mes_mas = col
    if (suma_mes >= ahorro_mas):
        ahorro_mas = suma_mes
        mes_menos = col

print("\n")
print(f"El mes que más se ha gastado ha sido {mes_mas} : {gasto_mas}")
print(f"El mes que más se ha ahorrado ha sido {mes_menos} : {ahorro_mas}")
print("\n")

# MEDIA DE GASTOS ANUAL Y GASTO TOTAL ANUAL
acumulado = 0
for col in df:
    suma_mes = df[col].sum()
    acumulado = acumulado + suma_mes

media = acumulado/12
print(f"La media de gastos es: {media}")
print("\n")
print(f"El gasto total anual es: {acumulado}")
print("\n")

# INGRESOS TOTALES A LO LARGO DEL AÑO
lista_ingresos = []
lista_meses = []
ingresos_anuales = 0
for col in df:
    suma_positivos = df[col][df[col]>0].sum()
    print(f"INGRESOS {col} = {suma_positivos}")
    ingresos_anuales = ingresos_anuales + suma_positivos
    lista_ingresos.append(suma_positivos)
    lista_meses.append(col)
print("\n")
print(f"INGRESOS TOTALES ANUALES {ingresos_anuales}")
print("\n")

# GRAFICA INGRESOS A LO LARGO DEL AÑO
df2 = pd.DataFrame(list(zip(lista_meses,lista_ingresos)), columns = ['Meses','Ingresos'])
print(df2)
plt.bar(df2["Meses"],df2["Ingresos"])
plt.show()
