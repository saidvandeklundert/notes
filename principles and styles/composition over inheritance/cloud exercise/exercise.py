from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth


class ACCloud(CloudProvider):
    def __init__(self, bucket_name: str, region: str) -> None:
        authentication = GoogleAuth("service_key.json")
        super().__init__(
            region=region,
            http_auth=authentication,
            secure=True,
        )
        self.bucket_name = bucket_name

    def find_files(self, query: str, max_result: int) -> list[str]:
        response = self.filter_by_query(
            bucket=self.bucket_name, query=query, max=max_result
        )
        return response["result"]["data"][0]


class VideoStorage(ACCloud):
    def __init__(self) -> None:
        super().__init__(
            bucket_name="video-backup.arjancodes.com",
            region="eu-west-1c",
        )
