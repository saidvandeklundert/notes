from E01_patch import get_report
from unittest import mock


def test_get_report():
    """
    Bad test because:
    - the function takes a long time. With hundreds of tests,
     this becomes a drag.
    - we do not know the actual return value, as live database
     data varies from time to time.

    """
    return_value = get_report()
    assert return_value == "100"


@mock.patch("E01_patch.get_database_data")
def test_get_report_patched(patched_function):
    """
    This patched version:
    - tests the logic in place for the calcucations
    - runs in a few milliseconds

    Even though we are using a patch instead of the real database,
    we still cover all our business logic and we can confidently
    make changes to the calculations in our report.

    """
    patched_function.return_value = [4324, 2341, 2324, 2424]
    return_value = get_report()
    assert return_value == 2853
