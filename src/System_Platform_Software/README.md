<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Software Platform Construction (軟體平台建置)</div> 
- ### Installing System Software Required for Self-Driving Cars 安裝自駕車所需的系統軟體  
  - #### System Platform Software Installation Process Diagram(系統軟體平台安裝程序圖)
   ![images](./img/software_setup.png) 
   - When installing PI OS, select "Raspberry Pi OS (Legacy)" for installation.
      - Software link：[Raspberry Pi](https://www.raspberrypi.com/news/new-old-functionality-with-raspberry-pi-os-legacy/) 
      - After installation, please update the operating system to ensure software compatibility.
   - Using the Mobaxterm tool (__tool introduction at the bottom of this page__), you can connect to a Raspberry Pi via VNC or SSH to perform system configuration, updates, and install software such as ROS, OpenCV, and more.

      ```
      $ sudo apt-get update  
      $ sudo apt-get upgrade   
      ``` 
    - After selecting "Interface Options," enable the Camera, SSH, VNC, and other desired features, then exit the menu.
    - Before installing OpenCV version 4.7.0.72, you should first check whether the versions of setuptools and wheel support the installation of this specific version of OpenCV.
    - Install ROS system version "noetic ninjemys", first set up the database, then create a workspace, proceed to install the required dependencies, and finally build the catkin workspace.
    - Install the PIGPIO Library to facilitate the control of the color sensor and read the field color values
    - To install the Dlidar LiDAR driver, first obtain the Lidar installation package. Then, set the USB interface permissions, install the required dependencies, compile the driver, and finally, add it to the environment variables.


    - 安裝PI OS時，選擇安裝Raspberry Pi OS (Legacy)  
      - 軟體連結：[樹梅派](https://www.raspberrypi.com/news/new-old-functionality-with-raspberry-pi-os-legacy/) 
      - 安裝完之後，請更新作業系統，以確保的軟體的相容性
    - 使用Mobaxterm工具(__工具介紹在本頁最下方__)的VNC或SSH，可連線至Raspberry Pi，進行系統設定、更新及ROS、OpenCV等軟體安裝。      
 <div align="center">
 <table>
 <tr align="center" > 
 <td><img src="./img/Mobaxterm_PI.png" width="400" alt="detect_color"> </td>
 <td><img src="./img/Mobaxterm_ssh.png" width="400" alt="detect_color"> </td>
 </tr>
 <tr align="center"></tr>
 </table>
 </div>

  - ####  中文
    -  選擇Interface Options之後打開Camera、SSH和VNC等功能後退出  
    - 安裝opencv版本:4.7.0.72，在裝之前要先確認 setuptools 和 wheel 的版本支援安裝的opencv  
    - 安裝ROS系統版本:noetic ninjemys，先設定資料庫，再來建立工作環境，之後安裝依賴項目，最後在建置catkin的工作環境  
    - 安裝PIGPIO Library，以利控制顔色感測器，讀取場地顏色值
    - 安裝Dlidar光達的驅動程式，首先先取得Lidar安裝包，再來設定USB接口權限，之後安裝依賴項目，然後編譯，最後加入環境變數

- ### Record Field Environment Values紀錄場地環境值
  - 在練習時，我們會事先紀錄場地中的藍、橘線、白色場地及積木顏色的數值到save_file資料夾中，方便正式賽使用，可提高正式賽的辨識準確率及節省正式賽準備時間。
  - In practice, we pre-record the color values of the blue, orange lines, white areas, and block colors in the field into the 'color_sensor.p' file. This is done to facilitate the use of these values during the actual competition, enhancing recognition accuracy and saving preparation time for the official race.
  - #### Field Environment Value Recording Configuration Workflow(場地環境值記綠設定運作流程圖)
    ![images](./img/setup_recode_obstacle.png)  
  - #### [line_color_write.py](../Programming/Open_Challenge/line_color_write.py)紀錄場地顏色數值

    - "The 'line_color_write.py" program is primarily designed to read the color values of white, orange, and blue colors in the competition field and record these values into the 'color_sensor.p' file within the 'save_file' data.
    - When the program is running, use the button on the vehicle to aim the color sensor at the blue, orange lines, and white areas on the field, moving back and forth. Press the button to record the lowest value in that area and save it in the 'color_sensor.p' file.
    - The 'color_sensor.p' file records the values of various colors in the competition field, and through program calculations, these values can be utilized in the official competition, making it convenient for retrieval and saving preparation time.

    - "line_color_write.py"程式主要提供讀取場地中白、橘、藍顏色的數值，並將數值紀錄到save_file資料中的color_sensor.p檔案裡。
    - 當程式執行時，利用車輛上的按鈕，再將顏色感測器對準場地中的藍、橘線及白色區域並來回移動，按下按鈕，記錄該區域的最低數值並記錄到color_sensor.p檔案中。
    - color_sensor.p檔案中的紀錄著競賽場地中各顏色數值，經過程式運算可以運用在正式賽中，方便讀取，節省準備時間。  


      |The Color Values of the Field in the 'color_sensor.p' File(color_sensor.p檔案中的場地顏色數值)|
      |:---:|
      |<img src="./img/detect_color.png" width="200" alt="detect_color">|

   - #### [HSV_Detect.py](../Programming/Obstacle_Challenge/HSV_Detect.py)紀錄積木閥值  
      - The "HSV_Detect.py" program primarily reads the color values of the blocks on the field and records these values in the "HSV_Green.p" and "HSV_Red.p" files within the "save_file" data directory.  
      - The "HSV_Green.p" and "HSV_Red.p" files contain the recorded color values of the blocks on the competition field. These values can be used during the official competition, making it easier to read and saving preparation time.  
      - When the HSV_Detect.py program is executed, the camera will be aligned with the block, and the following functions will be displayed on the computer screen, corresponding to the keyboard number keys 1~5:
        - Number 1: Display the last recorded green threshold value.
        - Number 2: Display the last recorded red threshold value.
        - Number 3: Reset the currently adjusted threshold values to default.
        - Number 4: Record the adjusted green threshold value to the HSV_Green.p file.
        - Number 5: Record the adjusted red threshold value to the HSV_Red.p file.
      - When adjusting the threshold values for recognizing the blocks, we place a block both at a distance and up close to ensure that the adjusted thresholds can identify blocks at any distance. After the adjustments, press either the number 4 or 5 to save the threshold values to the HSV_Green.p or HSV_Red.p files.
      - After completing the adjustment and recording, you can press the number 1 or 2 to display the previously recorded threshold values for further adjustments.

    - "HSV_Detect.py"程式主要提供讀取場地積木顏色的數值，並將數值紀錄到save_file資料中的HSV_Green.p、HSV_Red.p檔案裡。 
    - HSV_Green.p、HSV_Red.p檔案中的紀錄著競賽場地中積木的顏色數值，經過程式運算可以運用在正式賽中，方便讀取，節省準備時間。
    - 當 HSV_Detect.py 程式執行時，會將鏡頭對準積木，並將會在電腦螢幕顯示以下功能且對應於鍵盤數字鍵 1~5：  
        數字 1：顯示上次紀錄的綠色閥值。  
        數字 2：顯示上次紀錄的紅色閥值。  
        數字 3：將正在調整的閥值恢復為預設值。  
        數字 4：將調整完的綠色閥值記錄到 HSV_Green.p 檔案中。  
        數字 5：將調整完的紅色閥值記錄到 HSV_Red.p。 
    - 在調整積木閾值時，我們會在距離遠和近都放一顆積木，以確保調整的閾值可以辨識任何距離的積木。調整完後，按下數字鍵4或5，將閾值紀錄到HSV_Green.p或HSV_Red.p檔案裡。
    - 在調整記錄完成後，您可以按下數字鍵1、2來顯示上次記錄的閾值，以便進行再次調整。  
     
      |Adjust the Green Color Threshold Value<br>(調整綠色閾值)|Adjust the Red Color Threshold Value<br>(調整紅色閾值)|Display Button Functionality<br>(顯示按鈕功能)|
      |:---:|:---:|:---:|
      |<div align="center"> <img src="./img/Adjust_the_green_color_threshold.png" width="250" alt="Adjust_the_green_color_threshold"></div>|<div align="center"> <img src="./img/Adjust_the_red_color_threshold.png" width="250" alt="Adjust_the_red_color_threshold"></div>|<div align="center"> <img src="./img/Display_Button_Functionality.png" width="250" alt="Display_Button_Functionality"><div>|

- ### Competition Programming Language Introduction - Python(程式語言介紹 - Python)

   - Python is a high-level, general-purpose, interpreted programming language created by Guido van Rossum in 1991. It is designed to be concise, readable, and comes with a rich standard library, allowing developers to write code quickly and efficiently.
  standard library, enabling developers to write code quickly and efficiently. 
   - Python is widely used in web development, scientific computing, data analysis, artificial intelligence, machine learning, and various other fields. It features dynamic typing, automatic garbage collection, and supports multiple platforms.
   - With an active community, Python has a plethora of third-party libraries and tools, making development even more convenient. Python has become a popular choice for both beginners and experienced developers.  

  __Therefore, we choose Python as the programming language for the development of the self-driving vehicle.__

   - Python是一種高階、通用、直譯式程式語言，由Guido van Rossum於1991年創建。它設計簡潔、易讀且具有豐富的標準函式庫，使開發者能夠快速有效地撰寫程式碼。
   - Python被廣泛應用於Web開發、科學計算、數據分析、人工智慧、機器學習等領域。它具有動態類型、自動垃圾回收等特性，並支援多種平台。
   - Python社群活躍，有大量的第三方庫和工具，使得開發更加便捷，Python成為初學者和專業開發者的熱門選擇。

   __因此，我們選用python 作為自駕車輛的程式開發語言。__ 

- ### Competition Programming Editor Introduction - Mobaxterm ( Mobaxterm 的介紹)

  - MobaXterm is a feature-rich cross-platform remote computing management tool. 
  - It integrates various network tools such as X11 server, remote computing, SSH, VNC, and more, providing an intuitive user interface for easy connection to remote servers in Windows environments.
  - MobaXterm also supports simultaneous management of multiple sessions, allowing users to switch and operate different remote connections effortlessly. This tool is highly valuable for system administrators, network engineers, and developers.

  __Therefore, we chose Mobaxterm as the remote control programming tool for the Raspberry Pi in our self-driving vehicle.__


  - MobaXterm是一款功能豐富的跨平台遠端計算機管理工具。
  - 它整合了X11伺服器、遠端運算、SSH、VNC等多種網路工具，並提供一個直觀的用戶界面，方便用戶在Windows環境下連接到遠端伺服器。
  - MobaXterm還支援多個會話的同時管理，讓用戶輕鬆切換和操作不同的遠端連接。這款工具對於系統管理員、網路工程師和開發人員來說是一個極具價值的工具。

   __因此，我們選用Mobaxterm作為自駕車輛中Raspberry Pi的遠端控制編寫工具。__  

  - Software  Website：[Mobaxterm](https://mobaxterm.mobatek.net/) 
  

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
