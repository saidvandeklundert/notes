from __future__ import annotations

from typing import Any, Callable

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


FilterFn = Callable[[str, str, int], dict[str, Any]]


def find_files(
    filter_fn: FilterFn,
    bucket_name: str,
    query: str,
    max_result: int,
) -> list[str]:
    response = filter_fn(bucket_name, query, max_result)
    return response["result"]["data"][0]
