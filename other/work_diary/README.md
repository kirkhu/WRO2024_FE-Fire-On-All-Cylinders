<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Work Diary (工作日誌)</div>

  Here is the record of the process for own design and manufacturing of vehicle and components, with off the shelf electrical components, such as motors and sensors.  
以下為自行設計和製造車輛及其組件，利用選購的電動機和感應器等現成電氣元件的歷程紀錄

## 2024/03/25 ~ 2024/03/31  

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**  

At the beginning, since we were unsure of how to start building and making the vehicle, we referenced the Donkey Car official website. Therefore, the construction of the vehicle will be based on modifications of the vehicle design from the official website.

由於一開始我們還不知道如何開始建構及製作，因此我們參考了Donkey Car 官網，因此車輛的製作會基於官網的車輛來改造。

<div align="center">
<table>
<tr align="center"><th><a href="https://www.donkeycar.com/">Donkey Car 官網</a></th>
<th><a href="http://docs.donkeycar.com/">Donkey Car 技術文件</a></th>
</tr>
<tr align="center">
<td> <img src="./img/3/donkeycar.png" width = "300"  alt="資料" align=center /></td>
<td><img src="./img/3/donkeycar_doc.png" width = "300"  alt="資料" align=center /></td>
</tr>
</table>
</div>

<div align="center" width=100%>
<img src="./img/3/think.jpg" width="300" alt="Daily" >
</div>

## 2024/04/01 ~ 2024/04/07

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU
**Content:**

- To ensure the smooth progression of the competition, our team carefully planned the completion timeline for each stage of the competition activities.
- After reading the rules, We started to choose the controller. After watching the previous competitions, we found that most of them are raspberry pi but there are also jetson nano, so I decided to choose one of these two. In the end, I chose raspberry pi 4B because of its smaller size and cheaper price than jetson nano.

- 為確保競賽活動順利進行，我們小組進行了競賽活動各階段工作完成時間的細心規劃。，如下圖。
- 在閱讀完規則後，開始挑選控制器，因為看過歷屆的比賽，發現大多都是 raspberry pi ，但也有 jetson nano ，因此決定在這兩種裡挑一種，最後選擇了 raspberry pi 4B ，因為體積比較小而且價格也比 jetson nano 便宜。

  **競賽活動各階段工作完成時間規劃表(甘特圖)**

<div align="center" >
  <img src="../img/gantt.png" width = "600" height = "" alt="甘特圖" align=center />
</div>

### Vehicle Computing Controller(車輛運算控制器)

<div align="center" >
<table >
<tr align="center">
<th>Raspberry pi 4 B 8G</th>
<th>jetson nano </th>
<tr align="center">
<td>
<img src="./img/3/raspberry_pi_4.png" width = "300"  alt="樹梅派" /></td>
<td>
<img src="./img/3/jeston_nano.png" width = "300"  alt="jetson nano"/></td>
</tr>
</table>
</div>

## 2024/04/08 ~ 2024/04/14

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**  

- While waiting for the Raspberry Pi to initialize and libraries to be installed, we selected the motor for propulsion, with two options: JGA25-370 and JGA16-050. The former boasts higher torque, capable of moving heavier objects, while the latter is smaller and lighter, albeit with relatively lower torque. Considering the potential weight of the robot, we opted for the higher torque of the JGA25-370.
- Among the JGA25-370 options, there are several variations currently available within the club.
- During the testing of motor operation, a simple application of positive and negative voltage did not provide effective control over the JGA25-370's performance or speed adjustment. As a result, a motor controller is needed to regulate the speed of the DC geared motor. Two options were considered: the L293D chip and the L298N module. To minimize weight, we chose the compact L293D chip. Its small size allows us to accommodate more sensors, thereby saving space, reducing weight, and enhancing the robot's maneuverability.

- 在等待初始化樹梅派及安裝函式庫時，挑選作為動力的馬達，有兩種，分別是 JGA25-370 和 JGA16-050，前者的優點是扭力大，可以帶動較重的物體，後者的優點是體積小，重量也比較輕，但是扭力相對較小，由於考慮到機體可能會比較重，所以選了扭力較大的 JGA25-370
- 而 JGA25-370 有許多種不同的分支，下面幾顆是目前社團擁有的
- 在測試馬達的作動方式時，單純的提供正負極並沒有辦法很好的控制JGA25-370的作動，無法調節速度，因此還需要馬達控制器來調節直流減速馬達的速度，有兩種選擇：L293D晶片和L298N模組。為了減輕重量，我們選擇了體積較小的L293D晶片。它的小巧尺寸使我們能夠安裝更多的感應器，進而節省空間、減輕重量，並增加機器人的機動性。

#### DC Motor(直流馬達)

<div align="center"><table><tr align="center">
<th rowspan="2">Model(型號)</th>
<th>JGA25 370</th>
<th>JGA25 370</th>
<th>JGA25 370B</th>
<th>JGA25 371</th>
<th>JGA16-050</th>
</tr>
<tr  align="center">

<td><img src="./img/4/JGA25-370_1360RPM.JPG" width = "150" alt="JGA25-370_1360RPM" /></td>
<td><img src="./img/4/JGA25-370_620RPM.JPG" width = "150" alt="JGA25-370_620RPM" /></td>
<td><img src="./img/4/JGA25-370_620RPM.JPG" width = "150" alt="JGA25-370_620RPM" /></td>
<td><img src="./img/4/JGA25-371_1_34.JPG" width = "100" alt="JGA25-371M" /></td>
<td ><img src="./img/5/JGA16-050.png" width = "150" alt="JGA16-050" /></td>
</tr>
<tr align="center">
<td >Speed(轉速)</td>
<td >1360rpm</td>
<td >620rpm</td>
<td >467rpm</td>
<td >294rpm</td>
<td >220rpm</td>
</tr>
<tr align="center">
<td>Torque(力距)</td>
<td>4.27kg.cm</td>
<td>9.15kg.cm</td>
<td> </td>
<td>5.2kg.cm</td><td>1.15kgcm</td>
</tr><tr align="center">
<td>Power(功率)</td><td>5.4W</td><td>5.4W</td><td> </td><td>4.2W</td><td>0.33W</td>
</tr>
</table>
</div>

## 2024/04/15 ~ 2024/04/21  

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU
**Content:**  

- Due to the continuous movement of the vehicle, the power source needs to be changed to a battery. Considering that the motors require a 12V voltage to operate, we need to choose a battery with a voltage of 12V and a current of 3V. There are two options: lithium-ion batteries (18650) and lithium polymer batteries (3S). However, the 18650 battery is heavier and takes up more space, so we opted for the lithium polymer battery.
- However, the maximum voltage supported by the Raspberry Pi is only 5.2V. Therefore, we need to use a step-down module to reduce the voltage to prevent damage to the Raspberry Pi. We initially considered using the LM2596 DC-DC adjustable step-down module, as it has a numerical display to show the current output voltage. However, its maximum current capacity is only 3A. Therefore, we chose a constant voltage and constant current step-down power supply module that can handle up to 5A. Though it lacks a numerical display, we will install a low voltage alarm to detect the battery voltage and ensure its safety.

