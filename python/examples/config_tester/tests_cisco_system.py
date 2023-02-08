from typing import List


def test_hostname(cisco_configuration: List[str], hostname: str) -> None:
    """
    Assert the hostname is configured for the device
    """
    assert f"hostname {hostname}" in cisco_configuration


def test_ntp_loopback(cisco_configuration: List[str]) -> None:
    """
    Assert NTP traffic is properly sourced
    """
    assert "ntp source Loopback0" in cisco_configuration
