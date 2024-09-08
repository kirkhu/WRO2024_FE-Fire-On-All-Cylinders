<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Vehicle Chassis Design Process(車輛底盤設計)</div> 

- ### Vehicle Chassis Design
  - 此次競賽所使用車輛底盤，為自行設計研發。
  - 我們將Ackermann Steering Geometry設計在車輛底盤機構，以利車輛閃避障礙物及回轉。 
  - 下表為此次車輛底盤的3D模型及成品。 
  - The vehicle chassis used in this competition is self-designed and developed.
  - We applied Ackermann Steering Geometry to the vehicle chassis mechanism to facilitate obstacle avoidance and U-turns.
  - The following table shows the 3D models and finished products of the vehicle chassis.


    |3D Vehicle Chassis Design| Vehicle Chassis Top View | Vehicle Chassis Bottom View|
    |:----:|:----:|:----:|
    |<img src="./img/Vehicle chassis description.png" width="400" alt="vehicle_chassis_design_3D">|<img src="./img/down_layer_top_view.jpg" width="400" alt="up_view">|<img src="./img/down.png" width="400" alt="down_view">|

    - 我們將車輛底盤上的配件，除了齒輪、差速器、及輪胎外，其餘都是使用光固化3D印表機、雷切機自己設計的零件，這可以節省空間並依車輛需求調整尺寸、形狀等。
    - 因車輛的支撐架加入軸承，降低摩擦力，提高車輛速度。
    - 車輛底盤上阿克曼轉向幾何機構的支撐架，也透過3D繪圖輸出模型，使用光固化3D表機生產，這樣可以自由設計調整阿克曼率，找出最佳的迴轉精半徑。
    
    - We used a Stereolithography (SLA) 3D Printer and laser -cutting machine to design and produce all the components on the vehicle chassis, except for the gears, differential, and tires. This approach not only saves space but also allows us to customize dimensions and shapes according to the specific needs of the vehicle.
    - By incorporating bearings into the vehicle's support frame, we've reduced friction, thereby increasing the vehicle's speed.
    - The support frame for the Ackermann steering geometry on the vehicle chassis was designed through 3D modeling, and the model was then produced using a stereolithography (SLA) 3D printer. This approach allows for the flexible adjustment of the Ackermann ratio, helping us determine the optimal turning radius with precision.

- #### 車輛底盤改良紀錄 Vehicle Chassis Improvement Record

    - 在設計車輛底盤的過程中，遇到許多問題，我們將解決修改過程紀錄如下表：  
    - In the process of designing the vehicle chassis, we encountered many issues. We will document the problem-solving and modification process in the following table:


        |First Prototype| Explanation 說明 |
        |:----:|:----|
        |<img src="./img/2-1.png" width="500" alt="body_bottom_lego">|為了讓輪子轉動更順暢，我們新增了軸承，並使用光固化3D列印機制作軸承固定架，並在木板上切出相應位置的孔與軸承固定架相應配合。 To ensure smoother wheel rotation, we incorporated bearings. We utilized a Stereolithography (SLA) 3D Printer to create the bearing mounts, which were then accurately aligned with corresponding holes cut into the wooden board.|


        |Second Prototype | Explanation 說明 |
        |:----:|:----|
        |<img src="./img/4.png" width="500" alt="body_bottom_lego">|由於3D列印材料脆弱，因此我們改回原來使用的木板材料，並增加放置伺服馬達的位置，使光感也可以相對降低位置，降低重心。 Due to the fragility of the 3D printed material, we reverted back to using the original wooden board material. Additionally, we adjusted the placement of the servo motor to lower its position, thus reducing the center of gravity and enhancing stability.|

        |Final Build | Explanation 說明 |
        |:----:|:----|
        |<img src="./img/5.png" width="400" alt="body_bottom_lego">|這個版本改變的重點是將伺服馬達的位置由本來的靠左改為置中，否則左邊的木板將會太薄而斷裂。  The key change in this edition is shifting the position of the servo motor from being on the left side to being in the center. Otherwise, the left wooden board would be too thin and prone to breaking.|

