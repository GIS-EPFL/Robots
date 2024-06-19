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


## URDF

### Introduction

URDF (Unified Robot Description Format) is a file format and XML-based markup language used to specify a robot's kinematic and dynamic features. It is the foundation for robot description in ROS and is required for a variety of applications such as robot visualization, motion planning, and simulation.

[URDF Structure](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/URDF.png)

### Robot Description

To describe a robot using URDF, the first step is to break the physical structure down into separate components called links. The origin for the link's coordinate system can be chosen arbitrarily, though for rotating links, it should be at the pivot point.

Next, understand how the links are joined together and how they relate to each other through connections called joints. Joints define the relationship between the origins (coordinate frames) of the links, determining the position and rotation of each link in space. Each link, apart from the first one, has a corresponding joint specifying its connection to its parent link.

![Link Structure](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/Link.png)

### Joint Types

![Joint Structure](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/Joint.png)

When describing a joint, specify the type of motion it uses. The four common types of joints are:
1. **Fixed:** No relative movement between parent and child links.
2. **Revolute:** Rotational motion around a single axis.
3. **Prismatic:** Linear motion along a single axis.
4. **Continuous:** Similar to revolute but with unbounded rotation.

|  |  |
|-------|-------|
| Fixed | Revolute |
| ![GIF 1](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/Fixed.gif") | ![GIF 2](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/Revolute.gif) |
| Prismatic | Continuous |
| ![GIF 3](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/Prismatic.gif) | ![GIF 4](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/Continuous.gif) |
|  |  |


### XML Structure

URDF is based on XML, with components represented as a series of nested tags.

## XACRO

### Introduction

XACRO (eXtensible Access Control Markup Language) is a tool that extends the capabilities of URDF by enabling the use of macros to simplify and manage the robot description files.

### Benefits

- **File Splitting:** Allows URDF files to be split into multiple manageable files.
- **Avoid Repetition:** Provides tools to avoid repetitive definitions in URDF files.

### Usage

To enable the use of XACRO in URDF files, add the following to the robot tag:
```xml
<robot xmlns:xacro="http://wiki.ros.org/xacro">
```

This can be included in every robot tag in URDF files. To use the URDF file, run the XACRO program on it. XACRO processes the files, resolving any macros, and outputs a complete URDF into memory.

Typically, this processed URDF is fed into the robot state publisher, which then publishes the complete URDF on the robot description topic, making it available to any node that needs it. This process is usually managed through a launch file, which reads the URDF files, passes them into XACRO, and then into the robot state publisher.

![XACRO Processing](/robot_files/abb_irb_6700_track_irtb_6004_2x/image/XACRO.png)


### Example

An example of including another XACRO file:
```xml
<xacro:include filename="another_robot.xacro" />
```

Splitting URDF into multiple files helps manage large and complex robot descriptions by separating components, making it easier to locate and modify specific parts.


## Docker container 
- Functions of different ROS service (roscore, rosfilesaver, rosbridge, moveitsetup assistant, moveit, rrcdriver)
- Function of Xlaunch 
## Create moveit package
- https://gramaziokohler.github.io/compas_fab/0.11.0/examples/03_backends_ros/08_ros_create_moveit_package_from_custom_urdf.html
- SRDF File
- Other files for understanding

## RVIZ
## Grasshopper file for checking
