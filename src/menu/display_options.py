import src.menu.funcs as funcs
from src.menu.clear import clear


def display_options(display):
    if display == True:
        print('''
            1) Optimizar una comida existente
            2) Añadir tabla nutricional de un alimento
            3) Añadir una comida
            4) Salir
            ''')
    display = False

    
def option_func(salir,display):
    line()
    option = input('Ingrese una opción: ')
    if option == '1':
        line()
        funcs.optimizar_alimento()
    elif option == '2':
        line()
        funcs.anadir_tabla_nutricional()
    elif option == '3':
        line()
        funcs.anadir_comida()
    elif option == '4':
        print('¡Hasta luego!')
        salir = True
    elif option == '0':
        clear()
        display = True
    else:
        print('Opcion no valida')
    line()
    if salir == False:
        print('Para volver a ver las opciones, ingrese 0')
    return salir,display



def line():
    print('-----------------------------')