import pytest
from E10_sqs import SQSClient
from moto import mock_sqs
import boto3

# this fixture is a reusable Mock:
@pytest.fixture
def sqs_client():
    with mock_sqs():
        conn = boto3.client("sqs", region_name="us-east-1")
        yield conn


# This fixture gives us the queue name:
@pytest.fixture
def queue_name():
    return "example-queue"


# we pass both fixtures into the test function so we can use them:
def test_receive_message(sqs_client, queue_name):
    # test setup:
    client = SQSClient(sqs_client)
    sqs_client.create_queue(QueueName=queue_name)
    sqs_client.send_message(QueueUrl=queue_name, MessageBody="some message")
    # actual method under test:
    response = client.receive_message(queue_url=queue_name)
    # assert the message was properly read:
    assert response["Messages"][0]["Body"] == "some message"
