from ventana import *
import var, conexion


class Eventos():
    '''
    Eventos del programa. Xestión Furgonetas
    '''
    def matCapital():
        '''
        Pone en mayúscular la matrícular
        :return:
        :rtype:
        '''
        matricula = var.ui.txtMatricula.text()
        marca = var.ui.txtMarca.text()
        var.ui.txtMatricula.setText(matricula.upper())



    def cargaFurgo(self):
        furgo = [var.ui.txtMatricula, var.ui.txtMarca, var.ui.txtModelo]
        for i in furgo:
            var.newfurgo.append(i.text())
        conexion.Conexion.altaFurgo(var.newfurgo)

