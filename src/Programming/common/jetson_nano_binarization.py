import numpy as np
import cv2

# 尝试打开摄像头
imcap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=720, height=480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink', cv2.CAP_GSTREAMER)

if not imcap.isOpened():
    print("Error: Could not open video device.")
    exit()

# 创建窗口以显示滑动条
cv2.namedWindow('Threshold Adjustment')

# 滑动条的回调函数（不执行任何操作）
def nothing(x):
    pass

# 创建滑动条
cv2.createTrackbar('Threshold', 'Threshold Adjustment', 127, 255, nothing)

while True:
    ret, imageFrame = imcap.read()

    # 检查是否成功读取帧
    if not ret:
        print("Error: Failed to capture image")
        break

    # 转换为灰度图像
    grayFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)

    # 获取滑动条位置的阈值
    threshold_value = cv2.getTrackbarPos('Threshold', 'Threshold Adjustment')

    # 应用二值化
    _, binaryFrame = cv2.threshold(grayFrame, threshold_value, 255, cv2.THRESH_BINARY)

    # 显示原始图像和二值化图像
    cv2.imshow("Original Image", imageFrame)
    cv2.imshow("Threshold Adjustment", binaryFrame)

    # 按 'q' 键退出
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
imcap.release()  
cv2.destroyAllWindows()  