#人脸识别模块，不需要修改

import cv2
import imutils
import numpy as np
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from keras.models import load_model
from keras.preprocessing.image import img_to_array


#这个函数是用来做什么的？
def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x

class Recognize:
    def __init__(self):
        # 载入人脸检测模型
        detection_model_path= 'detection_model/detection_model.xml'
        self.face_detection = cv2.CascadeClassifier(detection_model_path)  # 级联分类器
        # 载入人脸表情识别模型
        self.emotion_classifier = load_model('model.hdf5', compile=False)
        # 表情类别
        self.EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised",
                         "neutral"]
        print('tell if we can init!')

    def run(self, frame_in,show_lable):
        # 调节画面大小
        frame = imutils.resize(frame_in, width=300)  # 缩放画面
        # frame = cv2.resize(frame, (300,300))  # 缩放画面
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转为灰度图
        # 检测人脸
        faces = self.face_detection.detectMultiScale(gray, scaleFactor=1.1,
                                                     minNeighbors=5, minSize=(30, 30),
                                                     flags=cv2.CASCADE_SCALE_IMAGE)
        preds = []  # 预测的结果
        label = None  # 预测的标签
        (fX, fY, fW, fH) = None, None, None, None  # 人脸位置
        frame_show = frame.copy()  # 复制画面


        if len(faces) > 0:
            # 根据ROI大小将检测到的人脸排序
            faces = sorted(faces, reverse=False, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))  # 按面积从小到大排序

            for i in range(len(faces)):
                if i == 0:
                    i = -1
                else:
                    break
                (fX, fY, fW, fH) = faces[0]

                # 从灰度图中提取感兴趣区域（ROI），将其大小转换为与模型输入相同的尺寸，并为通过CNN的分类器准备ROI
                roi = gray[fY:fY + fH, fX:fX + fW]
                roi = cv2.resize(roi, self.emotion_classifier.input_shape[1:3])
                roi = preprocess_input(roi)
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                # 用模型预测各分类的概率
                preds = self.emotion_classifier.predict(roi)[0]

                # 圈出人脸区域
                cv2.rectangle(frame_show, (fX, fY), (fX + fW, fY + fH), (145,44,238), 2)

        for (i, (emotion, prob)) in enumerate(zip(self.EMOTIONS, preds)):
            # 用于显示各类别概率
            text = "{}: {:.2f}%".format(emotion, prob * 100)
            print(text)
            # 绘制表情类和对应概率的条形图
            w = int(prob * 300) + 7


        show = cv2.resize(frame_show, (360, 320))
        #显示框框
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showFrame = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        show_lable.setPixmap(QPixmap.fromImage(showFrame))
