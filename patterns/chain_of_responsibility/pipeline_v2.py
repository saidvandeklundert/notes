from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, Union


class Check(ABC):
    _next_handler: Union[Check, None] = None

    @abstractmethod
    def set_next(self, handler: Check) -> Check:
        pass

    @abstractmethod
    def execute_check(self, request) -> Optional[str]:
        pass

    def is_final(self) -> bool:
        if self._next_handler is None:
            return True
        else:
            return False

    def get_next(self) -> Union[Check, None]:
        return self._next_handler


class AbstractCheck(Check):
    """
    The default pipeline of checks.
    """

    def set_next(self, handler: Check) -> Check:
        self._next_handler = handler

        return handler

    @abstractmethod
    def execute_check(self, context: Any) -> str:
        if self._next_handler:
            return self._next_handler.execute_check(context)

        return None


"""
Checks
"""


class BGPSummary(AbstractCheck):
    def execute_check(self, context: Any) -> str:
        print("show ip bgp summary")
        context["bgp result"] = True
        return "bgp result"


class Interface(AbstractCheck):
    def execute_check(self, context: Any) -> str:
        print("show ip int brief")
        context["interface result"] = True
        return "interface result"


class LACP(AbstractCheck):
    def execute_check(self, context: Any) -> str:
        print("show interfaces")
        context["lacp result"] = True
        return "lacp result"


class OSPF(AbstractCheck):
    def execute_check(self, context: Any) -> None:
        print("show ip ospf neighbors")
        context["ospf result"] = True


def pipeline_runner(chain_of_checks: Union[Check, None]) -> dict:
    """
    Runs a pipeline of checks
    """
    context = {"context": True}
    while chain_of_checks:
        chain_of_checks.execute_check(context)

        chain_of_checks = chain_of_checks.get_next()
    return context


if __name__ == "__main__":
    bgp = BGPSummary()
    interface = Interface()
    lacp = LACP()
    ospf = OSPF()
    ospf_1 = OSPF()
    ospf_2 = OSPF()
    ospf_3 = OSPF()
    ospf_4 = OSPF()
    ospf_5 = OSPF()

    bgp.set_next(interface)
    interface.set_next(lacp)
    lacp.set_next(ospf)

    result = pipeline_runner(bgp)
    print(result)
