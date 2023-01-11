# Instructions

## abb_experimental
- [x] Clone repo "abb_experimental" https://github.com/ros-industrial/abb_experimental
- [x] Copy similar model and change names to 6700_175_305 (two urdf xacro files )
- [x] Create .stl files for 3 links -> C:\IBOIS57\_Code\Software\abb_experimental\abb_irb6700_support\meshes\irb6700_175_305\visual
- [x] Create .stl files for low poly geometry -> C:\IBOIS57\_Code\Software\abb_experimental\abb_irb6700_support\meshes\irb6700_175_305\collision
- [x] Coordinates of each axis file -> C:\IBOIS57\_Code\Software\abb_experimental\abb_irb6700_support\urdf\irb6700_175_305.xacro
- [x] finish up the moveit config (https://gramaziokohler.github.io/compas_fab/latest/examples/03_backends_ros/08_ros_create_moveit_package_from_custom_urdf.html):
- **start** - reference file: C:\IBOIS57\_Code\Software\abb_experimental\abb_irb6700_support\urdf\irb6700_175_305_macro 
- **self-collisions** - skip
- **virtual joints** - Virtual joint Name: "fixed_base", Parent Frame name: "world"
![image](https://user-images.githubusercontent.com/18013985/192543916-040d7de3-dc76-480f-bd76-95a5801e95f9.png)
- **planning groups** - from base_link to tool_0
![image](https://user-images.githubusercontent.com/18013985/192544174-a5477d88-d830-4050-b4dc-3b4d705f1370.png)
- **robot poses** - Pose name: "home", Group name: "manipulator"
![image](https://user-images.githubusercontent.com/18013985/192544498-38e19e6b-b1c3-402e-8cff-1aa3f156a724.png)
- **end effectors** - skip
- **passive joints** - skip
- **author information** - write name and email
- **configuration files** - "/root/catkin_ws/src/abb_experimental/abb_irb6700_175_305_moveit_config" , then click generate package and manually place outside the 
![image](https://user-images.githubusercontent.com/18013985/192545130-f119ad45-5630-49b8-8178-0c5dd059a082.png)
- [x] Add the 3 lines in the docker.yml
![image](https://user-images.githubusercontent.com/18013985/192538639-b5f09ea0-ba8c-4dfe-8b3c-94aa807c12ab.png)
- [x] check if the package is running in compas_fab, mainly you need to check if meshes are correctly rotating:
![image](https://user-images.githubusercontent.com/18013985/192539156-75078ff9-8c96-4450-b0e9-093a2f1fe3b2.png)

- [x] cross check results of the IK solver against the values of RobotStudio (this could be done programmatically, using compas_fab to calculate IK solutions from frames and then using compas_rrc to control a RobotStudio virtual controller and verify that both are a match).
- [ ] submit a pull request to ROS-Industrial to add the new model to the upstream abb_experimental repository.

## Linear track
- [x] create a new urdf in vs code and moveit: abb_irbt6004_670_support 
- [x] the mesh of the track has to load

## Two robots + track
- [x] setting up urdf 

## compas custom repository for IBOIS robot control
- [x] create repository "COMPAS_ABB6700_IRBT" -> https://github.com/ibois-epfl/COMPAS_ABB6700_IRBT/blob/main/docker-compose.yml
- [x] create file docker-compose.yml
- [x] install XLaunch, by download from 
- [x] compose docker, now the move it should open: https://sourceforge.net/projects/vcxsrv/
![image](https://user-images.githubusercontent.com/18013985/191273672-6817796f-10f3-4169-b961-9572e6b9f511.png)
- [x] create a new support package for the linear axis + the robot mounted on it
- [ ] reduce mesh size for the track and the robot

## robot studio
- [ ] setup a meeting with Fleischmann Philippe <fleischmann@arch.ethz.ch and put cc Gonzalo Casas for the robot studio

## Errors: 
- [ ] piston axis is wrong:
![image](https://user-images.githubusercontent.com/18013985/192549082-d218920c-ae60-4efd-a00e-5164ba056915.png)



