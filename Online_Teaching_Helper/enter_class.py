# 功能：进入教室，检查改教室是否存在
#注意用try-except防止强退
# 应该新建一个线程，加入后教师端可以显示
#

import sys
import requests
import config
from PyQt5.QtGui import QKeyEvent, QKeySequence
from inClass import inClass
from enter_class_ui import Ui_EnterClass
from PyQt5.QtCore import pyqtSlot, QObject, QEvent
from PyQt5.QtWidgets import *

class Enterclass(QDialog,Ui_EnterClass):
    def __init__(self):
        super(Enterclass, self).__init__()
        self.setupUi(self)
        self.show()

        self.winlist=[]
        self.idEdit.setPlaceholderText("请输入课堂码")
        # 绑定事件
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

    @pyqtSlot()
    def enter_room(self):
        winlist=[]
        reportID=self.idEdit.text()
        studentID=101
        '''DB查找教室码，把该学生加入课堂, studentID由上一个界面得到'''
        enterclass_url = 'http://{}:5000/class/sign/{}/{}'
        url = enterclass_url.format(config.IP, reportID, studentID)
        try:
            response = requests.get(url)
            result = response.json().get('result')
            if result:
                print("ok")
                win = inClass()
                self.winlist.append(win)  ##注：没有这句，是不打开另一个主界面的！
                win.show()
                self.close()
            else:
                QMessageBox.warning(self, '错误', '输入错误，该课堂不存在！')
            return False
        except:
            print('Wrong!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    action = Enterclass()
    sys.exit(app.exec_())


