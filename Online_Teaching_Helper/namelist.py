# -*-coding:utf-8-*-
import sys
import config
import requests
from PyQt5.QtGui import QKeyEvent, QKeySequence, QPixmap, QStandardItemModel, QStandardItem
from in_class_teacher import In_class_teacher
from main_teacher_ui import Ui_MainWindow
from new_class import New_Class
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtWidgets import *
from namelist_ui import Ui_Dialog

class Namelist(QDialog,Ui_Dialog):
    def __init__(self):
        super(Namelist, self).__init__()
        self.setupUi(self)
        self.show()
        self.setTable()
        #绑定事件
        self.pushButton.clicked.connect(self.query)

        '''Tbale 绑定'''
    def setTable(self):
        # 初始化表格
        self.class_table_model = QStandardItemModel(4, 2)
        self.class_table_model.setHorizontalHeaderLabels(["学生学号", "学生姓名"])
        #self.classTable.setModel(self.class_table_model)
        # !!!!!这一句，平衡表格
        self.classTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '退出', '是否退出程序？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()

    def query(self):
        classID=self.lineEdit.text()
        nameList_url = 'http://{}:5000/namelist/{}'
        url = nameList_url.format(config.IP, classID)
        response = requests.get(url)
        d = response.json()
        # 填充表格
        # row=self.classTable
        row = 0
        clu = 1
        for key in d:
            t = d[key]
            for i in range(2):
                item = QStandardItem(str(t[i]))
                self.class_table_model.setItem(row, i, item)
            row += 1
        self.classTable.setModel(self.class_table_model)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    action = Namelist()
    sys.exit(app.exec_())