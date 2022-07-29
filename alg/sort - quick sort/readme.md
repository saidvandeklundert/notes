# Quicksort


Quicksort is a divide and conquer algorithm. 

Quicksort is a sorting algorithm that sorts a collection by choosing a pivot point, and partitioning the collection around the pivot, so that elements smaller than the pivot are before it, and elements larger than the pivot are after it. It continues to choose a pivot point and break down the collection into single-element lists, before combing them back together to form one sorted list.

The two core parts of the algorithm are these:
1. quicksort determines a pivot, which is a somewhat arbitrary element in the collection that needs sorting
2. using the pivot point, it partitions (divides) the larger unsorted collection into two, smaller lists. Logic is used to decide how to partition:
  - it moves all the elements smaller than the pivot to the left before the pivot element
  - moves all the elements larger than the pivot to the right after the pivot element

Think about the algorithm in the following steps:
1. Pick a "pivot point". Picking a good pivot point can greatly affect the running time.
2. Break the list into two lists: those elements less than the pivot element, and those elements greater than the pivot element.
3. Recursively sort each of the smaller lists.
4. Make one big list: the 'smallers' list, the pivot points, and the 'biggers' list.


The quick guide to implementing quicksort:
1. choose a pivot (usually the last element in the list, but can differ)
2. create a left pointer to the first element (that is not the pivot)
3. create a right pointer to the last element (that is not the pivot)
4. while the left is less than the pivot, move the pointer one element to the right. WHile the right is greater than the pivot, move the pointer one element to the left.
5. if both left is greater than the pivot AND right is smaller then the pivot, swap the elements at the two references
6. once the index of the left reference is greater than (or equal to) the index of the right reference, swap the pivot with the element at the LEFT reference


Is Quicksort a stable algorithm?
- No, Quicksort belongs to the group of unstable sorting algorithms.

What does a “stable sorting algorithm” mean?
- Stable sorting algorithms preserve the order of input elements.

[quick sort in 4 minutes](https://www.youtube.com/watch?v=Hoixgm4-P4M&t=1s)
[quick sort](https://www.youtube.com/watch?v=uXBnyYuwPe8)