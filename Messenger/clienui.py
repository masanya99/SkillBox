# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 191, 51))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(62, 60, 641, 31))
        self.name.setObjectName("name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_2.setObjectName("label_2")
        self.messages = QtWidgets.QTextBrowser(self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(10, 110, 781, 351))
        self.messages.setObjectName("messages")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 480, 631, 81))
        self.text.setObjectName("text")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(650, 480, 113, 81))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(50)
        self.send.setFont(font)
        self.send.setObjectName("send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cool Messenger"))
        self.name.setPlaceholderText(_translate("MainWindow", "Input your name"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.text.setPlaceholderText(_translate("MainWindow", "Input text"))
        self.send.setText(_translate("MainWindow", ">"))