- 由於車輛需要不斷的移動，因此需要將電力來源改成電池。考慮到馬達需要12V的電壓才能使用，我們選擇了電壓為12V、電流為3A的電池。有兩種選擇：鋰離子電池(18650)和鋰聚合電池(3S)。然而，由於18650電池重量較重且佔據空間較大，因此我們選擇了鋰聚合電池。
- 但是樹梅派最大電壓只能到5.2V，因此我們需要使用降壓板來將電壓降低，以避免樹梅派受損。最初我們打算使用LM2596 DC-DC可調降壓模組，因為它有數值顯示，可以顯示目前輸出電壓的大小。然而，它的最大電流只能接受3A，因此我們選擇了一個能夠支援最大5A電流的恆壓恆流降壓電源模組。儘管沒有數值顯示，我們將安裝一個能夠偵測電池電壓的低電壓警報器，以確定目前電池的電壓是否正常。

#### Batteries(電池)

<div align="center" width=100%>
<table >
<tr>
  <th> 18650 lithium batteries(18650充電電池) </th> <th>Li-Polymer 3S Battery (鋰聚合物電池 3S)
  </th>
</tr>
<tr>
  <td>
  <img src="./img/4/18650.jpeg" width = "300"  alt="18650" /> </td>
  <td>
  <img src="./img/4/lipo_battery.png" width = "300" alt="lipo_battery"  />
  </td>
</tr>
</table>
</div>

#### Step-Down Module(降壓模組)

<div align="center" width=100%>
<table >
<tr align="center">
  <th> LM2596 DC-DC可調降壓模組 </th>
  <th>5A恆壓恆流降壓電源模組 </th>
</tr>
<tr align="center">
  <td>  <img src="./img/4/LM25.jpeg" width = "250" height = "" alt="MG90S"/>  </td>
  <td><img src="./img/4/ADIO-DC36V5A.png" width = "300" height = "" alt="MG90S"/>
  </td>
  </tr>
</table>
</div>

#### Low Voltage Alarm(低電壓警報器)

<div align="center" width=100%>
<table >
<tr align="center">
  <th> 低電壓警報器</th>
</tr>
<tr align="center">
  <td>  <img src="./img/4/low_voltage_alarm.png" width = "150" alt="low_voltage_alarm"/>  </td>

  </tr>
</table>
</div>

## 2024/04/22 ~ 2024/04/28

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**  

- The next step is the steering motor. After searching the information on the Internet, I found that MG90S and SG90 are commonly used. The difference between MG90S and SG90 is that the front gear is metal, and the latter is plastic. Because we often need to rotate all the time, we choose MG90S, which is not easy to damage  

- 接下來是操控馬達。在網上搜尋資料後，我發現MG90S和SG90是常見的選擇。MG90S和SG90之間的差異在於前齒輪，前者是金屬的，後者則是塑料的。由於我們常常需要持續旋轉，我們選擇了MG90S，因為它不容易損壞。

#### Servo Motor(伺服馬達)

<div align="center">
<table>
<tr align="center">
<th rowspan="2">Model(型號)</th>
<th> MG90S</th>
<th >SG90</th>
</tr>
<tr align="center">
<td><img src="./img/4/MG90S.png" width = "150" height = "" alt="MG90S" align=center /></td>
<td > <img src="./img/4/SG90.png" width = "150" height = "" alt="SG90" align=center /></td>
</tr>
<tr align="center">
<td>Rotation angle(轉動角度)</td>
<td>90° MAX</td>
<td>0~90°/180° MAX</td>
</tr>
<tr align="center">
<td>Torque(轉矩)</td>
<td>2.0kg/cm</td>
<td>1.4 kg/cm</td>
</tr>
<tr align="center">
<td>Speed(轉速)</td>
<td>0.11s</td>
<td>0.1S</td>
</tr>
</table>
</div>

## 2024/04/29 ~ 2024/05/05

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- When the vehicle is uncertain about the distance ahead, it cannot turn in time when encountering a wall. Therefore, ultrasonic sensors have been added to enable the vehicle to turn before colliding with the wall.
- Based on the experiments conducted, it has been found that ultrasonic sensors can only detect obstacles in front of the vehicle. Additionally, they are less effective in detecting distances while the vehicle is swaying from side to side. Therefore, it has been decided to adopt a 360-degree LiDAR sensor for detecting distances in front of, as well as to the left and right sides of the vehicle.

- 車輛在不知道前方距離時，無法在遇到牆壁及時轉彎，因此加上了超音波，這樣就可以在撞到牆之前轉彎。
- 經實驗得知，超音波只能偵測前方障礙物距離，且在車輛左右晃動下，不容易偵測距離，因此改採用可以360度偵測的光達感測器，來當車輛的前方、左右邊的距離。

#### Distance Sensor(距離感測器 )

<div align="center" width=100%>
<table >
<tr align="center">
  <th >ultrasound (超音波)</th>
  <th>ydlidar x2(光達)</th>
</tr>
<tr>
  <td>  <img src="./img/4/ultrasound.png" width = "300"  alt="ultrasound" align=center />  </td>
  <td><img src="./img/4/Lidar_X2.jpg" width = "300"  alt="ydlidar x2" align=center />
  </td>
  </tr>
</table>
</div>

## 2024/05/06~ 2024/05/12

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**  

- To begin assembling the machine, I used LEGO parts from the club to build the base. I attached the motors, Raspberry Pi, and other components onto the chassis and made the machine functional.
After the vehicle becomes operational, additional sensors are added to allow the vehicle to sense its surroundings and respond accordingly based on the mission requirements.
- While moving the robot, I noticed that using LEGO blocks for construction resulted in slower and sometimes stuck movements. Therefore, I switched to using a laser cutter to cut wooden boards. With the use of wooden boards, the overall weight of the robot decreased, leading to increased speed and improved energy efficiency. Additionally, I can adjust the size and position of the wooden components based on specific requirements. Unlike LEGO blocks, which come pre-built and often require continuous modifications to fit the robot's needs, wooden boards offer more flexibility and can be custom-designed using Onshape.

- 首先，我們需要組裝機器，所以我利用社團的樂高零件先組裝底座，並將馬達和樹梅派等裝上車，讓車輛能夠行駛。
隨後，在車輛可以行駛之後，我們進一步添加其他感測器，讓車輛能夠感測場地環境，並根據任務需求做出相應的反應。
- 在進行測試時，我們發現使用樂高積木的移動速度不快，而且轉彎時重量過重，無法順利轉彎。因此，我們改用雷切機切割木板，使車輛的重量減輕，速度也相應提高，同時還節省了電力。使用木板的好處是可以根據需要自行調整尺寸和位置，而不像樂高需要不斷改裝以適應各種情況。這可以通過 Onshape 等工具進行自由繪畫和調整。

<div align="center" width=100%>
<table >
<tr align="center">
  <th>木板  </th>
  <th>onshape 網站  </th>
  </tr>
<tr align="center">
  <td><img src="./img/5/wood.jpg" width = "300"  alt="wood" align=center />  </td>
  <td><img src="./img/5/onshape.png" width = "300"  alt="onshape" align=center />
  </td>
  </tr>
</table>
</div>

## 2024/05/13 ~ 2024/05/19

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- Although it is possible to move straight and turn using the ultrasonic sensor, there is a risk of scraping against walls and getting stuck at corners. Therefore, we replaced the ultrasonic sensor with a lidar, which can detect the surroundings and maintain the robot in the center of the road. With the lidar, it can also detect turns ahead.  
- However, during the actual testing of the YDLIDAR X4 and DLIDAR X2, we also encountered the issue of missing angles (as shown in the attached image). Therefore, in this competition, we decided to use the D100 sensor for vehicle detection and measuring the distance to the side walls. The results obtained from the D100 sensor met our expectations and requirements.

