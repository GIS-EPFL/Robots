# Tutorials

## Create Environment

to create from scratch: 
```bash
conda env create -f environment.yml
```

to update the environment:
```bash
conda env update --name myenv --file environment.yml --prune
```

update with environment activated:
```bash
conda env update --file environment.yml --prune
```

## Axis Alignment and Default Orientation of the Robot

When robots axes are aligned, meaning all angles are set to zero the robot looks like the image below. Moving to this position might be needed when the batteries of the robot are out-of charge. (To-Do: write a procedure of teach-pendant what has to be done to reset the memore of the robot when the batteries are out of charge )

![1676553389308](image/ReadMe/1676553389308.png)

## Heights of the Ground | Rail | Pedestal |

The top of the pedestal is the robot Origin: 0.00 mm

The top mounting plate of the rail is the pedestal Origin: - 250 mm

The floor, even if it is not completely flat Origin: - 700 mm

![1676553962521](image/ReadMe/1676553962521.png)

## Control of the Robot using Teach Pendant

### Create | Change Tool

Temp

### Create WorkObject

Temp

### Movements: Linear | Axis | Tool | Speed | Home position

Temp
