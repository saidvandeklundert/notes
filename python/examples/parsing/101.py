import ast
from pprint import pprint
import inspect

# import some_lib.bgp as bgp
# source = inspect.getsource(bgp)
# pprint(ast.dump(ast.parse(source)))

tree = ast.parse(
    """
import pytest
def add(a, b):
  return a + b
"""
)
pprint(ast.dump(tree))


tree = ast.parse(
    """

@pytest.mark.ffnx
@pytest.mark.ffn
def test_ios_service_password_encryption(
    cisco_configurations_set_lan: CiscoConfigurationSet,
) -> None:
    '''
    Ensure that 'service password-encryption' is enabled for all Cisco devices.
    '''
    failures = []
    config_command = "service password-encryption"
    for configuration, hostname in cisco_configurations_set_lan:
        if config_command not in configuration:
            failures.append(f"{hostname}")

    assert len(failures) == 0, f"{config_command} not enabled everywhere: {failures}"
"""
)

pprint(ast.dump(tree))
