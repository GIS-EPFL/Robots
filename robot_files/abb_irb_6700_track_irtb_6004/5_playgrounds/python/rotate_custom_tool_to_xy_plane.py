import compas_rrc as rrc
from compas.geometry import Frame, Point, Vector


if __name__ == '__main__':

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

    # Get frame and external axes 
    frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())


    # Print received values
    print(frame, external_axes)

    # Change the x-value [mm]
    frame = Frame(Point(5055.355, 1989.710, 1507.021), Vector(0, 1, 0), Vector(1, 0,0))
    print(frame)

    # Set speed [mm/s]
    speed = 100

    # Move robot the new pos
    abb.send_and_wait(rrc.MoveToFrame(frame, speed, rrc.Zone.FINE, rrc.Motion.LINEAR))


    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')
 
    # Close client
    ros.close()
    ros.terminate()
