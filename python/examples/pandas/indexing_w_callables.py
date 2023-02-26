"""
You can pass a callable into the loc method of a dataframe. 

The callable will be passed the dataframe and you should return a boolean array (a list of booleans )
 that will be used to filter the dataframe.
"""
import pandas as pd
from typing import List

df = pd.read_csv("data\movies.csv")


def select_all(df: pd.DataFrame) -> List[bool]:
    """
    Select everything in the dataframe
    """
    return [True for x in range(len(df))]


df.loc[select_all]


def select_warner(df: pd.DataFrame) -> List[bool]:
    """
    Select all rows where the Stdui is "Warner Brothers"
    """
    return [x == "Warner Brothers" for x in df["Studio"]]


df.loc[select_warner]


def check_type(df: pd.DataFrame) -> List[bool]:
    """
    Raise a Value error and reveal the type that is passed into the callable.
    """

    raise ValueError(f"type {type(df)}")


df.loc[select_warner]
