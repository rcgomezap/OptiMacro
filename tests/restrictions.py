import numpy as np

def cost_int(x,peso_min):
    costo = 0
    if x<peso_min:
        costo = -1/peso_min*x + 1
    else:
        costo = np.sin(np.pi*x/peso_min)**2
    return costo


def rst(c,alimento):
    cost = 0

    # Prevenir valores negativos
    if c < 0:
            cost += 1e2*c**2

    # Peso mínimo
    if alimento.nombre == 'huevo':
        peso_min = 50
        if c % peso_min != 0:
            cost += 1e2*cost_int(c,peso_min) # Penalizar valores no enteros

    elif alimento.nombre == 'pollo':
        peso_min = 100
        if c<peso_min:
            cost += (peso_min - c)**2

    elif alimento.nombre == 'pan':
        peso_min = 17
        if c % peso_min != 0:
            cost += 1e1*cost_int(c,peso_min) # Penalizar valores no enteros

    elif alimento.nombre == 'leche':
        peso_max = 300
        peso_min = 200
        if c > peso_max:
            cost += (c - peso_max)**2
        elif c < peso_min:
            cost += (peso_min - c)**2
    elif alimento.nombre == 'mermelada':
        peso_max = 30
        if c > peso_max:
            cost += (c - peso_max)**2

    return cost

def macro_restrictions(sum_cal,sum_prot,sum_carb,req_calorias,req_proteinas,req_carbohidratos):
    cost = 0
    cost += 1e2*(req_calorias - sum_cal)**2
    # cost += 1e-1*(req_proteinas - sum_prot)**2

    if req_proteinas[0] > sum_prot:
        cost += 1e-1*(req_proteinas[0] - sum_prot)**2
    elif req_proteinas[1] < sum_prot:
        cost += 1e-1*(req_proteinas[1] - sum_prot)**2

    if req_carbohidratos[0] < sum_carb*4/sum_cal:
        cost += 1e-3*(req_carbohidratos[0] - sum_carb*4/sum_cal)**2
    elif req_carbohidratos[1] > sum_carb*4/sum_cal:
        cost += 1e-3*(req_carbohidratos[1] - sum_carb*4/sum_cal)**2
    return cost

    