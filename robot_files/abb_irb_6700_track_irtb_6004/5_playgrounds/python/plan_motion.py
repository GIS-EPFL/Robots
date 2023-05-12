import math

from compas.geometry import Frame
from compas_fab.backends import RosClient
from compas_fab.robots import to_degrees
from compas_fab.robots import to_radians
import compas_rrc as rrc
from compas.geometry import Frame, Point, Vector


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
    z_safety = 1000
    with RosClient("localhost") as client:
        robot = client.load_robot()
        group = robot.main_group_name

        frame_pick_0 = Frame(Point(7000/1000.0, 1500/1000.0, z_safety/1000.0),Vector(1,0,0), Vector(0,-1,0))
        tolerance_position = 0.001
        tolerance_axes = [math.radians(1)] * 3

        start_configuration = robot.zero_configuration()
        robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())
        angles = to_radians([robot_joints.rax_1,robot_joints.rax_2,robot_joints.rax_3,robot_joints.rax_4,robot_joints.rax_5,robot_joints.rax_6])
        start_configuration.joint_values = ( external_axes[0]/1000, angles[0],angles[1],angles[2],angles[3],angles[4],angles[5]   )
        print(start_configuration.joint_values)

        # create goal constraints from frame
        goal_constraints = robot.constraints_from_frame(frame_pick_0, tolerance_position, tolerance_axes, group)
        trajectory = robot.plan_motion(goal_constraints, start_configuration, group, options=dict(planner_id="RRT"))

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
    # End
    ##################################################################################################

    # End of Code
    print('Finished')
 
    # Close client
    ros.close()
    ros.terminate()



