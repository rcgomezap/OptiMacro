import pandas as pd
import numpy as np


df0 = pd.read_excel('Tabla de Composición Alimentos América Latina al 2010-EXCEL Editada para pag WEB.xlsx', sheet_name='TCA LA', skiprows=0)

df = pd.DataFrame()

df['nombre'] = df0['NOMBRE_CORTO']
df['proteina'] = df0['PROCNT']/100
df['carbohidratos'] = df0['CHOAVL']/100
df['grasas'] = df0['FAT']/100

for i in range(len(df)):
    if str(df['carbohidratos'].iloc[i]) == str(np.nan):
        df['carbohidratos'].iloc[i] = df0['CHOCDF'].iloc[i]/100
        if str(df['carbohidratos'].iloc[i]) == str(np.nan):
            df['carbohidratos'].iloc[i] = 0
        if str(df['grasas'].iloc[i]) == str(np.nan):
            df['grasas'].iloc[i] = 0
        if str(df['proteina'].iloc[i]) == str(np.nan):
            df['proteina'].iloc[i] = 0

df.to_csv('database/alimentos.csv', index=False)