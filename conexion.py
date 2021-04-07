from PyQt5 import QtWidgets, QtSql

class Conexion():
    def db_connect(self):
        filename = 'logista.db'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la BBDD',
                                           'Imposible Conexión.\n' 'Haga Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:

            QtWidgets.QMessageBox.warning(None, 'Abierta Base de Datos',
                                           'Haga Click para Continuar')

            print('Conexion Establecida')


    '''
    Funciones xestión furgonetas
    '''
    def altaFurgo(newfurgo):
        query = QtSql.QSqlQuery()
        query.prepare('insert into furgoneta (matricula, marca, modelo)'
                      'VALUES (:matricula, :marca, :modelo)')
        query.bindValue(':matricula',str(newfurgo[0]))
        query.bindValue(':marca', str(newfurgo[1]))
        query.bindValue(':modelo', str(newfurgo[2]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Alta Furgoneta Correcta',
                                          'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')
