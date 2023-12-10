import numpy as np
from scipy.optimize import minimize
import src.minimize.restrictions as rst

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
    bounds = (0,400)
    for i in range(50):
        x0 = np.random.randint(bounds[0],bounds[1],len(alimentos))
        res = minimize(cost_function, x0, method='CG', tol=1e-8, options={'maxiter': 1000})
        if i == 0:
            res_min = res
        else:
            if res.fun < res_min.fun:
                res_min = res
        print('Iteracion:',i+1,'Error:',res.fun)


    print('\n\n')

    sum_cal = 0
    sum_prot = 0
    sum_carb = 0

    for i in range(len(alimentos)):
        print(alimentos[i].nombre, res_min.x[i], 'gramos')
        sum_cal += res_min.x[i]*(alimentos[i].proteina*4 + alimentos[i].carbohidratos*4 + alimentos[i].grasas*9)
        sum_prot += res_min.x[i]*alimentos[i].proteina
        sum_carb += res_min.x[i]*alimentos[i].carbohidratos
    
    print(f'kcals: {sum_cal} Prot: {sum_prot} Carb: {sum_carb}')
    print('Error:', res_min.fun)
    # print(res_min.message)
    print('Numero de iteraciones:', res_min.nit)

    return res_min.x

