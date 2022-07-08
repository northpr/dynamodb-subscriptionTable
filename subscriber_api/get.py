import json
from boto3.dynamodb.conditions import Key
from helper import Helper

hlp = Helper()


def lambda_handler(event, context):
    dynamodb, table = hlp.connect_dynamodb("SUBSCRIBE_TABLE")
    path_parameters = event['pathParameters']

    if not hlp.validate_pk(path_parameters['pk']):
        return hlp.json_error("Partition key is error")

    response = table.query(KeyConditionExpression=Key('PK').eq(path_parameters['pk']))

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return hlp.json_success(json.dumps(response['Items']))
    else:
        return hlp.json_error("Cannot get items")
