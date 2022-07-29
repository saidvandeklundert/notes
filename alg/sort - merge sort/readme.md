# Merge sort

Merge sort was developed in 1945 by John von Neumann.

It is a general purpose sorting algorithm that uses a divide-merge approach.

In a recursive approach, the unsorted list is constantly halved in every recursive call. This is done untill the lists are of 0 or 1 length. After the lists are reduced to this size, the recursive call returns and the returned lists are merged together into sorted order. When the last recursive call returns, the list is in sorted order.

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


The time complexity for merge sort is `O(n log n)`.

Detailed explanation [here](https://www.youtube.com/watch?v=alJswNJ4P3U).

We constantly half the input list, so the time complexity for the input list can be described as `log n`. And for every input list we half, we do the sort. This is of linear complexity, so this is `n`.

We say merge sort is `O(n log n)` because we do linear work (`n`) for every single time we half the input (`log n`).


The space complexity is `O(n)` because we need extra space when we take the slices of the list we are sorting.


Is Mergesort a stable algorithm?
- Yes, Mergesort belongs to the group of stable sorting algorithms.

What does a “stable sorting algorithm” mean?
- Stable sorting algorithms preserve the order of input elements.

[leetcode explanation](https://leetcode.com/problems/sort-an-array/discuss/461394/Python-3-(Eight-Sorting-Algorithms)-(With-Explanation))
[leetcode challenge](https://leetcode.com/problems/sort-an-array)
[youtube guy](https://www.youtube.com/watch?v=mB5HXBb_HY8)
[youtube guy on sorting](https://www.youtube.com/watch?v=6pV2IF0fgKY)


https://www.brainscape.com/flashcards/sorting-algorithms-3907604/packs/5737327
