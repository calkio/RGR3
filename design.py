# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\projectsPy\RGR3\disain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_value = QtWidgets.QTextEdit(self.centralwidget)
        self.input_value.setGeometry(QtCore.QRect(20, 70, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_value.setFont(font)
        self.input_value.setObjectName("input_value")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 130, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.func_g = QtWidgets.QComboBox(self.centralwidget)
        self.func_g.setGeometry(QtCore.QRect(480, 180, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.func_g.setFont(font)
        self.func_g.setObjectName("func_g")
        self.func_g.addItem("")
        self.func_g.addItem("")
        self.func_g.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 280, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.avg_Y = QtWidgets.QTextEdit(self.centralwidget)
        self.avg_Y.setGeometry(QtCore.QRect(20, 340, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.avg_Y.setFont(font)
        self.avg_Y.setObjectName("avg_Y")
        self.cko_Y = QtWidgets.QTextEdit(self.centralwidget)
        self.cko_Y.setGeometry(QtCore.QRect(450, 340, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cko_Y.setFont(font)
        self.cko_Y.setObjectName("cko_Y")
        self.decide = QtWidgets.QPushButton(self.centralwidget)
        self.decide.setGeometry(QtCore.QRect(20, 110, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.decide.setFont(font)
        self.decide.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decide.setObjectName("decide")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите числа через пробел:"))
        self.label_2.setText(_translate("MainWindow", "Выберете функцию g(X):"))
        self.func_g.setItemText(0, _translate("MainWindow", "log(x)"))
        self.func_g.setItemText(1, _translate("MainWindow", "2^x"))
        self.func_g.setItemText(2, _translate("MainWindow", "e^x"))
        self.label_3.setText(_translate("MainWindow", "Cреднее значение функции Y"))
        self.label_4.setText(_translate("MainWindow", "Дисперсия функции Y"))
        self.decide.setText(_translate("MainWindow", "Решить"))
