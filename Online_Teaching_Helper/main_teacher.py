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
from query_teacher import Query_teacher
from namelist import Namelist

class Main_Teacher(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main_Teacher, self).__init__()
        self.setupUi(self)
        self.show()
        self.setTable()
        #绑定事件
        self.claInfEditBtn.clicked.connect(self.edit_class_inform)
        self.namelistBtn.clicked.connect(self.show_name_list)
        self.newRoomBtn.clicked.connect(self.new_room)
        self.new_calss_Btn.clicked.connect(self.new_class)
        self.detailBtn.clicked.connect(self.show_the_detail)
        self.outputBtn.clicked.connect(self.output)
        '''Tbale 绑定'''
    def setTable(self):
        # 初始化表格
        self.class_table_model = QStandardItemModel(4, 3)
        self.class_table_model.setHorizontalHeaderLabels(["课程编号", "课程名称", "学生人数"])
        #self.classTable.setModel(self.class_table_model)
        # !!!!!这一句，平衡表格
        self.classTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.reports_table_model = QStandardItemModel(4, 3)
        self.reports_table_model.setHorizontalHeaderLabels(["课程编号", "课程名称", "报告编号"])
        self.reportsTable.setModel(self.reports_table_model)
        self.reportsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        teacherID=110001
        teacherInform_url = 'http://{}:5000/inform/teacher/{}'
        url = teacherInform_url.format(config.IP, teacherID)
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

        show_brief_history_teacher_url = 'http://{}:5000/history/teacher/brief/{}'
        url = show_brief_history_teacher_url.format(config.IP, teacherID)
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

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '退出', '是否退出程序？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()

    def edit_class_inform(self):
        tips = QMessageBox.question(self, '修改课程', '确认修改课程信息？')

    def show_name_list(self):
        print("和数据库交互，显示在tableview上")
        new_dia=Namelist()
        new_dia.exec_()

    def new_room(self):
        reply=QMessageBox.question(self,'开始上课','确认开始上课？')
        if reply ==QMessageBox.Yes:
            new_dialog=In_class_teacher()
            new_dialog.exec_()

    def new_class(self):
        reply = QMessageBox.question(self, '新建课程', '确认新建课程？')
        if reply==QMessageBox.Yes:
            new_dialog=New_Class()
            new_dialog.exec_()

    def show_the_detail(self):
        print("跳到查询界面")
        new_dia=Query_teacher()
        new_dia.exec_()

    def output(self):
        print('选择路径')




if __name__ == "__main__":

    app = QApplication(sys.argv)
    action = Main_Teacher()
    sys.exit(app.exec_())
