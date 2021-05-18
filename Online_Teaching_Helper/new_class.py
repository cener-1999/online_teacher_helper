# -*-coding:utf-8-*-

# 功能：新建课程
# 不修改
import sys
import requests
from PyQt5.QtGui import QKeyEvent, QKeySequence, QPixmap

from new_class_ui import Ui_Dialog
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtWidgets import *

class New_Class(QDialog,Ui_Dialog):
    def __init__(self):
        super(New_Class, self).__init__()
        self.setupUi(self)
        self.show()

        self.class_ID_Edit.setPlaceholderText("请输入课程编号")
        self.class_name_Edit.setPlaceholderText("请输入课程名称")
        self.te_ID_Edit.setPlaceholderText("请输入任课老师编号")

        #绑定事件
        self.pushButton.clicked.connect(self.new_class)


        object = QObject()

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

        reply = QMessageBox.question(self, '退出', '是否结束新建课程？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()

    def new_class(self):
        class_ID=self.class_ID_Edit.text()
        class_name = self.class_name_Edit.text()
        teacher_ID = self.te_ID_Edit.text()
        try:
            new_class_url="http://127.0.0.1:5000/new_class/{}/{}/{}"
            url=new_class_url.format(class_ID,class_name,teacher_ID)
            response = requests.get(url)
            flag = response.json().get('flag')
            print("flag is ",flag)
            if flag:
                mes='新建课程成功课程号是'+str(class_ID)
                QMessageBox.about(self,'新建成功',mes)
                self.close()
            else:
                QMessageBox.warning(self, '错误', '输入有误，请检查！')
        except Exception:
            QMessageBox.warning(self, '错误','输入有误，请检查！')
            self.class_ID_Edit.clear()
            self.class_name_Edit.clear()
            self.te_ID_Edit.clear()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    action = New_Class()
    sys.exit(app.exec_())
