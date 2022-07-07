import simplejson as json
import os
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("SUBSCRIBE_TABLE")


def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    path_parameters = event['pathParameters']
    response = table.query(KeyConditionExpression=Key('PK').eq(path_parameters['pk']))

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }
