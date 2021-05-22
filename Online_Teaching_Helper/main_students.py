# -*-coding:utf-8-*-

# 功能：主界面，提供功能调整和基本的数据管理
# 修改：记得给每个学生分配自习室，并告知
# 数据导出功能，应该不难做到

import sys
import requests
import config
from PyQt5.QtGui import QKeyEvent, QKeySequence, QPixmap, QStandardItemModel, QStandardItem
from main_students_ui import Ui_MainWindow
from enter_class import Enterclass
from inClass import inClass
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtWidgets import *
from quert_student import Query_stuent

class Main_Students(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main_Students, self).__init__()
        self.setupUi(self)
        self.setTable()
        '''从数据库读数据到Table上'''

        self.show()


        #绑定事件
        self.newRoomBtn.clicked.connect(self.new_room)
        self.enterRoomBtn.clicked.connect(self.enter_room)
        self.detailBtn.clicked.connect(self.show_the_detail)
        self.outputBtn.clicked.connect(self.output)
        '''Tbale 绑定'''

    def setTable(self):
        # 初始化表格
        self.class_table_model = QStandardItemModel(4, 3)
        self.class_table_model.setHorizontalHeaderLabels(["课程编号", "课程名称", "任课老师"])
        #self.classTable.setModel(self.class_table_model)
        # !!!!!这一句，平衡表格
        self.classTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.reports_table_model = QStandardItemModel(4, 3)
        self.reports_table_model.setHorizontalHeaderLabels(["课程编号", "课程名称", "我的成绩"])
        self.reportsTable.setModel(self.reports_table_model)
        self.reportsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        studentID=2021000001
        teacherInform_url = 'http://{}:5000/inform/student/{}'
        url = teacherInform_url.format(config.IP, studentID)
        try:
            response = requests.get(url)
            d=response.json()
            #填充表格
            #row=self.classTable
            row=0
            clu=1
            for key in d:
                t=d[key]
                for i in range(3):
                    item=QStandardItem(str(t[i]))
                    self.class_table_model.setItem(row,i,item)
                row+=1
            self.classTable.setModel(self.class_table_model)
        except:
            print('Wrong whys!')

        show_brief_history_student_url = 'http://{}:5000/history/student/brief/{}'
        url = show_brief_history_student_url.format(config.IP, studentID)
        try:
            response = requests.get(url)
            d_=response.json()
            row=0
            clu=1
            for key in d_:
                t=d_[key]
                for i in range(3):
                    item=QStandardItem(str(t[i]))
                    self.reports_table_model.setItem(row,i,item)
                row+=1
            self.reportsTable.setModel(self.reports_table_model)
        except:
            print('Wrong!')

    windowList = []
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
    def new_room(self):
        reply=QMessageBox.question(self,'开始自习','确认开始自习？')
        if reply ==QMessageBox.Yes:
            """
            self.winList=[]
            new_win=inClass()
            self.winList.append(new_win)
            self.close()
            new_win.exec_()
            """
            win = inClass()
            self.windowList.append(win)  ##注：没有这句，是不打开另一个主界面的！
            win.show()
            #self.lst_widget.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '退出', '是否退出系统？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def enter_room(self):
        reply = QMessageBox.question(self, '进入教室', '确认进入教室？')
        if reply == QMessageBox.Yes:
            new_win=Enterclass()
            new_win.exec_()

    def show_the_detail(self):
        new_dia=Query_stuent()
        new_dia.exec_()
        print("跳到查询界面")

    def output(self):
        print('选择路径')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    action = Main_Students()
    sys.exit(app.exec_())
