# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_class.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_EnterClass(object):
    def setupUi(self, EnterClass):
        EnterClass.setObjectName("EnterClass")
        self.setWindowIcon(QIcon('image/ICO.ico'))
        EnterClass.resize(259, 141)
        EnterClass.setMouseTracking(False)
        EnterClass.setAutoFillBackground(False)
        EnterClass.setSizeGripEnabled(False)
        self.label = QtWidgets.QLabel(EnterClass)
        self.label.setGeometry(QtCore.QRect(20, 40, 72, 15))
        self.label.setObjectName("label")
        self.idEdit = QtWidgets.QLineEdit(EnterClass)
        self.idEdit.setGeometry(QtCore.QRect(90, 30, 131, 31))
        self.idEdit.setStyleSheet("\n""background-color: rgb(255, 255, 255);")
        self.idEdit.setObjectName("idEdit")
        self.class_beginBtn = QtWidgets.QPushButton(EnterClass)
        self.class_beginBtn.setGeometry(QtCore.QRect(80, 90, 93, 28))
        self.class_beginBtn.setStyleSheet("\n""background-color: rgb(255, 255, 255);")
        self.class_beginBtn.setObjectName("class_beginBtn")

        self.retranslateUi(EnterClass)
        QtCore.QMetaObject.connectSlotsByName(EnterClass)

    def retranslateUi(self, EnterClass):
        _translate = QtCore.QCoreApplication.translate
        EnterClass.setWindowTitle(_translate("EnterClass", "进入课堂"))
        self.label.setText(_translate("EnterClass", "课堂码"))
        self.class_beginBtn.setText(_translate("EnterClass", "进入课堂"))
