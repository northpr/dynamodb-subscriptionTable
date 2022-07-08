import json
from helper import Helper

hlp = Helper()


def lambda_handler(event, context):
    dynamodb, table = hlp.connect_dynamodb("SUBSCRIBE_TABLE")
    subscribers = json.loads(event['body'])

    # To check the body is match the format or not
    if not hlp.validate_body(subscribers):
        return hlp.json_error("Validation failed.")

    added_item = table.update_item(
        Key={
            'PK': subscribers['PK'],
            'SK': subscribers['SK']
        },
        UpdateExpression="set #N=:n, #D=:d, #A=:a",
        ExpressionAttributeNames={
            "#N": "Name",
            "#D": "Description",
            "#A": "Author"
        },
        ExpressionAttributeValues={
            ":n": subscribers['Name'],
            ":d": subscribers['Description'],
            ":a": subscribers['Author']
        },
        ReturnValues="UPDATED_NEW"

    )

    if added_item['ResponseMetadata']['HTTPStatusCode'] == 200:
        return hlp.json_success(json.dumps(subscribers))
    else:
        return hlp.json_error("Cannot create items")
