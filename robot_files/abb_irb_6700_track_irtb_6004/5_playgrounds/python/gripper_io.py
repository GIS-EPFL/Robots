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
    
    #io test
    print('light_in')
    abb.send_and_wait(rrc.SetDigital('Local_IO_0_DO1', 0), timeout=5)
    abb.send_and_wait(rrc.WaitTime(1))
    print('light')
    # Close client
    ros.close()
    ros.terminate()

