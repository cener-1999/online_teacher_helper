# -*-coding:utf-8-*-

# 功能：应该是一个线程管理器，可以统一结束线程，可以显示子线程的信息，可以统计
# 时间模块已经很好实现

import sys
import config
import requests
from PyQt5.QtGui import QKeyEvent, QKeySequence, QPixmap, QStandardItemModel, QStandardItem

from in_class_teacher_ui import Ui_Dialog
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent, QTime
from PyQt5.QtWidgets import *

class In_class_teacher(QDialog,Ui_Dialog):
    def __init__(self):
        super(In_class_teacher, self).__init__()
        self.setupUi(self)
        self.setTable()
        self.show()
        self.timer=QTime()

        "用Qtimer加一个刷新显示数据库"
        # 绑定事件
        #self.timer.timeout.connect(self.reflesh)
        self.endClassBtn.clicked.connect(self.endClass)
        object = QObject()
        # 事件过滤器，防止挂掉

    def setTable(self):
        # 初始化表格
        self.class_table_model = QStandardItemModel(4, 2)
        self.class_table_model.setHorizontalHeaderLabels(["学生学号", "学生姓名"])
        # self.classTable.setModel(self.class_table_model)
        # !!!!!这一句，平衡表格
        self.signinTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def reflesh(self):
        #reportID由上一个窗口获得
        reportID=6
        showsign_url = 'http://{}:5000/sign/{}'
        url = showsign_url.format(config.IP, reportID)
        try:
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
            self.signinTable.setModel(self.class_table_model)
        except:
            print('Wrong!')


    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(
                        QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)

    @pyqtSlot()
    def endClass(self):
        reply=QMessageBox.question(self,'下课','确认下课？')
        if reply==QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    action = In_class_teacher()
    sys.exit(app.exec_())


