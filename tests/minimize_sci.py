import numpy as np
from scipy.optimize import minimize
from scipy.optimize import basinhopping
import restrictions as rst

class alimento():
    def __init__(self,nombre,proteina,carbohidratos,grasas):
        self.nombre = nombre
        self.proteina = proteina
        self.carbohidratos = carbohidratos
        self.grasas = grasas


pollo = alimento('pollo', 23.09/100, 0, 1.24/100)
arroz = alimento('arroz', 6/100, 82/100, 0.)
aceite = alimento('aceite', 0., 0., 1.)
sopa_frijoles = alimento('sopa_frijoles', 2.6/100, 7.6/100, 1.58/100)
huevo = alimento('huevo', 12.58/100, 0.77/100, 9.94/100)
pan = alimento('pan', 7.64/100, 50.61/100, 3.29/100)
crema_mani = alimento('crema_mani', 23.3/100, 20./100, 53.33/100)
proteina_toning = alimento('proteina_toning', 45.45/100, 36.36/100, 9.39/100)
leche = alimento('leche', 3.1/100, 4.55/100, 1.55/100)
tocineta = alimento('tocineta', 33.33/100, 0., 41.67/100)
mermelada = alimento('mermelada', 0.54, 66.67/100, 0.14)
proteina_bipro = alimento('proteina_bipro', 90.91/100, 0., 0.)
avena = alimento('avena', 13.85/100, 69.23/100, 7.69/100)
pastas = alimento('pastas', 12/100, 75/100, 1.5/100)
queso = alimento('queso', 25/100, 0., 33.33/100)
lentejas = alimento('lentejas', 25.8/100, 60.08/100, 1.06/100)


alimentos = [lentejas]

def cost_function(x):

    req_calorias = 1000
    req_proteinas = (30,100)
    req_carbohidratos = (0.4,0.6)


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


#cg method
# res_min = minimize(cost_function, x0, method='CG', tol=1e-5, options={'maxiter': 1000})
# res_min = basinhopping(cost_function, x0, niter=1000)

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
for i in range(len(alimentos)):
    print(alimentos[i].nombre, res_min.x[i], 'gramos')
print('Error:', res_min.fun)
# print(res_min.message)
print('Numero de iteraciones:', res_min.nit)

