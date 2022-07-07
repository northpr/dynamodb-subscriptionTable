import simplejson as json


class Helper:
    """
    Helper functions to help check the string of json from post function
    """

    # Checking the value is a string
    def __is_string(self, value):
        if isinstance(value, str):
            return True
        else:
            return False

    # Check the value is greater than char count
    def __has_char_count(self, value, num=0):
        if len(value) >= num:
            return True
        else:
            return False

    # Check if the partition key name starts with a "U"
    def validate_pk(self, pk):
        if not pk.startswith("U"):
            return False
        else:
            return True

    # Check if the sort key name starts with a "C"
    def validate_sk(self, sk):
        if not sk.startswith("C"):
            return False
        else:
            return True

    # Throwing json error back
    def json_error(self, message):
        return {
            "statusCode": 403,
            "body": json.dumps({"message": message})
        }


