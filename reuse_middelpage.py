# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reuse_middelpage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(832, 884)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 700))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 813, 1000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 1000))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setGeometry(QtCore.QRect(150, 40, 471, 181))
        self.widget_2.setStyleSheet("background-color: rgb(220, 223, 231);")
        self.widget_2.setObjectName("widget_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(150, 250, 471, 181))
        self.widget_4.setStyleSheet("background-color: rgb(220, 223, 231);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

