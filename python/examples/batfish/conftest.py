import pytest
import pybatfish
from pybatfish.client.session import Session
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *

SNAPSHOT_DIR = "example/"
SNAP_SHOT_NAME = "example_snap_new"
SNAP_SHOT_NETWORK_NAME = "example_dc"

@pytest.fixture
def bf() -> pybatfish.client.session.Session:
    """returns a BatFish session for reuse throughtout the tests."""
    bf = Session(host="localhost")
    bf.set_network(SNAP_SHOT_NETWORK_NAME)
    bf.init_snapshot(SNAPSHOT_DIR, name=SNAP_SHOT_NAME, overwrite=True)
    bf.set_snapshot(SNAP_SHOT_NAME)
    return bf
