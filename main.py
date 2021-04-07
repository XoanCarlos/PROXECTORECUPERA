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
        conexion.Conexion.mostrarFurgo(self)

        '''
        llamadas a los eventos de los botones
        '''
        var.ui.btnGrabar.clicked.connect(eventos.Eventos.cargaFurgo)
        var.ui.txtMatricula.editingFinished.connect(eventos.Eventos.matCapital)
        var.ui.tabFurgo.clicked.connect(conexion.Conexion.datosUnaFurgo)
        var.ui.tabFurgo.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.setFixedSize(1024,768)
    window.show()
    sys.exit(app.exec())

