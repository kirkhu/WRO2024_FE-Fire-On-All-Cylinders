from machine import Pin, PWM, I2C, UART
import _thread
import struct
import time
from function import (
    initialize_bno055,
    read_bno055_heading,
    set_initial_heading_as_zero,
    read_relative_heading,
    set_servo_angle,
    control_motor,
    encoder_interrupt,
    pd_control,
    BNO055_PID,
    jetson_PID,
    run_encoder,
    run_to_wall,
    servo_to_angle,
    jetson_nano_return,
    jetson_all
)


# 初始化PWM、马达、编码器、I2C、按键引脚
servo_pin = PWM(Pin(28), freq=50)
motor_in1 = Pin(3, Pin.OUT)
motor_in2 = Pin(2, Pin.OUT)
motor_pwm = PWM(Pin(22), freq=1000)
encoder_pin_A = Pin(0, Pin.IN)
encoder_pin_B = Pin(1, Pin.IN)
button = Pin(18, Pin.IN, Pin.PULL_UP)
i2c1 = I2C(id=1, sda=Pin(26), scl=Pin(27), freq=400000)  # 陀螺仪感测器
i2c2 = I2C(id=0, sda=Pin(12), scl=Pin(13), freq=420000)  # 颜色感测器
turn_angle = [0,0,0,0]
right_turn = [90,180,-90,0]
left_turn = [-90,180,90,0]
turn_sevro = 180

uart = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))  # 调整 UART 端口和波特率

try:
    # 初始化TCS34725和BNO055
    set_servo_angle(0)
    set_initial_heading_as_zero()
    initialize_bno055()
    

    # 等待按钮按下
    while button.value() == 1:
        time.sleep(0.2)
        print(read_relative_heading())
        #print(jetson_nano_return(2),jetson_nano_return(4),jetson_nano_return(6))
        jetson_all()
    
    set_initial_heading_as_zero()
    initialize_bno055()
    
    turn_side = run_to_wall(80, 0)  # 示例运行函数，调整参数根据需要
    if turn_side == 1:
        turn_angle = right_turn
        turn_sevro = 180
    if turn_side == 2:
        turn_angle = left_turn
        turn_sevro = -180
    print(turn_angle)
    for i in range(3):
        for angle in turn_angle:
            print(angle)
            servo_to_angle(turn_sevro, 60,angle)
            print("turn_pass")
            run_encoder(3000, 100,angle)
            if i == 2:
                if turn_angle[3] == angle:
                    break
            run_to_wall(70, angle)
            print("wall_pass")
        
    control_motor(0)

except KeyboardInterrupt:
    motor_in1.off()
    motor_in2.off()
    set_servo_angle(0)
    print("程序中断")





