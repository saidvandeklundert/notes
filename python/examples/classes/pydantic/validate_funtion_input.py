from typing import Optional
from pydantic import validate_arguments, PositiveInt


def non_validated_get_payload(url: str, retries: PositiveInt) -> Optional[dict]:
    if url.startswith("http"):
        return {}
    return None


print(non_validated_get_payload("yolo", -1))


@validate_arguments  # 1
def validated_get_payload(url: str, retries: PositiveInt) -> Optional[dict]:
    if url.startswith("http"):
        return {}
    return None


try:
    print(validated_get_payload(23, 4))
except Exception as e:
    print("when using False, 4", e)

try:
    print(validated_get_payload("https://aws.com", -1))
except Exception as e:
    print(e)
