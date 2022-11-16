from __future__ import annotations

from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth

VIDEO_BUCKET = "video-backup.arjancodes.com"
REGION = "eu-west-1c"


def create_cloud_provider(region: str = REGION) -> CloudProvider:
    authentication = GoogleAuth("service_key.json")
    return CloudProvider(
        region=region,
        http_auth=authentication,
        secure=True,
    )


def find_files(
    cloud_provider: CloudProvider,
    bucket_name: str,
    query: str,
    max_result: int,
) -> list[str]:
    response = cloud_provider.filter_by_query(
        bucket=bucket_name, query=query, max=max_result
    )
    return response["result"]["data"][0]
