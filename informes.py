from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyQt5 import QtSql
from datetime import datetime, date
import os, var, random

class Informes:

    def cabecera(self):
        try:
            logo = '.\\img\icono.png'
            var.informe.drawImage(logo, 450, 760)
            var.informe.setFont('Helvetica-Bold', size=12)
            var.titulo = 'LISTADO RUTAS'
            var.informe.drawCentredString(300,750,var.titulo)
            var.informe.line(40,740,525,740)
            var.informe.line(40,735,525,735)
            var.informe.setFont('Helvetica-Bold', size=16)
            var.informe.drawString(50, 790, 'TRANSPORTES TEIS')

        except Exception as error:
            print("Error cabecera informe: %s" % str(error))

    def informeRutas(self):
        try:
            informe = random.randint(1,1000000)

            var.informe = canvas.Canvas('reportes/' + str(informe) + '.pdf', pagesize=A4)
            Informes.cabecera(self)
            Informes.pie(self)
            var.informe.setFont('Helvetica-Bold', size=10)
            var.informe.drawString(45,720, 'Cod.')
            var.informe.drawString(85, 720, 'Fecha')
            var.informe.drawString(135, 720, 'Matrícula')
            var.informe.drawString(215, 720, 'Conductor')
            var.informe.drawString(325, 720, 'KmIni')
            var.informe.drawString(375, 720, 'KmFin')
            var.informe.drawString(410, 720, 'Tarifa (€/km)')
            var.informe.drawString(475, 720, 'TOTAL')
            var.informe.line(40, 715, 525, 715)
            var.informe.line(40, 740, 40, 60)
            var.informe.line(525,740,525,60)

            rootPath = '.\\reportes'
            cont = 0
            total = 0.00
            iva = 0.00
            query = QtSql.QSqlQuery()
            query.prepare('select * from rutas')
            if query.exec_():
                i = 50
                j = 690  # altura desde donde empieza a listar
                while query.next():
                    if j <= 80:
                        var.informe.drawString(440,70, 'Página siguiente...')

                    var.informe.setFont('Helvetica', size = 10)
                    var.informe.drawCentredString(i, j, str(query.value(0)))
                    var.informe.drawRightString(i + 70, j, str(query.value(1)))
                    var.informe.drawString(i + 80, j, str(query.value(2)))
                    var.informe.drawString(i + 150, j, str(query.value(3)))
                    var.informe.drawRightString(i + 300, j, str(query.value(4)))
                    var.informe.drawRightString(i + 350, j, str(query.value(5)))
                    var.informe.drawRightString(i + 390, j, str(query.value(6)))
                    kmt = int(query.value(5)) - int(query.value(4))
                    tarifatotal = float(kmt) * float(query.value(6))
                    var.informe.drawRightString(i + 460, j, str('{0:.2f}'.format(float(tarifatotal)) + ' €'))
                    #van el resto de los values
                    j = j-25
                    total = float(total) + float(tarifatotal)
                iva = float(total) * 0.21
                var.informe.setFont('Helvetica-Bold', size=12)
                var.informe.line(40, 130, 525, 130)
                var.informe.line(380,130,380,60)
                var.informe.drawRightString(495, 110, 'IVA:     ' + ('{0:.2f}'.format(iva))+ ' €')
                var.informe.drawRightString(495, 90, 'TOTAL:     ' + ('{0:.2f}'.format(total)) + ' €')
                var.informe.setFont('Helvetica-Oblique', size=7)
                var.informe.drawAlignedString(95,125, 'Observaciones')
            var.informe.save()
            for file in os.listdir(rootPath):
                if file.endswith(str(informe) + '.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont += 1
        except Exception as error:
            print("Error cuerpo informe: %s" % str(error))

    def pie(self):
        try:
            var.informe.line(40,60,525,60)
            dia = datetime.now().day
            mes = datetime.now().month
            ano = datetime.now().year
            var.informe.setFont('Helvetica-Oblique', size=8)
            var.informe.drawString(250, 50, var.titulo)
            var.informe.drawString(460, 50, str(dia) + '/' + str(mes) + '/' + str(ano))
        except Exception as error:
            print("Error pie informe: %s" % str(error))