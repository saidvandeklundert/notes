import pandas as pd
import numpy as np


df = pd.read_csv("siena2018-pres.csv", index_col=0)
df.info(memory_usage="deep")

# change Bg column to something of the type Uint8:
df = df.assign(Bg=lambda df_: df_.Bg.astype("Uint8"))

df.info(memory_usage="deep")

# change multiple columns:
df = df.assign(
    Im=lambda df_: df_.Im.astype("uint8"),
    Int=lambda df_: df_.Int.astype("uint8"),
    PL=lambda df_: df_.PL.astype("uint8"),
    Prty=lambda df_: df_.Party.astype(
        "category"
    ),  # does not exist, so wil be created anew
    Party=lambda df_: df_.Party.replace({"Democratic": "D", "Republican": "R"}).astype(
        "category"
    ),  # multiple operations chained while changing the column
    new=lambda df_: df_.PL + df_.RC.astype("uint8"),  # create entirely new column
)
