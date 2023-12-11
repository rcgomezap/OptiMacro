from src.alimentos import crear_alimento
import src.minimize.minimize_sci as msc
from crear_comida import get_comida

alimentos = get_comida('DA_pan-crema_mani')
res = msc.minimize_sci(alimentos,500,(31,32),(0.4,0.6))