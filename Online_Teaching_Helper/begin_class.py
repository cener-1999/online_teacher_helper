import sys
import config
import requests
from PyQt5.QtGui import QKeyEvent, QKeySequence
from begin_class_ui import Ui_EnterClass
from PyQt5.QtCore import pyqtSlot, QObject, QEvent
from PyQt5.QtWidgets import *
from in_class_teacher import In_class_teacher

class Enterclass(QDialog,Ui_EnterClass):
    def __init__(self):
        super(Enterclass, self).__init__()
        self.setupUi(self)
        self.show()
        self.idEdit.setPlaceholderText("请输入课堂码")
        # 绑定事件
        self.class_newBtn.clicked.connect(self.new_room)
        self.class_beginBtn.clicked.connect(self.enter_room)
        object = QObject()
        # 事件过滤器，防止挂掉

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

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '退出', '是否退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def enter_room(self):
        class_id=self.idEdit.text()
        '''DB查找教室码，把该学生加入课堂'''
        beginclass_url = 'http://{}:5000/class/begin/{}'
        url = beginclass_url.format(config.IP, class_id)
        response = requests.get(url)
        result = response.json().get('result')
        if result:
            new_dia=In_class_teacher()
            new_dia.exec_()
            self.close()
        else:
            QMessageBox.warning(self, '错误', '输入错误，该课堂不存在！')
            return False

    def new_room(self):
        roomID = self.idEdit.text()
        reply=QMessageBox.question(self,'新建教室','确定新建该教室？')
        if(reply==QMessageBox.Yes):
            print('补充功能，把在DB表里新建该项，主键为roomID')
        elif(reply==QMessageBox.No):
            #print('瞎猜成功')
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    action = Enterclass()
    sys.exit(app.exec_())


