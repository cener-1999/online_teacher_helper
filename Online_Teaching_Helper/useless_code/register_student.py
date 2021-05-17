import sys

from PyQt5.QtGui import QKeyEvent, QKeySequence

from useless_code.student_register_ui import Ui_Dialog
from PyQt5.QtCore import pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtWidgets import *

class Register_student(QDialog,Ui_Dialog):
    def __init__(self):
        super(Register_student, self).__init__()
        self.setupUi(self)
        self.show()

        self.class_Edit.setPlaceholderText("请输入班级号")
        self.ID_studentEdit.setPlaceholderText("请输入学号")
        self.nameEdit.setPlaceholderText("请输入姓名")
        self.passwdEdit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许有上下文菜单
        self.passwdEdit.setPlaceholderText("请输入密码")
        self.passwdEdit.setEchoMode(QLineEdit.Password)  # 显示为不可见

        self.passwd_comfirmEdit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许有上下文菜单65
        self.passwd_comfirmEdit.setPlaceholderText("请再次输入密码")
        self.passwd_comfirmEdit.setEchoMode(QLineEdit.Password)  # 显示为不可见

        # 绑定事件
        self.registerBtn.clicked.connect(self.register)
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

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '退出', '是否退出程序？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def register(self):
        classID=self.class_Edit.text()
        ID=self.ID_studentEdit.text()
        name=self.nameEdit.text()
        if(self.compare_input()):
            passward=self.passwdEdit.text()
        else:
            QMessageBox.warning(self, '错误', '密码输入有误，请修改！')
            return False
        if(is_not_Empty(classID) and is_not_Empty(ID) and is_not_Empty(name) and is_not_Empty(passward)):
            print("完善保存数据库语句")
        else:
            QMessageBox.warning(self, '错误', '输入不完整，请补充！')

    def compare_input(self):
        pswd=self.passwdEdit.text()
        pswd_comfirm=self.passwd_comfirmEdit.text()
        #print(pswd,pswd_comfirm) 检查好了事件是没问题的
        if(pswd==pswd_comfirm):
            self.warnning.setVisible(False)
            flag = True
        else:
            self.warnning.setVisible(True)
            flag = False
        return flag

def is_not_Empty(string):
    if string =='':
        return False
    return True




if __name__ == "__main__":
    app = QApplication(sys.argv)
    action = Register_student()
    sys.exit(app.exec_())


