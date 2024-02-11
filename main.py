import math
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from trest import Ui_PhysicsMath
from fiz_Mex import Ui_Physics
from Math_Alg import Ui_Math
from Math_TF import Ui_TipeMath
from Fiz_TF import Ui_TipeFiz

app = QtWidgets.QApplication(sys.argv)
PhysicsMath = QtWidgets.QMainWindow()
ui = Ui_PhysicsMath()
ui.setupUi(PhysicsMath)
PhysicsMath.show()


def openPhysics():
    global TipeFiz
    TipeFiz = QtWidgets.QMainWindow()
    ui = Ui_TipeFiz()
    ui.setupUi(TipeFiz)
    TipeFiz.show()
    def Mex():

        print("Mex")
        TipeFiz.close()
        global T_Phiz_Max
        T_Phiz_Max = QtWidgets.QMainWindow()
        ui = Ui_Physics()
        ui.setupUi(T_Phiz_Max)
        T_Phiz_Max.show()



    def Termo():
        print("Termo")
    def Electro():
        print("Electro")
    def Optic():
        print("Optic")
    def Voln():
        print("Voln")
    def Spravoch():
        print("Spravoc")

    ui.pushButton.clicked.connect(Mex)
    ui.pushButton_5.clicked.connect(Termo)
    ui.pushButton_2.clicked.connect(Electro)
    ui.pushButton_4.clicked.connect(Optic)
    ui.pushButton_3.clicked.connect(Voln)
    ui.pushButton_6.clicked.connect(Spravoch)


def openMath():
    global TipeMath
    TipeMath = QtWidgets.QMainWindow()
    ui = Ui_TipeMath()
    ui.setupUi(TipeMath)
    TipeMath.show()
    def Algebra():
        print("Algebra")
        TipeMath.close()
        global T_Math_Alg
        T_Math_Alg = QtWidgets.QMainWindow()
        ui = Ui_Math()
        ui.setupUi(T_Math_Alg)
        T_Math_Alg.show()


    def Geometry():
        print("Geometry")
    def Teoria():
        print("Spravoc")

    ui.pushButton.clicked.connect(Algebra)
    ui.pushButton_2.clicked.connect(Geometry)
    ui.pushButton_3.clicked.connect(Teoria)


ui.pushButton_3.clicked.connect(openPhysics)
ui.pushButton_2.clicked.connect(openMath)


sys.exit(app.exec_())