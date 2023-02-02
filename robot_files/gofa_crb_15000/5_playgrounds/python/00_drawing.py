import compas_rrc as rrc
import compas
import os

HERE = os.path.dirname(__file__)
DATA = os.path.abspath(os.path.join(HERE, '..', 'data'))
file_name = DATA + "/"+ "20230202_cobot.json"
frames = compas.json_load(file_name)

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Set tool
    abb.send(rrc.SetTool('tool0'))

    # Set work object
    abb.send(rrc.SetWorkObject('wobj0'))

    # Read current frame position
    frame = abb.send_and_wait(rrc.GetFrame())

    # Print received values
    print(frame)

    # Set speed [mm/s]
    speed = 100


    for f in frames:
        done = abb.send_and_wait(rrc.MoveToFrame(f, speed, rrc.Zone.Z20, rrc.Motion.LINEAR))

        # Print feedback 
        print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
