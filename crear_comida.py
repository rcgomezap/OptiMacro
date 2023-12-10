from src.alimentos import crear_alimento
import pandas as pd

def crear_comida(nombre,id,low,high,int):
    comida = []
    nom_alimentos = []
    for i in range(len(id)):
        al = crear_alimento(id[i])
        al.low = low[i]
        al.high = high[i]
        al.int = int[i]
        nom_alimentos.append(al.nombre)
        comida.append(al)
    df = pd.DataFrame({'nombre':nom_alimentos,'id':id,'low':low,'high':high,'int':int})
    df.to_csv(f'database/comidas/{nombre}.csv',index=False)
    return comida


def get_comida(nombre):
    df = pd.read_csv(f'database/comidas/{nombre}.csv')
    id = df['id'].values.tolist()
    low = df['low'].values.tolist()
    high = df['high'].values.tolist()
    int = df['int'].values.tolist()
    comida = []
    for i in range(len(id)):
        al = crear_alimento(id[i])

        if low[i] != 'None':
            al.low = low[i]
        if high[i] != 'None':
            al.high = high[i]
        if int[i] != 'None':
            al.int = int[i]
        
        comida.append(al)

    return comida


# crear_comida('Monstruo',[6187,37,3746,4712,5348,6188,1639,1966],
#                                [None,None,None,None,None,None,None,None],
#                                [None,None,None,None,None,None,None,None],
#                                [None,None,None,None,None,None,None,None])

# aldict= {         'Proteina Toning': 6187,
#                   'Arroz': 37,
#                   'Pechuga': 3746,
#                   'Huevo': 4712,
#                   'Ensalada de frutas': 5348,
#                   'Pure de papa' : 6188,
#                   'Papa': 1639,
#                   'Aguacate': 1966,
#         }


