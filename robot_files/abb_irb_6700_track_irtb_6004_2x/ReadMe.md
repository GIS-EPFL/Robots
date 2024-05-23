# IRBT-6700 Calibration

## Tool calibration

- How to use the calibration camera system
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

# IRBT-6700  Dual Robot Calibration

## 8 Point calibration method

- Finish single robot axis calibration
- Set tool as the pintool, set coordinate system to base
- Reach the same 8 points 
- Calculate transformation matrix 
- Update URDF
- Calculate transformation matrix considering track calibration (quaternion)
# Create moveit package from URDF
## Xacro and URDF
## Docker container 
## Create moveit package
- https://gramaziokohler.github.io/compas_fab/0.11.0/examples/03_backends_ros/08_ros_create_moveit_package_from_custom_urdf.html
- SRDF File
- Other files for understanding
- Simplify reference files

## RVIZ
## Grasshopper file for checking
