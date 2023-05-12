import math

from compas.geometry import Frame
from compas_fab.backends import RosClient
from compas_fab.robots import to_degrees
from compas_fab.robots import to_radians
import compas_rrc as rrc
from compas.geometry import Frame, Point, Vector
from compas.geometry import Box
from compas_fab.robots import PositionConstraint, JointConstraint, Constraint
from compas_fab.robots import BoundingVolume


def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

if __name__ == '__main__':

    ##################################################################################################
    # Initialization
    ##################################################################################################

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Print text on FlexPenant
    done = abb.send_and_wait(rrc.PrintText('Welcome to COMPAS_RRC'))

    # Set tool
    #abb.send(rrc.SetTool('tool0'))
    abb.send(rrc.SetTool('ibois_gripper_rotation'))

    # Set work object
    abb.send(rrc.SetWorkObject('wobj0'))

    ##################################################################################################
    # Movement
    ##################################################################################################

    z_safety = 750
    speed = 1000
    ##################################################################################################
    # Home Position
    ##################################################################################################
    abb.send_and_wait(rrc.SetDigital('Local_IO_0_DO1', 0), timeout=5) # open gripper
    abb.send_and_wait(rrc.WaitTime(1))
   #  pick_config = robot.inverse_kinematics(pick_frame, start_configuration, group)
   #  # Get frame and external axes 
   #  frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())

   #  # Change the x-value [mm]
   #  frame.point[2] = 1500

   #  # Move robot the new pos
   #  done = abb.send_and_wait(rrc.MoveToRobtarget(frame, external_axes, speed, rrc.Zone.FINE))


   #  # Move robot track
   #  robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())
   #  speed = 1000 # Set speed [mm/s]
   #  external_axes = [5000]
   #  done = abb.send_and_wait(rrc.MoveToJoints(robot_joints, external_axes, speed, rrc.Zone.FINE))

    ##################################################################################################
    # Go to safety z from the last position
    # Planning is required to go from any position to the safety z
    ##################################################################################################


    with RosClient("localhost") as client:
    
       robot = client.load_robot()
       group = robot.main_group_name
       frame_pick_0 = Frame(Point(7000/1000.0, 1500/1000.0, 0.564985+z_safety/1000.0),Vector(-0.260359,0.965511,-0.001113), Vector(0.96545,0.260355,0.011044)) #0.564985+



       tolerance_position = 0.001
       tolerance_axes = [math.radians(1)] * 3

       start_configuration = robot.zero_configuration()
       robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())
       angles = to_radians([robot_joints.rax_1,robot_joints.rax_2,robot_joints.rax_3,robot_joints.rax_4,robot_joints.rax_5,robot_joints.rax_6])
       start_configuration.joint_values = ( external_axes[0]/1000, angles[0],angles[1],angles[2],angles[3],angles[4],angles[5]   )
       print(start_configuration.joint_values)

       # create goal constraints from frame
       constraints = []
       box = Box(Frame(Point(3.35, 1.2, 0),Vector(1,0,0), Vector(0,1,0)), 7, 2.0, 2.0)
       pc_5_ = PositionConstraint.from_box('rob1_joint_4', box)
       pc_6_ = PositionConstraint.from_box('rob1_joint_5', box)
       jc_3_ = JointConstraint('rob1_joint_3', 10, 70, -10, 1.0)
       jc_2_ = JointConstraint('rob1_joint_2', 10, 20, -15, 1.0)

       constraints.append(pc_5_)
       constraints.append(pc_6_)
       constraints.append(jc_3_)
       constraints.append(jc_2_)
       constraints = constraints + robot.constraints_from_frame(frame_pick_0, tolerance_position, tolerance_axes, group, True)

       
       print(constraints)
       trajectory = robot.plan_motion(constraints, start_configuration, group, options=dict(planner_id="RRT"))
       
       
       print(start_configuration)
       print("Computed free-space path with %d configurations." % len(trajectory.points))
       print("Executing this path at full speed would take approx. %.3f seconds." % trajectory.time_from_start)

       print(trajectory.points[0].joint_values)

       for i in range(len(trajectory.points)):
          c = trajectory.points[i]
 
          track_position = c.joint_values[0]*1000
          joints = to_degrees(c.joint_values)
          joints.pop(0)
          speed = 500
          if i < len(trajectory.points) - 1:
                zone = rrc.Zone.Z10
          else:
                zone = rrc.Zone.FINE
          print(c.joint_values)
         
          abb.send(rrc.MoveToJoints(joints, ext_axes=[track_position], speed=speed, zone=zone))

    ##################################################################################################
    # Move robot to pick position
    ##################################################################################################

    # Move robot track
    robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())
    speed = 1000 # Set speed [mm/s]
    external_axes = [5500]
    done = abb.send_and_wait(rrc.MoveToJoints(robot_joints, external_axes, speed, rrc.Zone.FINE))

    # Change the x-value [mm]
    frame_pick_0 = Frame(Point(7000, 1500, z_safety),Vector(1,0,0), Vector(0,-1,0))
    frame_pick_1 = Frame(Point(7000, 1500, -540), Vector(1,0,0), Vector(0,-1,0))
    frame_pick_2 = Frame(Point(7000, 1500, -640), Vector(1,0,0), Vector(0,-1,0))

    speed = 1000 # Set speed [mm/s]
    abb.send_and_wait(rrc.MoveToFrame(frame_pick_0, speed, rrc.Zone.FINE, rrc.Motion.JOINT)) # pick frame z safety
    abb.send_and_wait(rrc.MoveToFrame(frame_pick_1, speed, rrc.Zone.FINE, rrc.Motion.LINEAR)) # pick frame io open position
    abb.send_and_wait(rrc.SetDigital('Local_IO_0_DO1', 0), timeout=5) # open gripper
    abb.send_and_wait(rrc.WaitTime(1))
    abb.send_and_wait(rrc.MoveToFrame(frame_pick_2, 25, rrc.Zone.FINE, rrc.Motion.LINEAR)) # pick frame io close position
    abb.send_and_wait(rrc.SetDigital('Local_IO_0_DO1', 1), timeout=5) # close gripper
    abb.send_and_wait(rrc.WaitTime(1))
    abb.send_and_wait(rrc.MoveToFrame(frame_pick_0, speed, rrc.Zone.FINE, rrc.Motion.LINEAR)) # pick frame z safety

    ##################################################################################################
    # Move robot to place position
    ##################################################################################################

    x = 4000
    y = 1650 # MIN 1100 MAX 2200
    z = -630
    x_axis = Vector(0.707107,0.707107,0)
    y_axis = Vector(0.707107,-0.707107,0)

    frame_place_0 = Frame(Point(x, y, z_safety),x_axis, y_axis)
    frame_place_1 = Frame(Point(x, y, z+500), x_axis, y_axis) # upper position before release
    frame_place_2 = Frame(Point(x, y, z), x_axis, y_axis) # target position

    frames = [frame_place_0, frame_place_1, frame_place_2]


    for i in range(1):

      with RosClient("localhost") as client:
         
            robot = client.load_robot()
            group = robot.main_group_name
            frame_place_0_fab = Frame(Point(frames[i].point[0]/1000.0, frames[i].point[1]/1000.0,  0.564985+frames[i].point[2]/1000.0),x_axis, y_axis)
            #frame_pick_0 = Frame(Point(7000/1000.0, 1500/1000.0, 0.564985+z_safety/1000.0),Vector(-0.260359,0.965511,-0.001113), Vector(0.96545,0.260355,0.011044)) #0.564985+
            robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())
            angles = to_radians([robot_joints.rax_1,robot_joints.rax_2,robot_joints.rax_3,robot_joints.rax_4,robot_joints.rax_5,robot_joints.rax_6])
            start_configuration.joint_values = ( clamp(external_axes[0]/1000-0,5.0,6.7), angles[0],angles[1],angles[2],angles[3],angles[4],angles[5]   )
            print(start_configuration.joint_values)

            # create goal constraints from frame
            constraints = []
            pc_5_ = PositionConstraint.from_box('rob1_joint_4', box)
            pc_6_ = PositionConstraint.from_box('rob1_joint_5', box)
            jc_3_ = JointConstraint('rob1_joint_3', 10, 70, -10, 1.0)
            jc_2_ = JointConstraint('rob1_joint_2', 10, 20, -15, 1.0)

            constraints.append(pc_5_)
            constraints.append(pc_6_)
            constraints.append(jc_3_)
            constraints.append(jc_2_)
            constraints = constraints + robot.constraints_from_frame(frame_place_0_fab, tolerance_position, tolerance_axes, group, True)

            trajectory = robot.plan_motion(constraints, start_configuration, group, options=dict(planner_id="RRT"))
            

            for i in range(len(trajectory.points)):
               c = trajectory.points[i]
      
               track_position = c.joint_values[0]*1000
               joints = to_degrees(c.joint_values)
               joints.pop(0)
               if i < len(trajectory.points) - 1:
                     zone = rrc.Zone.Z10
               else:
                     zone = rrc.Zone.FINE
               print(c.joint_values)
               
               abb.send(rrc.MoveToJoints(joints, ext_axes=[track_position], speed=speed, zone=zone))
         


   #  robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())
   #  external_axes = [clamp(frame_place_0.point[0]+1000,0,6700)]
   #  done = abb.send_and_wait(rrc.MoveToJoints(robot_joints, external_axes, speed, rrc.Zone.FINE))

    #abb.send_and_wait(rrc.MoveToFrame(frame_place_0, speed, rrc.Zone.FINE, rrc.Motion.JOINT)) # place frame z safety
    abb.send_and_wait(rrc.MoveToFrame(frame_place_1, speed, rrc.Zone.FINE, rrc.Motion.LINEAR)) # place frame 
    abb.send_and_wait(rrc.MoveToFrame(frame_place_2, 50, rrc.Zone.FINE, rrc.Motion.LINEAR)) # place frame 
    abb.send_and_wait(rrc.SetDigital('Local_IO_0_DO1', 0), timeout=5) # open gripper
    abb.send_and_wait(rrc.WaitTime(1))
    abb.send_and_wait(rrc.MoveToFrame(frame_place_0, speed, rrc.Zone.FINE, rrc.Motion.LINEAR)) # place frame 

    ##################################################################################################
    # End
    ##################################################################################################

    # End of Code
    print('Finished')
 
    # Close client
    ros.close()
    ros.terminate()
