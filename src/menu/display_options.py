import src.menu.funcs as funcs
import os


def display_options(display):
    if display == True:
        print('''
            1) Optimizar una comida existente
            2) Salir
            ''')
    display = False
def option_func(salir,display):
    line()
    option = input('Ingrese una opción: ')
    if option == '1':
        line()
        funcs.optimizar_alimento()
    elif option == '2':
        print('¡Hasta luego!')
        salir = True
    elif option == '0':
        os.system('cls')
        display = True
    else:
        print('Opcion no valida')
    line()
    if salir == False:
        print('Para volver a ver las opciones, ingrese 0')
    return salir,display



def line():
    print('-----------------------------')