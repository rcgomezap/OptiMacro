from src.alimentos import crear_alimento
import src.minimize.minimize_sci as msc
from crear_comida import get_comida
import os

def optimizar_alimento():
    files = os.listdir('./database/comidas')
    dict_comidas = {}
    for i in range(len(files)):
        dict_comidas[str(i+1)] = files[i].split('.')[0]
    
    print('Comidas disponibles: ')
    for key, value in dict_comidas.items():
        print(f'{key}) {value}')

    option = input('Ingrese una comida a optimizar: ')
    if option in dict_comidas.keys():
        alimentos = get_comida(dict_comidas[option])
        kcal = float(input('Ingrese las kcal que desea: '))
        minprot = float(input('Ingrese la cantidad minima de proteina en gramos: '))
        maxprot = float(input('Ingrese la cantidad maxima de proteina en gramos: '))
        mincarb = float(input('Ingrese la cantidad minima de carbohidratos en porcentaje: '))/100
        maxcarb = float(input('Ingrese la cantidad maxima de carbohidratos en porcentaje: '))/100
        msc.minimize_sci(alimentos,kcal,(minprot,maxprot),(mincarb,maxcarb  ))
    else:
        print('Opcion no valida')