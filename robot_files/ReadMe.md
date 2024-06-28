# **Section 0** - For General Users (Jingwen)

## **I .** Introduction

If you do not need to recalibrate the robots (for example, you only need to use one robot without track, one robot with already calibrated track, or you need to use two robots and they are already calibrated). You only need to understand the file structure and the use of yml file with docker (follow II, III). 

For people who want to calibrate robots (for example they want to recalibrate tracks, they have a new two robot system...), you can follow **Section 1 - 3** to create your own moveit package. Before doing so on GIS-robots, please inform repo maintainer (Jingwen, Eleni, Alex, Marirena, Joseph). We just want to check if your new calibration will change the current URDF data. Also let us know if you find out any mistakes with the URDF file. 

**Disclaimer:** The calibration method for two robots here is developed by Jingwen Wang and Wenjun Liu during their master thesis at ETH Zurich, and it is not the only method of doing calibration. We believe it is a relative good method for robots with absolute accuracy (FYI ABB Gofa does not have absolute accuracy, so this method is tricky to be used there). If you have your own easier workflow feel free to use it instead of following our workflow, since not every project need high accuracy. Also if you believe you have better/faster calibration method feel free to discuss with us ;) We are open to improvements.  

## **II .** File Structure



## **III .** General uses



# **Section 1** - IRBT-6700 Single Robot Calibration (Alex)

## **I .** Tool calibration

Prior to calibration, the tool centre point (TCP) defaults to the centre point of the robot flange - the mounting plate to which a tool or end effector will be attached. After mounting a desired tool, such as a gripper, milling, or other end effector to perform robotic function, the TCP is the exact point where this tool will interact with a workpiece. It is important to accurately determine this point in order to achieve precision in robotic path planning and motion control.

TCP calibration is the process through which the user defines where in space the Tool Centre Point is with respect to the base coordinate system of the robot. Generally, the process includes the following steps:
1. Install the tool securely on the robot's flange or mounting plate
2. Select the tool calibration method

**Manual Calibration is what we use here at the GIS** - _using a fixed pointed object_

      - Set-up your calibration tool in a suitable position within reach of the robot(s). A point/spike on a heavy plate exists for this purposed in the GIS (ask Gregory or Gilles)
      - Approach the end of this spike several times, from several different approach angles (depending on if 3 or 4-point calibration is used)
      - Each time, record the position data from the robot's controller
      - Use the recorded positions to compute the TCP using geometric algorithms

3. Record and save the TCP position in the robot controller
4. Make sure you've declared your new tool as the current tool

**Common Challenges:**

      - Accuracy: Ensuring that the recorded positions are accurate and free from errors
      - Repeatability: Verifying that the robot can consistently return to the same TCP
      - Environmental Factors: Accounting for any environmental changes that could affect the calibration process

**STEP-BY-STEP:**
Robot controller --> Jogging --> Tool --> New --> Define --> 4 point

<img width="574" alt="ToolCalibration" src="https://github.com/GIS-EPFL/Robots/assets/91248123/0bf19fa6-5085-4f98-b4f1-1806e2da1735">


**II.** IBOIS Tool Calibration Camera
-------
The IBOIS camera system can be used to calibrate your tool. This device is accompanied by a laptop where the calibration program, SharpCap, is pre-installed. The steps for use are as follows:  
      - Open the device case and accompanying laptop, and plug the two USB cords from the cameras into the inputs on the laptop.  
      <img width="300" alt="camera" src="https://github.com/GIS-EPFL/Robots/assets/14881383/98f057ad-546a-4d0b-82e5-e6817c2fabae">  
      - Open two separate instances of the software, SharpCap. Split screens so you have a side-by-side view of the two windows.  
      - In each opened instance of the software, select the dropdown menu "Cameras" --> on one window select USB 1, one the other window select USB 2 (just ensure you are viewing one camera from each instance of the software)  
      - In each window, select the below dropdown menu --> "Circle"  
      <img width="300" alt="circle" src="https://github.com/GIS-EPFL/Robots/assets/14881383/8119fa67-c883-43c0-84e2-f1e4c2d5a55b">  
      - Adjust the focus (manually) on each camera until you see a sharp image in the respective camera view. **After adjusting in this step, don't touch the camera focus again throughout the process or you will incur potential error**  
      - Jog the robot until you see the TCP (tool centre point) as close as possible to the central crosshairs in the camera view.  
      <img width="300" alt="twoview" src="https://github.com/GIS-EPFL/Robots/assets/14881383/7ded446a-2305-4ff9-bf68-1bf38a335e23">
      
