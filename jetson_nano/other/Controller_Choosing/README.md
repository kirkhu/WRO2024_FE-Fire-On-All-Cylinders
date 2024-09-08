<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center">Controller Selection</div> 

- Two commonly available low-cost controllers capable of handling AI image recognition are the Jetson Nano and Raspberry Pi.
- They are suitable for various applications, including programming education in the field of education, smart home devices, self-driving cars, DIY projects, and more. This compact yet powerful microcomputer has become the top choice for electronics enthusiasts, students, and professionals.  
- We will compare the controller's specifications and prices to help us choose the right controller for our self-driving car.

- 在市售常見低價可以處理AI影像辦識的控制器有Jetson Nano 和 Raspberry Pi可以選擇，
- 它們適用於各種應用，如教育領域的編程教育、智能家居設備、自動駕駛汽車、DIY項目等。這款小巧而強大的微型電腦已成為電子愛好者、學生和專業人士的首選。
- 我們將針對控制器配備規格及價格等方面做比較，以便做為我們自駕車控制器的選擇依據。

## Controller Comparison(控制器的比較)
<div align=center>
<table>
<tr>
<th rowspan="2" width=300>圖片</th>
<th>Nvidia Jetson Nano</th>
<th>Raspberry Pi 4B</th>
</tr><tr>
<th><img src="./img/jeston_nano.png" width=200></th>
<th><img src="./img/raspberry_pi_4.png" width=200></th>
</tr><tr>
<th>Number of Pins 針腳數量</th>
<td>40P</td>
<td>40P</td>
</tr><tr>
<th>CPU</th>
<td>四核心 ARM® Cortex®-A57 MPCore 處理器</td>
<td>1.5GHz 64 位四核 ARM Cortex-A72 CPU</td>
</tr><tr>
<th>GPU</th>
<td>NVIDIA Maxwell™ 架構配備 128 個 NVIDIA CUDA® 核心</td>
<td>博通 VideoCore VI；H.265（4kp60 解碼）、<br>H264（1080p60 解碼、1080p30 編碼）
OpenGL ES 3.1、Vulkan 1.0</td>
</tr><tr>
<th>Storage Space 儲存空間</th>
<td>4 GB 64-bit LPDDR4</td>
<td>8GB LPDDR4-3200 SDRAM</td>
</tr><tr>
<th>Built-in Bluetooth and Wireless WiFi Connectivity內建藍芽與無線WIFI連接</th>
<td>需外接</td>
<td>有內建</td>
</tr><tr>
<th>Gflops(每秒浮點運算次數)</th>
<td>472</td>
<td>13.5</td>
</tr><tr>
<th>Price</th>
<td>Expensive</td>
<td>Cheap</td>  
</tr>
</table>
</div>

- At the beginning of the competition, we chose the Raspberry Pi, which is more affordable and has AI image recognition capabilities, as the controller for our self-driving car. However, we found that the Raspberry Pi controller had insufficient image recognition performance.   
- we attempted to switch to the Jetson Nano as the controller for our self-driving car, as it offered significantly faster image recognition processing.  
- However, after actual experiments, although the image recognition speed is very fast, the speed of reading the color sensor is very slow, which leads to the inability to make timely judgments and make correct operations, which delays the turning of the vehicle and makes the vehicle unable to drive correctly. This may be a problem of our insufficient technical capabilities.
- To ensure it wouldn't affect upcoming competitions, we reverted to using the Raspberry Pi as the controller. Although its image recognition speed is slower, it allows the vehicle to operate reliably. Additionally, we are implementing other solutions to address the Raspberry Pi's limitations in image recognition performance.  
- __In conclusion, we have chosen to use the Raspberry Pi as the controller for our self-driving car in this competition.__

- 比賽開始我們選擇具有AI影像辨識功能且價格較便宜的 Raspberry Pi，來做為我們自駕車的控制器，但發現Raspberry Pi控制器會有影像辨識效能不足的情形。
- 我們嘗試改用影像辦識運算效率較快的Jetson Nano 當自駕車的控制器。
- 但經過實際實驗，雖然影像辨識速度極快，但是讀取顏色感測器的速度卻很慢，造成無法及時判斷做出正確運作而延遲車輛轉彎，使車輛無法正確行駛，這有可能是我們的技術能力不足的問題。
- 為了不影響後續的比賽，我們將控制器改回Raspberry Pi，雖然影像辨識速度較慢，但是至少車輛可以正常行駛，我們也會使用其他方式輔助解決Raspberry Pi影像辨識效能不足的地方。
- __綜合以上說明，最後選擇使用樹梅派作為我們這次比賽自駕車的控制器__



# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div> 
