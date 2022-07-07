import simplejson as json
import os
import boto3
from subscriber_api.helper import Helper

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("SUBSCRIBE_TABLE")


def lambda_handler(event, context):
    subscribers = json.loads(event['body'])
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=subscribers)

    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps({"message": "Subscribers created"})
    }




