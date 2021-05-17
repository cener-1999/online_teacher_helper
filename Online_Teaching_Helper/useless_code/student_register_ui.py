# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_register.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.setWindowIcon(QIcon('../image/ICO.ico'))
        Dialog.resize(323, 442)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 421))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(60, 120, 151, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.no1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.no1.setContentsMargins(0, 0, 0, 0)
        self.no1.setObjectName("no1")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.no1.addWidget(self.label_8)
        self.class_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.class_Edit.setObjectName("class_Edit")
        self.no1.addWidget(self.class_Edit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 170, 151, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.no2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.no2.setContentsMargins(0, 0, 0, 0)
        self.no2.setObjectName("no2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.no2.addWidget(self.label_6)
        self.ID_studentEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.ID_studentEdit.setObjectName("ID_studentEdit")
        self.no2.addWidget(self.ID_studentEdit)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 270, 151, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.no4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.no4.setContentsMargins(0, 0, 0, 0)
        self.no4.setObjectName("no4")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.no4.addWidget(self.label_9)
        self.passwdEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.passwdEdit.setObjectName("passwdEdit")
        self.no4.addWidget(self.passwdEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 220, 151, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.no3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.no3.setContentsMargins(0, 0, 0, 0)
        self.no3.setObjectName("no3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.no3.addWidget(self.label_5)
        self.nameEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.no3.addWidget(self.nameEdit)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 320, 181, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.passwd_comfirmEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.passwd_comfirmEdit.setObjectName("passwd_comfirmEdit")
        self.horizontalLayout_6.addWidget(self.passwd_comfirmEdit)
        self.registerBtn = QtWidgets.QPushButton(self.groupBox)
        self.registerBtn.setGeometry(QtCore.QRect(130, 380, 93, 28))
        self.registerBtn.setObjectName("registerBtn")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../image/student.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.warnning = QtWidgets.QLabel(self.groupBox)
        self.warnning.setEnabled(True)
        self.warnning.setGeometry(QtCore.QRect(220, 290, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.warnning.setFont(font)
        self.warnning.setMouseTracking(True)
        self.warnning.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.warnning.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.warnning.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.warnning.setTextFormat(QtCore.Qt.AutoText)
        self.warnning.setScaledContents(False)
        self.warnning.setWordWrap(True)
        self.warnning.setObjectName("warnning")
        self.warnning.setVisible(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注册"))
        self.groupBox.setTitle(_translate("Dialog", "学生注册"))
        self.label_8.setText(_translate("Dialog", "班级"))
        self.label_6.setText(_translate("Dialog", "学号"))
        self.label_9.setText(_translate("Dialog", "密码"))
        self.label_5.setText(_translate("Dialog", "姓名"))
        self.label_10.setText(_translate("Dialog", "确认密码"))
        self.registerBtn.setText(_translate("Dialog", "确认注册"))
        self.warnning.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" color:#ff0000;\">输入密码不一致</span></p></body></html>"))

