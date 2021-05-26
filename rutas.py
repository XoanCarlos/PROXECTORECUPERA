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


    def cargaRuta(self):
           try:
               newruta = []
               newruta.append(var.ui.txtFecha.text())
               newruta.append(var.ui.cmbMat.currentText())
               newruta.append(var.ui.cmbCon.currentText())
               newruta.append(int(var.ui.txtKmi.text()))
               newruta.append(int(var.ui.txtKmf.text()))
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
               conexion.Conexion.cargaRutas(self)
                #conexion.Conexion.altaRuta(newruta)
           except Exception as error:
               print('Error alta Ruta en rutas %s' % str(error))

    def cargaUnaRuta(self):
        try:
            fila = var.ui.tabRutas.selectedItems()  #seleccionar la fila
            if fila:
                fila = [dato.text() for dato in fila]
            var.ui.lblRuta.setText(str(fila[0]))
            var.ui.txtFecha.setText(str(fila[1]))
            var.ui.cmbMat.setCurrentText(str(fila[2]))
            var.ui.cmbCon.setCurrentText(str(fila[3]))
            var.ui.lblKmtotal.setText(str(fila[4]))
            var.ui.lblPrecio.setText(str(fila[6]))

        except Exception as error:
            print('Cargar una ruta: %s: ' % str(error))

    def bajaRuta(self):
        try:
            numruta = int(var.ui.lblRuta.text())
            conexion.Conexion.bajaRuta(numruta)
            conexion.Conexion.cargaRutas(self)


        except Exception as error:
            print('Error baja ruta en rutas %s: ' % str(error))

