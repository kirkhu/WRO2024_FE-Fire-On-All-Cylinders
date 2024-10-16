# 程式架構

## jetson nano端

### 執行程式

開啟UART串口
```
sudo chmod 777 /dev/ttyTHS1
```
啟動程式，後加程式名，這裡以jetson_nano_main為例
```
python3 jetson_nano_main
```
### jetson_nano_funtion
匯入函式庫
```
import cv2
import numpy as np
import serial as AC
import struct
```
定義颜色范圍和對應的颜色，使用jetson_nano_HSV來取得數值
```
color_ranges = {
    'Orange': ([0, 175, 120], [15, 220, 155], (0, 165, 255)),
    'Blue': ([100, 105, 80], [125, 215, 135], (255, 0, 0))
}
```
定義ROI感測區(於主程式定義)
```
rois = [
            (469, 100, 569, 150),  # 大右感测区域
            (150, 100, 250, 150),  # 大左感测区域
            (250, 70, 469, 100),   # 中横感测区域
            (335, 0, 385, 100)     # 中直感测区域
        ]
```
嘗试打开串口，根据需要调整波特率
```
try:
    ser = AC.Serial('/dev/ttyTHS1', 115200, timeout=1)
except AC.SerialException as e:
    print(f"Error: Could not open serial port: {e}")
    exit()
```
將畫面轉為灰階將畫面轉為灰階，再轉為二質化，最後依照給的座標來進行感測區繪製，並把感測區反白
```
    roi = frame[y1:y2, x1:x2]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY_INV)
```
找出黑色面積，也就是反白厚的白色，標示出並算出其面積
```
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        black_pixels = int(cv2.contourArea(largest_contour))  
        cv2.drawContours(binary, [largest_contour], -1, (255, 255, 255), -1)
    else:
        black_pixels = 0
```
將圖像從BGR轉為HSV，以便於分離色
```
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```
創建顏色掩碼
```
    for color, (lower, upper, bgr) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        color_mask = cv2.inRange(hsv_frame, lower, upper)
        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```
找到辨識出面積最大的色塊
```
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 500: 
```
以XY座標標示出色塊所在位置，以便於比較色塊位置
```
    x, y, w, h = cv2.boundingRect(largest_contour)
    center_x, center_y = x + w // 2, y + h // 2
    cv2.rectangle(frame, (x, y), (x + w, y + h), bgr, 2)
    cv2.circle(frame, (center_x, center_y), 5, bgr, -1)
```
開啟鏡頭，設定鏡頭資訊(例如width=720, height=480為畫面小)
```
cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=720, height=480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink', cv2.CAP_GSTREAMER)
```
整理數據(4個ROI面積、4個顏色辨識XY)，打印在終端機以供調試
```
    data_to_send = roi_values + [coord for color_pos in color_positions for coord in color_pos] 
    print(f"Sent: {data_to_send}")
```
在數據前加入包頭以防因PICO板和jeston nano傳輸速率不同導致數據有誤，並將整筆數據打包成二進制傳送
```
    header = b"A"
    send_data_value = struct.pack('8i', *data_to_send)
    send_data_value = header + send_data_value
    ser.write(send_data_value)
```
計算校正角度

