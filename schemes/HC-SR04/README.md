，<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Ultrasonic sensor Introduction</div> 

- ## __HC-SR04 Ultrasonic sensor 超音波感測器__
<div align="center">
<table>
<tr>  
<td>
  <ul>
  <li>The HC-SR04 ultrasonic sensor was chosen because it can detect the distance between us and the side wall when we are about to enter the parking lot, making it easier for us to make parking actions.</li>
  <li>The main functions of the HC-SR04 ultrasonic sensor on vehicles are:</li>
     <ol>
     <li>Before we enter the parking lot, the rear of the car will face the parking lot. We can use the ultrasonic sensor at the rear of the car to measure the distance between us and the wall, thereby knowing our position on the field.</li>
   </ol>

  <li>HC-SR04 超音波感測器被選中是因為它可以在我們要進入停車場時，偵測出我們與邊牆的距離，方便我們做出停車的動作。</li>
   <li>HC-SR04 超音波感測器在車輛上的主要功能是：</li>
   <ol>
     <li>在我們要進入停車場前，車尾會面對停車場，我們就可以透過車尾的超音波感測器測出我們與牆面的距離，藉此知道我們在場地上的位置。</li>
   </ol>
</ul>
</td>
 <td width=250 ><img src="./img/HC-SR04.png" alt="HC-SR04" width="250" />
</td>
</tr>
</table>
</div>  

We encountered a bottleneck when using the Ultrasonic sensor to detect lines because I was unsure how to write a Python program to detect the values of blue and orange lines.

With the guidance of my teacher, we successfully completed it.  
  __The partial code is as follows:__


  在使用超音波感測器，我們透過上網查找相關資料來嘗試撰寫超音波感測器的程式，完成後的片段程式如下。


  #### Function
```
class HC-SR04():
    def __init__(self):
        self.enable_selection()
        self.time_selection()
        self.gain_selection()
    def enable_selection(self):
        """Select the ENABLE register configuration from the given provided values"""
        ENABLE_CONFIGURATION = (HC-SR04_REG_ENABLE_AEN | HC-SR04_REG_ENABLE_PON)
        bus.write_byte_data(HC-SR04_DEFAULT_ADDRESS, HC-SR04_REG_ENABLE | HC-SR04_COMMAND_BIT, ENABLE_CONFIGURATION)
    def time_selection(self):
        """Select the ATIME register configuration from the given provided values"""
        bus.write_byte_data(HC-SR04_DEFAULT_ADDRESS, HC-SR04_REG_ATIME | HC-SR04_COMMAND_BIT, HC-SR04_REG_ATIME_2_4)
        """Select the WTIME register configuration from the given provided values"""
        bus.write_byte_data(HC-SR04_DEFAULT_ADDRESS, HC-SR04_REG_WTIME | HC-SR04_COMMAND_BIT, HC-SR04_REG_WTIME_2_4)
    def gain_selection(self):
        """Select the gain register configuration from the given provided values"""
        bus.write_byte_data(HC-SR04_DEFAULT_ADDRESS, HC-SR04_REG_CONTROL | HC-SR04_COMMAND_BIT, HC-SR04_REG_CONTROL_AGAIN_1)
    def readluminance(self):
        """Read data back from HC-SR04_REG_CDATAL(0x94), 8 bytes, with HC-SR04_COMMAND_BIT, (0x80)
        cData LSB, cData MSB, Red LSB, Red MSB, Green LSB, Green MSB, Blue LSB, Blue MSB"""
        data = bus.read_i2c_block_data(HC-SR04_DEFAULT_ADDRESS, HC-SR04_REG_CDATAL | HC-SR04_COMMAND_BIT, 8 )        
  # Convert the data
        cData = data[1] * 256 + data[0]
        red = data[3] * 256 + data[2]
        green = data[5] * 256 + data[4]
        blue = data[7] * 256 + data[6]        
  # Calculate luminance
        luminance = (-0.32466 * red) + (1.57837 * green) + (-0.73191 * blue)
        return {'c' : cData, 'r' : red, 'g' : green, 'b' : blue, 'l' : luminance}
``` 
  #### Snippet of Code  
```
data = bus.read_i2c_block_data(HC-SR04_DEFAULT_ADDRESS, HC-SR04_REG_CDATAL | HC-SR04_COMMAND_BIT, 8 )        
        # Convert the data
        cData = data[1] * 256 + data[0]
        red = data[3] * 256 + data[2]
        green = data[5] * 256 + data[4]
        blue = data[7] * 256 + data[6]        
# Calculate luminance
        luminance = (-0.32466 * red) + (1.57837 * green) + (-0.73191 * blue)
        return {'c' : cData, 'r' : red, 'g' : green, 'b' : blue, 'l' : luminance}
```
- ### Ultrasonic sensor detection side wall program judgment process 超音波感測器偵測邊牆程式判斷流程
***

1. When the program executes the part where it needs to stop, it will first read the distance between the robot and the wall, and     record the value into the variable.
2. Then, on the way back, it will always judge whether the value read by the ultrasonic sensor is less than the target value of 40. When the target value is reached, it will turn into the parking lot through gyro tracking.

***

1. 程式執行到要停車的部分，首先會讀取機器人與牆壁的距離，並將數值一直記錄到變數裡。
2. 然後，在後退的途中會一直判斷超音波感測器讀取到的數值是否小於目標值40，當達到目標值，會透過gyro循跡轉進停車場。

***

<div align=center><img src="./img/color_sensor.png"></div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  