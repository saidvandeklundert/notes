"""

Data gathered from a Batfish snapshot and stored as CSV.

Some example test cases written for use with pytest.

Data was gathered like this:
>>> import pandas as pd
>>> from pybatfish.client.session import Session
>>> from pybatfish.datamodel import *
>>> from pybatfish.datamodel.answer import *
>>> from pybatfish.datamodel.flow import *
>>> bf = Session(host="localhost")
>>> SNAPSHOT_DIR = "/var/tmp/"
>>> SNAP_SHOT_NAME = "example_snap_new"
>>> SNAP_SHOT_NETWORK_NAME = "example_dc"

>>> bf.set_network(SNAP_SHOT_NETWORK_NAME)
>>> bf.init_snapshot(SNAPSHOT_DIR, name=SNAP_SHOT_NAME, overwrite=True)
>>> bf.set_snapshot(SNAP_SHOT_NAME)

>>> df = bf.q.bgpProcessConfiguration().answer().frame()
>>> df.to_csv("bgp_process_configuration.csv")
>>> df = bf.q.bgpPeerConfiguration().answer().frame()
>>> df.to_csv("bgp_peer_configuration.csv")

Run these tests:
    python -m pytest test_bgp_configuration.py 
"""
import pandas as pd
import pytest


@pytest.fixture
def peer_conf():
    peer_conf: pd.DataFrame = pd.read_csv("bgp_peer_configuration.csv")
    return peer_conf


@pytest.fixture
def process_conf():
    process_conf: pd.DataFrame = pd.read_csv("bgp_process_configuration.csv")
    return process_conf


@pytest.fixture
def different_as(peer_conf):
    """Dataframe with peers residing in different autonomous systems."""
    diff_as = peer_conf["Local_AS"] != peer_conf["Remote_AS"]
    return peer_conf[diff_as]


def test_external_peers_no_empty_import_policies(different_as):
    """
    Check if there are BGP sessions with differing AS-numbers that
     have no import policy applied.
    """
    no_import_policy = different_as["Import_Policy"] == "[]"
    df = different_as[no_import_policy]
    offending_peers = df[["Node", "Remote_IP"]]
    assert df.empty, f"eBGP sessions without import policy:\n{offending_peers}"


def test_send_community_border_false():
    pass