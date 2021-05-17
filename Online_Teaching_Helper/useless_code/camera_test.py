import numpy as np
import cv2

# read camera
#为了获取视频，需要创建一个VideoCapture对象，参数可以是设备的索引号，一般默认的摄像头参数是0
cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    #参数ret是一个bool，代表有没有读取到图片
    #frame表示截取到一帧的图片
    ret, frame = cap.read()
    #print(ret)
    #print(frame)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()