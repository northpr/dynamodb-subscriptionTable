import json
from helper import Helper

hlp = Helper()


def lambda_handler(event, context):
    dynamodb, table = hlp.connect_dynamodb("SUBSCRIBE_TABLE")
    path_parameters = event['pathParameters']

    # # Validate the partition and sort key
    # if not hlp.validate_pk(path_parameters['pk']):
    #     return hlp.json_error("Partition key is not match the format")
    # if not hlp.validate_sk(path_parameters['sk']):
    #     return hlp.json_error("Sort key is not match the format")

    deleted_item = table.delete_item(
        Key={
            "PK": path_parameters["pk"],
            "SK": path_parameters["sk"]
        }
    )
    if deleted_item['ResponseMetadata']['HTTPStatusCode'] == 200:
        return hlp.json_success("Item deleted")
    else:
        return hlp.json_error("Cannot delete items")


