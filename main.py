from ventana import *
import sys, conexion, var, eventos

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        '''
        Genera y conecta todos los eventos.
        '''
        super(Main,self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Conexión a la base de datos.
        '''
        conexion.Conexion.db_connect(self)
        conexion.Conexion.listarFurgo(self)

        '''
        llamadas a los eventos de los botones
        '''
        var.ui.btnGrabar.clicked.connect(eventos.Eventos.cargaFurgo)
        var.ui.txtMatricula.editingFinished.connect(eventos.Eventos.matCapital)
        var.ui.btnReload.clicked.connect(eventos.Eventos.limpiaFurgo)
        var.ui.btnEliminar.clicked.connect(eventos.Eventos.bajaFurgo)
        var.ui.btnModificar.clicked.connect(eventos.Eventos.modifFurgo)
        var.ui.btnAltacon.clicked.connect(eventos.Eventos.altaCon)

        '''
        eventos de las tablas
        '''
        var.ui.tabFurgo.clicked.connect(eventos.Eventos.datosUnoFurgo)
        var.ui.tabFurgo.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.setFixedSize(1024,768)
    window.show()
    sys.exit(app.exec())

