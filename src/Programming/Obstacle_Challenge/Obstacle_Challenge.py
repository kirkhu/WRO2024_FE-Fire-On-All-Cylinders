from vehicle_function import*
import time
import pickle
import threading
import math
import numpy as np
import rospy
from sensor_msgs.msg import LaserScan
import signal
#opencv_detect.get_program_fps()  取得影像辨識FPS
#opencv_detect.get_keyboard()     取得鍵盤的按鍵
#opencv_detect.get_green_node_x() 取得綠色積木與斜線之交點X(沒辨識到目標數值為-1)
#opencv_detect.get_red_node_x()   取得紅色積木與斜線之交點X(沒辨識到目標數值為-1)
#opencv_detect.get_green_x()      取得綠色積木X座標(沒辨識到目標數值為-1)
#opencv_detect.get_green_y        取得綠色積木Y座標(沒辨識到目標數值為-1)
#opencv_detect.get_green_area()   取得綠色積木面積大小(沒辨識到目標數值為0)
#opencv_detect.get_red_x()        取得紅色積木X座標(沒辨識到目標數值為-1)
#opencv_detect.get_red_y          取得紅色積木Y座標(沒辨識到目標數值為-1)
#opencv_detect.get_red_area()     取得紅色積木面積大小(沒辨識到目標數值為0)

LED = LED_control()
button = button_control()
motor = dc_motor()
servo = servo_motor()
gyro_sensor = BNO055()
color_sensor = TCS34725()
mapping = tools()

park=0
direction = 0
thread_run = True
color = 0
k = 0
green_lower = 0
green_upper = 0
red_lower = 0
red_upper = 0
line_middle = 0
color_direction_middle = 0
white_color = 0
turn_direction = [0, -90, -180, -270]
pluse_turn = -90
gyro_value = 180
gyro = 0
record_box = 2
count = 0
RADIAN_TO_DEGREES = 180000/3141.59
lidar_data = 0
lidar_run = False
Location = False
last_color = False
last_angle = 0
#____________________________________________
dodgeblock_kp = 0.11
center_kp =0.7
gyro_kp = 0.8
power = 63
#___________________________________________
def lidar_callback(data):
    global lidar_data, lidar_run
    lidar_data = data
    lidar_run = True

def lidar_get_distance(set_gyro):
    lens = int((lidar_data.angle_max - lidar_data.angle_min) / lidar_data.angle_increment) - 50
    mid = -1
    left = -1
    right = -1
    gyro_value = gyro_relative(set_gyro)
    for i in range(lens):
        angle_error = int((lidar_data.angle_min + i * lidar_data.angle_increment) * RADIAN_TO_DEGREES) + 180
        if angle_error >= 0:
            angle = angle_error % 360 - 180
        else:
            angle = 359 - (-1 - angle_error) % 360 - 180
        ranges = lidar_data.ranges[i] * 100
        if not math.isnan(ranges):
            if abs(angle - gyro_value) < 10:
                mid = ranges
            if abs(angle - 90 + gyro_value) < 5:
                left = ranges
            if abs(angle + 90 + gyro_value) < 5:
                right = ranges
    return int(left), int(mid), int(right) ,gyro_value

def line_color_read():#讀取地上顏色數值
    global line_middle, color_direction_middle, white_color
    with open('save_file/color_sensor.p', mode='rb') as f:
        file = pickle.load(f)
    blue_color = file['Blue']
    orange_color = file['Orange']
    white_color = file['white']
    color_direction_middle = (blue_color + orange_color) / 2 + 2
    line_middle = (white_color + orange_color) / 2
    print('orange:' + str(orange_color))
    print('blue:' + str(blue_color))
    print('white:' + str(white_color))
    print('direction_middle:', color_direction_middle)
    print('line middle:', line_middle)
    print('=======================')
    
