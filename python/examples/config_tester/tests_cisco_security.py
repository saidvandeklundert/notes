from typing import List


def test_cpp_policy(cisco_configuration: List[str]) -> None:
    """
    Assert policy-map system-cpp-policy is applied
    """
    assert "policy-map system-cpp-policy" in cisco_configuration
