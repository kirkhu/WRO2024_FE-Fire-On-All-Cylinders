from machine import Pin, PWM, I2C, UART
import struct
import time

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
HEADER = b"A"  # 包头定义
HEADER_SIZE = len(HEADER)
DATA_SIZE = 20  # 5个整数，每个4字节，共20字节
TOTAL_SIZE = HEADER_SIZE + DATA_SIZE  # 包头 + 数据的总长度

# 配置UART
uart = UART(0, baudrate=115200, bits=8, parity=None, stop=1, tx=Pin(16), rx=Pin(17))


# 全局变量设置
kp_heading = 4  # 默认航向角比例增益
kd_heading = 6 # 默认航向角微分增益
kp_data = 0.008 # 默认数据列比例增益
kd_data = 0.01  # 默认数据列微分增益
encoder_count = 0  # 初始化编码器计数
initial_heading = 0  # 初始化初始航向角
last_state_A = encoder_pin_A.value()  # 初始化编码器状态
data_value = [0] * 12  # 初始化数据列表
current_last = 0
current = 0
turn_side = 0
value = [0] * 12
# 设置BNO055为NDOF模式
def initialize_bno055():
    try:
        i2c1.writeto_mem(0x28, 0x3D, bytes([0x00]))  # 配置模式
        time.sleep_ms(10)
        i2c1.writeto_mem(0x28, 0x3D, bytes([0x0C]))  # NDOF模式（融合算法）
        time.sleep_ms(20)
    except OSError as e:
        print('BNO055初始化错误:', e)

# 读取BNO055航向角数据的函数
def read_bno055_heading():
    try:
        heading_bytes = i2c1.readfrom_mem(0x28, 0x1A, 2)
        heading = struct.unpack('<h', heading_bytes)[0] / 16.0  # 航向角（Yaw）
        if heading > 180:
            heading -= 360
        return heading
    except OSError as e:
        print('读取BNO055错误:', e)
        return None

# 设置初始航向角为0度
def set_initial_heading_as_zero():
    global initial_heading
    i = 0
    while i < 5:
        initial_heading = read_bno055_heading()
        i += 1
        time.sleep(0.1)
    if initial_heading is None:
        raise Exception("无法读取初始航向角")

# 读取相对航向角（相对于初始航向角）
def read_relative_heading():
    heading = read_bno055_heading()
    if heading is not None:
        relative_heading = heading - initial_heading
        if relative_heading > 180:
            relative_heading -= 360
        elif relative_heading < -180:
            relative_heading += 360
        return relative_heading
    return None



# 从 Jetson Nano 读取数据
def jetson_nano_return(number):
    global data_value
    HEADER = b"A"  # 包头定义
    HEADER_SIZE = len(HEADER)
    DATA_SIZE = 20  # 5个整数，每个4字节，共20字节
    TOTAL_SIZE = HEADER_SIZE + DATA_SIZE  # 包头 + 数据的总长度

    if uart.any():
        data = uart.read(TOTAL_SIZE)
        
        # 检查是否接收到完整的数据包
        if len(data) == TOTAL_SIZE:
            # 查找包头
            header_index = data.find(HEADER)
            if header_index != -1:
                # 如果找到了包头，移除包头并提取数据
                start_index = header_index + HEADER_SIZE
                data = data[start_index:] + data[:start_index]
                data_value = struct.unpack('5i', data[:DATA_SIZE])
                return data_value[number]
            else:
                print("Error: Incorrect header received.")
        else:
            print("Error: Incomplete data received.")
    return data_value[number]
# 设置舵机角度
def set_servo_angle(angle):
    min_duty = 1000  # 对应1ms的占空比
    max_duty = 2000  # 对应2ms的占空比
    duty = int(min_duty + (angle-15 + 180) * (max_duty - min_duty) / 360)
    duty_u16 = int(duty * 65535 / 20000)
    servo_pin.duty_u16(duty_u16)


# 定义马达控制函数
def control_motor(speed):
    if speed > 0:
        motor_in1.high()
        motor_in2.low()
    elif speed < 0:
        motor_in1.low()
        motor_in2.high()
    else:
        motor_in1.low()
        motor_in2.low()
    motor_pwm.duty_u16(int(abs(speed) * 65535 / 100))  # 设置PWM占空比

# 定义编码器中断处理函数
def encoder_interrupt(pin):
    global encoder_count, last_state_A
    state_A = encoder_pin_A.value()
    state_B = encoder_pin_B.value()
    if state_A != last_state_A:
        encoder_count += 1 if state_B != state_A else -1
    last_state_A = state_A

# GPIO中断设置
encoder_pin_A.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=encoder_interrupt)

# 定义PD控制函数
def pd_control(target, current, kp, kd):
    global current_last  # 使用全局变量
    error = current - target
    derivative = (current - current_last) 
    control_signal = -(kp * error + kd * derivative)
    current_last =  current  # 在 return 之前更新 current_last
    return control_signal

def BNO055_PID(target_angle):
    global last_heading
    if read_relative_heading()<-135:
        heading_control_signal = pd_control(-target_angle, read_relative_heading(), kp_heading, kd_heading)
    else:
        heading_control_signal = pd_control(target_angle, read_relative_heading(), kp_heading, kd_heading)
    return heading_control_signal

def jetson_PID(mode, space):
    control_signal = pd_control(space, jetson_nano_return(mode), kp_data, kd_data)
    return control_signal

def run_encoder(motor_angle, speed, target_angle):
    global encoder_count
    encoder_count = 0  # 在运行前将编码器计数归零
    while abs(encoder_count) < motor_angle:
        # 根据 data_mode 选择 PD 控制信号
        combined_control_signal = BNO055_PID(target_angle) 
        
        # 使用控制信号调整舵机
        set_servo_angle(combined_control_signal)
        control_motor(speed)
        
        print(f"编码器计数: {encoder_count}, combined_control_signal: {combined_control_signal}, read_bno055_heading: {read_bno055_heading()}")
        jetson_all()
        time.sleep(0.01)


def run_to_wall(speed, target_angle):
    global turn_side
    control_motor(speed)
    jetson_all()
    while value[2] <= 6100:
        jetson_all()
        if turn_side == 0:
            if  value[3] > value[4]:
                turn_side = 1
            elif value[3] < value[4]:
                turn_side = 2
        # 根据 data_mode 选择 PD 控制信号
        if value[0] >= 4000 :
            combined_control_signal = jetson_PID(0, 4000)
        elif value[1] >= 3500:
            combined_control_signal = -jetson_PID(1, 3500)
        else:
            combined_control_signal = BNO055_PID(target_angle)
        # 使用控制信号调整舵机
        set_servo_angle(combined_control_signal)
        control_motor(speed)
        print(BNO055_PID(target_angle))
        time.sleep(0.2)
    return turn_side

def servo_to_angle(angle, speed, target_angle):
    relative_heading = read_relative_heading()

    while relative_heading > target_angle + 5 or relative_heading < target_angle - 5:
        relative_heading = read_relative_heading()
        set_servo_angle(angle)
        control_motor(speed)
        print(read_relative_heading())
        time.sleep(0.02)
        jetson_all()
    set_servo_angle(0)
def jetson_all():
    global value
    value[0] = jetson_nano_return(0)
    value[1] = jetson_nano_return(1)
    value[2] = jetson_nano_return(2)
    value[3] = jetson_nano_return(3)
    value[4] = jetson_nano_return(4)
    print(value[0],value[1],value[2],value[3],value[4])