def block_color_read():  # 讀取積木的HSV數值
    global green_lower, green_upper, red_lower, red_upper, pink_lower, pink_upper
    
    # 讀取綠色的HSV值
    with open('save_file/YCrCb_Green.p', mode='rb') as f:
        file = pickle.load(f)
    g_lower = file['Lower']
    g_upper = file['Upper']
    print('Green_Lower:' + str(g_lower))
    print('Green_Upper:' + str(g_upper))
    
    # 讀取紅色的HSV值
    with open('save_file/YCrCb_Red.p', mode='rb') as f:
        file = pickle.load(f)
    r_lower = file['Lower']
    r_upper = file['Upper']
    print('Red_Lower:' + str(r_lower))
    print('Red_Upper:' + str(r_upper))
    
    # 讀取粉紅色的HSV值
    with open('save_file/YCrCb_Pink.p', mode='rb') as f:
        file = pickle.load(f)
    p_lower = file['Lower']
    p_upper = file['Upper']
    print('Pink_Lower:' + str(p_lower))
    print('Pink_Upper:' + str(p_upper))
    
    # 將讀取的HSV值轉換為numpy數組
    green_lower = np.array(g_lower, np.uint8)
    green_upper = np.array(g_upper, np.uint8)
    red_lower = np.array(r_lower, np.uint8)
    red_upper = np.array(r_upper, np.uint8)
    pink_lower = np.array(p_lower, np.uint8)
    pink_upper = np.array(p_upper, np.uint8)

def color_read():#讀取顏色感應器數值
    global color
    while thread_run:
        color = color_sensor.readluminance()['c']
        time.sleep(0.01)
def gyro_read():
    global gyro
    while thread_run:
        gyro = gyro_sensor.raw()
        time.sleep(0.01)

def gyro_relative(value):
    error = value - gyro + 180
    if error >= 0:
        result = (error % 360) - 180
    else:
        result = 359 - ((-1 - error) % 360) - 180
    return result

def car_control():#鍵盤控制直流馬達前進與停止
    while thread_run:
        if opencv_detect.get_keyboard() == ord('w'):
            motor.power(90)
        elif opencv_detect.get_keyboard() == ord('s'):
            motor.power(0)
            
        elif opencv_detect.get_keyboard() == ord('x'):
            motor.power(-90)

            
        time.sleep(0.1)

def dodgeblock_control(set_gyro):#影像辨識控制伺服馬達閃避積木
    global record_box
    left, mid, right, gyro = lidar_get_distance(set_gyro)
    if opencv_detect.get_red_y() == -1 and opencv_detect.get_green_y() == -1 and left <100 and right < 100:
        #print('gyro go')
        
        left, mid, right, gyro = lidar_get_distance(set_gyro)
        if left > 0 and right > 0:
            center_error = (right - left) / 1.8
        elif left > 0:
            center_error = 48 - left
        else:
            center_error = right - 48
        servo_angle = ((center_error * center_kp) + (gyro * gyro_kp))
    elif opencv_detect.get_red_y() > opencv_detect.get_green_y() and opencv_detect.get_red_y() < 370:
        servo_angle =  (opencv_detect.get_red_x() - opencv_detect.get_red_node_x()) * dodgeblock_kp
    elif opencv_detect.get_red_y() < opencv_detect.get_green_y() and opencv_detect.get_green_y() < 370:
        see = time.time()
        servo_angle =  (opencv_detect.get_green_x() - opencv_detect.get_green_node_x()) * dodgeblock_kp
    else:
        left, mid, right, gyro = lidar_get_distance(set_gyro)
        servo_angle = (gyro * gyro_kp)
    servo.angle(-servo_angle)

def dodgeblock_control_final(set_gyro):#影像辨識控制伺服馬達閃避積木
    global record_box
    left, mid, right, gyro = lidar_get_distance(set_gyro)
    
    if opencv_detect.get_red_y() == -1 and opencv_detect.get_green_y() == -1 and left <100 and right < 100:
        #print('gyro go')
        left, mid, right, gyro = lidar_get_distance(set_gyro)
        if left > 0 and right > 0:
            center_error = (right - left) / 1.8
        elif left > 0:
            center_error = 48 - left
        else:
            center_error = right - 48
        servo_angle = ((center_error * center_kp) + (gyro * gyro_kp))
    
    elif opencv_detect.get_red_y() > opencv_detect.get_green_y() and opencv_detect.get_red_y() < 370:
        if  opencv_detect.get_red_y() > 340:
            record_box =1
        servo_angle =  (opencv_detect.get_red_x() - opencv_detect.get_red_node_x()) * dodgeblock_kp
    elif opencv_detect.get_red_y() < opencv_detect.get_green_y() and opencv_detect.get_green_y() < 370:
        see = time.time()
        if  opencv_detect.get_green_y() > 340:
            record_box =2
        servo_angle =  (opencv_detect.get_green_x() - opencv_detect.get_green_node_x()) * dodgeblock_kp
    else:
        left, mid, right, gyro = lidar_get_distance(set_gyro)
        servo_angle = (gyro * gyro_kp)
    servo.angle(-servo_angle)