- 雖然可以直行和利用超音波轉彎，但是有可能轉彎時擦到牆壁，然後卡牆邊無法繼續運行，之後我們將超音波改成了光達，光達可以偵測四周，因此可以維持在道路中央，還可以偵測前方轉彎。
- 然而我們在實測光達時也發現了ydlidar x4、dlidar x2 所遇之缺角問題(如附圖所示)因此，在本次競賽中，我們決定採用D100感測器來進行車輛偵測場邊牆距離，並且使用的結果符合預期的需求。

<div align="center" width=100%>
<table >
<tr align="center" >
  <th>ydlidar x4</th>
  <th>ydlidar x2</th>
  <th>lidar 100</th>
</tr>
<tr align="center">
  <td><img src="./img/7/Lidar_X4.jpg" width = "300"  alt="ydlidar x4" align=center />  </td>
  <td><img src="./img/4/Lidar_X2.jpg" width = "300" height = "" alt="ydlidar x2" align=center />  </td>
  <td><img src="./img/7/Lidar-D100.png" width = "300"  alt="ydlidar x4" align=center /> </td>
</tr>
</table>
</div>

<div align="center" width=100%>
<table >
<tr align="center">
  <th colspan="2">ydlidar x4、X2 距離呈像</th>
  <th >lidar 100 距離呈像</th>
</tr>
<tr align="center">
  <td>  <img src="./img/7/Lidar_X2_X4_error1.jpg" width = "400" height = "" alt="偵測缺角" align=center />  </td>
  <td><img src="./img/7/Lidar_X2_X4_error.jpg" width = "400" height = "" alt="偵測缺角" align=center />  </td>
  <td> <img src="./img/7/d100.png" width = "400" height = "" alt="D100" align=center />  
  </td>
  </tr>
</table>
</div>

## 2024/05/20 ~ 2024/05/26

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**  

- TCS34725 color sensor
  - In the competition, vehicles need to demonstrate more functionalities than just turning. To achieve clockwise and counterclockwise turns, we must equip the vehicle with a color sensor to detect the colors of the lines on the ground and make appropriate judgments accordingly. Therefore, we must be particularly cautious in selecting the color sensor.
  - The TCS34725 color sensor has been chosen because it meets all the requirements of this competition. Firstly, it possesses outstanding sensing capabilities, allowing it to quickly and accurately identify the colors of the ground lines.Secondly, the sensor is thin and compact, enabling it to be placed close to the ground without interfering with the vehicle's movements.
  - The high precision of this sensor ensures that the vehicle can accurately recognize the colors of the ground lines and execute clockwise or counterclockwise turns as needed.
  
   This is a crucial factor in the vehicle's excellent performance and victory in the competition.In conclusion, the TCS34725 color sensor is a perfect fit for the requirements of this competition.Its slim design and highly accurate color recognition capabilities enable the vehicle to adapt flexibly to changes in ground lines, achieve clockwise and counterclockwise turns, and enhance its performance in the competition.
  
   I encountered a bottleneck when using the color sensor to detect lines because I was unsure how to write a Python program to detect the values of blue and orange lines.
  With the guidance of my teacher, I successfully completed it. The partial code is as follows:

- During the implementation testing, it was discovered that we originally used a USB 180-degree adapter (as shown in the lower left image), but it was prone to colliding with obstacles, particularly building blocks. As a result, we made a change and switched to using a USB 3.0 90-degree adapter for the connection. This modification makes it less likely to accidentally hit obstacles when trying to avoid them.

- TCS34725 顏色感測器
  - 車輛在競賽中需要展現更多功能，而僅僅懂得轉彎是不夠的。為了實現順時針和逆時針的轉彎，我們必須裝備車輛以感測地上線的顏色，並相應地做出適當的判斷。因此，我們在挑選顏色感測器時，要特別謹慎。
  - TCS34725 顏色感測器被選中是因為它滿足了此次競賽的所有要求。首先，它具有出色的感測功能，可以快速而準確地辨識地面線條的顏色。其次，這款感測器相當薄且小巧，這意味著它可以輕鬆貼近地面，不會對車輛的運行造成任何干擾。
  - 該感測器的高度精確度確保了車輛可以準確識別地面線條的顏色，並且根據需要執行順時針或逆時針的轉彎動作。這是車輛在競賽中表現出色並獲得優勝的關鍵因素之一。
  
   綜上所述，TCS34725 顏色感測器是一款完美符合本次競賽要求的感測器。它的薄型設計和高度精確的顏色識別功能使車輛能夠靈活適應地面線條的變化，實現順時針和逆時針的轉彎，從而提升了車輛在競賽中的表現。

   在使用顏色感測器偵測線時遇到瓶頸，因為不知道如何使用python撰寫程式來偵測藍、橘線的數值，經過老師指導，成功完成，片段程式如下。
- 在實作測試時發現，本來我們是使用usb 180度轉接頭(如左下圖)，但容易撞到積木，因此我們改成使用 usb3.0 90 度轉接頭來連接，就不容易避開障礙物時碰到障礙物。

<div align="center" width=100%>
<table >
<tr align="center">
  <th>Snippet of Code(片段程式)</th>
  <th>Function(定義成函數)</th>
</tr>
<tr align="center">
  <td><img src="./img/5/TCS34725_code.png" alt="TCS34725" width=500/ > </td>
  <td><img src="./img/5/TCS34725_code_class.png" alt="TCS34725" width=500 />
  </td>  
  </tr>
</table>
</div>

<div align="center" width=100%>
<table >
<tr align="center">
  <th>USB 水平 180°</th>
  <th>USB 垂直 90°</th>
</tr>
<tr align="center">
  <td align="center"><img src="./img/5/180degree.jpg" alt="USB180" width=400/></td>
  <td align="center"><img src="./img/5/90degree.jpg" alt="USB90" width=400/></td>
</tr>
</table>
</div>

<div align="center" width=100%>
<table >
<tr align="center">
  <th >Event Photo(活動照片)</th>
  <th >Event Photo(活動照片)</th>
</tr>
<tr>
  <td align="center"><img src="./img/4/site.jpg" width=300 alt="site" /</td>
  <td align="center"><img src="./img/4/work_photo_2_1_0417.jpg" width=300 alt="work_photo_2_1_0417" /></td>
</tr>
</table>
</div>

## 2024/05/27 ~ 2024/06/02

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**  

- In order to enable the vehicle to avoid obstacles accurately, we need to install a camera module on the vehicle. Since we are using a Raspberry Pi as the controller, we need to find a compatible camera module for it. To do this, we referred to the camera module used by the American team in last year's competition and compared it with other camera modules in the same series. Here is the product information:
- 為了讓車輛能夠正確地閃避積木，我們需要在車輛上安裝一個鏡頭模組。由於我們使用的控制器是 Raspberry Pi，因此我們需要尋找與其相容的鏡頭模組。為此，我們參考了去年美國隊伍使用的鏡頭模組，並尋找了同一系列的鏡頭模組進行比較。以下是產品資訊：

1. raspberry pi camera Rev 1.3(傳感器:OmniVision OV5647)
2. raspberry pi camera Module V2(傳感器:Sony IMX219)
3. raspberry pi camera Module V3(傳感器:Sony IMX708)

