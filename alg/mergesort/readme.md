# Merge sort

Merge sort was developed in 1945 by John von Neumann.

It is a general purpose sorting algorithm that uses a divide-merge approach.

In a recursive approach, the unsorted list is constantly halved in every recursive call. This is done untill the lists are of 0 or 1 lenght. After the lists are reduced to this size, the recursive call returns and the returned lists are merged together into sorted order. When the last recursive call returns, the list is in sorted order.

The mergesort function starts by checking for the base case. If the unsorted list is 0 or 1, it returns:

```python
def mergesort(items: list[int]):
    print(f"merge sort called on: {items}")

    # base case: 0 or more items are naturally sorted:
    if len(items) == 0 or len(items) == 1:
        return items
```

The reason it returns is because a list of 0 or 1 is sorted by default.

If the list is not sorted, it is split in half and the function is called recursively:
```python
    middle = math.floor(len(items) / 2)

    left = mergesort(items[:middle])
    right = mergesort(items[middle:])
```

The recursive call returns the left and right half in sorted order. The next step is to merge the sorted halfs in order.

```python
    sorted_result = []
    ileft = 0
    iright = 0
    while len(sorted_result) < len(items):
        # since left and right are sorted, we constantly
        # check the lowest value of both lists and 
        # add that value to the 'sorted_result'.
        if left[ileft] < right[iright]:
            sorted_result.append(left[ileft])
            ileft += 1
        else:
            sorted_result.append(right[iright])
            iright += 1
        
        # if one of the pointers reached the end of the list
        # we put the rest of the other list into
        # sorted_result
        if ileft == len(left):
            sorted_result.extend(right[iright:])
            break
        elif iright == len(right):
            sorted_result.extend(left[ileft:])
            break
    # we return the left and right list in
    # sorted order
    return sorted_result
```