def dodgeblock_to_line_parking(set_gyro):#閃避積木到偵測地上線
    global Location
    while color > line_middle:
        if opencv_detect.get_pink_y() != -1 :
            Location = True

            break
            
        #dodgeblock_control_final(set_gyro)
        dodgeblock_control(set_gyro)
        time.sleep(0.001)


def dodgeblock_to_line(set_gyro):#閃避積木到偵測地上線
    while color > line_middle:
        #dodgeblock_control_final(set_gyro)
        dodgeblock_control(set_gyro)
        time.sleep(0.001)

def dodgeblock_to_line_final(set_gyro):#閃避積木到偵測地上線
    while color > line_middle:
        dodgeblock_control_final(set_gyro)
        time.sleep(0.001)

def dodgeblock_to_time_parking(set_time, set_gyro):#閃避積木到時間
    set_reset = time.time()
    while time.time() - set_reset < set_time:
        if opencv_detect.get_pink_y() != -1 :
            Location = True
            dodgeblock_control(set_gyro)
        time.sleep(0.001)
def dodgeblock_to_time(set_time, set_gyro):#閃避積木到時間
    
    set_reset = time.time()
    while time.time() - set_reset < set_time:
        dodgeblock_control(set_gyro)
        time.sleep(0.001)

def dodgeblock_to_time_final(set_time, set_gyro ):#閃避積木到時間
    
    set_reset = time.time()
    while time.time() - set_reset < set_time:
        dodgeblock_control_final(set_gyro)
        time.sleep(0.001)

def direction_detect():
    global turn_direction, pluse_turn, final_angle
    print('direction detect')
    while color > line_middle:
        dodgeblock_control(0)
    low_color = 100
    while color < line_middle:
        dodgeblock_control(0)
        if color < low_color:
            low_color = color
    if low_color < color_direction_middle:
        print('blue line')
        final_angle = -270
    else:
        print('orange line')
        turn_direction = [0, 90, 180, 270]
        final_angle = 270
        pluse_turn = 90


    
        




# def lest_round():
#     print('\nstart go back')
#     dodgeblock_to_line(turn_direction[3])
#     print('lest block: ', record_box)
#     if record_box == 'red':
#         reverse_direction = [90, 0, 270, 180]
#         gyro_turn_to(reverse_direction[0], 10)
#         dodgeblock_to_time(2, reverse_direction[0])
#         reverse_count = 0
#         for i in range(3):
#             dodgeblock_to_line(reverse_direction[reverse_count])
#             dodgeblock_to_time(3, reverse_direction[reverse_count + 1])
#             reverse_count = reverse_count + 1
#     else:
#         dodgeblock_to_line(0)
#         dodgeblock_to_time(2.2, 0)

# 
def center_control(set_gyro,angle):
    global road
    left, mid, right, gyro = lidar_get_distance(set_gyro)
    if left + right < 70:
        LED.red_on()
        _road = 'narrow'
        if left > 0 and right > 0 and left < 200 and right < 200:
            center_error = (right - left-angle) / 1.8
        elif right < 0 or right > 200:
            center_error = 48 - left
        else:
            center_error = right - 48
        servo.angle(-center_error * 0.8 + -gyro * 1.2)
    else:
        LED.red_off()
        _road = 'width'
        if left < 17 and left > 0:
            servo.angle(-20)
        elif right < 17 and right > 0:
            servo.angle(20)
        else:
            servo.angle(-gyro * 1.2)

    return left, mid, right, _road
def handler(signum, frame):
    exit(0)

#=====================main=====================
#=============陀螺儀初始化=============

