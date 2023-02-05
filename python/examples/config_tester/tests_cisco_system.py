from typing import List


def test_hostname(cisco_configuration: List[str], hostname: str) -> None:
    """
    Assert the hostname is configured for the device
    """
    assert f"hostname {hostname}" in cisco_configuration
