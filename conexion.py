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
        tar = []
        query = QtSql.QSqlQuery()
        query.prepare('select * from tarifas')
        if query.exec_():
            while query.next():
                var.tarifas[0].setText(str(query.value(1)))
                tar.append(query.value(1))
                var.tarifas[1].setText(str(query.value(2)))
                tar.append(query.value(2))
                var.tarifas[2].setText(str(query.value(3)))
                tar.append(query.value(3))
                var.tarifas[3].setText(str(query.value(4)))
                tar.append(query.value(4))
        return tar

    def actualizaTarifas(self):
        try:
            nuevatarifa = []
            id = 1
            #CARGO LAS NUEVAS TARIFAS
            for i, dato in enumerate(var.tarifas):
                nuevatarifa.append('{0:.2f}'.format(float(dato.text())))
            #CARGO LAS NUEVAS TARIFAS EN LA BASE DE DATOS
            query = QtSql.QSqlQuery()
            query.prepare('update tarifas set local=:local, provincial=:provincial, regional =:regional, '
                          'nacional=:nacional where id =:id')
            query.bindValue(':id', int(id))
            query.bindValue(':local', (nuevatarifa[0]))
            query.bindValue(':provincial', (nuevatarifa[1]))
            query.bindValue(':regional', (nuevatarifa[2]))
            query.bindValue(':nacional', (nuevatarifa[3]))
            if query.exec_():
                QtWidgets.QMessageBox.information(None, 'Tarifas modificadas',
                                                  'Haga Click para Continuar')
            else:
                QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                              'Recuerde que las tarifas son únicas. Haga Click para Continuar')
        except Exception as error:
            print('Error actualizar tarifas: %s: ' % str(error))


    def selectTarifa(valor):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select * from tarifas')
            if query.exec_():
                while query.next():
                    if valor == 0:
                        return query.value(1)
                    elif valor == 1:
                        return query.value(2)
                    elif valor == 2:
                        return query.value(3)
                    elif valor == 3:
                        return query.value(4)
        except Exception as error:
            print('Error select tarifa %s' % str(error))


    def altaRuta(newruta):
        try:

            query = QtSql.QSqlQuery()
            query.prepare('insert into rutas (fecha, matricula, conductor, kmini, kmfin, tarifa) values (:fecha, :matricula, :conductor, :kmini, :kmfin, :tarifa)')
            query.bindValue(':fecha', newruta[0])
            query.bindValue(':matricula', newruta[1])
            query.bindValue(':conductor', newruta[2])
            query.bindValue(':kmini', newruta[3])
            query.bindValue(':kmfin', newruta[4])
            query.bindValue(':tarifa', newruta[5])

            if query.exec_():
                print('correcto')
            else:
                print('error alta ruta')

        except Exception as error:
            print('Error alta ruta en conexion' % str(error))

    def cargaRutas(self):
        try:
            index = 0
            kmt = 0
            total = 0.00
            query = QtSql.QSqlQuery()
            query.prepare('select * from rutas')
            if query.exec_():
                while query.next():
                    var.ui.tabRutas.setRowCount(index + 1)  # creo la fila
                    var.ui.tabRutas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tabRutas.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                    var.ui.tabRutas.setItem(index, 2, QtWidgets.QTableWidgetItem(query.value(2)))
                    var.ui.tabRutas.setItem(index, 3, QtWidgets.QTableWidgetItem(query.value(3)))
                    kmt = int(query.value(5)) - int(query.value(4))
                    var.ui.tabRutas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(kmt)))
                    var.ui.tabRutas.setItem(index, 5, QtWidgets.QTableWidgetItem(str(query.value(6))))
                    total = float(query.value(6)) * float(kmt)
                    var.ui.tabRutas.setItem(index, 6, QtWidgets.QTableWidgetItem(str(total)))
                    index = index + 1
        except Exception as error:
            print('Cargar rutas: %s: ' % str(error))


    def bajaRuta(numruta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from rutas where codigo = :numruta')
            query.bindValue(':numruta', int(numruta))
            if query.exec_():
                QtWidgets.QMessageBox.information(None, 'Ruta Eliminada',
                                                      'Haga Click para Continuar')

            else:
                QtWidgets.QMessageBox.warning(None, query.lastError().text(),
                                              'Haga Click para Continuar')


        except Exception as error:
            print('Baja ruta en conexion %s: ' % str(error))
