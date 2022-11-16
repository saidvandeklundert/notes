from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth
from typing import Protocol


class Authenticator(Protocol):
    def auth(self):
        ...


class CloudService(Protocol):
    def filter_by_query(self, bucket: str, query: str, max: int) -> list[str]:
        ...


class ACCloud(CloudProvider):
    def __init__(
        self,
        bucket_name: str,
        region: str,
        authenticator: Authenticator,
        cloudservice: CloudService,
    ) -> None:
        authentication = authenticator.auth()
        self.cloudservice = cloudservice(
                region=region,
                http_auth=authentication,
                secure=True,
            ),
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
