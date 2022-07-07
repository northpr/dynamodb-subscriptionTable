import simplejson as json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("SUBSCRIBE_TABLE")


def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    subscribers = json.loads(event['body'])

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

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({"message": "Subscriber Updated}"})
    }
