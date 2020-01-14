class Dieta:

    def __init__(self):
        self.Desayuno = {}
        self.Comida = {}
        self.Cena = {}

    def Info(self):
        lista_des = ''
        i = 0
        for x, y in zip(self.Desayuno.keys(), self.Desayuno.values()):
            i += 1
            lista_des += (' %s (%s g)'% (x, y))
            if i < len(self.Desayuno.values()):
                lista_des += ';'
        lista_com = ''
        i = 0
        for x, y in zip(self.Comida.keys(), self.Comida.values()):
            i += 1
            lista_com += (' %s (%s g)' % (x, y))
            if i < len(self.Comida.values()):
                lista_com += ';'
        lista_cen = ''
        i = 0
        for x, y in zip(self.Cena.keys(), self.Cena.values()):
            i += 1
            lista_cen += (' %s (%s g)' % (x, y))
            if i < len(self.Cena.values()):
                lista_cen += ';'

        return ('Desayuno:'+lista_des+'\n\nComida:'+lista_com+'\n\nCena:'+lista_cen)