- Considering that V3 is not compatible with our existing Raspberry Pi operating system, we decided not to use that version. Additionally, the detection rate of version 1.3 is only 30p, whereas the V2 version can reach a maximum of 90p. Therefore, we ultimately chose the Raspberry Pi Camera Module V2 for our project. Through experimentation, we found that the V2 version has the best recognition performance.
- 考慮到V3與我們現有的Raspberry Pi作業系統不相容，我們決定不使用該版本。而1.3版本的偵測率僅為30p，相比之下，V2版本的偵測率最高達到90p。因此，我們最終選擇了Raspberry Pi相機模組V2作為我們的選擇。經過實驗，我們發現V2版本具有最佳的辨識效果。

### Camera Module(攝影模組)

#### Camera Module(攝影模組)

<div align="center">
<table>
<tr  align="center">
<th rowspan="2">Model(型號)</td>
<th>raspberry pi camera Rev 1.3</th>
<th >raspberry pi camera Module V2</th>
<th >raspberry pi camera Module V3</th>
</tr>
<tr  align="center">
<td ><img src="./img/5/V1.jpeg" width=200 alt="V1"  /></td>
<td ><img src="./img/5/V2.jpeg" width=200 alt="V2" ></td>
<td ><img src="./img/5/V3.jpeg" width=200 alt="V3" /></td>
</tr>
<tr  align="center">
<td>sensor</td>
<td>Omnivision OV547</td>
<td >Sony IMX 219</td>
<td>Sony IMX 708</td>
</tr>
<tr  align="center">
<td>sensor resolution</td>
<td >2592 * 1944 pix</td>
<td>3280 * 2464 pix</td>
<td>4608 * 2592 pix</td>
</tr>
<tr  align="center">  
<td>FPS幀率</td>
<td >30p MAX</td>
<td>90p MAX</td>
<td>120p MAX</td>
</tr>
</table>
</div>

- During subsequent testing, we found that the vehicle was unable to anticipate the position of the next block while avoiding obstacles. This posed a challenge for the vehicle's obstacle avoidance strategy. As a result, we decided to modify the original camera and convert it into a wide-angle lens. Compared to the original 72-degree field of view, the wide-angle lens provides a 160-degree field of view, allowing us to anticipate the position of the next block in advance. This improvement has enhanced the vehicle's obstacle avoidance effectiveness.

- 在之後的測試中，我們發現當車輛閃避積木時無法預先得知下一個積木的位置，這對於車輛的避障策略造成了困擾。因此，我們決定將原本的鏡頭進行改裝，將其轉換成廣角鏡頭。相較於原本的72度視野範圍，廣角鏡頭提供了160度的視野範圍，能夠讓我們提前預測下一個積木的位置，從而改善車輛的避障效果。

#### wide-angle lens(廣角鏡)

<div align="center">
<table>
<tr>
<th align="center"> Without the wide-angle lens 未加廣角鏡</th>
<th align="center">With the wide-angle lens 已加廣角鏡</th>
</tr>
<tr>
<td align="center"><img src="./img/5/V2.jpeg" width=200 alt="common" ></td><td>
<img src="./img/5/V2_wide_angle.jpeg" width=200 alt="wide angle" >
</td>
</tr>
<td align="center"><img src="./img/5/72angle.png" width=200 alt="common view" ></td>
<td align="center"> <img src="./img/5/160angle.png" width=200 alt="wide angle view" ></td>
</tr>
</table>
</div>

- In the Raspberry Pi program, it is possible to configure the resolution of the camera module. We conducted experiments with the following common resolutions.
- 在raspberry pi的程式中可以設定鏡頭模組的解析度，我們將實驗以下常見的解析度

  1. 1080x640 幀率30p
  2. 640x320 幀率60p
  3. 320x240 幀率90p

- In our experiments, we found that when the camera module's resolution was set to 1080x640, the high-resolution image processing demands led to a significant amount of time being spent on block recognition, resulting in a decrease in computational efficiency. On the other hand, when the resolution was set to 320x240, the computational efficiency was extremely high, but the low resolution hindered the proper recognition of the blocks. However, when we set the resolution to 640x320, we observed that the program could successfully recognize the blocks without compromising computational efficiency, thus avoiding collisions with the blocks. Therefore, we ultimately decided to set the camera module's resolution to 640x320.
- 在我們的實驗發現，當相機模組的解析度設定為1080x640時，由於高解析度的影像處理需求，程式需要花費大量的時間來辨識積木，這導致了程式的運算效率降低。另一方面，當解析度設定為320x240時，雖然運算效率極高，但由於解析度過低，導致無法正常辨識積木。然而，當解析度設定為640x320時，我們觀察到可以正常辨識積木，而且運算效率也不會太慢，避免了車輛撞上積木的問題。因此，我們最終選擇將相機模組的解析度設定為640x320。

## 2024/06/03 ~ 2024/06/09  

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- By using VS Code along with Git to edit our technical documentation, we can effectively manage potential conflicts and improve collaboration. The advantages of this approach include easy version control, immediate notifications to editors when conflicts arise due to simultaneous edits, and the ability for editors who upload data later to merge conflicts by comparing the data. This way, we can ensure a smoother and more efficient process when working on the technical documentation.

- 在撰寫技術文件時，我們決定使用VS Code加上git來編輯。這樣的做法有很多好處，其中包括容易進行版本控制，當不同編輯者同時編輯同一個檔案時，git會立即通知編輯者有衝突發生，這樣較晚上傳資料的編輯者就可以透過資料的比較來合併衝突。這樣的作法讓我們在編輯技術文件時能夠更有效率地合作和管理可能的衝突。

