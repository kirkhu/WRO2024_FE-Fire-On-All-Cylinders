import cv2
import numpy as np
import serial as AC
import struct
import time
import Adafruit_BNO055.BNO055 as BNO055
from function import process_roi, detect_color_final, pd_control,draw_multiple_curves


# 定义感测区域
rois = [
    (370, 100, 640, 150),  # 大右感测区域
    (0, 100, 260, 150)  # 大左感测区域
]

# 定义多条线的颜色、起点和终点
colors = [(0, 0, 255), (0, 255, 0)]  # 红色和绿色
start_points = [(0, 480), (640, 480)]  # 起点列表
end_points = [(270, 60), (370, 60)]      # 终点列表
slope_values = [1.7, -1.7]  # 斜率
curvature_factors = [0.5, 0.5]  # 弯曲度

target_heading = [0]*4
left_heading = [90,180,-90,0]
right_heading = [-90,-180,90,0]
red_left_heading = [90,0,-90,180]
red_right_heading = [-90,0,90,-180]
turn_side = 0
kp_roi = 0.01  # 默认数据列比例增益
kd_roi = 0.02  # 默认数据列微分增益
kp_heading = 5  # 默认航向角比例增益
kd_heading = 7.5  # 默认航向角微分增益
kp_X = 0.5  # 默认航向角比例增益
kd_X = 0.8  # 默认航向角微分增益
combined_control_signal = 0
count = 0
set_PWM = 70
PWM = 0
round_number = 0
turn_side = 0
turn_time = 0
turn_diside = False
pass_block = True
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
    global set_PWM
    global before_turn
    global round_number
    global turn_time
    global turn_diside
    global pass_block
    window_name = "Camera Preview"
    binary_window_name = "Binary Preview"


    # 初始红色和绿色 X 差值
    last_red_x_diff = 0
    last_green_x_diff = 0

    # 打开摄像头
    cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=30/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink drop=true sync=false', cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
    bno = BNO055.BNO055(busnum=1)

    if not bno.begin():
        raise RuntimeError('Failed to initialize BNO055!')
    combined_control_signal = 0

    while True:

        ret, frame = cap.read()
        if not ret:
            break
        # 讀取BNO055感應器數據
        heading, roll, pitch = bno.read_euler()
        accel_x, accel_y, accel_z = bno.read_linear_acceleration()
        if heading > 180:
            heading -= 360
        # 使用校准参数对图像进行失真校正
        h, w = frame.shape[:2]
        new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w, h), 0.14, (w, h))
        undistorted_frame = cv2.undistort(frame, camera_matrix, distortion_coefficients, None, new_camera_matrix)

        # 创建一个二值化的副本
        gray = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2GRAY)
        _, binary_frame = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)
        binary_frame = cv2.cvtColor(binary_frame, cv2.COLOR_GRAY2BGR)

        # 处理每个感测区域
        roi_values = []
        for x1, y1, x2, y2 in rois:
            processed_roi, black_pixels = process_roi(undistorted_frame, x1, y1, x2, y2)
            roi_values.append(black_pixels)
            binary_frame[y1:y2, x1:x2] = processed_roi

       
        # 颜色检测，并将 red_curve_points 传递进去，获得红色和绿色的 X 差值
        color_y_positions, red_x_diff, green_x_diff = detect_color_final(undistorted_frame, last_red_x_diff, last_green_x_diff, start_points, end_points, slope_values, curvature_factors, colors)

        # 保存当前的红色和绿色 X 差值，供下一帧使用
        last_red_x_diff = red_x_diff
        last_green_x_diff = green_x_diff


        #Straight
        if turn_side == 0 or turn_side == 2:
            PWM = set_PWM
            if color_y_positions[0] > color_y_positions[1]:     
                if target_heading == [0] * 5:
                    target_heading = left_heading
                if color_y_positions[0] > 200:
                    turn_side = 1
            elif color_y_positions[0] < color_y_positions[1]:
                if target_heading == [0] * 5:
                    target_heading = right_heading
                if color_y_positions[1] > 200:
                    turn_side = 1           
            else:
                turn_side = 0
            # 根据 data_mode 选择 PD 控制信号
            if color_y_positions[2] < color_y_positions[3]:
                combined_control_signal = -pd_control(0, green_x_diff, kp_X, kd_X)
                if color_y_positions[3] > 60:
                    a = (70 - 35) / (480 - 60)
                    b = 70 - a * 480
                    PWM = a * color_y_positions[3] + b
                else:
                    PWM = 70
            elif color_y_positions[2] > color_y_positions[3]:
                combined_control_signal = pd_control(0, red_x_diff, kp_X, kd_X)
                if color_y_positions[2]> 50:
                    a = (70 - 35) / (480 - 60)
                    b = 70 - a * 480
                    PWM = a * color_y_positions[2] + b
                else:
                    PWM = 70
            elif roi_values[0] >= 8200:
                combined_control_signal = pd_control(8000, roi_values[0], kp_roi, kd_roi)
            elif roi_values[1] >= 6900:
                combined_control_signal = -pd_control(6700, roi_values[1], kp_roi, kd_roi)
            else:
                PWM = 70
                #combined_control_signal = pd_control(target_heading[count], heading, kp_heading, kd_heading)
            start_time = time.time()  # 獲取當前時間（秒）

        #Turn
        if turn_side == 1:
            # 根据 data_mode 选择 PD 控制信号
            if color_y_positions[2] < color_y_positions[3]:
                turn_diside = False
                combined_control_signal = -pd_control(0, green_x_diff, kp_X, kd_X)
                if color_y_positions[3] > 60:
                    a = (70 - 35) / (480 - 60)
                    b = 70 - a * 480
                    PWM = a * color_y_positions[3] + b
                else:
                    PWM = 70
            elif color_y_positions[2] > color_y_positions[3]:
                turn_diside = True
                combined_control_signal = pd_control(0, red_x_diff, kp_X, kd_X)
                if color_y_positions[2]> 60:
                    a = (70 - 35) / (480 - 60)
                    b = 70 - a * 480
                    PWM = a * color_y_positions[2] + b
                else:
                    PWM = 70
            elif roi_values[0] >= 9000:
                combined_control_signal = pd_control(1000, roi_values[0], kp_roi, kd_roi)
            elif roi_values[1] >= 8000:
                combined_control_signal = -pd_control(1000, roi_values[1], kp_roi, kd_roi)
            else:
                if target_heading == left_heading or target_heading == red_right_heading:
                    combined_control_signal = 170
                else:
                    combined_control_signal = -170     
            PWM = 50
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 1 and heading < target_heading[count] + 30 and heading > target_heading[count] - 30:
                turn_side = 2
                if count >= 3:
                    count = 0
                    round_number +=1
                    if round_number == 2:
                        turn_side = 3
                else:
                    count += 1
                combined_control_signal = 0
        if turn_side == 3:
            if turn_diside:
                combined_control_signal = pd_control(0, red_x_diff, kp_X, kd_X)
                if color_y_positions[2]> 60:
                    a = (70 - 35) / (480 - 60)
                    b = 70 - a * 480
                    PWM = a * color_y_positions[2] + b
                else:
                    PWM = 70
                if color_y_positions[2] == 0 and pass_block:
                   pass_block = False
                   turn_time = time.time()
                elif turn_time != 0 :
                   current_time = time.time()
                   elapsed_time = current_time - turn_time
                   if elapsed_time >= 0.3:
                       if abs(heading) > 150:
                           if target_heading == left_heading:
                               target_heading = red_left_heading
                           else:
                               target_heading = red_right_heading
                           turn_side = 2
                       combined_control_signal = -170
    
                
            else:
                turn_side = 2
                count = 0
                round_number +=1

        if combined_control_signal > 180:
            combined_control_signal=180
        if combined_control_signal < -180:
            combined_control_signal=-180
   
        # 准备发送的数据
        data_to_send = (int(combined_control_signal), int(turn_side),int(PWM))
        
        # 打印发送的数据以供调试
        print(f"Sent: {data_to_send}",roi_values[1], roi_values[0], count, target_heading)

        # 将包头 "A" 加入到数据包前面
        header = b"A"
        send_data_value = struct.pack('3i', *data_to_send)  # 打包 3 个整数
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