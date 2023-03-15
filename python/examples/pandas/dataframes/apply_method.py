import pandas as pd
import numpy as np


df = pd.read_csv("siena2018-pres.csv", index_col=0)


def tweak_siena_pres(df):
    def int64_to_uint8(df_):
        cols = df_.select_dtypes("int64")
        return df_.astype({col: "uint8" for col in cols})

    return (
        df.rename(columns={"Seq.": "Seq"})
        # 1
        .rename(
            columns={
                k: v.replace(" ", "_")
                for k, v in {
                    "Bg ": "Background",
                    "PL ": "Party leadership",
                    "CAb ": "Communication ability",
                    "RC ": "Relations with Congress",
                    "CAp ": "Court appointments",
                    "HE ": "Handling of economy",
                    "L": "Luck",
                    "AC ": "Ability to compromise",
                    "WR ": "Willing to take risks",
                    "EAp ": "Executive appointments",
                    "OA ": "Overall ability",
                    "Im ": "Imagination",
                    "DA ": "Domestic accomplishments",
                    "Int ": "Integrity",
                    "EAb ": "Executive ability",
                    "FPA ": "Foreign policy accomplishments",
                    "LA ": "Leadership ability",
                    "IQ ": "Intelligence",
                    "AM ": "Avoid crucial mistakes",
                    "EV ": "Experts ' view",
                    "O": "Overall",
                }.items()
            }
        ).astype({"Party": "category"})
        # 2
        .pipe(int64_to_uint8)
        # 3
        .assign(
            Average_rank=lambda df_: (
                df_.select_dtypes("uint8")  # 4
                .sum(axis=1)
                .rank(method="dense")
                .astype("uint8")
            ),
            Quartile=lambda df_: pd.qcut(
                df_.Average_rank, 4, labels="1st 2nd 3rd 4th".split()
            ),
        )
    )


pres = tweak_siena_pres(df)

# preferred over apply:
pres.select_dtypes("number").pipe(
    lambda df_: df_.max(axis="columns") - df_.min(axis="columns")
)


# some examples using apply:
pres.select_dtypes("number").apply(lambda row: row.max() - row.min(), axis="columns")

pres.apply(lambda row: row.President + " san", axis="columns")


def apply_to_columns(row: pd.Series) -> pd.Series:
    """
    This function is applied to each column in a dataframe
    """
    print(row)
    print(type(row))
    if row.Party == "Democratic":
        row.Party = "D"
        row.President = "D " + row.President
    if row.Party == "Republican":
        row.Party = "R"
        row.President = "R " + row.President
    return row


pres = pres.apply(apply_to_columns, axis="columns")


def apply_to_index(s: pd.Series) -> pd.Series:
    """
    Using apply accross the index will apply
    the function to every column.

    The column is passed in the function as a Series.
    """
    print(s)
    print(type(s))
    return s


pres = pres.apply(apply_to_index, axis="index")