[github 主頁 : https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/tree/main](https://github.com/kirkhu/WRO2023_Future-Engineers-Fire-On-All-Cylinders/tree/main)

<div align="center">
<table>
<tr align="center">
<th> 要在VS Code編輯只要點擊原始檔控制，並按下複製儲存庫</th>
<th>輸入網址，就能在VS Code做編輯及版本控制</th>
</tr>
<tr>
<td align="center"><img src="./img/5/clone_dictionary.png" width = "300" alt="clone" align=center /></td><td>
<img src="./img/5/choose_link.png" width = "300"  alt="WEB" align=center />
</td>
</tr>
</table>
</div>

## 2024/06/10 ~ 2024/06/16

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- During the hardware design process, we encountered a few instances where the Raspberry Pi controller or IC was damaged due to incorrect power or data cable connections. To prevent such issues, we implemented a solution using male-female connectors for both power supply and data transmission. This approach ensured correct wiring and effectively mitigated the risk of the Raspberry Pi or IC getting burnt. These design improvements have enhanced the stability of the hardware system, leading to increased overall product reliability and lifespan.
- During the hardware design process, we initially used a breadboard to connect the circuits. Unfortunately, we encountered some instances of burning or poor contacts, resulting in abnormal functionality or potential issues that were challenging to detect. To improve this situation, we made the decision to switch to soldering the circuits onto a prototyping board. This change significantly reduced the risks of burning or poor contacts while ensuring stable and reliable connections. Through this improvement, we successfully enhanced the overall hardware system's reliability and ensured proper functionality.  

- 在硬體設計過程中，遇到過幾次因電源接錯或資料線插錯而導致樹莓派控制器或IC損壞的情況。為了避免這樣的問題，我們採用了使用公母插座進行電源供應及資料傳輸的解決方案。透過公母插座，確保了正確的接線，有效地避免了樹莓派或IC燒毀的風險。這樣的設計改進增加了硬體系統的穩定性，提高了整體產品的可靠性和使用壽命。
- 在硬體設計過程中，我們最初使用麵包板連接電路，但不幸遇到了一些燒毀或接觸不良的現象，這導致功能運作不正常或存在潛在問題，且很難發現。為了改善這種情況，我們決定改用銲接方式將電路固定在電木板上。這樣的改變明顯地降低了燒毀或接觸不良的風險，同時確保了穩定可靠的連接。透過這項改進，我們成功地提高了整體硬體系統的可靠性，並確保了功能的正常運作。

<div align="center">
<table>
<tr  align="center">
<th> <img src="./img/6/anit_daze.png" alt="插座" width="350"></th>
<th><img src="./img/6/anit_daze_2.jpg" alt="電木板" width="350"></th>
</tr>
</table>
</div>

## 2024/06/17 ~ 2024/06/23

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- Before dodging the blocks, we need to complete the basic task of circling the track three times. During this circling process, we noticed the possibility of the machine rubbing against the walls while turning. To address this, we utilize the 360-degree detection capability of LiDAR to keep the vehicle centered on the track. By subtracting the distances on the left and right sides, we obtain an error value, which is then corrected using the servo motor to ensure the vehicle continues to travel along the center of the track.

- 在閃避積木之前，我們需要先完成基本的環繞場地三圈。在繞圈的過程中，我們發現機器有可能在轉彎時擦撞到牆壁，因此需要利用光達的360度偵測功能來使機器維持在道路中央。透過將左右邊的距離相減，我們可以得到一個誤差值，再利用伺服馬達來修正這個誤差，使機器能夠持續行駛在道路中央。

<div align="center">
<table>
<tr  align="center">
<th> 車輛撞擊邊牆</th>
<th>偵測左右牆距離</th>
</tr>
<tr align="center">
<td><img src="./img/5/hit_wall.jpeg" width = "300"  alt="hit wall"  /></td>
<td><img src="./img/5/LIDAR_readings.png" width = "200"  alt="Distance to wall."/></td>
</tr>
</table>
</div>

## 2024/06/24 ~ 2024/06/30  

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- The robot is now able to operate successfully. The next step is to use the camera to avoid obstacles (blocks). First, we need to detect the distance to the obstacles (blocks). and then identify the color of the blocks. Utilizing the features of OpenCV, we can calculate the distance between the blocks and the robot to avoid obstacles. By implementing an algorithm, we can control the front wheels to steer around these obstacles.
- However, there is an issue at the corners where the robot cannot avoid obstacles in a timely manner. To address this, we need to combine the gyroscope's readings with the output values from the algorithm to successfully navigate around corners

- 機器人現在已經能夠成功運作。接下來的步驟是使用攝影機來避開障礙物（積木）。首先，我們需要偵測與障礙物（積木）的距離，然後識別積木的顏色。透過利用OpenCV的功能，我們可以計算出積木與機器人之間的距離，以避開障礙物。透過實現一個演算法，我們可以控制前輪來繞過這些障礙物。  
- 然而，在轉彎處有一個問題，機器人無法及時避開障礙物。為了解決這個問題，我們需要將原本方向的數值與演算法的輸出值結合起來，以成功地在轉彎處繞過障礙物。  

<div align="center">
<table>
<tr align="center">
<th> 偵測積木距離</th>
<th> 撞擊積木</th>
</tr>
<tr align="center">
<td><img src="./img/6/sign.png" width=250 alt="block distance" ></td>
<td><img src="./img/5/hit_block.jpg" width=300 alt="hit block" >
</td>
</table>
</div>

## 2024/07/01 ~ 2024/07/07

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- During today's testing, we discovered that the robot tends to misinterpret people wearing red or green clothing in its surroundings as obstacles, causing it to unnecessarily avoid them and potentially miss avoiding the next block in time. To address this issue, we added an additional layer of black masking at the top of the camera's field of view, preventing the robot from detecting colors outside of the track area.After adding the black masking, the robot will no longer detect colors outside of the track area, reducing the chances of interference.

- 今天在測試時發現當機器在周圍人穿紅色衣物或綠色衣物時會誤測成積木讓機器閃避，導致無法及時閃過下一個積木，因此我們在畫面的上方將上一層黑色遮罩，讓機器無法偵測場地以外的顏色。在加上黑色遮罩之後，就不會再偵測到場外的顏色，減少被干擾的機率。

<div align="center">
<table>
<tr align="center">
<th>使用黑色遮罩屏蔽場外的顏色</th>
</tr>
<tr align="center">
<td><img src="./img/6/black_hid.png" width="300" alt="cover"></td>
</table>
</div>

## 2024/07/08 ~ 2024/07/14

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- This week, as most of the programming has been completed, we began testing the success rate of the robot. We started with 50% speed, and due to the slower pace, the robot mostly responded well. However, when accelerating to 70%, the color sensor occasionally misjudged the color of the track due to the high speed. As a result, we modified the turning conditions to utilize the LiDAR's measurements of left and right directions to determine the turning direction. This adjustment reduces the likelihood of turning in the wrong direction due to color misjudgment

- 這周我們已經完成了大部分的程式編寫，於是我們開始進行機器的成功率測試。一開始我們選擇了50%的速度，由於速度相對較慢，機器大多能夠順利做出反應。然而，當我們提高到70%的速度時，我們發現顏色感測器有時會因為速度過快而誤判地上線的顏色。因此，我們進行了調整，改用光達測量左右方向的方式來辨識轉彎方向，這樣可以減少因為顏色誤判而轉錯方向的情況。

#### 偵測轉彎方向

```
if get_left_dis > 100:
    reverse = False
else:
    reverse = True
if get_mid_dis > 55:
    servo.angle(-40)
```

## 2023/07/15 ~ 2023/07/21

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- The robot is now capable of successfully avoiding obstacles and completing the third lap around the track. The next task is to detect blocks and perform a turnaround maneuver. The turnaround will only be executed if the last block of the second lap is red. Therefore, it is necessary to detect the lap count. We will utilize the color sensor to count the number of times the line is crossed and determine whether the set count has been reached.

- If the specified count has not yet been achieved, the system will continue to record the color of the nearest traffic sign until the count of line crossings is greater than or equal to the set value. At this point, color recording will cease.

- Once the color of the nearest traffic sign has been recorded, the program will determine whether the color is red. If the color is red, the system will set the angle of the servo motor to initiate a right turn and continue turning until the vehicle is oriented in the specified direction. If the detected color is not red, the vehicle will continue moving forward. However, if the color of the traffic sign is red, a turnaround maneuver will be executed.

- 已經可以完成閃避積木及繞場第三圈，接下來就是偵測積木並迴轉，迴轉是在第二圈的最後一個積木是紅色的才要進行的動作，因此要先偵測圈數，要利用顏色感測器來偵測經過的線條次數，並判斷是否超過了設定的次數。
- 如果未達到指定次數，系統將會持續紀錄距離最近的交通標誌顏色，直到經過的線條次數大於或等於設定次數，此時將不再紀錄顏色。
- 紀錄完最近的交通標誌顏色後，程式將判斷最近的交通標誌顏色是否為紅色。若標誌顏色為紅色，系統將設定伺服馬達角度為右轉角度，持續轉動直到車輛轉向指定的方向。若最近的交通標誌顏色不是紅色，則車輛會繼續向前行駛。

<div align="center">
<table>
<tr align="center">
<th>顯示線條次數與最近的交通標誌顏色</th>
<th>正在調整數值</th>
</tr>
<tr align="center">
<td><img src="./img/7/detect_last_obstacle.png" width="200" alt="print color"></td>
<td><img src="./img/7/check.jpeg" width="300" alt="check"></td>
</table>
</div>

## 2024/07/22 ~ 2024/07/28  

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- As the field mission has been roughly completed, we are now starting to write the technical report. Since we are not familiar with the correct technical report format, we referred to the official website's technical report documentation, and found that the report should include the following sections:

  1. module: This folder should contain documentation related to the vehicle models, such as files for laser cutting machines and 3D printers.

  2. other: This folder is used to store data that does not belong to other categories, such as communication protocols and engineering logs.

  3. schemes: This folder is dedicated to hardware introductions, explaining the functions of electronic components and how they are connected.

  4. src: All programs should be placed in this folder.

  5. t-photos: This folder should contain team photos, including a group photo and humorous pictures.

  6. v-photos: Machine photos from six different perspectives should be placed in this folder.

  7. video: Videos demonstrating the machine's operation should be placed in this folder, with each video lasting more than 30 seconds.

- When writing the technical report, we are switching between VS Code and the GitHub website. We use a desktop computer to view the GitHub web page and a laptop to edit the report in VS Code.

- 由於場地任務已經大致完成，因此要開始撰寫技術報告，由於我們還不清楚正確的技術報告標準，因此參考官網的技術報告文件，發現需要以下部分

  1. module 此資料夾內需放入車輛模型的文件，如雷射切割機、3D列印機的檔案
  
  2. other 此資料夾用於放置不屬於其他分類的資料，如通訊協定、工程日誌等
  
  3. schemes 此資料夾用於硬體介紹，說明電子元件的作用與如何連接
  
  4. src 此資料夾需要放入所有程式
  
  5. t-photos 此資料夾需要放入團隊的合照，包括一張合照和搞笑照片
  
  6. v-photos 此資料夾需要放入機器的照片，包括六個不同方位的視圖
  
  7. video 此資料夾應該放入機器運作影片，要超過30秒

- 再撰寫技術文件時，由於需要再VS Code和Github網站之間切換，因此我們改用一台桌機檢視Github網頁，一台筆電用VS Code編輯

<div align="center">
<table>
<tr align="center">
<th>官方網站的github範例</th>
<th>筆電和桌機對照修改</th>
</tr>
<tr align="center">
<td><img src="./img/7/github_example.png" width="300" alt="github_example"></td>
<td><img src="./img/7/vs_code.jpeg" width="300" alt="更改文件"></td>
</table>
</div>

## 2024/07/29 ~ 2024/08/04

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

- We made significant progress in our project. We successfully organized and listed the components in the parts inventory, and we uploaded it to the technical documentation. Additionally, we completed the drawing of the vehicle's introduction diagram. Throughout this process, we embarked on a learning journey, gradually familiarizing ourselves with GitHub syntax. Although we are not yet fully proficient in using GitHub, we dedicated time to researching relevant information online and steadily improving our skills. These achievements have brought valuable advancements to our report and project as a whole.
- Over these few days, we have been continuously adjusting and fine-tuning the execution of venue tasks, making constant adjustments to motor speed and various parameters in the hopes of effectively reducing the error rate. We are eager to achieve better performance and improve our overall competition results.
- During practical testing, we discovered that the vehicle was getting stuck at the junctions of the terrain due to protrusions, which was affecting its normal operation. To address this issue, we adopted a method of using a laser cutting machine to create 3mm thick spacers. These spacers were then placed under the vehicle chassis to elevate its height, enabling the vehicle to pass over the obstacles smoothly.

- 我們完成了將零件清單整理並列點，並上傳至技術文件中。此外，我們也完成了車體的介紹圖的繪製工作。在這個過程中，我們逐步學習了GitHub語法的使用並逐漸熟悉它。儘管對GitHub的使用不是很熟練，但我們努力在網上查詢相關資訊，並逐步提高了技能水平。這些進展為我們的報告帶來了寶貴的進步。
- 這幾天我們持續調整及修正場地任務執行，不斷地進行馬達速度和各項參數的微調，期望能有效降低失誤率，期待能夠取得更好的表現並提高整體競賽成績。
- 在進行實際測試時，我們發現車輛在場地圖交界處因凸起而出現卡車的情況，這影響了車輛的正常運行。為了解決這個問題，我們採取了一個方法，使用雷切機切割出3mm厚的墊片，並將其放置在車身底部，從而將車身撐高，以便車輛能夠順利通行。

#### Overcoming Terrain Protrusions (克服場地凸起)

<div align="center">
<table>
<tr align="center">
<th> <img src="./img/7/Spacer1.png" alt="Spacer" width=300 /></th>
<th><img src="./img/7/Spacer2.jpg" alt="Spacer" width=300 /></th>
<th><img src="./img/7/Spacer3.jpg" alt="Spacer"  width=300/></th>
</tr>
<tr align="center">
<td><img src="./img/7/Spacer4.jpg" alt="Spacer" width=300 /></td>
<td><img src="./img/7/Spacer5.jpg" alt="Spacer" width=300 /></td>
<td><img src="./img/7/Spacer6.jpg" alt="Spacer"  width=300/></td>
</table>
</div>

### Team Members' Practice Status(隊員練習狀況)

<div align="center">
<table>
<tr  align="center">
<th> <img src="./img/7/work_photo_2_1_0729.jpg" alt="work_photo_2_1_0729" width=300 /></th>
<th><img src="./img/7/work_photo_2_2_0729.jpg" alt="work_photo_2_2_0729" width=300 /></th>
</tr>
<tr align="center">
<td><img src="./img/7/work_photo_1_1_0727.jpg" alt="work_photo_1_1_0727"  width=300/></td>
<td><img src="./img/7/work_photo_2_1_0727.jpg" alt="work_photo_2__0727" width=300 /></td>
</tr>
</table>
</div>

## 2024/08/05 ~ 2024/08/11

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**  

- As the deadline for submitting the technical report is next week, we have begun revising the content of the technical documentation. We are also adjusting the website according to the official grading criteria and continuously adding to the technical report.
- Complete recording videos for each task and upload them to YouTube.

- 由於下星期就要交出技術文件，因此我們開始修改技術到告的內容，並依官方評分標準調整網頁，持續補充技術報告。
- 完成各任務錄影，並上傳YOUTUBE

<table>
<tr align="center">
<th> 舊目錄 </th>
<th> 修改過的目錄上 </th>
<th> 修改過的目錄下 </th>
</tr>
<tr align="center">
<td><img src="./img/8/old_content.png" alt="old_content"  width="300"/> </td>
<td> <img src="./img/8/new1_content.png" alt="new1_content"  width="300"/></td>
<td> <img src="./img/8/new2_content.png" alt="new1_content"  width="300"/></td>
</tr>
</table>

  **Open Challenge 資格賽影片**

- [Open Challenge 全窄 速度70%](https://youtu.be/QtpuHt05MDg)
- [Open Challenge 全窄 速度50%](https://youtu.be/QaYUrrdAtE8)
- [Open Challenge 半寬半窄 速度70%](https://youtu.be/pcTpH8QgJFU)
- [Open Challenge 半寬半窄 速度50%](https://youtu.be/7HdWxfWPfWc)
- [Open Challenge 全寬 速度70%](https://youtu.be/MA1k2P87LdE)
- [Open Challenge 全寬 速度50%](https://youtu.be/OUg0x4Qdc0c)  

 **Open Challenge 任務賽影片**

- [Obstacle Challenge 速度50%](https://youtu.be/Jo7555gfXG8)
- [Obstacle Challenge 速度70%](https://youtu.be/iCmcXbACizY)

**Team Members' Practice Status(隊員練習狀況)**

<div align="center">
<table>
<tr align="center">
<th>Report writing 報告撰寫</th>
<th>Mechanism adjustment 機構調整</th>
<th>Report writing 報告撰寫</th>
<th>Field mission practice場地任務練習</th>
</tr>
<tr align="center">
<td><img src="./img/8/work_photo_1_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_2_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_3_0805.jpg" width="500" alt="work_daily"></td>
<td><img src="./img/8/work_photo_4_0805.jpg" width="500" alt="work_daily"></td>
</table>
</div>

## 2024/08/12 ~ 2024/08/18

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

This week, as our machine has been adjusted to run the mission race smoothly on the field, we have started shooting an introductory video for the mission race. In the video, we will showcase the actions our vehicle performs during the mission race, and we will provide explanations through subtitles synchronized with the video.

這星期由於我們的機器已經將數值調整到可以正常在場地上運行任務賽，因此我們開始拍攝任務賽的影片。

<div align="center">
<table>
<tr align="center">
<th>Modify the program and test the vehicle 修改程式及測試車輛</th>
<tr align="center">
<td><img src="./img/8/work_photo_1_0813.jpg" width="100%" ></td>
</table>
</div>

**任務賽影片**

<td>

[![Open Challenge 任務賽影片(迴轉)](../../video/Obstacle_Challenge/img/任務賽.png)](https://youtu.be/n0Pp--26QGQ)</td>

## 2024/08/19 ~ 2024/08/25

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

As the competition is scheduled for this week, we have intensified our practice efforts, trying out various scenarios and adjusting our program to adapt to a wide range of situations. Experimenting with different scenarios has the advantage of helping us anticipate challenges that our machine might face and making necessary adjustments in advance. Here's our practice approach:

- We have assigned lane labels A, B, C, and D. Each lane is divided into three sections, with placement points for blocks both on the inner and outer sides in each section. Red blocks indicating turning conditions will be placed sequentially, while the positions of other blocks will be randomized.
- The record sheet will include the following information:
  1. Completion time
  2. Number of successful attempts/number of failed attempts
We believe that this approach will assist our machine in preparing for a variety of scenarios, ensuring that we are well-prepared for the competition.

由於比賽即將在本週舉行，我們已經開始加強練習，嘗試不同的題目並調整程式，以適應大多數的情況。嘗試不同的題目有一個好處，就是可以幫助我們找出機器可能遇到的挑戰，並提前進行必要的調整。以下是我們的練習方式：

- 我們將走道編號為A、B、C、D。每個走道分為三個區域，每個區域都有內外兩個放置方塊的點。指示轉彎條件的紅色方塊會按順序放置，其他方塊則會隨機調整。
- 紀錄表將包括以下信息：
  1. 完成時間
  2. 成功嘗試次數/失敗次數  

我們相信，這種做法將幫助我們的機器準備應對各種不同的情況，確保我們在比賽中做好充分的準備。

<div align="center">
<table>
<tr align="center">
<th>Field Setup 場地配置</th>
<th>Record Sheet 紀錄表</th>
</tr>
<tr align="center">
<td><img src="./img/8/block.png" width="400" alt="work_daily"></td>
<td><img src="./img/8/grade.png" width="500" alt="work_daily"></td>
</table>
</div>  

- Today is 8/25,our match day. In the first half of the qualifying round, due to our Request for Maintenance during the initial round, the score was reduced by 50%, resulting in our obtaining 15 points. In the second round, we successfully completed it and achieved a full score of 30 points, allowing us to advance to the second half of the obstacle course. During the first obstacle race, our robot hit the wall and stopped due to excessive avoidance; fortunately, after adjustments, the second attempt by our team resulted in a perfect score. This marked a successful conclusion to today's competition.

今日為8/25，我們的比賽日，在上半場的資格賽中，第一場順利跑滿圈數獲得了滿分，但第二場我們則因為機器上的雷達讀取有問題所以申請維修，但當機器雷達恢復正常時我們的時間只剩下一分鐘，導致我們只有跑完2圈，但最後我們還是有成功晉級下半場障礙賽。在第一場障礙賽時，因為躲避幅度過大而撞牆停止比賽，但幸好在調整過後，第二場順利獲得滿分，為今日比賽做了完美的結尾。

<div align="center">
<table>
<tr align="center">
<th>Waiting for test 等待測試</th>
<th>Competition photo 比賽照片</th>
<th>Award-winning photo 上台領獎</th>
</tr>
<tr align="center">
<td><img src="./img/8/0825_0.jpg" width="300" alt="work_daily"></td>
<td><img src="./img/8/0825_1.jpg" width="300" alt="work_daily"></td>
<td><img src="./img/8/0825_2.jpg" width="300" alt="work_daily"></td>
</tr>
</table>
</div>

## 2024/08/26 ~ 2024/09/01

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

Since we have confirmed our participation in the international competition, we are attempting to modify the machine. We have started testing the Raspberry Pi 5 and Jetson Nano, aiming to choose one of these controllers for replacement.

- The Raspberry Pi 5 has a processor speed that is 2 to 3 times faster than the Raspberry Pi 4, with GPU performance that is twice as powerful as the previous generation. Its memory and I/O bandwidth are also doubled, and it consumes less power for the same tasks.
- The Jetson Nano, compared to our original controller, the Raspberry Pi 4, offers significantly better performance and has a more powerful GPU (graphics processing unit) than the Raspberry Pi 4, which enhances camera recognition capabilities.

由於我們已經確定要參加國際賽，所以我們嘗試將機器進行改造，我們分別開始測試 Raspberry pi 5 和 Jetson nano ，想要從這兩種中選一種控制器更換。

- Raspberry pi 5 處理器速度是 Raspberry pi 4 的2~3倍，GPU效能為上一代的兩倍，記憶體與I/O頻寬也是上一代的兩倍，且在同樣的任務上有較少的功耗。
- Jetson nano 相較於我們的原控制器 Raspberry pi 4 的性能高上許多，而且擁有比 Raspberry pi 4 處理功能更強大的GPU（圖形處理器），鏡頭辨識較強。

<div align="center">
<table>
<tr align="center">
<th>Raspberry pi 4</th>
<th>Raspberry pi 5</th>
<th>Jetson nano</th>
</tr>
<tr align="center">
<td><img src="./img/8/pi_4.png" width="300" alt="work_daily"></td>
<td><img src="./img/8/pi_5.png" width="300" alt="work_daily"></td>
<td><img src="./img/8/jetson_nano.png" width="300" alt="work_daily"></td>
</table>
</div>

#### Raspberry pi 5

We set up a machine with a controller of Raspberry pi 5 and started to install and test the functions of Raspberry pi 5.

- When we tried to insert the SD card from our Raspberry Pi 4 into the Raspberry Pi 5, we found that the boot operation could not be performed. Therefore, we formatted the SD card that was originally a backup for the Raspberry Pi 4 to use it for the Raspberry Pi 5 image file. After burning the Raspberry Pi 5 image file, the boot was successful.
- We began setting up the environment. We chose to start the installation using VNC, which allows us to control the Raspberry Pi 5 from the computer for subsequent actions. Then we installed two pieces of software: OpenCV and ROS. OpenCV is the software used to operate the camera, while ROS is the software needed to run the radar.

我們組了一臺跟 Raspberry Pi 4 一樣的機器，將控制器更改為 Raspberry pi 5 的機器，著手安裝測試 Raspberry pi 5 的功能。

- 在我們嘗試將我們在 Raspberry pi 4 上的SD卡插入 Raspberry pi 5 上時，發現無法進行開機動作，因此我們將原本備用 Raspberry pi 4 的SD卡格式化，要拿來灌入 Raspberry pi 5 的映像檔，燒入 Raspberry pi 5 的映像檔後才成功開機。
- 我們開始進行環境架設工作，我們選擇從 VNC 開始安裝，這樣可以讓我們從電腦操縱 Raspberry pi 5 進行後續動作，接著我們安裝 OpenCV 和 ROS 這兩個軟體， OpenCV 是要執行鏡頭用的軟體，而 ROS 是執行雷達需要用到軟體。

<div align="center">
<table>
<tr align="center">
<th>SD卡設置</th>
<th>VNC 遠端連線安裝</th>
<th>OpenCV 安裝</th>
<th>ROS 安裝</th>
</tr>
<tr align="center">
<td><img src="./img/8/SDcard_set.jpg" width="300" alt="SDcard"></td>
<td><img src="./img/8/VNC.png" width="300" alt="VNC"></td>
<td><img src="./img/8/open_cv.jpg" width="300" alt="opencv"></td>
<td><img src="./img/8/ROS.jpg" width="300" alt="ROS"></td>
</table>
</div>

#### Jetson nano

我們額外組裝了一台機器給 Jetson nano 使用，開始研究 Jetson nano 。
- 由於我們在之前就有研究過 Jetson nano ，所以我們現在在測試使用鏡頭進行二值化偵測邊牆與地上的線，方便我們做轉彎判斷。

##### 鏡頭視角
<div align="center">
<table>
<tr align="center">
<th>偵測牆壁</th>
<th>偵測地面線(逆時針方向)</th>
<th>偵測地面線(順時針方向)</th>
</tr>

<tr align="center">
<td><img src="./img/8/wall.png" width="300" alt="wall"></td>
<td><img src="./img/8/line_left.png" width="300" alt="left"></td>
<td><img src="./img/8/line_right.png" width="300" alt="right"></td>
</table>
</div>

- 我們判斷牆壁的部分是透過鏡頭正上方區塊偵測是否看到邊牆，進而做後續動作。
- 鏡頭中左右兩個區塊會透過判斷地板上的線是左邊先偵測到還是右邊先偵測到，若是左邊先測到那就左轉；若是右邊先測到那就右轉。

#### Raspberry pi 4

我們開始修改我們在全國賽中發生的問題，當作未來的備用品。
- 我們在資格賽第一場有發生迴轉失敗的問題，我們我們嘗試調整迴轉的速度與角度，讓我們可以順利迴轉。
- 我們在兩場資格賽中停車動作都無法照常進行，因此我們在資格賽中選擇不進行停車，現在我們要嘗試使用其他方法進行停車。

## 2024/09/02 ~ 2024/09/08

**Member:** HU,SIAN-YI、LAI,MENG-CHENG、HUANG,KE-FU  
**Content:**

#### Raspberry pi 5

我們繼續嘗試將 Raspberry pi 4 上有安裝的功能安裝到 Raspberry pi 5 上，卻發現有些功能並沒有辦法安裝，像是執行雷達需要的ROS、讀取腳位要用的GPIO，都無法安裝使用，只有 VNC 系統和鏡頭的 OpenCV 安裝成功，我們在網路上查詢有發現是版本不相容、不適用等問題，導致無法安裝，以致我們無法執行我們的主程式，因此我們決定暫緩 Raspberry pi 5 的研究，先將 Raspberry pi 4 調整到最佳狀態。

<div align="center">
<table>
<tr align="center">
<th>查詢資料</th>
</tr>

<tr align="center">
<td><img src="./img/9/查找資料.jpg" width="300" alt="wall"></td>
</table>
</div>

#### Jetson nano

We performed basic line tracking using a camera and a gyroscope. The camera was used for binarization to determine the area of the line on the ground for judgment, while the gyroscope was used to read the angle and direction. Since we used binarization, we needed to use black and white checkered paper to calibrate the camera. After taking about 20 photos of the paper from different angles through the program, the camera was ready for use, allowing us to perform the preliminary qualifying run using the camera and gyroscope.

我們有透過鏡頭與陀螺儀進行基礎的循跡，透過鏡頭進行二值化判斷地面上線的面積，進而進行判斷，並搭配陀螺儀讀去角度方向，而我們因為使用二值化所以需要使用黑色與白色格子的紙張校正鏡頭，大約透過程式使用鏡頭對紙張進行不同角度的拍攝20張左右的照片後，鏡頭就可以進行使用，透過鏡頭和陀螺儀進行初步資格賽的運行。

<div align="center">
<table>
<tr align="center">
<th>檢測降壓板</th>
<th>檢測電路板</th>
<th>焊接電路板</th>
</tr>

<tr align="center">
<td><img src="./img/9/查降壓板.jpg" width="300" alt="wall"></td>
<td><img src="./img/9/查電路.jpg" width="300" alt="left"></td>
<td><img src="./img/9/焊接.jpg" width="300" alt="left"></td>
</table>
</div>

## 2024/09/09 ~ 2024/09/15

#### Raspberry pi 4

We are not sure what went wrong with our Raspberry Pi 4 that caused it to burn out. We started by checking the power supply line from the Lipo battery, using a multimeter to measure continuity. Then, we checked the buck converter and used the multimeter to measure the output voltage and current, ensuring the voltage was 5 volts and the current was 3 amps. After testing the buck converter and confirming it had no issues, we turned to check the circuit on the circuit board to see if there was any reversed polarity. A few days ago, we had replaced the connection line between the circuit board and Raspberry Pi, so we weren't sure if the connection line was faulty and caused a short circuit. However, after the final inspection, we found no issues. In the end, we decided to solder a new circuit board, as we believed the likelihood of the problem was with the circuit board, leading us to make this decision.

我們 Raspberry pi 4 不確定出了什麼問題導致 Raspberry pi 4 燒毀了，我們從 Lipo 電池供電線開始檢查，使用三用電表測量有沒有導通，接著我們再檢查降壓板，使用三用電表測量降壓板輸出端的電壓和電流，電壓是否為5伏特和電流是否為3安培，在測試過降壓板確定沒問題後，我們轉而測試電路板的線路，看電路板有沒有地方正負接反，因為我們在幾天前有更換電路板與樹梅派的連接線，所以我們不確定是不是連接線有問題而短路，然而經過最後的檢查也是沒有發現問題，最後我們打算重新焊接一塊新的電路板，因為我們認為電路板出問題的機率較大，才做出此項決定。

<div align="center">
<table>
<tr align="center">
<th>檢測降壓板</th>
<th>檢測電路板</th>
<th>焊接電路板</th>
</tr>

<tr align="center">
<td><img src="./img/9/查降壓板.jpg" width="300" alt="wall"></td>
<td><img src="./img/9/查電路.jpg" width="300" alt="left"></td>
<td><img src="./img/9/焊接.jpg" width="300" alt="left"></td>
</table>
</div>

#### Jetson nano


我們機器出了點問題，執行程式起來都怪怪的，而我們在查找電路板的電路板的時候，發現 pico 板有些腳位異常，導致我們無法正常執行我們的程式，而且我們打算重新規劃電路圖，我們要將

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>
