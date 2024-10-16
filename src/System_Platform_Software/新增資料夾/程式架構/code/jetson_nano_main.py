import cv2
import numpy as np
import serial as AC
import struct
import Adafruit_BNO055.BNO055 as BNO055
from function import process_roi, detect_color, pd_control


# 定义感测区域
rois = [
    (319, 100, 519, 150),  # 大右感测区域
    (100, 100, 300, 150),  # 大左感测区域
    (200, 70, 419, 100),   # 中横感测区域
]
target_heading = [0]*5
left_heading = [0,90,180,-90,0]
right_heading = [0,-90,180,90,0]
turn_side = 0
kp_roi = 0.008  # 默认数据列比例增益
kd_roi = 0.01  # 默认数据列微分增益
kp_heading = 4  # 默认航向角比例增益
kd_heading = 6  # 默认航向角微分增益
combined_control_signal = 0
count = 0
PWM = 70

# 加載校準數據
calibration_data = np.load('calibration_data.npz')
camera_matrix = calibration_data['camera_matrix']
distortion_coefficients = calibration_data['distortion_coefficients']

# 尝试打开串口
try:
    ser = AC.Serial('/dev/ttyTHS1', 115200, timeout=1)  # 根据需要调整波特率
except AC.SerialException as e:
    print(f"Error: Could not open serial port: {e}")
    exit()



def main():
    global turn_side
    global target_heading
    global left_heading
    global right_heading
    global count
    global PWM
    current_last = 0  # 初始化 current_last 变量
    window_name = "Camera Preview"
    binary_window_name = "Binary Preview"
    
    # 打开摄像头
    cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=30/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink drop=true sync=false', cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
    bno = BNO055.BNO055(busnum=1)

    if not bno.begin():
        raise RuntimeError('Failed to initialize BNO055!')

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 讀取BNO055感應器數據
        heading, roll, pitch = bno.read_euler()
        accel_x, accel_y, accel_z = bno.read_linear_acceleration()
        if heading > 180:
            heading -= 360
        # 使用校準參數對影像進行失真校正
        h, w = frame.shape[:2]
        new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w, h), 0.12, (w, h))
        undistorted_frame = cv2.undistort(frame, camera_matrix, distortion_coefficients, None, new_camera_matrix)

        # 创建一个二值化的副本
        gray = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2GRAY)
        _, binary_frame = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)
        binary_frame = cv2.cvtColor(binary_frame, cv2.COLOR_GRAY2BGR)

        roi_values = []
        for i, (x1, y1, x2, y2) in enumerate(rois):
            processed_roi, black_pixels = process_roi(undistorted_frame, x1, y1, x2, y2)  # 获取黑色像素数量
            roi_values.append(black_pixels)
            binary_frame[y1:y2, x1:x2] = processed_roi

        # 颜色检测，返回 Y 坐标
        color_y_positions = detect_color(undistorted_frame)
        
        
        
            
        if turn_side != 1:
            if roi_values[2] > 6000:
                turn_side = 1
            elif color_y_positions[0] > color_y_positions[1] and target_heading == [0]*5:     
                turn_side = 2
                target_heading = left_heading
            elif color_y_positions[0] < color_y_positions[1] and target_heading == [0]*5:
                turn_side = 3  
                target_heading = right_heading
            else:
                turn_side = 0
            # 根据 data_mode 选择 PD 控制信号
            if roi_values[0] >= 4000:
                combined_control_signal = pd_control(4000, roi_values[0], kp_roi, kd_roi)
            elif roi_values[1] >= 3500:
                combined_control_signal = -pd_control(3500, roi_values[1], kp_roi, kd_roi)
            else:
                if heading < -135:
                    combined_control_signal = pd_control(-target_heading[count], heading, kp_heading, kd_heading)
                else:
                    combined_control_signal = pd_control(target_heading[count], heading, kp_heading, kd_heading)
            # 准备发送的数据
            data_to_send = (int(combined_control_signal), int(turn_side),PWM)
        if turn_side == 1:
            if target_heading == right_heading:
                combined_control_signal = -180
            if target_heading == left_heading:
                combined_control_signal = 180
            if heading < target_heading[count+1] + 5 and heading > target_heading[count+1] - 5:
                turn_side = 4
                if count >= 3:
                    count = 0
                else:
                    count += 1
            data_to_send = (int(combined_control_signal), int(turn_side),PWM)



        # 打印发送的数据以供调试
        print("Sent: ", data_to_send)

        # 将包头 "A" 加入到数据包前面
        header = b"A"
        send_data_value = struct.pack('3i', *data_to_send)  # 确保打包 3 个整数
        send_data_value = header + send_data_value

        # 发送带包头的数据
        ser.write(send_data_value)

        # 显示两个窗口
        cv2.imshow(window_name, undistorted_frame)
        cv2.imshow(binary_window_name, binary_frame)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()