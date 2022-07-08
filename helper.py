import json
import boto3
import os


class Helper:
    """
    Helper functions to help check the string of json from post function
    """

    # Check the value is a string
    @staticmethod
    def __is_string(value):
        if isinstance(value, str):
            return True
        else:
            return False

    # Check the value is greater than char count
    @staticmethod
    def __has_char_count(value, num=0):
        if len(value) >= num:
            return True
        else:
            return False

    # Validate the dictionary body
    def validate_body(self, dict_event: dict):
        keys = dict_event.keys()
        body_valid = True

        # Check the keys are in dict_event
        required = {"PK", "SK", "Name", "Description", "Author"}
        for key in required:
            if key not in keys:
                body_valid = False

        # Validation
        body_valid = self.__is_string(dict_event['PK'])
        body_valid = self.__has_char_count(dict_event['PK'], 4)
        body_valid = self.__is_string(dict_event['SK'])
        body_valid = self.__has_char_count(dict_event['SK'], 4)
        body_valid = self.__is_string(dict_event['Name'])
        body_valid = self.__is_string(dict_event['Description'])
        body_valid = self.__is_string(dict_event['Author'])

        return body_valid

    # Connect to table of dynamodb server by insert a table_name
    @staticmethod
    def connect_dynamodb(table_name: str):
        dynamodb = boto3.resource("dynamodb")
        table_name = os.environ.get(table_name)
        table = dynamodb.Table(table_name)
        return dynamodb, table

    # Check if the partition key name starts with a "U"
    @staticmethod
    def validate_pk(pk):
        if not pk.startswith("U"):
            return False
        else:
            return True

    # Check if the sort key name starts with a "C"
    @staticmethod
    def validate_sk(sk):
        if not sk.startswith("C"):
            return False
        else:
            return True

    # Throwing json error back
    @staticmethod
    def json_error(message: str):
        return {
            "statusCode": 403,
            "body": json.dumps({"message": message})
        }

    # Throwing json success message
    @staticmethod
    def json_success(dict_event):
        return {
            "statusCode": 200,
            "body": dict_event
        }
