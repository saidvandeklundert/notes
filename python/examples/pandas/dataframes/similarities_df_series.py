import pandas as pd

url = "https://github.com/mattharrison/datasets/raw/master/data/siena2018-pres.csv "
df = pd.read_csv(url, index_col=0)
df.to_csv("siena2018-pres.csv", index=False)
df = pd.read_csv("siena2018-pres.csv", index_col=0)


# when reading from CSV, you will lose the type information:
df.dtypes

# viewing data:
df.head()
df.tail()
df.sample(5)


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


df = tweak_siena_pres(df)


# make a heatmap:
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(10, 10), dpi=600)
g = sns.heatmap(
    (tweak_siena_pres(df).set_index("President").iloc[:, 2:-1]),
    annot=True,
    cmap="viridis",
    ax=ax,
)
g.set_xticklabels(g.get_xticklabels(), rotation=45, fontsize=8, ha="right")
_ = plt.title("Presidential Ranking")
fig.savefig("20-pres.png", bbox_inches="tight")
