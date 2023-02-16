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

    # Get frame and external axes 
    frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())

    # Print received values
    print(frame, external_axes)

    # Change the x-value [mm]
    frame.point[0] -= 100

    # Set speed [mm/s]
    speed = 100

    # Move robot the new pos
    done = abb.send_and_wait(rrc.MoveToRobtarget(frame, external_axes, speed, rrc.Zone.FINE))

    # Print feedback 
    print('Feedback = ', done)

    # End of Code
    print('Finished')
 
    # Close client
    ros.close()
    ros.terminate()
