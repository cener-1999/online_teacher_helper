import sys
import requests
from PyQt5.QtGui import QKeyEvent, QKeySequence, QPixmap
from login_ui import Ui_Dialog
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtWidgets import *
import register
from main_teacher import Main_Teacher
from main_students import Main_Students
from config import IP

class Login(QDialog,Ui_Dialog):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.show()
        self.windowList = []
        self.accoutEdit.setPlaceholderText("请输入账号")
        self.pswdEdit.setContextMenuPolicy(Qt.NoContextMenu)#不允许有上下文菜单
        self.pswdEdit.setPlaceholderText("请输入密码")
        self.pswdEdit.setEchoMode(QLineEdit.Password)#显示为不可见

        #绑定事件
        self.loginBtn.clicked.connect(self.login)
        self.registBtn.clicked.connect(self.register)
        self.comboBox.currentIndexChanged.connect(self.change_head)

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

    @pyqtSlot()

    def login(self):
        #获取用户输入
        self.user_role=self.comboBox.currentText()
        self.accout=self.accoutEdit.text()
        self.pswd=self.pswdEdit.text()
        print(type(self.accout))
        if(self.user_role=="学生"):
            role="student"
        else:
            role = "teacher"
        """
        插入数据库语句
        """
        register_url = "http://{}:5000/login/{}/{}/{}"
        url = register_url.format(IP, self.accout, self.pswd, role)
        print(url)
        response = requests.get(url)
        legal=response.json().get('legal')
        if legal:#判断
            if role=="student":

                new_win = Main_Students()
                self.windowList.append(new_win)  ##注：没有这句，是不打开另一个主界面的！
                self.close()
                new_win.show()
            elif role=="teacher":
                new_win = Main_Teacher()
                self.windowList.append(new_win)  ##注：没有这句，是不打开另一个主界面的！
                self.close()
                new_win.show()
        else:
            QMessageBox.warning(self, '错误','密码错误或账号不存在')
            self.accoutEdit.clear()
            self.pswdEdit.clear()

    def register(self):
        print('跳转到注册界面')
        goto= register.Register()
        goto.exec_()



    def change_head(self):
        #QMessageBox.warning(self, '错误', '密码错误或账号不存在')事件绑定是正确的
        self.user_role = self.comboBox.currentText()
        print(self.user_role)
        if(self.user_role=='学生'):
            pix = QPixmap('image/student_head.png')
        elif(self.user_role=='老师'):
            pix = QPixmap('image/teacher_head.png')
        self.head.setPixmap(pix)
        self.head.setScaledContents(True)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    action = Login()
    sys.exit(app.exec_())
