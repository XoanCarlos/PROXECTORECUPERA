from PyQt5 import QtWidgets, QtSql
from ventana import *
from tarifas import *
import var

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

    def listarFurgo(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select matricula, marca, modelo from furgoneta')
        if query.exec_():
            while query.next():
                var.ui.tabFurgo.setRowCount(index+1) #creo la fila
                var.ui.tabFurgo.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tabFurgo.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                var.ui.tabFurgo.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                index += 1
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def deleteFurgo(matricula):
        query = QtSql.QSqlQuery()
        query.prepare('delete from furgoneta where matricula = :matricula')
        query.bindValue(':matricula', str(matricula))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Furgoneta Eliminada',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def modifFurgo(furgomodif):
        query = QtSql.QSqlQuery()
        print(furgomodif)
        query.prepare('update furgoneta set marca=:marca, modelo=:modelo'
                      ' where matricula=:matricula')
        query.bindValue(':marca',str(furgomodif[1]))
        query.bindValue(':modelo', str(furgomodif[2]))
        query.bindValue(':matricula', str(furgomodif[0]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Furgoneta Modificada',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Recuerde que no puede modificar la matrícula. Haga Click para Continuar')


    '''
    Gestión conductores
    '''
    def nuevoCon(newcon):
        query = QtSql.QSqlQuery()
        query.prepare('insert into conductor (dni, nombre) '
                      'VALUES (:dni, :nombre)')
        query.bindValue(':dni',str(newcon[0]))
        query.bindValue(':nombre', str(newcon[1]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Alta Conductor?',
                                          'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def listarCon(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, nombre from conductor')
        if query.exec_():
            while query.next():
                var.ui.tabConductor.setRowCount(index+1) #creo la fila
                var.ui.tabConductor.setItem(index, 0, QtWidgets.QTableWidgetItem(query.value(0)))
                var.ui.tabConductor.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                index += 1
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def deleteCon(dni):
        query = QtSql.QSqlQuery()
        query.prepare('delete from conductor where dni = :dni')
        query.bindValue(':dni', str(dni))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Conductor Eliminado',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Haga Click para Continuar')

    def modifCon(conmodif):
        query = QtSql.QSqlQuery()
        query.prepare('update conductor set nombre=:nombre '
                      ' where dni=:dni')
        query.bindValue(':nombre', str(conmodif[1]))
        query.bindValue(':dni', str(conmodif[0]))
        if query.exec_():
            QtWidgets.QMessageBox.information(None, 'Conductor Modificada',
                                              'Haga Click para Continuar')
        else:
            QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                          'Recuerde que no puede modificar la matrícula. Haga Click para Continuar')

    def cargarCmbC(cmbCon):
        cmbCon.clear()
        cmbCon.addItem('')
        query =QtSql.QSqlQuery()
        query.prepare('select nombre from conductor')
        if query.exec_():
            while query.next():
                cmbCon.addItem(str(query.value(0)))

    def cargarCmbM(cmbMat):
        cmbMat.clear()
        cmbMat.addItem('')
        query = QtSql.QSqlQuery()
        query.prepare('select matricula from furgoneta')
        if query.exec_():
            while query.next():
                cmbMat.addItem(str(query.value(0)))

    def cargarTarifas(self):
        query = QtSql.QSqlQuery()
        query.prepare('select * from tarifas')
        if query.exec_():
            while query.next():
                var.tarifas[0].setText(str(query.value(0)) + ' €/km')
                var.tarifas[1].setText(str(query.value(1)) + ' €/km')
                var.tarifas[2].setText(str(query.value(2)) + ' €/km')
                var.tarifas[3].setText(str(query.value(3)) + ' €/km')


    def actualizaTarifas(self):
        nuevatarifa = []
        print('hola')
        for i, dato in enumerate(var.tarifas):
            nuevatarifa.append(dato.text())
        print(nuevatarifa)
        query = QtSql.QSqlQuery()
        query.prepare('update tarifas set local=:local, provincial=:provincial, regional =:regional',
                      ' nacional=:nacional')
        query.bindValue(':local', '{0:.2f}'.format(float(nuevatarifa[0])))
        query.bindValue(':provincial', '{0:.2f}'.format(float(nuevatarifa[1])))
        query.bindValue(':regional', '{0:.2f}'.format(float(nuevatarifa[2])))
        query.bindValue(':nacional', '{0:.2f}'.format(float(nuevatarifa[3])))
