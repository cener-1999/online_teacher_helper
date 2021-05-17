# -*-coding:utf-8-*-
import sys
import requests
from do_with_DB import do_with_db
from PyQt5.QtGui import QKeyEvent, QKeySequence, QPixmap
#from server.http_test import HTTP
from register_ui import Ui_Dialog
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtWidgets import *

class Register(QDialog,Ui_Dialog):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.show()

        self.IDEdit.setPlaceholderText("请输入教师编号")
        self.nameEdit.setPlaceholderText("请输入姓名")
        self.passwdEdit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许有上下文菜单
        self.passwdEdit.setPlaceholderText("请输入密码")
        self.passwdEdit.setEchoMode(QLineEdit.Password)  # 显示为不可见
        self.passwd_comfirmEdit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许有上下文菜单65
        self.passwd_comfirmEdit.setPlaceholderText("请再次输入密码")
        self.passwd_comfirmEdit.setEchoMode(QLineEdit.Password)  # 显示为不可见

        # 绑定事件
        self.registerBtn.clicked.connect(self.register)
        self.comboBox.currentIndexChanged.connect(self.change_role)
        self.passwd_comfirmEdit.editingFinished.connect(self.compare_input)

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
    def register(self):
        ID=self.IDEdit.text()
        name=self.nameEdit.text()
        self.role = self.comboBox.currentText()
        if (self.role=="教师"):
            role="teacher"
        else:
            role="student"

        if(self.compare_input()):
            passward=self.passwdEdit.text()
        else:
            QMessageBox.warning(self, '错误', '密码输入有误，请修改！')
            return False
        if(is_not_Empty(ID) and is_not_Empty(name) and is_not_Empty(passward)):
            #print(type(ID),type(name),type(passward),type(role))
            #do_with_db.register(int(ID),int(passward),role,name)
            register_url = "http://127.0.0.1:5000/register/{}/{}/{}/{}"
            url = register_url.format(ID,passward,role,str(name))
            print(url)
            #local_url = "127.0.0.1:5000/register/5432551/123/teacher/eee"
            #result=HTTP.get(local_url)
            #print(result)
            response = requests.get(url)
            #print("完善保存数据库语句",ID,name,passward,role)
            message = '您的账号是:' + ID + ',身份是:' + role
            flag=response.json().get('flag')
            if flag:
                QMessageBox.about(self, '注册成功', message)
                self.close()
            else:
                QMessageBox.warning(self, '注册失败', '注册失败！请检查输入内容')
                self.passwdEdit.clear()
                self.passwd_comfirmEdit.clear()

        else:
            QMessageBox.warning(self, '错误', '输入不完整，请补充！')

    def compare_input(self):
        pswd=self.passwdEdit.text()
        pswd_comfirm=self.passwd_comfirmEdit.text()
        if(pswd==pswd_comfirm):
            self.warnning.setVisible(False)
            flag = True
        else:
            self.warnning.setVisible(True)
            flag = False
        return flag

    def change_role(self):
        self.user_role = self.comboBox.currentText()
        print(self.user_role)
        if(self.user_role=='学生'):
            pix = QPixmap('image/student.png')
            self.IDEdit.setPlaceholderText("请输入学号")
            self.rolelable.setText("学号")
        elif(self.user_role=='教师'):
            pix = QPixmap('image/teacher.png')
            self.IDEdit.setPlaceholderText("请输入教师编号")
            self.rolelable.setText("教工编号")
        self.picLable.setPixmap(pix)
        self.picLable.setScaledContents(True)


def is_not_Empty(string):
    if string =='':
        return False
    return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    action = Register()
    sys.exit(app.exec_())


