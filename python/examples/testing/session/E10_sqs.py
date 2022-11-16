import boto3


class SQSClient:
    def __init__(self, client):
        self.client = client

    def receive_message(self, queue_url: str):
        return self.client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
        )


if __name__ == "__main__":
    client = boto3.client("sqs")
    resp = SQSClient(client=client).receive_message("example-queue")
    print(resp)
