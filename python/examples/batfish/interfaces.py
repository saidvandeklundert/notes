"""
Working with data that was obtained as follows:

>>> df = bf.q.interfaceProperties().answer().frame()  # store everything in df
>>> df.to_csv()

"""
import pandas as pd

df = pd.read_csv("interfaces.csv")
# set standard MTU and display deviating MTU ( ~ is not)
mtu_std = df["MTU"] == 1500
df[~mtu_std]
# alternative way:
small_mtu = df["MTU"] < 1500
big_mtu = df["MTU"] > 1500
df[small_mtu | big_mtu]
# find all interfaces with MTU of 1800:
mtu_1800 = df["MTU"] == 1800
df[mtu_1800]
df[mtu_1800]["Description"]

# Check descriptions:
has_description = df["Description"].notnull()
df[has_description]

# Non-default vrf:
non_default_vrf = df["VRF"] != "default"
df[non_default_vrf]