```
    error = current - target
    derivative = current - current_last
    control_signal = -(kp * error + kd * derivative)
    current_last =  current  # 在 return 之前更新 current_last
    return control_signal
```
### 计算中间控制点的位置来控制弯曲程度
```
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        control_x = mid_x
        control_y = int(mid_y - curvature * slope * (x2 - x1))  # 使用弯曲度和斜率来调整中间控制点
```
### 使用贝塞尔曲线绘制
```
        curve_points = []
        for t in np.linspace(0, 1, 100):
            xt = (1 - t)**2 * x1 + 2 * (1 - t) * t * control_x + t**2 * x2
            yt = (1 - t)**2 * y1 + 2 * (1 - t) * t * control_y + t**2 * y2
            curve_points.append((int(xt), int(yt)))
```
### jetson_nano_HSV
創建空白障為調整的視窗
```
img2 = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
```
創建拉趕來進行顏色選取
```
cv2.createTrackbar('H_low','image',0,255,nothing) 
cv2.createTrackbar('H_high','image',255,255,nothing) 
cv2.createTrackbar('S_low','image',0,255,nothing) 
cv2.createTrackbar('S_high','image',255,255,nothing) 
cv2.createTrackbar('V_low','image',0,255,nothing) 
cv2.createTrackbar('V_high','image',255,255,nothing) 
```
設定並開啟攝像頭
```
imcap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER) 

imcap.set(cv2.CAP_PROP_BRIGHTNESS, 60) 
imcap.set(3, 480) # set width as 640 
imcap.set(4, 360) # set height as 480 
```
取得拉桿數值已跟著改變螢幕
```
  H_high = cv2.getTrackbarPos('H_high','image') 
  H_low = cv2.getTrackbarPos('H_low','image') 
  S_high = cv2.getTrackbarPos('S_high','image') 
  S_low = cv2.getTrackbarPos('S_low','image') 
  V_high = cv2.getTrackbarPos('V_high','image') 
  V_low = cv2.getTrackbarPos('V_low','image') 
```
創建並套用掩碼
```
  success, img = imcap.read() 
  hls = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
  hls_low = np.array([H_low, S_low, V_low]) 
  hls_high = np.array([H_high, S_high, V_high]) 
  mask = cv2.inRange(hls, hls_low, hls_high) 
  mask = cv2.dilate(mask,kernal,iterations=1) 
  res = cv2.bitwise_and(img, img, mask=mask) 
```
調整完的值需手動輸入jetson_nano_main或jetson_nano_main_final

### jetson_nano_black_HSV
轉為灰度圖像
```
    grayFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)
```
讀取拉桿數值並套用二值化
```
    threshold_value = cv2.getTrackbarPos('Threshold', 'Threshold Adjustment')
    _, binaryFrame = cv2.threshold(grayFrame, threshold_value, 255, cv2.THRESH_BINARY)
```
顯示原始圖像和二值化圖像
```
    cv2.imshow("Original Image", imageFrame)
    cv2.imshow("Threshold Adjustment", binaryFrame)
```
調整完的值需手動輸入jetson_nano_main或jetson_nano_main_final
## Raspberry pi pico端

### thonny_function
匯入函式庫
```
from machine import Pin, PWM, I2C, UART
import struct
import time
```
初始化PWM、馬達、编碼器、I2C、按键引脚、UART
```
servo_pin = PWM(Pin(28), freq=50)
motor_in1 = Pin(20, Pin.OUT)
motor_in2 = Pin(21, Pin.OUT)
motor_pwm = PWM(Pin(22), freq=1000)
encoder_pin_A = Pin(0, Pin.IN)
encoder_pin_B = Pin(1, Pin.IN)
button = Pin(18, Pin.IN, Pin.PULL_UP)
i2c1 = I2C(id=1, sda=Pin(26), scl=Pin(27), freq=400000)
i2c2 = I2C(id=0, sda=Pin(12), scl=Pin(13), freq=420000)
uart = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
```
全局變量設置
```
kp_heading = 5  # 默认航向角比例增益
kd_heading = 7 # 默认航向角微分增益
kp_data = 0.001 # 默认数据列比例增益
kd_data = 0.005  # 默认数据列微分增益
encoder_count = 0  # 初始化编码器计数
initial_heading = 0  # 初始化初始航向角
last_state_A = encoder_pin_A.value()  # 初始化编码器状态
data_value = [0] * 12  # 初始化数据列表
current_last = 0
current = 0
turn_side = 0
```
```
def initialize_bno055():
    try:
        i2c1.writeto_mem(0x28, 0x3D, bytes([0x00]))  # 配置模式
        time.sleep_ms(10)
        i2c1.writeto_mem(0x28, 0x3D, bytes([0x0C]))  # NDOF模式（融合算法）
        time.sleep_ms(20)
    except OSError as e:
        print('BNO055初始化错误:', e)
```