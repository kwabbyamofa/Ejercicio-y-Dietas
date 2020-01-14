import inspect
def str_var(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var][0]

# Valores nutricionales para cada 100 gramos:
# Calorias ---> [kcal]
# Proteinas ---> [g]
# Grasas ---> [g]
# Hidratos ---> [g]

class Alimento:

    def __init__(self, calorias, proteinas, grasas, carbohidratos):
        self.cal = calorias
        self.prot = proteinas
        self.gras = grasas
        self.carbo = carbohidratos
        self.ProporcionCal = calorias / 100  # En kcal/g
        self.PorcentajeProt = proteinas/100  # En tanto por 1
        self.PorcentajeGras = grasas / 100  # En tanto por 1
        self.PorcentajeCarbo = carbohidratos / 100  # En tanto por 1

    def Info(self):
        return ('Calorias: %3s kcal \nProteinas: %2s g \nGrasas: %2s g '
                '\nCarbohidratos: %2s g'% (self.cal, self.prot, self.gras, self.carbo))


