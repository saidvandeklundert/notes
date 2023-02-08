from typing import List


def test_lisp_activated(cisco_configuration: List[str]) -> None:
    """
    Assert LSP is activated
    """
    assert "router lisp" in cisco_configuration
