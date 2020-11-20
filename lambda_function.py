import json

def lambda_handler(event, context):
    if 'body' in event.keys():
        data = json.loads(event['body'])
        if 'input' in data.keys():
            input_data = int(data['input'])
            prediction = 5 * input_data + 1
            return prediction
    else:
        return 'error'
