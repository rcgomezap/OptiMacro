import src.menu.display_options as do
from src.menu.clear import clear
clear()


print('¡Bienvenido a OptiMacro!')
salir = False
display = True

while salir == False:
    display = do.display_options(display)
    salir,display = do.option_func(salir,display)

