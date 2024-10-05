<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# 停車邏輯
__這是我們跑完三圈後，執行停車任務的程式碼，以下是程式內容__
- ### Parking program(停車程式)
  - This program will initially detect whether the gyro has reached the target direction. When it reaches the target, it will turn into the parking lot.
  - 這段程式一開始會偵測gyro是否達到目標方向，在達到目標時，轉彎進入停車場。
    ```
    motor.power(58)
        dodgeblock_to_time(3,170)
        motor.power(60)
        print(gyro)
        left, mid, right, gyro = lidar_get_distance(final_angle)
        while gyro <= 85 and  gyro >= 95 :
            left, mid, right, gyro = lidar_get_distance(final_angle)
            servo.angle(40)
            print(gyro)
        servo.angle(0)
        cm = measure()
        while cm <= 40 :
            cm = measure()
            gyro_p(90)
        if opencv_detect.get_pink_x() >=320 :
            Location = 1
            left, mid, right, gyro = lidar_get_distance(final_angle)
            while gyro <= 175 and  gyro >= -175 :
                left, mid, right, gyro = lidar_get_distance(final_angle)
                servo.angle(40)
                print(gyro)
            while 紅外線左 == 1 :
                gyro_p(90)
            motor.power(-60)
            left, mid, right, gyro = lidar_get_distance(final_angle)
            while gyro <= -5 and  gyro >= 5 :
                left, mid, right, gyro = lidar_get_distance(final_angle)
                servo.angle(40)
                print(gyro)
        else :
            Location = 2
            left, mid, right, gyro = lidar_get_distance(final_angle)
            while gyro <= -5 and  gyro >= 5 :
                left, mid, right, gyro = lidar_get_distance(final_angle)
                servo.angle(40)
                print(gyro)
            while 紅外線右 == 1 :
                gyro_p(90)
            motor.power(-60)
            left, mid, right, gyro = lidar_get_distance(final_angle)
            while gyro <= -5 and  gyro >= 5 :
                left, mid, right, gyro = lidar_get_distance(final_angle)
                servo.angle(-40)
                print(gyro)
        motor.power(60)
        servo.angle(0)
        while cm <= 10 :
            cm = measure()
            gyro_p(90)
        motor.power(0)
    ```   
__以下是這是我們的停車測試影片__
- ### Parking test video(停車測試影片)
[![Open Challenge power 50 Full width On-All-Cylinders](./img/stop_car.png)](https://www.youtube.com/watch?v=h04wtojxz30)

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
