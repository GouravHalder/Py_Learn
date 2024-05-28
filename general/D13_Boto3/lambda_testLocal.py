import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Bombieeee!')
    }

# Mock event and context
mock_event = {}
mock_context = {}

# Call the handler and print the response
response = lambda_handler(mock_event, mock_context)
print(response)