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


    def altaRuta(self):
           try:
               newruta = []
               newruta.append(var.ui.txtFecha.text())
               newruta.append(var.ui.cmbMat.currentText())
               newruta.append(var.ui.cmbCon.currentText())
               newruta.append(var.ui.txtKmi.text())
               newruta.append(var.ui.txtKmf.text())
               if var.ui.rbtLocal.isChecked():
                   tarifa = conexion.Conexion.selectTarifa(0)
               elif var.ui.rbtProvincial.isChecked():
                   tarifa = conexion.Conexion.selectTarifa(1)
               elif var.ui.rbtRegional.isChecked():
                   tarifa = conexion.Conexion.selectTarifa(2)
               elif var.ui.rbtNacional.isChecked():
                   tarifa = conexion.Conexion.selectTarifa(3)
               newruta.append(float(tarifa))
               conexion.Conexion.altaRuta(newruta)
               print(newruta)

                #conexion.Conexion.altaRuta(newruta)

           except Exception as error:
               print('Error alta Ruta en eventos %s' % str(error))