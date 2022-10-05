"""
python -m pytest .\test\
"""
import pytest
from network.repository.network_repository import (
    InMemmoryCache,
    DynamoDBRepository,
    SqlLiteRepo,
)
from network.network_service.network import Device, Os, Vendor
from ezaws import DynamoDB, Region


@pytest.fixture
def ddb_repo():
    return DynamoDBRepository(
        ddb_client=DynamoDB(region=Region.eu_central_1), table_name="Devices"
    )


@pytest.fixture
def in_mem_repo():
    return InMemmoryCache()


@pytest.fixture
def sql_lit_repo():
    return SqlLiteRepo()


def test_ddb_repo_list(ddb_repo):
    list_result = ddb_repo.list()
    assert isinstance(list_result, list)
    assert isinstance(list_result[0], Device)


def test_inmemmory_cache_list(in_mem_repo):

    list_result = in_mem_repo.list()

    assert list_result == [
        Device(
            id="ac591eeb-c963-435f-9e22-08242dbb53d6",
            name="r1",
            os=Os.JUNOS,
            vendor=Vendor.JUNIPER,
        ),
        Device(
            id="ac591eeb-c963-435f-9e22-08242dbb53d7",
            name="r2",
            os=Os.IOSXR,
            vendor=Vendor.CISCO,
        ),
    ]


def test_sql_lite_repo_list(sql_lit_repo):
    list_result = sql_lit_repo.list()

    assert isinstance(list_result, list)
    assert isinstance(list_result[0], Device)
