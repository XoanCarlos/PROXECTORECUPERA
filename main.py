from ventana import *
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        '''
        Genera y conecta todos los eventos.
        '''
        super(Main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.setFixedSize(1024,768)
    window.show()
    sys.exit(app.exec())

