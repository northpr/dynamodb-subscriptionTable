import json
from helper import Helper

hlp = Helper()


def lambda_handler(event, context):
    dynamodb, table = hlp.connect_dynamodb("SUBSCRIBE_TABLE")
    subscribers = json.loads(event['body'])

    # Validate the partition key
    if not hlp.validate_pk(subscribers['PK']):  # if function is false it will return
        return hlp.json_error("Partition key is error")

    # To check the body is match the format or not
    if not hlp.validate_body(subscribers):
        return hlp.json_error("Validation failed.")

    response = table.put_item(Item=subscribers)

    # return {
    #     "statusCode": 201,
    #     "headers": {},
    #     "body": json.dumps({"message": "Subscribers created"})
    # }
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return hlp.json_success(json.dumps(subscribers))
    else:
        return hlp.json_error("Cannot create items")



