# -*-coding:utf-8-*-
# 功能：表情识别
# 要改的：时间统计
# 把表情识别的标签存下来，算值，或者取比例最大的标签，算法的核心部分
# 在结束时应该生成一条record并且入库
#
import requests
import config
from sys import argv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from core import Recognize
from inClass_ui import Ui_inClass
import cv2


class inClass(QMainWindow, Ui_inClass):
    def __init__(self):
        super(inClass, self).__init__()
        print("why close")
        self.timer_camera = QtCore.QTimer()  # 定时器
        self.setupUi(self)
        #路径不一致，图片没加载
        self.setWindowIcon(QIcon('./image/ICO.ico'))
        self.videoDisplay.setPixmap(QtGui.QPixmap("./image/enter_class.png"))
        self.retranslateUi(self)  # (1)
        self.show()
        self.slot_init()  # 槽函数设置
        self.cap = cv2.VideoCapture()  # 屏幕画面对象
        self.CAM_NUM = 0  # 摄像头标号
        print("why close")

    def slot_init(self):  # 定义槽函数
        self.cameraBtn.clicked.connect(self.start_camera)
        self.timer_camera.timeout.connect(self.show_camera)
        self.exitBtn.clicked.connect(self.exitClass)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '离开教室', '你确定要离开教室吗？')

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def start_camera(self):
        if self.timer_camera.isActive() == False:  # 检查定时状态
            flag = self.cap.open(self.CAM_NUM)  # 检查相机状态
            if flag == False:  # 相机打开失败提示
                QMessageBox.warning(self, '摄像头开启失败', '请检查摄像头是否可用！')

            else:
                self.videoDisplay.clear()
                QtWidgets.QApplication.processEvents()
                # 新建对象
                self.recognize = Recognize()
                QtWidgets.QApplication.processEvents()
                # 打开定时器
                self.timer_camera.start(30)
        else:
            # 定时器未开启，界面回复初始状态
            self.timer_camera.stop()
            self.cap.release()
            self.videoDisplay.setPixmap(QtGui.QPixmap("image/enter_class.png"))
            self.cameraBtn.setText('打开摄像头')

    def show_camera(self):
        # 定时器槽函数，每隔一段时间执行
        ret, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)  # 左右翻转
        '''
        self.frame_1=self.frame.copy()
        show = cv2.resize(self.frame, (360, 320))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showFrame = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.videoDisplay.setPixmap(QPixmap.fromImage(showFrame))      #放到功能块里，否则框框被覆盖
        '''
        #cv2.rectangle(self.frame, (100,100), (50,50), (255, 255, 0), 1)
        result = self.recognize.run(self.frame,self.videoDisplay)

    def exitClass(self):
        # """写入数据库"""
        # reportID=
        # studentID=
        # grade=77
        # """reportID, studentID又上一个跳转页面得来，成绩又core计算"""
        # endclass_url = 'http://{}:5000/class/end/{}/{}/{}'
        # url = endclass_url.format(config.IP, reportID, studentID, grade)
        # response = requests.get(url)
        # result = response.json().get('result')
        self.close()

if __name__ == '__main__':
    app = QApplication(argv)
    action = inClass()
    exit(app.exec_())

