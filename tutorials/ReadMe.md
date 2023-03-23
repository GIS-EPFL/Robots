Last updated: 2023_03_17 by Petras Vestartas

# Tutorials

## Software

Follow the instructions below:
- [X] [ABB6700 + Track Connect to the robot and check a basic movement](https://github.com/GIS-EPFL/Robots/tree/main/robot_files/abb_irb_6700_track_irtb_6004)

## Robot Model Technical Specifications

### Axis Alignment and Default Orientation of the Robot

When robots axes are aligned, meaning all angles are set to zero the robot looks like the image below. Moving to this position might be needed when the batteries of the robot are out-of charge. (To-Do: write a procedure of teach-pendant what has to be done to reset the memory of the robot when the batteries are out of charge )

![1676553389308](image/ReadMe/1676553389308.png)

### Heights of the Ground | Rail | Pedestal |

The top of the pedestal is the robot Origin: **0.00 mm**

The top mounting plate of the rail is the pedestal Origin: **-250 mm**

The floor, even if it is not completely flat Origin: **-700 mm**

![1676553962521](image/ReadMe/1676553962521.png)

## Teach Pendant

### Turn On/Off

Switch the handle and plug the ethernet cable to the controller and your pc.
Then you should see on the teach pendant a similar view on the right side:

![on_off](https://user-images.githubusercontent.com/18013985/225984329-56f43016-a6f9-4e6f-adf7-cc0670f27ddd.jpg)


### Movements: Linear | Axis | Tool

For jogging go to the following menu:
![jogging_menu](https://user-images.githubusercontent.com/18013985/225979059-431a4fcb-7fd9-4ebc-9030-1f43d4b99720.jpg)

Track has only one direction:
![20230209_094307](https://user-images.githubusercontent.com/18013985/225979146-65525091-7adf-4d52-9f72-df013cd666d7.jpg)

Movement type can be changed between a track and a robot. To switch between the two, follow the process below:
![Movement](https://user-images.githubusercontent.com/18013985/225983975-a22513bc-b423-4fd5-a185-2268fb997702.jpg)


There are two white buttons in the middle right of the teach:
a) the first one allows to change the robot movement between a tool and cartesian linear axis movements
b) and the one below allows to move the robot axis by axis.

![MovementTypes](https://user-images.githubusercontent.com/18013985/225982691-c6d79932-86ce-4187-a432-6fc942160425.jpg)


### Default Tool - CRCL robot
* t_RRC_Act 

### Create Tool

https://vimeo.com/809136839


### Change Tool

https://vimeo.com/809137342

### Create and Change WorkObject

https://vimeo.com/809137450

### Movements: Speed

https://vimeo.com/809137684

### Movements: Home position

https://vimeo.com/809137558

### IOs

Temp
