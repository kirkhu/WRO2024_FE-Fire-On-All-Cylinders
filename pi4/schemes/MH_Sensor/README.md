，<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Introduction to infrared sensors</div> 

- ## __MH sensor Series 紅外線感測器__
<div align="center">
<table>
<tr>  
<td>
  <ul>
  <li>The MH sensor Series infrared sensor was selected because of its small size and its ability to sense objects on the field.</li>
  <li>The main functions of MH sensor Series infrared sensors on vehicles are:</li>
     <ol>
     <li>By using infrared sensors to detect whether the side wall of the parking lot is sensed when entering the parking lot, it is convenient for us to make parking actions.</li>
   </ol>

  <li>MH sensor Series 紅外線感測器被選中是因為它體積較小且可以達到感測場地上物件的目的。 </li>
   <li>MH sensor Series 紅外線感測器在車輛上的主要功能有：</li>
   <ol>
     <li>透過在進入停車場中，使用紅外線感測器偵測是否感測到停車場邊牆，以方便我們做出停車動作。</li>
   </ol>
</ul>
</td>
 <td width=250 ><img src="./img/MH sensor.png" alt="MH sensor" width="250" />
</td>
</tr>
</table>
</div>  

 
  __The partial code is as follows:__

  - When using infrared sensors, we searched for relevant information on the Internet and tried to write a program for the infrared sensor. The completed program fragment is as follows.

  - 在使用紅外線感測器，我們透過上網查找相關資料來嘗試撰寫紅外線感測器的程式，完成後的片段程式如下。


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
- ### Infrared sensor detection parking lot side wall program process 紅外線感測器偵測停車場邊牆程式流程
***

1. When the program starts to execute the parking part, it will repeatedly detect whether the parking lot side wall is sensed.
2. When the side wall of the parking lot is sensed, it will be determined whether the infrared sensor on the left or the right of the robot has detected it, and then the subsequent parking program will be executed.

***

1. 程式在開始執行停車的部分時，會重複偵測是否有感測到停車場邊牆。
2. 當感測到停車場邊牆時，會判斷是機器人左方的紅外線感測器偵測到還是右方的紅外線感測器偵測到，在藉此執行後續停車程式。

***

<div align=center><img src="./img/color_sensor.png"></div>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