## **III.** Track calibration / Axis calibration

Track calibration has been completed for GIS robot set-up, and **should not normally need to be changed or adjusted.** It should only be redone if completely necessary, and only after speaking with one of the individuals managing this repo (Jingwen Wang, Marirena Kladeftira, Joseph Tannous, or Alexandra Pittiglio)! The robot's external linear track can be a useful tool to extend the reach and capabilities of the system. This is the process through which a robot's external linear track / rail is calibrated to ensure accurate positioning and movement. 

**STEP-BY-STEP:**
Main menu --> Calibration --> Track --> Base Frame --> 3-points --> Modify Position (REPEAT 3 TIMES) --> Save Positions
![PAGE 27](https://github.com/GIS-EPFL/Robots/assets/14881383/c16326eb-4039-47dd-ac1f-a554347d7ee0)

## **IV.** Update in URDF (Alex)

1. Get quaternion values from Robotstudio
     ![robotstudio_axis_calibration](https://github.com/GIS-EPFL/Robots/assets/91248123/9a07bf4c-0c0c-4dae-9579-f0b5070a409d)
2. Calculate from Euler angles from quaternion 
     - The calculation file is in robot_files\abb_irb_6700_track_irtb_6004\5_playgrounds\python\calibration_rpy.py

3. Input Euler angles into URDF for robot motion planning
     - robot_files\abb_irb_6700_track_irtb_6004\4_urdfs\abb_irbt6004_670_support\urdf\abb_irb6700_175_305_ibois.xacro
     - empty files in robot_files\abb_irb_6700_track_irtb_6004\4_urdfs\abb_irbt6004_670_moveit_config
     - create moveit package (refer to **Section 3**)

# **Section 2** - IRBT-6700  Dual Robot Calibration (Marirena)

I have a little suggestion, can the image in this chapter to be more compacted when you have time? so they won't occupy so much space in a page. (Jingwen)

## **I.** 8 Point calibration method

1. Finish the axis calibration for each robot you want to use collaboratively as described in the steps above. (Technically this is already finished. You can obtain the Euler angle values from folder abb_irb_track_irtb_6004 and abb_irb_track_irtb_6004_iris, refer to Section 1 IV). IRBT 6700 two robots are named as Aurora and Iris (Facing north, left is Aurora and right is Iris). 

2. Mount a "pin tool" on each robot so you can measure the points accurately. There are two pins available in GIS that you can use.
    <img width="574" alt="pins" src="https://github.com/GIS-EPFL/Robots/assets/22766174/9f3e3cb6-77df-41a8-a17c-74883bce9ea9">

4. Set tool as the corresponding pintool (e.g. screwPin for the threaded pin, or pencil for the wooden pencil in the picture)
    <img width="574" alt="pinTool" src="https://github.com/GIS-EPFL/Robots/assets/22766174/6c0f20da-6777-409c-8fc8-f2e87fd87c22">

4. Set coordinate system to base

6. Get the precision camera and the laptop that contains the software from CRCL. This is a custom equipment with two micro cameras to help you reach the same point with the two robots precisely. (refer to **Section1 II**)
    <img width="574" alt="camera" src="https://github.com/GIS-EPFL/Robots/assets/22766174/199a2f2c-ff50-4bd2-b2fb-937eeb4904eb">

6. Consider 8 points that you want to measure with the two robots. Keep in mind that in the area where the 8 points are measured the urdf will be most accurate, so try to disperse them in the area of reach of both robots. (Mathematically you only need three points to calculate the transformation matrix, we decided to use 8 to minimize the error.)

7. For each point you place this camera at jog one robot first in place until you see the tip well in the target area. Write down the position of the robot at that point. Repeat for the second robot. Move to the next point until you have measured all 8 points with both robots.

9. Navigate to the following following directory <your_local_directory>/Robots/robot_files/<new_setup(new_setup>(in this case abb_irb_6700_track_irtb_6004_2x)/5_playgrounds and open or create a calibration file. You can find it in this repo with the name "dual_robot_calibration.py".
   Replace the values that you measured with the two robots for the 8 points in the matrix as seen below:
    <img width="574" alt="measured_pts" src="https://github.com/GIS-EPFL/Robots/assets/22766174/6a0b3c07-e774-47ec-9eac-e338e00f276b">

   Run the script on your editor to calculate the transformation matrix and see the error. Copy the parameter on your console as seen in the picture bellow and paste it in the "param" variable in the script. (Those value is estimated based on average method, the error is based on min squared error. We use those values as the starting point of the optimization.)
    <img width="574" alt="param" src="https://github.com/GIS-EPFL/Robots/assets/22766174/7735c864-9a8a-43e6-84b7-1dfee42dad8f">

   Re-run the script, and if the optimization method reduce the min square errors. If yes, use the top parameters instead of the bottom parameters. 
   
   (Screenshot)
   
   By far we only calculated the transformation matrix between two coordinate system. But the track axis of the robot also need to add on to that transformation matrix so that robot can be located to the right location. So we need to go to step 9. 
   
   (I suggest to add a picture to explain those transformation  Jingwen... let me know if this is too complicated or not)
   
9. Calculate combined transformation of two robot and axis transformation with the script

    robot_files\abb_irb_6700_track_irtb_6004_2x\5_playgrounds\axis_calibration.py

    To be noticed, here **rob_1 is Iris. rob_2 is Aurora.**

    Basically here we are calculating the relative transformation matrix or Aurora relatively to Iris. 

##  **II.** Update URDF

- Update URDF
  - Empty the folder <your_local_directory>\robot_files\abb_irb_6700_track_irtb_6004_2x\4_urdfs\abb_irbt6004_670_tworobots_moveit_config
  - Update the robot_files\abb_irb_6700_track_irtb_6004_2x\4_urdfs\abb_irbt6004_670_support\urdf\abb_irb6700_175_305_ibois_tworobots.xacro with the value you already calculated from 10 and from previous track calibration
  - rob_1 is Iris. rob_2 is Aurora
  - rob_1 values should consider track calibration of Iris, rob_2 valuse should use the one from Step 9
- Create moveit package from URDF (refer to **Section 3**)

# **Section 3** - Create moveit package from URDF (Joseph)

To understand general knowledge about URDF, XACRO... please refer to
[General Knowledge](https://github.com/GIS-EPFL/Robots/blob/main/robot_files/General%20Knowledge.md)

1. Update URDF as described in **Section 1 IV / 2 II** 
2. Empty the folder 4_urdfs\abb_irbt6004_670_moveit_config
3. Change the docker yml file 4_urdfs\docker-compose_for_the_use_of_simulation.yml, comment out moveit-service, uncomment moveit-service-setup-assistant
4. Open docker container (clean up existing containers if necessary, one screenshot here)
5. Open Xlaunch / Xming app as the background (acting as GUI for listening to Linux virtual machine in docker ) 
6. Compose up the yml file (remember to open yml file with GISROBOTS, as it refers to many other folders) (Screenshot)
7. https://gramaziokohler.github.io/compas_fab/0.11.0/examples/03_backends_ros/08_ros_create_moveit_package_from_custom_urdf.html
8. For one robot
   - Generate Self-Collision Matrix - > will become SRDF file
   - Add Virtual Joints
   - Generate planning group
     - "manipulator" | "arm_track" (briefly explain the difference)
     - Kinematic Solver: kdl
     - Group Default Planer
     - Add components to group - Add Kin. Chain 
     - Can be checked with srdf file later. (Screenshot)

   - End Effectors, Passive Joints (skip)
   - Author Information (do not put any special symbols such as "&" there)
   - Generate Configuration Files: Select the mapped moveit config folder

9. For two robot
   - Generate Self-Collision Matrix - > will become SRDF file
   - Add Virtual Joints
   - Generate planning group
     - "rob1" | "rob1_track" | "rob2" | "rob2_track" (briefly explain the difference)
     - Kinematic Solver: kdl
     - Group Default Planer
     - Add components to group - Add Kin. Chain 
     - Can be checked with srdf file later. (Screenshot)
   - End Effectors, Passive Joints (skip)
   - Author Information (do not put any special symbols such as "&" there)
   - Generate Configuration Files: Select the mapped moveit config folder

10. Compose down
11. Uncomment moveit-service, comment out moveit-service-setup-assistant
12. Put RVIZ as true, compose up as quick check (screenshot)
13. Put RVIZ as false save everything
14. Create yml files for simulation and file for use for real robots (abb driver is there or not)
15. (Optional) You can already use the above files for everything you need. But if you prefer to work with cleaner folder structure, you can combine XXX_moveit_config with XXX_support. Just copy /meshes /urdf folder from /support to /moveit_config, change all the reference to /support folder to /_moveit_config folder, delete the mapping address in yml file. It's a bit of work but it looks cleaner. 
16. You can now use the moveit package, compose up with docker and play around with grasshopper file in 5_playgrounds, do not forget to compuse down everytime when you finish your work
