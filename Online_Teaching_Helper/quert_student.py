# -*-coding:utf-8-*-
# 学生的查询自己记录的功能
# t c

import sys
import requests
import config
from PyQt5.QtGui import QKeyEvent, QKeySequence, QStandardItemModel, QStandardItem
from query_student_ui import Ui_Dialog
from PyQt5.QtCore import pyqtSlot, QEvent
from PyQt5.QtWidgets import *

class Query_stuent(QDialog,Ui_Dialog):
    def __init__(self):
        super(Query_stuent, self).__init__()
        self.setupUi(self)
        self.setTable()
        '''从数据库读数据到Table上'''
        self.show()
        self.student_id=2020100001
        self.query()
        #绑定事件
        self.clearBtn.clicked.connect(self.clear)
        self.outputBtn.clicked.connect(self.output)
        '''Tbale 绑定'''

    def setTable(self):
        # 初始化表格
        self.class_table_model = QStandardItemModel(4, 2)
        self.class_table_model.setHorizontalHeaderLabels(["报告编号","评价结果"])
        #self.classTable.setModel(self.class_table_model)
        # !!!!!这一句，平衡表格
        self.classTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.classTable.setModel(self.class_table_model)

    #事件过滤器，防止挂掉
    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)


    @pyqtSlot()
    def query(self): #不健壮，不能输入空和错误
        query_history_by_teacher_url = 'http://{}:5000/history/student/report/{}'
        url = query_history_by_teacher_url.format(config.IP,self.student_id)
        try:
            response = requests.get(url)
            d=response.json()
            print(d)
            row=self.classTable
            row=0
            for key in d:
                self.class_table_model.setItem(row,0,QStandardItem(key))
                self.class_table_model.setItem(row,1,QStandardItem(str(d[key])))
                row+=1
            #self.classTable.setModel(self.class_table_mode)
        except:
            print('Wrong')

    def clear(self):
        self.classTable.clearSpans()

    def output(self):
        print('选择路径')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    action = Query_stuent()
    sys.exit(app.exec_())
