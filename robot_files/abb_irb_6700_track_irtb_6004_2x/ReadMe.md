# IRBT-6700 Single Robot Calibration (Alex)

## Tool calibration

- How to use the calibration camera system from IBOIS
- Robot controller - jogging - tool - new - define - 4 point
<img width="574" alt="ToolCalibration" src="https://github.com/GIS-EPFL/Robots/assets/91248123/0bf19fa6-5085-4f98-b4f1-1806e2da1735">

## Track calibration / Axis calibration

- Conduct tool calibration before track calibration
- Calibration - three point

## Update in URDF

- From Robotstudio to get quaternion
![robotstudio_axis_calibration](https://github.com/GIS-EPFL/Robots/assets/91248123/9a07bf4c-0c0c-4dae-9579-f0b5070a409d)
- from quaternion to Euler angles 
- from Euler angles to URDF

# IRBT-6700  Dual Robot Calibration (Marirena)

## 8 Point calibration method

1. Finish the axis calibration for each robot you want to use collaboratively as described in the steps above.
2. Mount a "pin tool" on each robot so you can measure the points accurately. There are two pins available in GIS that you can use.
<img width="574" alt="pins" src="https://github.com/GIS-EPFL/Robots/assets/22766174/9f3e3cb6-77df-41a8-a17c-74883bce9ea9">

4. Set tool as the corresponding pintool (e.g. screwPin for the threaded pin, or pencil for the wooden pencil in the picture)
<img width="574" alt="pinTool" src="https://github.com/GIS-EPFL/Robots/assets/22766174/6c0f20da-6777-409c-8fc8-f2e87fd87c22">

5. Set coordinate system to base
6. Get the precision camera and the laptop that contains the software from CRCL. This is a custom equipment with two micro cameras to help you reach the same point with the two robots precisely.
<img width="574" alt="camera" src="https://github.com/GIS-EPFL/Robots/assets/22766174/199a2f2c-ff50-4bd2-b2fb-937eeb4904eb">

7. Consider 8 points that you want to measure with the two robots. Keep in mind that in the area where the 8 points are measured the urdf will be most accurate, so try to disperse them in the area of reach of both robots.
8. For each point you place this camera at jog one robot first in place until you see the tip well in the target area. Write down the position of the robot at that point. Repeat for the second robot. Move to the next point until you have measured all 8 points with both robots.
9. 
- Calculate transformation matrix 
- Update URDF
- Calculate transformation matrix considering track calibration (quaternion)
# Create moveit package from URDF (Joseph)
## URDF and Xacro
- Understand the single URDF (Gonzalo's class has some explaination)
- How Xacro files connect multi-URDF together
## Docker container 
- Functions of different ROS service (roscore, rosfilesaver, rosbridge, moveitsetup assistant, moveit, rrcdriver)
- Function of Xlaunch 
## Create moveit package
- https://gramaziokohler.github.io/compas_fab/0.11.0/examples/03_backends_ros/08_ros_create_moveit_package_from_custom_urdf.html
- SRDF File
- Other files for understanding

## RVIZ
## Grasshopper file for checking
