from test_08_ddb_data import WITH_DATA, WITHOUT_DATA, EXPECTED_RESULT
import E08_ddb
import pytest
from unittest import mock

# TODO: look into MOTO


def test_check_table_no_data():
    client = mock.Mock()
    client.scan = mock.Mock()
    client.scan.return_value = WITHOUT_DATA

    with pytest.raises(ValueError):
        E08_ddb.check_table(client)


def test_check_table_with_data():
    client = mock.Mock()
    client.scan = mock.Mock()
    client.scan.return_value = WITH_DATA

    result = E08_ddb.check_table(client)
    assert result == EXPECTED_RESULT
