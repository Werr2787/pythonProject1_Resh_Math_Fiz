import sys #Этот модуль предоставляет доступ к некоторым переменным, используемым или поддерживаемым интерпретатором Python.
from PyQt5.QtWidgets import *  #Это модули PyQt5, библиотеки для создания графических пользовательских интерфейсов (GUI) в Python.
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow):# Определяет класс MainWindow, который является подклассом QMainWindow из библиотеки PyQt5.
    def __init__(self): #Конструктор класса, который выполняется при создании нового объекта этого класса.
        super().__init__()

        self.menu_bar = QMenuBar(self) #Создает строку меню и привязывает ее к главному окну.
        self.menu = QMenu('Subject', self) #Создает меню с названием "Subject" и привязывает его к главному окну.
        self.menu_bar.addMenu(self.menu)

        self.math_action = self.menu.addAction('Mathematics')#Создает действие "Mathematics" в меню для выбора темы математики.
        self.math_action.triggered.connect(self.show_math_window) #Привязывает метод show_math_window к событию "Mathematics" (при выборе этого пункта меню).
        self.physics_action = self.menu.addAction('Physics') #Создает действие "Physics" в меню для выбора темы физики.
        self.physics_action.triggered.connect(self.show_physics_window) #Привязывает метод show_physics_window к событию "Physics".

    # self.physics_action = self.menu.addAction('Physics'): Создает действие "Physics" вменю для выбора темы физики.
    # self.physics_action.triggered.connect(self.show_physics_window): Привязывает метод show_physics_window к событию "Physics".
    def show_math_window(self):
        self.math_window = MathWindow()
        self.math_window.show()

    def show_physics_window(self):
        self.physics_window = PhysicsWindow()
        self.physics_window.show()

class MathWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.combo_box = QComboBox(self)
        self.combo_box.addItem('Topic 1')
        self.combo_box.addItem('Topic 2')
        # ... add more topics

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.combo_box)

class Ui_Math(object):
    def setupUi(self, Math):
        Math.setObjectName("Math")
        Math.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Math)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 70, 271, 22))
        self.comboBox.setObjectName("comboBox")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(100, 140, 291, 131))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 129))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Math.setCentralWidget(self.centralwidget)

        self.retranslateUi(Math)
        QtCore.QMetaObject.connectSlotsByName(Math)

    def retranslateUi(self, Math):
        _translate = QtCore.QCoreApplication.translate
        Math.setWindowTitle(_translate("Math", "Math"))

class PhysicsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.combo_box = QComboBox(self)
        self.combo_box.addItem('Topic 1')
        self.combo_box.addItem('Topic 2')
        # ... add more topics

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.combo_box)

if __name__ == '__main__': #Этот блок выполняется только в том случае, если файл запускается как основная программа (а не импорт).
    app = QApplication(sys.argv)
    window = MainWindow() #Создает главное окно.
    window.show() #Отображает главное окно.
    sys.exit(app.exec_()) #Запускает цикл событий приложения.