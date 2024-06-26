# IRBT-6700 Single Robot Calibration (Alex)

## Tool calibration

Prior to calibration, the tool centre point (TCP) defaults to the centre point of the robot flange - the mounting plate to which a tool or end effector will be attached. After mounting a desired tool, such as a gripper, milling, or other end effector to perform robotic function, the TCP is the exact point where this tool will interact with a workpiece. It is important to accurately determine this point in order to achieve precision in robotic path planning and motion control.

TCP calibration is the process through which the user defines where in space the Tool Centre Point is with respect to the base coordinate system of the robot. Generally, the process includes the following steps:
1. Install the tool securely on the robot's flange or mounting plate
2. Select the tool calibration method

  **Manual Calibration is what we use here at the GIS** - _using a fixed object or calibration plate_
      - Move the robot to several different positions (depending on if 3 or 4-point calibration is used)
      - Record the position data from the robot's controller
      - Use the recorded positions to compute the TCP using geometric algorithms
    
3. Record and save the TCP position in the robot controller
4. Declare the new tool as current **add images - Alex**

**Common Challenges:**
- Accuracy: Ensuring that the recorded positions are accurate and free from errors
- Repeatability: Verifying that the robot can consistently return to the same TCP
- Environmental Factors: Accounting for any environmental changes that could affect the calibration process

**STEP-BY-STEP:**
Robot controller --> Jogging --> Tool --> New --> Define --> 4 point
<img width="574" alt="ToolCalibration" src="https://github.com/GIS-EPFL/Robots/assets/91248123/0bf19fa6-5085-4f98-b4f1-1806e2da1735">


OUTSTANDING
-------
- How to use the calibration camera system from IBOIS -- spoke to Andreas regarding this, currently requesting information and contact info from Gilles and Petras for the calibration consultants that came in


## Track calibration / Axis calibration

Track calibration has been completed for GIS robot set-up, and should not normally need to be changed or adjusted. It should only be redone if completely necessary, and only after speaking with one of the individuals managing this repo (Jingwen Wang, Marirena Kladeftira, Joseph Tannous, or Alexandra Pittiglio)! The robot's external linear track can be a useful tool to extend the reach and capabilities of the system. This is the process through which a robot's external linear track / rail is calibrated to ensure accurate positioning and movement. 

**STEP-BY-STEP:**
Main menu --> Calibration --> Track --> Base Frame --> 3-points --> Modify Position (REPEAT 3 TIMES) --> Save Positions
![PAGE 27](https://github.com/GIS-EPFL/Robots/assets/14881383/c16326eb-4039-47dd-ac1f-a554347d7ee0)

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
9. Navigate to the following following directory <your_local_directory>/Robots/robot_files/<new_setup(new_setup>(in this case abb_irb_6700_track_irtb_6004_2x)/5_playgrounds and open or create a calibration file. You can find it in this repo with the name "dual_robot_calibration.py".
   Replace the values that you measured with the two robots for the 8 points in the matrix as seen below:
  <img width="574" alt="measured_pts" src="https://github.com/GIS-EPFL/Robots/assets/22766174/6a0b3c07-e774-47ec-9eac-e338e00f276b">

   Run the script on your editor to calculate the transformation matrix and see the error. Copy the parameter on your console as seen in the picture bellow and paste it in the "param" variable in the script.
  <img width="574" alt="param" src="https://github.com/GIS-EPFL/Robots/assets/22766174/7735c864-9a8a-43e6-84b7-1dfee42dad8f">

11.

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
