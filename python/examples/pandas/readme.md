
`Dataframe`: a datatable with columns and rows. A DataFrame is a 2-dimensional data structure that can store data of different types in columns. Every column in a DataFrame is a `Series`.

In short, a dataframe is a multicolumn data set.

`Series`: a one-dimensional labeled array capable of holding any data stype. The axis labels are referred to as the `index`. The `Series` represent a single column in a dataframe.

In short, a series is a single column data set.


### Things about types

The string is a an object since it's size is not known at compile time. THerefore, there is a pointer to the string, which does have a fixed size.


## Tips

- chain functions. You are interested in the end-result, not the intermediate steps.Put the end result under test.
- use apply for strings only. For other types, moving to the Python realm is a lot slower than using the vectorized operations.
- look at the types and see if they are optimized. For example, if you have a column of integers, you can use the `Int64` type instead of `object` (string). Also try to use categories in case there are a finite number of values.
- master aggregation
- watch out for storing data as csv as it is not very efficient as well as you cannot store actual python objects.

## Other resources

[source dode](https://github.com/pandas-dev/pandas)
[pandas excercises](https://github.com/guipsamora/pandas_exercises)
[learn pandas by doing videos](https://www.youtube.com/watch?v=pu3IpU937xs&list=PLgJhDSE2ZLxaY_DigHeiIDC1cD09rXgJv)

[storing data](https://berthub.eu/articles/posts/big-data-storage/)