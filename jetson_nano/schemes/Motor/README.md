<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

# <div align="center"> Motor Selection</div> 
When the vehicle is in motion, the Raspberry Pi sends speed information to __the motor controller(L293D)__ to control the __rear-wheel drive DC motor__. Simultaneously, the Raspberry Pi also sends messages to the __servo motor of the front steering mechanism__, enabling the vehicle to maneuver freely and move forward.  

### Front Steering Mechanism by Servo Motor
- To select a servo motor among commonly available options in the market, considering factors such as weight, rotation angle, and torque, we have identified two suitable servo motors: MG90S and SG90.
- The difference between MG90S and SG90 lies in the front gears, where the former has metal gears, while the latter has plastic ones. Since we often require continuous rotation, we have __chosen the MG90S__ due to its durability, as it is less prone to damage.

<div align="center">
<table>
<tr ><th colspan="3">Servo Motor Comparison</th></tr>
<tr align="center">
<th rowspan="2" >Model</th>
<th>MG90S</th>
<th>SG90</th>
</tr>
<tr align="center">
<td><img src="./img/MG90S.png" width = "150" height = "" alt="MG90S" align=center /></td>
<td> <img src="./img/SG90.png" width = "150" height = "" alt="SG90" align=center /></td>
</tr>
<tr align="center">
<td>Rotation Angle</td>
<td>90° MAX</td>
<td>360° MAX</td>
</tr>
<tr align="center">
<td>Torque</td>
<td>2.0kg/cm</td>
<td>1.4 kg/cm</td>
</tr>
<tr align="center">
<td>Speed</td>
<td>0.11s</td>
<td>0.1S</td>
</tr>
</table>
</div>

### Rear-Drive DC Motor
- When selecting a DC motor among commonly available options in the market, considering factors such as weight, rotational speed, and torque, we have identified the following four suitable DC motors.
- Among them, the three types of motors, JGA25, have different model numbers but share a similar physical appearance, and their differences are as follows.
<div align="center"><table>
<tr ><th colspan="6">DC Motor Comparison</th></tr>
<tr align="center">
<th rowspan="2" >Model</th>
<th >JGA25 370</th>
<th >JGA25 370</th>
<th >JGA25 371</th>
<th >JGA16-050</th>
</tr>
<tr align="center">
<td ><img src="./img/JGA25-370_1360RPM.JPG" width = "150" alt="JGA25-370_1360RPM" /></td>
<td ><img src="./img/JGA25-370_620RPM.JPG" width = "150" alt="JGA25-370_620RPM" /></td>
<td ><img src="./img/JGA25-371_1_34.JPG" width = "100" alt="JGA25-371M" /></td>
<td ><img src="./img/JGA16-050.png" width = "150" alt="JGA16-050" /></td>
<td ><img src="./img/WHEELTEC.png" width = "150" alt="JGA16-050" /></td>
</tr>
<tr align="center">
<td >Speed</td>
<td >1360rpm</td>
<td >620rpm</td>
<td >294rpm</td>
<td >220rpm</td>
</tr>
<tr align="center"><td>Torque</td><td>4.27kg.cm</td><td>9.15kg.cm</td><td>5.2kg.cm</td><td>1.15kgcm</td></tr><tr align="center">
<td>Power</td><td>5.4W</td><td>5.4W</td><td>4.2W</td><td>0.33W</td>
</tr>
</table>
</div>  

- After conducting experimental research, we found that choosing the high-speed 1630rpm JGA-370 motor resulted in lower torque, making it difficult for the vehicle to move effectively. On the other hand, opting for the high-torque JGA-371 motor led to an excessively low rotational speed, which did not meet the requirements for the vehicle's operation.
- __Therefore, based on these findings, we ultimately selected the 620rpm JGA-370 motor as the rear-wheel drive DC motor for the vehicle. This choice strikes a balance between rotational speed and torque, providing the necessary performance for the vehicle's propulsion.__  

### Motor Drive Controller
- When testing the operation of the motor, simply providing power does not effectively control the movement of the GA25-370 motor, making it impossible to adjust the speed. Therefore, we need to install a motor controller to regulate the speed of the DC gear motor. Currently, there are two options available in the market: the L293D chip and the L298N module. To reduce weight, we __chose the smaller L293D chip.__   
- __Its compact size allows us to install more sensors, thereby saving space, reducing weight, and increasing the maneuverability of the vehicle.__


<div align="center">
<table>
<tr><th colspan="3">Motor Control Comparison</th></tr>
<tr align="center" >
<th rowspan="2">Model</th>
<th>L293D</th>
<th>L298N</th>
</tr>
<tr align="center">
<td> <img src="./img/l293d.png" width = "300"  alt="l293d" align=center /></td>
<td ><img src="./img/L298N.png" width = "300"  alt="l298n" align=center /></td>
</tr>
<tr align="center">
<td>Occupied Area(mm)</td>
<td>29.5x8</td>
<td>43.5x43.5</td>
</tr>
<tr align="center">
<td>Output Voltage</td>
<td>4.5V to 36V</td>
<td>5V to 46V</td>
</tr>
<tr align="center">
<td>Rated Power </td>
<td>5W</td>
<td>10W</td>
</tr>
</table>
</div>

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  