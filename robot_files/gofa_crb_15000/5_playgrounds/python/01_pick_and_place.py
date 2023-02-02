import compas_rrc as rrc
import compas
import os
from helper import ProductionData

HERE = os.path.dirname(__file__)
DATA = os.path.abspath(os.path.join(HERE, '..', 'data'))
file_name = DATA + "/"+ "20230201_cobot.json"

production_data = ProductionData.from_data(file_name)
actions = production_data.actions

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')


    for action in actions:
        instruction = '{}{}'.format(rrc, action.name)
        abb.send(instruction)

        # Print feedback 
        print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
