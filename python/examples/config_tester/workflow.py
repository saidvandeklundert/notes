"""
python -m mypy .
python .\workflow.py  
"""
from __future__ import annotations

from typing import List
import tests_cisco_system
import tests_cisco_lisp
import tests_cisco_security
from interfaces import Test, TestSequence, TestContext


class TestSystem(Test):
    def __init__(self, context: TestContext):
        self.context = context

    def run_tests(self) -> None:
        print(f"making asserting for {self.context.hostname}")
        tests_cisco_system.test_hostname(
            self.context.configuration_lines, self.context.hostname
        )
        tests_cisco_system.test_ntp_loopback(self.context.configuration_lines)


class TestLISP(Test):
    def __init__(self, context: TestContext):
        self.context = context

    def run_tests(self) -> None:

        tests_cisco_lisp.test_lisp_activated(
            self.context.configuration_lines,
        )


class TestSecurity(Test):
    def __init__(self, context: TestContext):
        self.context = context

    def run_tests(self) -> None:

        tests_cisco_security.test_cpp_policy(
            self.context.configuration_lines,
        )


class CiscoTestSequence(TestSequence):
    def __init__(self, context: TestContext):
        self.context = context

    def get_tests(self) -> List[Test]:
        return [
            TestSystem(context=self.context),
            TestLISP(context=self.context),
            TestSecurity(context=self.context),
        ]


if __name__ == "__main__":
    with open("private/configs/den4-fc-dis-r-2-1.cfg", "rt") as f:
        cisco_config = f.read()
    context = TestContext(hostname="den4-fc-dis-r-2-1", configuration=cisco_config)
    wf = CiscoTestSequence(context)
    wf.execute_tests()
