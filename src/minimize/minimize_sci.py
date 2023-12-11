import numpy as np
from scipy.optimize import minimize
import src.minimize.restrictions as rst
from src.menu.clear import line
from tqdm import tqdm

def minimize_sci(alimentos,cal,prot,carb):
    def cost_function(x):

        req_calorias = cal
        req_proteinas = prot
        req_carbohidratos = carb


        sum_cal = 0
        sum_prot = 0
        sum_carb = 0

        cost = 0
        for i in range(len(alimentos)):
            sum_cal += x[i]*(alimentos[i].proteina*4 + alimentos[i].carbohidratos*4 + alimentos[i].grasas*9)
            sum_prot += x[i]*alimentos[i].proteina
            sum_carb += x[i]*alimentos[i].carbohidratos

            #restricciones
            cost += rst.rst(x[i],alimentos[i])

        cost += rst.macro_restrictions(sum_cal,sum_prot,sum_carb,req_calorias,req_proteinas,req_carbohidratos)

        return cost


    # Loop variando vectores iniciales
    bounds = (0,500)
    n = 50
    barra = tqdm(total=n, desc="Procesando")
    for i in range(n):
        x0 = np.random.randint(bounds[0],bounds[1],len(alimentos))
        res = minimize(cost_function, x0, method='CG', tol=1e-8, options={'maxiter': 1000})
        if i == 0:
            res_min = res
        else:
            if res.fun < res_min.fun:
                res_min = res
        barra.update(1)
    barra.close()

    display_result(alimentos,res_min)

    return res_min.x

def display_result(alimentos,res):

    print('\n\n')
    line()

    sum_cal = 0
    sum_prot = 0
    sum_carb = 0

    for i in range(len(alimentos)):
        if str(alimentos[i].int) != 'nan':
            print(alimentos[i].nombre, (res.x[i]/alimentos[i].low).round(1), 'unidades')
        else:
            print(alimentos[i].nombre, res.x[i].round(1), 'gramos')
           
        sum_cal += res.x[i]*(alimentos[i].proteina*4 + alimentos[i].carbohidratos*4 + alimentos[i].grasas*9)
        sum_prot += res.x[i]*alimentos[i].proteina
        sum_carb += res.x[i]*alimentos[i].carbohidratos
    
    line()
    print(f'Energia: : {sum_cal:.2f} kcal -  Prot: {sum_prot:.2f} g -  Carb: {(sum_carb*4/sum_cal*100):.2f} %')
    line()
    line()
    print('Residual:', res.fun)