try:
    
    if gyro_sensor.begin() is not True:
        print("Error initializing device")
        exit()
    time.sleep(1)
    gyro_sensor.setExternalCrystalUse(True)

    #=============定義多執行序=============
    color_read_thread = threading.Thread(target = color_read)
    gyro_read_thread = threading.Thread(target = gyro_read)
    car_control_thread = threading.Thread(target = car_control)

    line_color_read()
    block_color_read()
    opencv_detect = opencv_recognition(red_lower, red_upper, green_lower, green_upper, pink_lower, pink_upper)#opencv影像辨識功能定義與初始化opencv功能
    opencv_detect.start()
    color_read_thread.start()
    gyro_read_thread.start()
    car_control_thread.start()
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, lidar_callback)
    signal.signal(signal.SIGINT, handler)
    print('ros callback ...')
    while not lidar_run:
        pass
    print('ros running...\n')
    servo.angle(0)
    print('waitting start ...')
    button_state = 1
    while button_state == 1 and not opencv_detect.get_keyboard() == ord('g') and not opencv_detect.get_keyboard() == ord('c'):
        button_state = button.raw_value()
        time.sleep(0.05)
        #center_control(0)
        left, mid, right, gyro = lidar_get_distance(0)
        #print( opencv_detect.get_pink_y() ,opencv_detect.get_pink_x())
        #print(gyro)
        #print('left:', left, ' mid:', mid, ' right:', right)
    print('start run')
    motor.power(power)
    #=============開始閃避積木=============
    direction_detect()
    dodgeblock_to_time(2,pluse_turn)
    for angle in turn_direction:#turn_1
        count = count + 1
        if count == 1:
            continue
        dodgeblock_to_line(angle)
        print('count',count)
        
        if count ==4:
            dodgeblock_to_time_final(2, angle + pluse_turn)
            print('record_box',record_box)
        else:   
            dodgeblock_to_time(2, angle + pluse_turn)
    #turn_direction.pop()
    print('END_turn_1')
    
    for angle in turn_direction:#turn_2
        print(angle)
        dodgeblock_to_line(angle)
        dodgeblock_to_time(2.2, angle + pluse_turn)
    
    print('END_turn_2')
    print('record_box', record_box)
    count = count + 2
    print(count)
    if record_box == 1 and final_angle ==270 :
        final_turn = -90
        style =  1
        print('shun')
        #dodgeblock_to_line(final_angle,count)
        #dodgeblock_to_time(2.2,0,count)
        while opencv_detect.get_red_y() != -1 and opencv_detect.get_red_y() < 320 :
            dodgeblock_control(0)
        gyro_1 =0
        while gyro_1 < -170:
            left, mid, right, gyro_1 = lidar_get_distance(final_angle)
            servo.angle(40)
        dodgeblock_to_line(180)
        dodgeblock_to_time(2.5,90)
        turn_direction_final =[90,0,-90]
        for angle in turn_direction_final:
            dodgeblock_to_line(angle)
            dodgeblock_to_time(3.5, angle + final_turn)
        
    elif record_box == 1 and final_angle==-270:
        style = 1
        print('inverse')
        #dodgeblock_to_line(final_angle,count)
        #dodgeblock_to_time(2.2,0,count)
        while opencv_detect.get_red_y() != -1 and opencv_detect.get_red_y() < 350:
            dodgeblock_control(0)
        print('End')
        gyro_1=0
        while gyro_1 < 150:
            left, mid, right, gyro_1 = lidar_get_distance(final_angle)
            servo.angle(40)
            print(gyro_1)
        print('end')
        dodgeblock_to_line(-180)
        dodgeblock_to_time(2,-120)
        turn_direction_final = [-90, 0, 90]
        pluse_turn = 90
        
        for angle in turn_direction_final:
            dodgeblock_to_line(angle)
            dodgeblock_to_time(3.5, angle + pluse_turn)
    else:
        if final_angle==-270:#blue color
            style = 2
            pluse_turn=-90
            turn_direction_1 = [90, 0, -90, -180, 90]
            for angle in turn_direction_1:
                dodgeblock_to_line(angle)
                dodgeblock_to_time(2, angle + pluse_turn)
            Final_Direction = -90
        else:#orange color
            style = 2
            pluse_turn=90
            turn_direction=[-90, 0, 90, 180, -90]
            for angle in turn_direction:
                dodgeblock_to_line(angle)
                dodgeblock_to_time(2, angle + pluse_turn)
            Final_Direction = 90
    
    #=============結束============
finally:
    print('\nshutdown')
    motor.power(0)
    #servo.angle(0)
    thread_run = False
    color_read_thread.join()
    car_control_thread.join()
    gyro_read_thread.join()
    opencv_detect.shutdown()#opencv影像辨識功能停止串流
