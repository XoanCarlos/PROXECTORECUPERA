from PyQt5 import QtWidgets
from ventana import *
from tarifas import *
import var, conexion

class Rutas():
    '''
    Módulos gestión rutas
    '''

    def mostrarTarifas(self):
        try:
            var.dlgtarifas.show()
            conexion.Conexion.cargarTarifas(self)
        except Exception as error:
            print('Error mostrar ventana tarifas: %s: ' % str(error))
