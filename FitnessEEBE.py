import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QStackedWidget
from Alimento import *
from Dieta import *

Alimentos = {
'Pollo': Alimento(145, 22.2, 6.2, 0),
'Pavo': Alimento(157, 20.18, 8.5, 0),
'Conejo': Alimento(88.3, 10.38, 5.2, 0),
'Cerdo': Alimento(219, 17.5, 16.5, 1), # Carne cerdo semigrasa
'Bacon': Alimento(682, 14.6, 69.3, 0),
'Canelones': Alimento(132, 6.21, 5.4, 13.4),
'Lasana': Alimento(139, 6.3, 7.9, 10.3),
'Arroz': Alimento(364, 6.67, 0.9, 81.6),
'Avena': Alimento(353, 11.72, 7.09, 55.7),
'Maiz': Alimento(102.3, 3.32, 1.28, 18.2), # Grano hervido en lata
'Pasta': Alimento(359, 12.78, 1.58, 70.9),
'Garbanzo': Alimento(341, 20.8, 5.5, 44.3),
'Platano': Alimento(95.03, 1.06, 0.27, 20.8),
'Melon': Alimento(55.44, 0.88, 0.1, 12.4),
'Sandia': Alimento(28.4, 0.63, 0.3, 5.6),
'Aguacate': Alimento(233, 1.88, 23.5, 0.4),
'Patata': Alimento(73.59, 2.34, 0.11, 14.8), # Patata nueva
'Patatas fritas': Alimento(276, 4.1, 13.5, 32.79), # De bolsa congeladas
'Huevo': Alimento(162, 12.68, 12.1, 0.68),
'Miel': Alimento(302, 0.38, 0, 75.1),
'Leche desnatada': Alimento(37, 3.89, 0.2, 4.9),
'Yogur desnatado': Alimento(44.88, 4.25, 0.32, 6.3),
'Espinaca': Alimento(20.74, 2.63, 0.3, 0.61),
'Lechuga': Alimento(19.6, 1.37, 0.6, 1.4),
'Tomate': Alimento(22.17, 0.88, 0.21, 3.5),
'Zanahoria': Alimento(39.4, 1.25, 0.2, 6.9),
'Pepino': Alimento(13.28, 0.63, 0.2, 1.9),
'Cebolla': Alimento(31.85, 1.19, 0.25, 5.3),
'Azucar': Alimento(399, 0, 0, 99.8),
'Pescadilla': Alimento(73.9, 16.68, 0.8, 0),
'Bacalao': Alimento(79.8, 17.68, 1.01, 0),
'Raya': Alimento(96.8, 20.56, 1.26, 0.8),
'Rape': Alimento(65.5, 14.87, 0.67, 0),
'Salmon': Alimento(191, 20.62, 12.1, 0),
}

Dietas = {}


# -*- coding: utf-8 -*-

# Base PyQt5

# Cargar nuestro formulario *.ui
form_class = uic.loadUiType("FitnessEEBE.ui")[0]

