 <div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">OpenCV Introduction</div> 
- OpenCV（Open Source Computer Vision Library） of Introduction
   OpenCV (Open Source Computer Vision Library) is an open-source computer vision library that serves as a powerful tool for processing images and videos in computer vision tasks. It supports various programming languages, including Python, C++, Java, and more, making it accessible across different platforms.

- OpenCV offers a wide range of functionalities and algorithms, encompassing tasks such as image processing, feature detection, object recognition, video analysis, and more. It finds applications in numerous fields, such as machine vision, image processing, video tracking, facial recognition, augmented reality, and others.

- The first step to using OpenCV typically involves installing the OpenCV library and then utilizing the relevant APIs for image or video processing tasks. This may involve reading image or video files, applying various image processing techniques (such as filtering, edge detection, color conversion, etc.), or performing object recognition and tracking tasks. 

## OpenCV安裝
更新
```
sudo apt-get update
```
```
sudo apt-get upgrade
```
下載 nano
```
sudo apt-get install nano
```
下載 dphys-swapfile
```
sudo apt-get install dphys-swapfile
```
檢查記憶體
```
free -m
```
需6.5GB
擴大空間
```
wget https://github.com/Qengineering/Install-OpenCV-Jetson-Nano/raw/main/OpenCV-4-5-0.sh
```
```
sudo chmod 755 ./OpenCV-4-5-0.sh
```
安裝
```
./OpenCV-4-5-0.sh
```
```
rm OpenCV-4-5-0.sh
```
刪除 dphys-swapfile
```
sudo /etc/init.d/dphys-swapfile stop
```
```
sudo apt-get remove --purge dphys-swapfile
```
節省 275 MB 的提示
```
sudo rm -rf ~/opencv
```
```
sudo rm -rf ~/opencv_contrib
```
安裝 pyserial 模組
```
pip install pyserial
```
下載imx477的韌體
```
cd ~
wget https://github.com/ArduCAM/MIPI_Camera/releases/download/v0.0.3/install_full.sh

```
```
chmod +x install_full.sh
./install_full.sh -m imx477
```
參考資料:https://qengineering.eu/install-opencv-on-jetson-nano.html 、
https://docs.arducam.com/Nvidia-Jetson-Camera/Native-Camera/Quick-Start-Guide/?fbclid=IwZXh0bgNhZW0CMTEAAR3rpGy1GsiVuHBFvi6qkJIelI8P88syOjCk1rvKRaBONlKQOsQ7BPMmfVI_aem_jJuQ5IOzOy0no-wMudOhlQ


## Installing OpenCV
Update System
```
sudo apt-get update
```
```
sudo apt-get upgrade
```
Download Nano
```
sudo apt-get install nano
```
Download dphys-swapfile
```
sudo apt-get install dphys-swapfile
```
Check Memory
```
free -m
```
Ensure you have at least 6.5GB.
Expand Swap Space
```
wget https://github.com/Qengineering/Install-OpenCV-Jetson-Nano/raw/main/OpenCV-4-5-0.sh
```
```
sudo chmod 755 ./OpenCV-4-5-0.sh
```
Install OpenCV
```
./OpenCV-4-5-0.sh
```
```
rm OpenCV-4-5-0.sh
```
Remove dphys-swapfile
```
sudo /etc/init.d/dphys-swapfile stop
```
```
sudo apt-get remove --purge dphys-swapfile
```
This will save approximately 275 MB.
```
sudo rm -rf ~/opencv
```
```
sudo rm -rf ~/opencv_contrib
```
Install the pyserial Module
```
pip install pyserial
```
Download Firmware for IMX477 Camera
```
cd ~
wget https://github.com/ArduCAM/MIPI_Camera/releases/download/v0.0.3/install_full.sh

```
```
chmod +x install_full.sh
./install_full.sh -m imx477
```
Reference links:https://qengineering.eu/install-opencv-on-jetson-nano.html 、
https://docs.arducam.com/Nvidia-Jetson-Camera/Native-Camera/Quick-Start-Guide/?fbclid=IwZXh0bgNhZW0CMTEAAR3rpGy1GsiVuHBFvi6qkJIelI8P88syOjCk1rvKRaBONlKQOsQ7BPMmfVI_aem_jJuQ5IOzOy0no-wMudOhlQ



- <small>References:[Wikipedia](https://zh.wikipedia.org/wiki/OpenCV)</small>

- <small>References:[steam educational website](https://steam.oxxostudio.tw/category/python/ai/opencv.html#google_vignette)</small>

# <div align="center">![HOME](../../img/home.png)[Return Home](../../)</div> 
