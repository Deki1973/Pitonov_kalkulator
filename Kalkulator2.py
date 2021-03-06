# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kalkulator2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
import podaci
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 420, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.pushButton_Jedan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Jedan.setGeometry(QtCore.QRect(10, 90, 60, 41))
        self.pushButton_Jedan.setObjectName("pushButton_Jedan")
        self.pushButton_Jedan.clicked.connect(self.jedan)


        self.pushButton_Dva = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dva.setGeometry(QtCore.QRect(70, 90, 60, 41))
        self.pushButton_Dva.setObjectName("pushButton_Dva")
        self.pushButton_Dva.clicked.connect(self.dva)

        self.pushButton_Tri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tri.setGeometry(QtCore.QRect(130, 90, 60, 41))
        self.pushButton_Tri.setObjectName("pushButton_Tri")
        self.pushButton_Tri.clicked.connect(self.tri)

        self.pushButton_Cetiri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cetiri.setGeometry(QtCore.QRect(10, 140, 60, 41))
        self.pushButton_Cetiri.setObjectName("pushButton_Cetiri")
        self.pushButton_Cetiri.clicked.connect(self.cetiri)

        self.pushButton_Pet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Pet.setGeometry(QtCore.QRect(70, 140, 60, 41))
        self.pushButton_Pet.setObjectName("pushButton_Pet")
        self.pushButton_Pet.clicked.connect(self.pet)

        self.pushButton_Sest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sest.setGeometry(QtCore.QRect(130, 140, 60, 41))
        self.pushButton_Sest.setObjectName("pushButton_Sest")
        self.pushButton_Sest.clicked.connect(self.sest)

        self.pushButton_Sedam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sedam.setGeometry(QtCore.QRect(10, 190, 60, 41))
        self.pushButton_Sedam.setObjectName("pushButton_Sedam")
        self.pushButton_Sedam.clicked.connect(self.sedam)

        self.pushButton_Osam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Osam.setGeometry(QtCore.QRect(70, 190, 60, 41))
        self.pushButton_Osam.setObjectName("pushButton_Osam")
        self.pushButton_Osam.clicked.connect(self.osam)

        self.pushButton_Devet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Devet.setGeometry(QtCore.QRect(130, 190, 60, 41))
        self.pushButton_Devet.setObjectName("pushButton_Devet")
        self.pushButton_Devet.clicked.connect(self.devet)

        self.pushButton_Nula = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Nula.setGeometry(QtCore.QRect(70, 240, 60, 41))
        self.pushButton_Nula.setObjectName("pushButton_Nula")
        self.pushButton_Nula.clicked.connect(self.nula)

        self.pushButton_Zapeta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Zapeta.setGeometry(QtCore.QRect(130, 240, 60, 41))
        self.pushButton_Zapeta.setObjectName("pushButton_Zapeta")
        self.pushButton_Zapeta.clicked.connect(self.zapeta)

        self.pushButton_Promeni_znak = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Promeni_znak.setGeometry(QtCore.QRect(10, 240, 60, 41))
        self.pushButton_Promeni_znak.setObjectName("pushButton_Promeni_znak")
        self.pushButton_Promeni_znak.clicked.connect(self.promeni_znak)

        self.pushButton_Sabiranje = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sabiranje.setGeometry(QtCore.QRect(200, 90, 111, 41))
        self.pushButton_Sabiranje.setObjectName("pushButton_1")
        self.pushButton_Sabiranje.clicked.connect(self.sabiranje)

        self.pushButton_Izracunaj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Izracunaj.setGeometry(QtCore.QRect(200, 140, 111, 41))
        self.pushButton_Izracunaj.setObjectName("pushButton_2")
        self.pushButton_Izracunaj.clicked.connect(self.izracunaj)

        self.pushButton_Obrisi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Obrisi.setGeometry(QtCore.QRect(320, 140, 111, 41))
        self.pushButton_Obrisi.setObjectName("pushButton_3")
        self.pushButton_Obrisi.clicked.connect(self.brisanje)
        print("pritisnuto dugme 3")

        self.pushButton_memorisi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_memorisi.setGeometry(QtCore.QRect(440, 140, 111, 41))
        self.pushButton_memorisi.setObjectName("pushButton_memorisi")
        self.pushButton_memorisi.clicked.connect(self.memorisi)


        self.pushButton_oduzimanje = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_oduzimanje.setGeometry(QtCore.QRect(320, 90, 111, 41))
        self.pushButton_oduzimanje.setObjectName("pushButton_oduzimanje")
        self.pushButton_oduzimanje.clicked.connect(self.oduzimanje)

        self.pushButton_mnozenje = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mnozenje.setGeometry(QtCore.QRect(440, 90, 111, 41))
        self.pushButton_mnozenje.setObjectName("pushButton_mnozenje")
        self.pushButton_mnozenje.clicked.connect(self.mnozenje)

        self.pushButton_deljenje = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deljenje.setGeometry(QtCore.QRect(560, 90, 111, 41))
        self.pushButton_deljenje.setObjectName("pushButton_deljenje")
        self.pushButton_deljenje.clicked.connect(self.deljenje)

        self.pushButton_memorija_pozovi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_memorija_pozovi.setGeometry(QtCore.QRect(560, 140, 111, 41))
        self.pushButton_memorija_pozovi.setObjectName("pushButton_pozovi_iz_memorije")
        self.pushButton_memorija_pozovi.clicked.connect(self.pozovi_iz_memorije)

        self.pushButton_PI=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PI.setGeometry(QtCore.QRect(200,190,111,41))
        self.pushButton_PI.setObjectName("pushButton_PI")
        self.pushButton_PI.clicked.connect(self.prikazi_PI)

        self.pushButton_stepenuj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stepenuj.setGeometry(QtCore.QRect(320, 190, 111, 41))
        self.pushButton_stepenuj.setObjectName("pushButton_stepenovanje")
        self.pushButton_stepenuj.clicked.connect(self.stepenuj)

        self.pushButton_Log10=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Log10.setGeometry(QtCore.QRect(440,190,111,41))
        self.pushButton_Log10.setObjectName("pushButton_Log10")
        self.pushButton_Log10.clicked.connect(self.logaritam_po_bazi_10)

        self.pushButton_LogN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LogN.setGeometry(QtCore.QRect(560, 190, 111, 41))
        self.pushButton_LogN.setObjectName("pushButton_LogE")
        self.pushButton_LogN.clicked.connect(self.logaritam_po_bazi_E)

        self.pushButton_SIN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SIN.setGeometry(QtCore.QRect(200, 240, 111, 41))
        self.pushButton_SIN.setObjectName("pushButton_SIN")
        self.pushButton_SIN.clicked.connect(self.sinus)

        self.pushButton_COS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_COS.setGeometry(QtCore.QRect(320, 240, 111, 41))
        self.pushButton_COS.setObjectName("pushButton_COS")
        self.pushButton_COS.clicked.connect(self.cosinus)

        self.pushButton_TAN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_TAN.setGeometry(QtCore.QRect(440, 240, 111, 41))
        self.pushButton_TAN.setObjectName("pushButton_TAN")
        self.pushButton_TAN.clicked.connect(self.tangens)

        self.pushButton_Reciproc=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reciproc.setGeometry(QtCore.QRect(560,240,111,41))
        self.pushButton_Reciproc.setObjectName("pushButton_Reciproc")
        self.pushButton_Reciproc.clicked.connect(self.reciproc)

        self.pushButton_Stepeni_u_radijane = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Stepeni_u_radijane.setGeometry(QtCore.QRect(440, 40, 111, 41))
        self.pushButton_Stepeni_u_radijane.setObjectName("pushButton_Step_u_rad")
        self.pushButton_Stepeni_u_radijane.clicked.connect(self.pretvori_stepene_u_radijane)

        self.pushButton_Radijani_u_stepene=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Radijani_u_stepene.setGeometry(QtCore.QRect(560,40,111,41))
        self.pushButton_Radijani_u_stepene.setObjectName("pushButton_Rad_u_step")
        self.pushButton_Radijani_u_stepene.clicked.connect(self.pretvori_radijane_u_stepene)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def sabiranje(self):
        p1.operand1=float(self.plainTextEdit.toPlainText())
        print(str(p1.operand1))
        p1.operator="plus"
        self.plainTextEdit.clear()
        self.plainTextEdit.setFocus()


    def oduzimanje(self):
        p1.operand1=float(self.plainTextEdit.toPlainText())
        print(str(p1.operand1))
        p1.operator="minus"
        self.plainTextEdit.clear()
        self.plainTextEdit.setFocus()

    def mnozenje(self):
        p1.operand1=float(self.plainTextEdit.toPlainText())
        print(str(p1.operand1))
        p1.operator="puta"
        self.plainTextEdit.clear()
        self.plainTextEdit.setFocus()

    def deljenje(self):
        p1.operand1=float(self.plainTextEdit.toPlainText())
        print(str(p1.operand1))
        p1.operator="kroz"
        self.plainTextEdit.clear()
        self.plainTextEdit.setFocus()

    def prikazi_PI(self):
        self.plainTextEdit.setPlainText(str(math.pi))

    def stepenuj(self):
        p1.operand1 = float(self.plainTextEdit.toPlainText())
        print(str(p1.operand1))
        p1.operator = "stepenovanje"
        self.plainTextEdit.clear()

    def logaritam_po_bazi_10(self):

        p1.operand1=float(self.plainTextEdit.toPlainText())
        if p1.operand1<0:
            p1.operand1=math.fabs(p1.operand1)
        #p1.operator="logaritam_po_10"
        p1.rezultat=float(math.log10(p1.operand1))
        self.plainTextEdit.setPlainText(str(p1.rezultat))

    def logaritam_po_bazi_E(self):
        p1.operand1=float(self.plainTextEdit.toPlainText())
        if p1.operand1<0:
            p1.operand1=math.fabs(p1.operand1)
        #p1.operator="logaritam_po_E"
        p1.rezultat=float(math.log(p1.operand1,math.e))
        self.plainTextEdit.setPlainText(str(p1.rezultat))

    def sinus(self):
        p1.operand1=float(self.plainTextEdit.toPlainText())
        p1.rezultat=float(math.sin(p1.operand1))
        self.plainTextEdit.setPlainText(str(p1.rezultat))

    def cosinus(self):
        p1.operand1=float(self.plainTextEdit.toPlainText())
        p1.rezultat=float(math.cos(p1.operand1))
        self.plainTextEdit.setPlainText(str(p1.rezultat))

    def tangens(self):
        p1.operand1 = float(self.plainTextEdit.toPlainText())
        p1.rezultat=float(math.tan(p1.operand1))
        self.plainTextEdit.setPlainText(str(p1.rezultat))

    def reciproc(self):
        p1.operand1 = float(self.plainTextEdit.toPlainText())
        if p1.operand1 != 0:
            p1.rezultat=(float(math.pow(p1.operand1,-1)))
            self.plainTextEdit.setPlainText(str(p1.rezultat))
        else:
            self.plainTextEdit.setPlainText("NE MOZETE DELITI NULOM!")

    def pretvori_stepene_u_radijane(self):
        p1.operand1 = float(self.plainTextEdit.toPlainText())
        p1.rezultat=(float(math.radians(p1.operand1)))
        self.plainTextEdit.setPlainText(str(p1.rezultat))

    def pretvori_radijane_u_stepene(self):
        p1.operand1 = float(self.plainTextEdit.toPlainText())
        p1.rezultat = (float(math.degrees(p1.operand1)))
        self.plainTextEdit.setPlainText(str(p1.rezultat))

    def izracunaj(self):
        p1.operand2=float(self.plainTextEdit.toPlainText())
        #print(str(p1.operand2))
        try:
            if p1.operator=="plus":
                p1.rezultat=p1.operand1+p1.operand2
            elif p1.operator=="minus":
                p1.rezultat = p1.operand1 - p1.operand2
            elif p1.operator=="puta":
                p1.rezultat=p1.operand1 * p1.operand2
            elif p1.operator=="kroz":
                if p1.operand2==0:
                    self.plainTextEdit.setPlainText("NE MOZE SE DELITI NULOM!")
                else:
                    p1.rezultat=p1.operand1 / p1.operand2
            elif p1.operator=="stepenovanje":
                p1.rezultat=math.pow(p1.operand1,p1.operand2)
            self.plainTextEdit.setPlainText(str(p1.rezultat))
        except:
            self.plainTextEdit.setPlainText("GRESKA!")


    def memorisi(self):
        p1.memorija=float(self.plainTextEdit.toPlainText())
        print(str(p1.memorija))

    def pozovi_iz_memorije(self):
        print("POZOVI IZ MEMORIJE")
        print(str(p1.memorija))
        self.plainTextEdit.setPlainText(str(p1.memorija))

    def brisanje(self):
        self.plainTextEdit.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KALKULATOR"))
        self.pushButton_Sabiranje.setText(_translate("MainWindow", "+"))
        self.pushButton_Izracunaj.setText(_translate("MainWindow", "="))
        self.pushButton_Obrisi.setText(_translate("MainWindow", "DEL"))
        self.pushButton_memorisi.setText(_translate("MainWindow", "MEM"))
        self.pushButton_oduzimanje.setText(_translate("MainWindow", "-"))
        self.pushButton_mnozenje.setText(_translate("MainWindow", "*"))
        self.pushButton_deljenje.setText(_translate("MainWindow", "/"))
        self.pushButton_stepenuj.setText(_translate("MainWindow", "x^y"))
        self.pushButton_memorija_pozovi.setText(_translate("MainWindow","M_POZOVI"))
        self.pushButton_PI.setText(_translate("MainWindow","PI"))
        self.pushButton_Log10.setText(_translate("MainWindow","Log10"))
        self.pushButton_LogN.setText(_translate("MainWindow","LogN"))
        self.pushButton_SIN.setText(_translate("MainWindow","SIN"))
        self.pushButton_COS.setText(_translate("MainWindow", "COS"))
        self.pushButton_TAN.setText(_translate("MainWindow", "TAN"))
        self.pushButton_Reciproc.setText(_translate("MainWindow","1/X"))
        self.pushButton_Stepeni_u_radijane.setText(_translate("MainWindow","DEG -> RAD"))
        self.pushButton_Radijani_u_stepene.setText(_translate("MainWindow","RAD -> DEG"))
        self.pushButton_Jedan.setText(_translate("MainWindow","1"))
        self.pushButton_Dva.setText(_translate("MainWindow", "2"))
        self.pushButton_Tri.setText(_translate("MainWindow", "3"))
        self.pushButton_Cetiri.setText(_translate("MainWindow", "4"))
        self.pushButton_Pet.setText(_translate("MainWindow", "5"))
        self.pushButton_Sest.setText(_translate("MainWindow", "6"))
        self.pushButton_Sedam.setText(_translate("MainWindow", "7"))
        self.pushButton_Osam.setText(_translate("MainWindow", "8"))
        self.pushButton_Devet.setText(_translate("MainWindow", "9"))
        self.pushButton_Promeni_znak.setText(_translate("MainWindow","+/-"))
        self.pushButton_Zapeta.setText(_translate("MainWindow",","))
        self.pushButton_Nula.setText(_translate("MainWindow","0"))

    def jedan(self):
        self.plainTextEdit.insertPlainText("1")

    def dva(self):
        self.plainTextEdit.insertPlainText("2")

    def tri(self):
        self.plainTextEdit.insertPlainText("3")
    def cetiri(self):
        self.plainTextEdit.insertPlainText("4")

    def pet(self):
        self.plainTextEdit.insertPlainText("5")
    def sest(self): self.plainTextEdit.insertPlainText("6")
    def sedam(self): self.plainTextEdit.insertPlainText("7")
    def osam(self): self.plainTextEdit.insertPlainText("8")
    def devet(self): self.plainTextEdit.insertPlainText("9")
    def nula(self): self.plainTextEdit.insertPlainText("0")
    def zapeta(self):self.plainTextEdit.insertPlainText(".")
    def promeni_znak(self):
        znak1=float(self.plainTextEdit.toPlainText())
        znak1=(-1) * znak1
        self.plainTextEdit.setPlainText(str(znak1))




if __name__ == "__main__":
    import sys
    p1=podaci.podaci()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
