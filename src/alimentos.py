import numpy as np
import pandas as pd

df_alimentos = pd.read_csv('database/alimentos.csv')
class alimento():
    def __init__(self,nombre,proteina,carbohidratos,grasas):
        self.nombre = nombre
        self.proteina = proteina
        self.carbohidratos = carbohidratos
        self.grasas = grasas

        self.low = -np.inf
        self.high = np.inf
        self.int = False



    def restrict(self,low,high,int):
        self.low = low
        self.high = high
        self.int = int

def crear_alimento(id):
    al = alimento(df_alimentos['nombre'].iloc[id],df_alimentos['proteina'].iloc[id],df_alimentos['carbohidratos'].iloc[id],df_alimentos['grasas'].iloc[id])
    return al