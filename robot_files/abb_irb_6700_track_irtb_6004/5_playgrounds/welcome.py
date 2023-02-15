import compas_rrc as rrc

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
    abb.send(rrc.SetTool('tool0'))

    # Set work object
    abb.send(rrc.SetWorkObject('wobj0'))

    # Read current frame position
    #frame = abb.send_and_wait(rrc.GetFrame())

    # Change the x-value [mm]
    #frame.point[0] -= 50

    # Set speed [mm/s]
    #speed = 100
    
    # Move robot the new pos
    #done = abb.send_and_wait(rrc.MoveToFrame(frame, speed, rrc.Zone.FINE, rrc.Motion.LINEAR))

    # Move robot the new pos
    #done = abb.send_and_wait(rrc.MoveToTarget(frame, speed, rrc.Zone.FINE, rrc.Motion.LINEAR))

    # Get frame and external axes 
    frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())

    # Print received values
    print(frame, external_axes)

    # Print received values
    print(frame)

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
