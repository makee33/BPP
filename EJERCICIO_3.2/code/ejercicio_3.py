from numpy import dtype
import pandas as pd

class dataframes:
    """Esta clase opera a partir de un csv y su dataframe
    """

    def __init__ (self, archivo_csv, df):
        self.archivo_csv = archivo_csv
        self.df = df
        


    def crear_dataframe (self):
        """Esta función crea un dataframe a partir de un csv dado
        """
        df = pd.read_csv(self.archivo_csv, sep="\t")
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
    def gasto_mas(self):
        """Esta función filtra el més en que se gasta más
        """
        maximo_gasto = 0
        for col in self.df:
            suma_mes = self.df[col].sum()
            if (suma_mes <= maximo_gasto):
                maximo_gasto = suma_mes
        return maximo_gasto
        

    #MES QUE GASTA MENOS
    def gasto_menos(self):
        """Esta función filtra el més en que se gasta menos
        """
        minimo_gasto = 0
        for col in self.df:
            suma_mes = self.df[col].sum()
            if (suma_mes >= minimo_gasto):
                minimo_gasto = suma_mes
        return minimo_gasto

    # GASTO TOTAL ANUAL
    def gasto_total(self):
        """Esta función nos dice cual es el gasto total anual
        """
        gasto_total = 0
        for col in self.df:
            suma_mes = self.df[col].sum()
            gasto_total = gasto_total + suma_mes
        return gasto_total

    # MEDIA DE GASTOS ANUAL
    def media_anual(self):
        """Esta función nos devuelve la media de gastos anuales
        """
        gasto_total = 0
        for col in self.df:
            suma_mes = self.df[col].sum()
            gasto_total = gasto_total + suma_mes     
            media_anual = gasto_total/12
        return media_anual

    # INGRESOS TOTALES A LO LARGO DEL AÑO
    def ingresos_anuales(self):
        """Esta función suma los ingresos sin gastos del año
        """
        ingresos_anuales = 0
        for col in self.df:
            suma_positivos = self.df[col][self.df[col]>0].sum()
            ingresos_anuales = ingresos_anuales + suma_positivos
        return ingresos_anuales

