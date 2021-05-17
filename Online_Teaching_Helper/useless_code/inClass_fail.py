from sys import argv
import cv2
from core import Recognize
from PyQt5 import QtWidgets, QtCore
from inClass_ui import Ui_inClass
from PyQt5.QtWidgets import *

class inClass(QMainWindow, Ui_inClass):
    def __init__(self):
        super(inClass, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)#(1)
        self.show()

        # 为摄像机新建一个QTimer对象
        self.timer_camera = QtCore.QTimer()
        # 为了获取视频，需要创建一个VideoCapture对象，参数可以是设备的索引号，一般默认的摄像头参数是0
        self.cap = cv2.VideoCapture()
        self.CAMERA_NUM = 0  # 摄像头编号

        # 绑定事件
        self.timer_camera.timeout.connect(self.show_camera)
        self.cameraBtn.clicked.connect(self.start_camera)
        self.exitBtn.clicked.connect(self.exitClass)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '退出', '是否退出程序？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def show_camera(self):
        ret, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)  # 左右翻转

        #print(ret, 'camera is ok')
        #print('show me if camera work?')
        #print(self.frame)g
        #print('camera is working,problem with label')
        show = cv2.resize(self.frame, (360, 320))
        # 视频色彩转换回RGB
        show = cv2.cvtColor(show,cv2.COLOR_BGR2RGB)
        #print('show me if show work?')
        #print(show)
        #print('i got it ,problem in the show')
        # 把读取到的视频数据变成QImage形式
        show = cv2.resize(self.frame, (360, 320))
        # 视频色彩转换回RGB
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        result = self.emotion_model.run(self.image)
        #result=self.recognize.run(self.frame)
        #QtWidgets.QApplication.processEvents()
        #Recognize.test(self=None)



    def start_camera(self):
        '''
        # QMessageBox.warning(self,'连上了吗','连上了')
        if not self.timer_camera.isActive():
            ret = self.cap.open(0)
            if not ret:
                QMessageBox.warning(self, '摄像头开启失败', '请检查摄像头是否可用！')
            else:
                self.videoDisplay.clear()
                #新建对象，用以识别
                print('first is ok')
                QtWidgets.QApplication.processEvents()
                self.mytest=Test()
                #self.recognize = Recognize()
                QtWidgets.QApplication.processEvents()
                print('inti is ok')
                self.timer_camera.start(30)  # 摄像频率
                self.cameraBtn.setText('关闭摄像头')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.videoDisplay.setPixmap(QtGui.QPixmap("../image/enter_class.png"))
            self.cameraBtn.setText('打开摄像头')
        '''
        if self.timer_camera.isActive() == False:  # 检查定时状态
            flag = self.cap.open(0)  # 检查相机状态
            if flag == False:  # 相机打开失败提示
                msg = QtWidgets.QMessageBox.warning(self.centralwidget, u"Warning",
                                                    u"请检测相机与电脑是否连接正确！ ",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                # 准备运行识别程序
                #.textEdit_pic.setText('文件未选中')
                QtWidgets.QApplication.processEvents()
                #self.textEdit_camera.setText('实时摄像已开启')
                #self.label_face.setText('正在启动识别系统...\n\nleading')
                # 新建对象
                #self.recognize = Recognize()
                self.emotion_model = Recognize()
                QtWidgets.QApplication.processEvents()
                # 打开定时器
                self.timer_camera.start(30)
        else:
            # 定时器未开启，界面回复初始状态
            self.timer_camera.stop()
            self.cap.release()
            #self.label_face.clear()
            #self.textEdit_camera.setText('实时摄像已关闭')

    def exitClass(self):
        QMessageBox.question(self, '离开教室', '你确定要离开教室吗？')


if __name__ == '__main__':
    app = QApplication(argv)
    action=inClass()
    exit(app.exec_())