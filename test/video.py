# 导入opencv和numpy的库文件
import cv2
import numpy as np

# VideoCapture()用来捕获视频设备的ID，device = 0表示只有一个摄像头
device = 0
cap = cv2.VideoCapture(device)

cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# fourcc(Four-Character-Codes)：独立显示视频数据流格式的四字符编码
# 定义视频编码器为XVID
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 设定输出视频的名称和格式，以及帧率和分辨率
out = cv2.VideoWriter('output1.mp4', fourcc, 24.0, (640, 480))

while True:
    # ret的返回值为True或者False，表示有没有读取到图片；frame表示一帧图片
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰度视频流的参数设置
    out.write(frame)  # 将视频保存

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    cv2.imshow('frame', frame)  # 显示原视频流
    # cv2.imshow('gray', gray)  # 显示灰度格式的视频流

    if cv2.waitKey(1) == ord('q'):  # 按下q后退出条件成立
        break

# 释放内存
cap.release()
out.release()
cv2.destroyAllWindows()