- #### What is an Ackermann Steering Geometry?(何謂阿克曼轉向幾何?)

  - #### 阿克曼轉向幾何介紹  Ackermann Steering Geometry Introduction 
    - The Ackermann steering geometry, proposed by German automotive engineer Lankensperger in 1817, is a steering system design used in automobiles. It was developed to address the geometric discrepancy in the paths of the inner and outer turning wheels when a vehicle makes a turn.
    - People apply Ackermann steering geometry to the steering mechanism of vehicles. Through the corresponding cranks of the four-linkage system, the steering angle of the wheels relative to the projected tire is increased by about 2 to 4 degrees. This results in the rough convergence of the trajectory centers of all four wheels along the extension line of the rear axle, thereby achieving the vehicle's turning.

    - 阿克曼轉向幾何是由德國車輛工程師「Lankensperger」於1817年提出的，一種用於汽車的轉向系統設計，為了解決交通工具轉彎時，內外轉向輪路徑指向的圓心不同的幾何學。
    - 人們將阿克曼轉向幾何應用在車輛轉向機構，透過四連桿的對應曲柄，使車輪在輪胎時的轉向角相對於預計輪胎增加約2至4度。這樣，四個車輪的軌跡中心大致交匯後軸的延長線，從而在實現車輛的彎曲。
    
      <img src="./img/Ackermann_steering_geometry.png" width="500" alt="Ackermann_steering_geometry">  

      Reference Link：[Ackermann steering geometry@Wikipedia](https://zh.wikipedia.org/zh-tw/%E9%98%BF%E5%85%8B%E6%9B%BC%E8%BD%89%E5%90%91%E5%B9%BE%E4%BD%95)
      #### __The principle of Ackermann steering geometry is based on the following concepts: 阿克曼轉向幾何的原理基於以下概念：__
      
      - __轉向半徑差異：__ 當車輛進行轉彎時，兩前輪需要轉動不同的角度，以便車輛可以繞著一個中心點旋轉。
      - __兩前輪的轉向角度：__ 阿克曼轉向幾何的設計保證了兩前輪在轉向時能夠同時經過一個中心點。

    - 此轉向機構相較於原來0%樂高積木零件製作的阿克曼轉向幾何機構，本競賽活動車輛的轉向機構是參考阿克曼轉向幾何機構80%而設計，具有阻力減少和更平滑轉彎的優點，並使用光固化3D印列機生產阿克曼轉向幾何機構零件來實現，然而過程中遇到最難解決的問題則是調整阿克曼率，以達到適合我們車輛閃避積木的轉彎角度。
       - __Difference in Turning Radius:__ When the vehicle makes a turn, the two front wheels need to rotate at different angles to allow the vehicle to pivot around a central point.
       - __Turning Angles of the Two Front Wheels:__ The design of the Ackermann steering geometry ensures that both front wheels pass through a central point simultaneously during steering.
    - Compared to the Ackermann steering geometry made from the original 0% LEGO bricks, the steering mechanism of this competition vehicle is designed with reference to an 80% Ackermann steering geometry. It offers advantages such as reduced resistance and smoother turns. The Ackermann steering geometry parts are produced using a stereolithography (SLA) 3D printer. However, the most challenging aspect of the process was adjusting the Ackermann ratio to achieve the ideal turning angle for our vehicle to navigate around blocks effectively.
    
  
  - #### 為何選擇阿克曼率80%? Why Choose an 80% Ackermann Ratio?
    - 從理論上講，這種設計對於平穩、高效的轉彎來說是最佳選擇，但可能會導致輪胎過度磨損，所以在汽車設計中通常不會選擇100%的阿克曼率與100%的阿克曼率相比，80%的阿克曼率可以實現更平穩、更可預測的轉彎、改善操控性並減少輪胎磨損。
    - In theory, this design is the optimal choice for smooth and efficient turns. However, it may lead to excessive tire wear. Therefore, in automobile design, a 100% Ackermann ratio is usually not chosen. Compared to a 100% Ackermann ratio, an 80% Ackermann ratio allows for smoother, more predictable turns, improves maneuverability, and reduces tire wear.


  - #### 使用Stereolithography (SLA) 3D Printer生產阿克曼轉向幾何機構零件(80%阿克曼率) Producing Ackermann steering geometry components (80% Ackermann angle) using Stereolithography (SLA) 3D Printer
    - 在左下圖紅框內的阿克曼轉向幾何機構零件是使用樂高積木零件組成。
    - 在右下圖紅框內的阿克曼轉向幾何機構零件是使用Stereolithography (SLA) 3D Printer生產自製的塑膠零件組成。
    - 使用樂高積木組裝轉向系統可以節省成本和時間，而使用光固化 3D 列印機製造塑料零件可以提高精度和可定製性。
    - 在製作和測試的過程中，我們發現使用樂高積木零件時會受原有規格限制的問題，導致無法製作出最符合我們需求的結構，反觀使用Stereolithography (SLA) 3D Printer生產阿克曼轉向幾何機構零件，可以按照所需尺寸、形狀自行設計打印
    - __因此最終我們決定選擇使用Stereolithography (SLA) 3D Printer生產阿克曼轉向幾何機構零件作為車輛轉向機構__。
    - The Ackermann steering geometry components within the red box in the bottom-left diagram are assembled using LEGO bricks.
    - The Ackermann steering geometry components within the red box in the bottom-right diagram are assembled from self-produced plastic parts using a Stereolithography (SLA) 3D Printer.
    - Assembling the steering system with LEGO bricks can save costs and time, while using a Stereolithography (SLA) 3D printer to manufacture plastic parts can enhance precision and customization.
    - During the process of production and testing, we found that using LEGO bricks was limited by the original specifications, making it difficult to create a structure that perfectly suited our needs. In contrast, utilizing a Stereolithography (SLA) 3D Printer to produce the Ackermann steering geometry components allowed for customization in size and shape, giving us the flexibility to design and print according to our specific requirements. 
    - __As a result, we ultimately decided to use the SLA 3D Printer to manufacture the Ackermann steering geometry components for the vehicle's steering mechanism.__



    <div align=center>
    <table>
    <tr>

    <th>Assembled Using Photocured PartsAssembling Parts Produced with a SLA 3D Printer 使用SLA 3D Printer生產零件組裝</th>
    </tr><tr>
   
    <td align=center><img src="./img/car_wood_up-removebg-preview.png"></td>
    </tr>
    </table>
    </div>

    - #### 以繪圖方式計算出阿克曼率 (a-b = ack) Calculating the Ackermann Angle Graphically (a-b = ack)

    <div align="center">
    <table>
    <tr align=center>
    <td><img src="./img/angle.png" width="300" alt="angle"></td>
    <td><img src="./img/80acmen.png" width="350" alt="Ackermann_steering_geometry_lego"></td>
    </tr>
    </table>
    </div>

    Reference Video website：[汽车转弯 没那么简单: 阿克曼转向几何是个啥？How does Ackerman steering geometry work?](https://www.youtube.com/watch?v=8AimxDPWKcM)






      
# <div align="center">![HOME](../../other/img/Home.png)[Return Home](../../)</div>  
