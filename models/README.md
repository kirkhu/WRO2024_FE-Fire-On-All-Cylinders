<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">NoMachine</div> 

- NoMachine 是一款跨平台的遠端桌面存取軟體，讓使用者無論身處何地都可以從一個裝置連接到另一台電腦。它的設計目的是提供快速、流暢且高效的遠端桌面體驗，並支持多種作業系統，包括 Windows、macOS、Linux 和 Android。

- NoMachine 使用 NX 技術來實現高效的遠端連線，能夠減少延遲，即使在低速網路下也能保持良好的畫質。此外，它提供多平台支援，使使用者可以從電腦、平板或手機等設備連接到其他裝置。用戶還可以在本地與遠端設備之間傳輸檔案，分享印表機和硬碟等資源，並通過加密連線和多重身份驗證確保連線安全。

- 適合遠端工作、IT 支援和遠端教育，NoMachine 支持資源共享和低延遲的音訊與視訊流媒體播放。NoMachine 提供免費的個人版以及適合企業的商業版本，後者具備更多進階功能和技術支援。其高效性和廣泛的兼容性，使其成為遠端桌面存取的熱門選擇。

- NoMachine is a cross-platform remote desktop access software that allows users to connect from one device to another computer no matter where they are. It is designed to provide a fast, smooth, and efficient remote desktop experience and supports multiple operating systems, including Windows, macOS, Linux, and Android.

- NoMachine uses NX technology to achieve efficient remote connections, which can reduce delays and maintain good image quality even on low-speed networks. In addition, it provides multi-platform support, allowing users to connect to other devices from computers, tablets, or mobile phones. Users can also transfer files between local and remote devices, share resources such as printers and hard drives, and ensure connection security through encrypted connections and multi-factor authentication.

- Suitable for remote work, IT support and remote education, NoMachine supports resource sharing and low-latency audio and video streaming. NoMachine offers a free personal version and a business version suitable for enterprises, the latter with more advanced features and technical support. Its efficiency and broad compatibility make it a popular choice for remote desktop access.

## 安裝 Nomachine
1.[Nomachine(jetson nano端)](./zip/Nomachine_7.10.1_1_arm64.zip)
下載完成後至終端輸入cd Downloads來進入資料夾
```
cd Downloads
```
接著輸入unzip Nomachine_7.10.1_1_arm64.zip以解壓縮檔案
```
unzip Nomachine_7.10.1_1_arm64.zip
```
完成後輸入sudo dpkg -i nomachine_7.10.1_1_arm64.deb來安裝
```
sudo dpkg -i nomachine_7.10.1_1_arm64.deb
```
看到這個圖示表示安裝完成
<td><img src="./img/nomachine_ok.png" width="500" alt="nomachine download"></td>

最後輸入cd來退出資料夾
```
cd
```
2.[Nomachine(Windows端)](./zip/Nomachine_7.10.1_1.zip)
下載完成後，執行安裝檔，最後須重新啟動
<td><img src="./img/nomachine_download.png" width="500" alt="nomachine download"></td>


3.連接jetson nano
在windows開啟nomachine
<td><img src="./img/nomachine_open.png" width="500" alt="nomachine open"></td>

輸入jetso nano底址
查找地址
```
ifconfig  
```
查找用戶名
```
hostname
```
<td><img src="./img/nomachine_ip.png" width="500" alt="nomachine ip"></td>

連上後輸入用戶明及密碼 
<td><img src="./img/nomachine_connet.png" width="500" alt="nomachine connet"></td>

完成後就能連上
<td><img src="./img/nomachine_jetson_ok.png" width="500" alt="nomachine jetson ok"></td>

資料參考:https://www.waveshare.net/wiki/JetRacer_ROS_AI_Kit_%E6%95%99%E7%A8%8B%E4%BA%8C%E3%80%81%E5%AE%89%E8%A3%85Jetson_nano_%E9%95%9C%E5%83%8F?fbclid=IwZXh0bgNhZW0CMTEAAR0V-M05bMx0xIQx-QcMI9sqtP8dBWXZpjhOegNngVdwizYW9Frqc738AiA_aem_wfqPbQnY9yv5tcLjEwcHYw#Jetson_Nano.E4.B8.8A.E5.AE.89.E8.A3.85


## Installing NoMachine
1.[NoMachine (on Jetson Nano)](./zip/Nomachine_7.10.1_1_arm64.zip)
After downloading, open the terminal and enter cd Downloads to navigate to the folder.
```
cd Downloads
```
Then, enter unzip Nomachine_7.10.1_1_arm64.zip to unzip the file.
```
unzip Nomachine_7.10.1_1_arm64.zip
```
Once extracted, enter sudo dpkg -i nomachine_7.10.1_1_arm64.deb to install.
```
sudo dpkg -i nomachine_7.10.1_1_arm64.deb
```
If you see this icon, the installation is complete.
<td><img src="./img/nomachine_ok.png" width="500" alt="nomachine download"></td>

Finally, enter cd to exit the folder.
```
cd
```
2.[NoMachine (on Windows)](./zip/Nomachine_7.10.1_1.zip)

After downloading, run the installation file. You will need to restart the computer afterward.
<td><img src="./img/nomachine_download.png" width="500" alt="nomachine download"></td>


3.Connecting to Jetson Nano
Open NoMachine on Windows.
<td><img src="./img/nomachine_open.png" width="500" alt="nomachine open"></td>

Enter the Jetson Nano IP address.

Find the IP address.
```
ifconfig  
```
Find the username.
```
hostname 
```
<td><img src="./img/nomachine_ip.png" width="500" alt="nomachine ip"></td>

After connecting, enter the username and password. 
<td><img src="./img/nomachine_connet.png" width="500" alt="nomachine connet"></td>

Once done, you’ll be able to connect.
<td><img src="./img/nomachine_jetson_ok.png" width="500" alt="nomachine jetson ok"></td>

Reference link:https://www.waveshare.net/wiki/JetRacer_ROS_AI_Kit_%E6%95%99%E7%A8%8B%E4%BA%8C%E3%80%81%E5%AE%89%E8%A3%85Jetson_nano_%E9%95%9C%E5%83%8F?fbclid=IwZXh0bgNhZW0CMTEAAR0V-M05bMx0xIQx-QcMI9sqtP8dBWXZpjhOegNngVdwizYW9Frqc738AiA_aem_wfqPbQnY9yv5tcLjEwcHYw#Jetson_Nano.E4.B8.8A.E5.AE.89.E8.A3.85



- 安裝參考鏈接:https://www.nomachine.com/
- <small>參考:[Wikipedia](https://en.wikipedia.org/wiki/NX_technology)</small>

- Installation reference link:https://www.nomachine.com/
- <small>Reference:[Wikipedia](https://en.wikipedia.org/wiki/NX_technology)</small>

# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
