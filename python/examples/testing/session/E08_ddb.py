from pprint import pprint
from ezaws import Region
from ezaws import DynamoDB
import boto3

from typing import Dict, Union


def check_table(client: boto3.client):

    result = client.scan(TableName="Humans")
    if result["Count"] == 0:
        raise ValueError("should not be 0")

    return result["Items"]


if __name__ == "__main__":
    client = boto3.client("dynamodb")
    result = check_table(client)
    pprint(result)
