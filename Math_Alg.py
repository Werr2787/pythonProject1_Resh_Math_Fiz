# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Math.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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


