from prelude import *

make

# determine cardinality of of values for the make series:
make.value_counts()

# you can also look at the items in the series and check the unique value count:
make.shape
make.nunique()

# this gives you an idea on whether or not to use categories.

# categories use a lot less memory:
cat_make = make.astype("category")
cat_make.memory_usage(deep=True)  #   95888
make.memory_usage(deep=True)  #     2606395


# you can also categorize a series and sort the categories at the same timeL
make_type = pd.CategoricalDtype(categories=sorted(make.unique()), ordered=True)
ordered_make = make.astype(make_type)

# if the items have an order, you can use reducing operations like maximum and minimum
ordered_make.max()
ordered_make.sort_values()

# categories also have a cat accessor, allowing you to easily rename the categories
# by passing in a list or dict
