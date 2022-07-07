import simplejson as json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("SUBSCRIBE_TABLE")

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    path_parameters = event['pathParameters']
    deleted_item = table.delete_item(
        Key={
            "PK": path_parameters["pk"],
            "SK": path_parameters["sk"]
        }
    )
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({"message": f"Customer deleted"})
    }


