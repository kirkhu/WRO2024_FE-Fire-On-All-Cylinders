<div align="center"><img src="./other/img/logo.png" width="300" alt=" logo"></div> 

- This is the official GitHub repository for the WRO TAIWAN team "__Fire On All Cylinders.__" All code, documentation, and files are located here.
- The inspiration for the hardware and software design of this autonomous vehicle came from the model designed by our seniors last year, and we also drew on the strengths of the model that won first place in last year’s competition. Based on this, we made improvements and replaced the main controller from "Raspberry Pi 4B" to "Nvidia Jetson Nano," aiming to enhance performance and innovative design, making it more competitive.
- Here you can find the links to the technical report content and setup instructions, organized separately for learners and judges, for easy access during either learning or assessment. 
- In this technical document, the directory will be established based on the scoring criteria, and the directory headings will be hyperlinked for easy access for judges or learners to navigate to the key content of the technical document, facilitating quick assessment.  
    #### [For Learners](learners_contents.md)
## Rubric for Judging Engineering Documentation 
- ###  ${{\color{red} Hardware Overview }} $ 
  #### 1. Mobility Management
    * [1-1 Vehicle 2D/3D Models in CAD](models/Vehicle_2D_3D/README.md)
    * [1-2 Vehicle Chassis Design](schemes/Vehicle_Chassis_Design/README.md)
    * [1-3 Motor Selection](schemes/Motor/README.md)

    
  #### 2. Power and Sense Management
    - __Vehicle Design__
      - [2-1-1 BOM Parts List](schemes/Parts_List/README.md)
      - [2-1-2 Circuit Design](models/Circuit_Design/README.md)
      - [2-1-3 Hardware Fool-Proof Design](schemes/Fool-Proof-Design/README.md) 
      - [2-1-4 Assembly Instructions & Wiring Diagrams](schemes/Assembly_Instructions/README.md)    
      
    - __Power Management__
      - [2-2-1 Power Supply System](schemes/Power_supply_system/README.md) 
      - [2-2-2 Li-Polymer Battery Low Voltage Alarm and Charging Equipment](schemes/Li-Polymer_Battery/README.md)  
   
    - __Controller Selection__
      - [2-3-1 Main Controller Comparison 運算控制器](other/Main_Controller_Choosing/README.md)
      - [2-3-2 The motor and sensor controller Comparison 驅動控制器](other/Motor_Sensor_Controller_Choosing/README.md)
    - __Sense Management__
      - [2-4-1 HC-SR04 Selection 要介紹3.3V和5V的差異，pico不支援救3.3V](schemes/HC-SR04/README.md)
      - [2-4-2 BNO055](schemes/Lidar/README.md)
      - [2-4-3 Camera Selection](schemes/Camera/README.md)
  
- ### ${{\color{red} Software Overview }} $ 
  #### 3. Obstacle Management
    - [3-1 OpenCV Introduction](other/OpenCV/README.md)
    - [3-2 Software Platform Construction](src/System_Platform_Software/README.md)
    - __Image Processing and Steering__
      - [3-4-1 Image Processing](src/Image_Processing_and_Steering/Image_Processing/README.md)  
      - [3-4-2 Steering Overview](src/Image_Processing_and_Steering/Steering_overview/README.md) 
    - __Programming__
      - [3-5-1 Open Challenge Code Overview](src/Programming/Open_Challenge/README.md)
      - [3-5-2 Obstacle Challenge Code Overview](src/Programming/Obstacle_Challenge/README.md)
      - [3-5-3 Distinctive Pseudo Code](src/Distinctive_Pseudo_Code/README.md)
      - [3-5-4 Parking Instructions](src/park/park.md)
    - __remote connection__
      - [3-6-1 NoMachine](other/NoMachine/README.md)
- ### ${{\color{red} Other}} $
  #### 4. Pictures – Team and Vehicle
    - [4-1 Team Members Introduction](t-photos/README.md) 
    - [4-2 Vehicle Photos](v-photos/README.md)  
  #### 5. Performance Videos
    - [5-1 Open Challenge](video/Open_Challenge/video.md)
    - [5-2 Obstacle Challenge](video/Obstacle_Challenge/video.md)
    - [5-3 Self-Driving Car Design Process Video](video/ALL_video/video.md)
  #### 6. GitHub Utilization
    - [6-1 GitHub Edit(VScode Edit/GIT)](src/GitHub_Edit/README.md)
    - [6-2 GitHub Web Editing Languages](src/GitHub_Languages/README.md)  
  #### 7. Engineering Factor  
    - [7-1 Work Diary](other/work_diary/README.md)
- ### ${{\color{red} CompetitionSchedule}} $  
# <div align="center">![Competition Schedule Gantt](./other/img/gantt.png)</div> 

