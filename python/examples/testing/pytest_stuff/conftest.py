"""
python -m pytest

conftest.py can be used to group all fixtures.

"""
import pytest
from textwrap import dedent


@pytest.fixture(scope="session")
def api_call_return() -> str:
    """Example api call returning JSON"""
    # aws sqs api call return:
    json_response = """
    {
        "ApproximateNumberOfMessages": "57",
        "ApproximateNumberOfMessagesDelayed": "0",
        "ApproximateNumberOfMessagesNotVisible": "0",
        "CreatedTimestamp": "1641811174",
        "DelaySeconds": "5",
        "LastModifiedTimestamp": "1646251633",
        "MaximumMessageSize": "262144",
        "MessageRetentionPeriod": "345600",
        "QueueArn": "arn:aws:sqs:eu-central-1:717687450252:example-queue",
        "ReceiveMessageWaitTimeSeconds": "0",
        "SqsManagedSseEnabled": "false",
        "VisibilityTimeout": "29",
    }    
    """
    return dedent(json_response)
