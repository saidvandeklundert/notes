"""
https://batfish.readthedocs.io/en/latest/getting_started.html

docker pull batfish/allinone
docker run --name batfish -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone
# docker start batfish
docker cp example/. batfish:/var/tmp
docker exec -it batfish bash
apt-get update
apt-get install vim
ipython
# now you are in the repl and you can run the below code by pasting it in


# copy the example config from the example dir:

"""
import pandas as pd
from pybatfish.client.session import Session
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *

# setup session with the batfish service:
bf = Session(host="localhost")
SNAPSHOT_DIR = "/var/tmp/"
SNAP_SHOT_NAME = "example_snap_new"
SNAP_SHOT_NETWORK_NAME = "example_dc"

bf.set_network(SNAP_SHOT_NETWORK_NAME)
bf.init_snapshot(SNAPSHOT_DIR, name=SNAP_SHOT_NAME, overwrite=True)
bf.set_snapshot(SNAP_SHOT_NAME)
bf.q.initIssues().answer()
bf.q.bgpPeerConfiguration().answer().frame

# show available questions:
dir(bf.q)

# understand the type of the answer:
type(bf.q.bgpPeerConfiguration().answer().frame())
# >>> <class 'pandas.core.frame.DataFrame'>   <--- Pandas dataframe!!!


"""
Parse section
"""

# parse nodes:
bf.q.nodeProperties().answer().frame()

# parse nodes that contain substring in their name:
bf.q.nodeProperties(nodes="/border/").answer().frame()

# show some data:
df = bf.q.nodeProperties().answer().frame()
df.columns  # show columns of the dataframe
df.iloc[0]  # show first row of the dataframe
df.iloc[0:5]["Hostname"]  # show hostname field for slice of rows
df.iloc[0:5][
    "Interfaces"
].values  # display configured interface names for slice of routers

"""
List undefined values:
"""
bf.q.undefinedReferences().answer().frame()
issues_answer = bf.q.initIssues().answer().frame()
issues_answer.iloc[0]
issues_answer.iloc[1]
"""
Interfaces
"""
bf.q.interfaceProperties().answer().frame()  # everything
df = bf.q.interfaceProperties().answer().frame()  # store everything in df
df.columns  # check data available for interfaces
# set standard MTU and display deviating MTU ( ~ is not)
mtu_std = df["MTU"] == 1500
df[~mtu_std]
# alternative way:
small_mtu = df["MTU"] < 1500
big_mtu = df["MTU"] > 1500
df[small_mtu | big_mtu].values
# find all interfaces with MTU of 1800:
mtu_1800 = df["MTU"] == 1800
df[mtu_1800]

# Sift through data:
df = (
    bf.q.interfaceProperties(
        interfaces="/Ethernet/",
        properties="VRF,Primary_Address,Description,Incoming_Filter_Name,Outgoing_Filter_Name",
    )
    .answer()
    .frame()
)
# list the dataframe:
df
# now everything with a filter applied to it:
df[df.Incoming_Filter_Name.notnull()]


"""
BGP
"""
parse_status = bf.q.fileParseStatus().answer().frame()

# query filters:
bf.q.findMatchingFilterLines(
    headers=HeaderConstraints(applications="DNS")
).answer().frame()


# get the result:
result = bf.q.fileParseStatus().answer().frame()
# check device state
result.iloc[0]

# check BGP:
bf.q.bgpProcessConfiguration().answer().frame()
bf.q.bgpPeerConfiguration().answer().frame().iloc[27]