# Crear la Clase MyWindowClass con el formulario cargado.
class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.Ventanas.setVisible(False)
        for i in Alimentos.keys():
            self.SelecAlimento.addItem(i)
            self.SelecAlimento_2.addItem(i)
        self.bCrearAlimento.setEnabled(False)
        self.SelecComidas.addItems(['Desayuno', 'Comida', 'Cena'])
        self.bCrearDieta.setEnabled(False)
        self.GrupoEditarDietas.setVisible(False)
        self.bPonerAlimento.setEnabled(False)
        self.GrupoAlimentos.setVisible(False)

    #######################################
    ##### Slots Bases del formulario ######
    #######################################

    def ActPerfil(self):
        self.Ventanas.setVisible(True)
        self.Ventanas.setCurrentIndex(0)

    def ActDietas(self):
        self.Ventanas.setVisible(True)
        self.Ventanas.setCurrentIndex(1)

    def ActCalendario(self):
        self.Ventanas.setVisible(True)
        self.Ventanas.setCurrentIndex(2)

    def ActAnalisis(self):
        self.Ventanas.setVisible(True)
        self.Ventanas.setCurrentIndex(3)

    def ActConfiguracion(self):
        self.Ventanas.setVisible(True)
        self.Ventanas.setCurrentIndex(4)

    def ActInformacion(self):
        self.Ventanas.setVisible(True)
        self.Ventanas.setCurrentIndex(5)

    ##############################################
    ######### Slots del apartado Dietas ##########
    ##############################################

    def MostrarInfoAlimento(self):
        self.LabelAlimento.clear()
        if self.SelecAlimento.count() > 0:
            self.LabelAlimento.setText(Alimentos[self.SelecAlimento.itemText(self.SelecAlimento.currentIndex())].Info())
        # Muestra automaticamente la información del alimento que pone en el
        # ComboBox

    def ActivarCrearAlimento(self):
        try:
            Calorias = float(self.InputCalorias.text())
            Proteinas = float(self.InputProteinas.text())
            Grasas = float(self.InputGrasas.text())
            Hidratos = float(self.InputHidratos.text())
            self.bCrearAlimento.setEnabled(True)
        except:
            self.bCrearAlimento.setEnabled(False)
        if self.InputNombre.text() == '':
            self.bCrearAlimento.setEnabled(False)

    def CrearAlimento(self):
        Nombre = self.InputNombre.text()
        Calorias = float(self.InputCalorias.text())
        Proteinas = float(self.InputProteinas.text())
        Grasas = float(self.InputGrasas.text())
        Hidratos = float(self.InputHidratos.text())
        if Nombre not in Alimentos.keys():
            Alimentos[Nombre] = Alimento(Calorias, Proteinas, Grasas, Hidratos)
            self.SelecAlimento.addItem(Nombre)
            self.SelecAlimento_2.addItem(Nombre)

    def BorrarAlimento(self):
        if self.SelecAlimento_2.count() == 0:
            pass
        else:
            Indice = self.SelecAlimento_2.currentIndex()
            Nombre_Alimento = self.SelecAlimento_2.itemText(self.SelecAlimento_2.currentIndex())
            del Alimentos[Nombre_Alimento]
            self.SelecAlimento_2.removeItem(Indice)
            self.SelecAlimento.removeItem(Indice)

    def CrearDieta(self):
        Nombre = self.InputDietas.text()
        if Nombre not in Dietas.keys():
            Dietas[Nombre] = Dieta()
            self.SelecDietas.addItem(Nombre)

    def BorrarDieta(self):
        if self.SelecDietas.count() == 0: # Para evitar que el programa falle al intentar
            pass                          # borrar un elemento cuando no hay ninguno.
        else:
            Indice = self.SelecDietas.currentIndex()
            Nombre_Alimento = self.SelecDietas.itemText(self.SelecDietas.currentIndex())
            del Dietas[Nombre_Alimento]
            self.SelecDietas.removeItem(Indice)

    def ActivarCrearDieta(self):
        self.bCrearDieta.setEnabled(True)
        if self.InputDietas.text() == '':
            self.bCrearDieta.setEnabled(False)

    def EditarDieta(self):
        if self.SelecDietas.count() == 0:
            pass
        else:
            self.GrupoEditarDietas.setVisible(True)
            self.SelecDietas.setEnabled(False)
            self.bBorrarDieta.setEnabled(False)

    def SalirEditarDieta(self):
        self.GrupoEditarDietas.setVisible(False)
        self.SelecDietas.setEnabled(True)
        self.bBorrarDieta.setEnabled(True)

    def ActivarPonerAlimento(self):
        try:
            gramos = float(self.InputCantidad.text())
            self.bPonerAlimento.setEnabled(True)
        except:
            self.bPonerAlimento.setEnabled(False)

    def PonerAlimento(self):
        if self.SelecAlimento.count() == 0:
            pass
        else:
            Nombre_Dieta = self.SelecDietas.itemText(self.SelecDietas.currentIndex())
            Nombre_Alimento = self.SelecAlimento.itemText(self.SelecAlimento.currentIndex())
            if self.SelecComidas.currentIndex() == 0: # Desayuno
                # Se añade el alimento y su cantidad al diccionario Desayuno de la Dieta 'Nombre_Dieta'.
                Dietas[Nombre_Dieta].Desayuno[Nombre_Alimento] = float(self.InputCantidad.text())
            elif self.SelecComidas.currentIndex() == 1: # Comida
                # Se añade el alimento y su cantidad al diccionario Comida de la Dieta 'Nombre_Dieta'.
                Dietas[Nombre_Dieta].Comida[Nombre_Alimento] = float(self.InputCantidad.text())
            elif self.SelecComidas.currentIndex() == 2: # Cena
                # Se añade el alimento y su cantidad al diccionario Cena de la Dieta 'Nombre_Dieta'.
                Dietas[Nombre_Dieta].Cena[Nombre_Alimento] = float(self.InputCantidad.text())

    def QuitarAlimento(self):
        if self.SelecAlimento.count() == 0:
            pass
        else:
            Nombre_Dieta = self.SelecDietas.itemText(self.SelecDietas.currentIndex())
            Nombre_Alimento = self.SelecAlimento.itemText(self.SelecAlimento.currentIndex())
            if self.SelecComidas.currentIndex() == 0:
                # Si el alimento se encuentra dentro del Desayuno de la dieta 'Nombre_Dieta' se borra.
                if Nombre_Alimento in Dietas[Nombre_Dieta].Desayuno:
                    del Dietas[Nombre_Dieta].Desayuno[Nombre_Alimento]
            elif self.SelecComidas.currentIndex() == 1:
                # Si el alimento se encuentra dentro de la Comida de la dieta 'Nombre_Dieta' se borra.
                if Nombre_Alimento in Dietas[Nombre_Dieta].Comida:
                    del Dietas[Nombre_Dieta].Comida[Nombre_Alimento]
            elif self.SelecComidas.currentIndex() == 2:
                # Si el alimento se encuentra dentro de la Cena de la dieta 'Nombre_Dieta' se borra.
                if Nombre_Alimento in Dietas[Nombre_Dieta].Cena:
                    del Dietas[Nombre_Dieta].Cena[Nombre_Alimento]

    def EditarAlimento(self):
        self.GrupoAlimentos.setVisible(True)
        self.GrupoEditarDietas.setEnabled(False)

    def SalirEditarAlimento(self):
        self.GrupoAlimentos.setVisible(False)
        self.GrupoEditarDietas.setEnabled(True)

    def MostrarInfoDieta(self):
        self.LabelDietas.clear()
        if self.SelecDietas.count() > 0:
            Nombre_Dieta = self.SelecDietas.itemText(self.SelecDietas.currentIndex())
            label = Dietas[Nombre_Dieta].Info()
            self.LabelDietas.setText(label)

    def EditarFecha(self):
        date = self.Calendario.selectedDate()
        self.Fecha.setText(date.toString())

    def slotPrueba(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()