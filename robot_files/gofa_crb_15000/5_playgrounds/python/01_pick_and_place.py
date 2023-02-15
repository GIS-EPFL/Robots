import compas_rrc as rrc
import os
from helper import ProductionData
import json
import sys
import roslibpy

HERE = os.path.dirname(__file__)
DATA = os.path.abspath(os.path.join(HERE, '..', 'data'))
file_name = DATA + "/"+ "20230215_pick_and_place.json"
output_path = os.path.join(file_name + '_output.json')

PRODUCTION_LOG_CONFIG = dict(
    ENABLED=True,                       # Generate a log of received feedback
    OVERWRITE=True,                     # When True, it will create a new log file every time, otherwise, it will append to existing
    CONSOLE_OUTPUT=True,                # When True, it will print received feedback on the console
)

if __name__ == '__main__':

    #open json nd read production data
    if os.path.exists(file_name):
        print('Using production data file: {}'.format(file_name))
        with open(file_name, 'r') as fp:
            production_data = ProductionData.from_data(json.load(fp))
            #print (len(production_data.actions))
    else:
        print('Cannot find production data file: {}'.format(file_name))
        sys.exit(-1)
    
    #to receive feedback
    if PRODUCTION_LOG_CONFIG['ENABLED']:
        print('Using production output file: {}'.format(output_path))
        PRODUCTION_LOG = []

        if not PRODUCTION_LOG_CONFIG['OVERWRITE']:
            if os.path.exists(output_path):
                with open(output_path, 'r') as ofp:
                    PRODUCTION_LOG = json.load(ofp)

    def store_production_log(msg):
        PRODUCTION_LOG.append(msg)
        if PRODUCTION_LOG_CONFIG['CONSOLE_OUTPUT']:
            print(msg['instruction'], msg['feedback'], msg['float_values'], msg['feedback_id'])


    #Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    #Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    if PRODUCTION_LOG_CONFIG['ENABLED']:
        feedback = roslibpy.Topic(ros, '/rob1/robot_response', 'compas_rrc_driver/RobotMessage')
        feedback.subscribe(store_production_log)

    for i in range(len(production_data.actions)):

        action = production_data.actions[i]
        prefixed_action_class_name = '{}{}'.format("rrc.", action.name)
        instruction_type = eval(prefixed_action_class_name)

        if instruction_type is None:
            raise Exception('Cannot find implementation for instruction: {}'.format(action.name))
        instruction = instruction_type(**action.parameters)
        abb.send(instruction)

        # Store production log
    if PRODUCTION_LOG_CONFIG['ENABLED']:
        with open(output_path, 'w+') as ofp:
            json.dump(PRODUCTION_LOG, ofp, indent=2, sort_keys=True)

    #End of Code
    print('Finished')

    #Close client
    ros.close()
    ros.terminate()
