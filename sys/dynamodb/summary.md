# Import DynamoDB components and terms:

`Tables`: a table is a collection of data.

`Items`: each table contains 0 or more items. An item can be seen as a row, record or tuple in other database systems. In dynamo, the item is a group of attributes that is uniquely identifiable among all of the other items.

`Attributes`: every items consists of 1 or more attributes. An attribute is a fundamental data element, something that does not need to be broken down any further.

For example, consider a table called `Human` with 2 items that each have an attribute called 'id' and another attribute called 'name':

```
{
    "id": 1,
    "name":"Jan"
},
{
    "id": 2,
    "name":"Marie"
}
```

`Primary key`: upon table creation, you have to specify a table name and a primary key for that table. The primary key uniquely identifies each item in the table. No two items are allowed to have the same key.

There are 2 different kinds of primary keys:

1. partition key: a simple primary key, composed of one attribute known as the partition key. The partition keys value is used as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to Dynamo) in which the item will be stored.

2. partion key and sort key: aka _composite primary key_. This type of key is composed of two attributes: the primary key and the sort key. 

DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. All items with the same partition key value are stored together, in sorted order by sort key value.

In a table that has a partition key and a sort key, it's possible for multiple items to have the same partition key value. However, those items must have different sort key values.

A composite primary key gives you additional flexibility when querying data. For example, if you provide only the value for Artist, DynamoDB retrieves all of the songs by that artist. To retrieve only a subset of songs by a particular artist, you can provide a value for Artist along with a range of values for SongTitle.

Each primary key attribute must be a scalar (meaning that it can hold only a single value). The only data types allowed for primary key attributes are string, number, or binary. There are no such restrictions for other, non-key attributes as they need not be hashed.

`Secondary indexes`:

You can create one or more secondary indexes. A secondary index lets you query the data in the table using an alternate key, in addition to queries against the primary key.

You are not required to use indexes, but they will give you additional flexibility when querying your data. After you create a secondary index, you can read data from the index in much the same way as you do from the table.

Dynamo supports two kinds of indexes:
- Global secondary index: an index with a partition key and sort key that can be different from those on the table.
- Local secondary index: an index that has the same partition key as the table, but a different sort key.

There can be 20 global secondary indexes and 5 local secondary indexes.


`Read consistency`: Dynamo supports eventually consistent and strongly consistent reads:
- `eventually consistent`: the read response might not always reflect the latest completed write operation.
- `strongly consistent`: a read response will always return the most up-to-date data. This has a performance cost. Also, strongly consisten reads are not supported on global secondary indexes and strongly consistent reads use more throughput capacity than eventually consistent reads.