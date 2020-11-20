import json
import numpy as np

def lambda_handler(event, context):
    if 'body' in event.keys():
        data = json.loads(event['body'])
        if 'input' in data.keys():
            input_data = np.float(data['input'])
            prediction = 5 * input_data + 1
            return prediction
    else:
        return 'error'
