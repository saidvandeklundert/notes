from __future__ import annotations

from dataclasses import dataclass

from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth

VIDEO_BUCKET = "video-backup.arjancodes.com"
REGION = "eu-west-1c"


def create_cloud_provider(
    region: str = REGION, bucket_name: str = VIDEO_BUCKET
) -> ACCloud:
    authentication = GoogleAuth("service_key.json")
    cloud = CloudProvider(
        region=region,
        http_auth=authentication,
        secure=True,
    )
    return ACCloud(cloud, bucket_name)


@dataclass
class ACCloud:
    cloud_provider: CloudProvider
    bucket_name: str

    def find_files(self, query: str, max_result: int) -> list[str]:
        response = self.cloud_provider.filter_by_query(
            bucket=self.bucket_name, query=query, max=max_result
        )
        return response["result"]["data"][0]
