Stacks and Queues are similar data structures.

A stack is last-in first-out (LiFo) and a queue is first-in first-out (FiFo). A priority queue is a queue that stores items based on priority.

For simple cases, you can use a `list`. For more advanced use-cases, you can look to the `queue` module that is part of the standard library. It offers a variety of implementations of stacks and queues, some of which are thread safe. The queue module code is found [here](https://github.com/python/cpython/blob/3.9/Lib/queue.py). For a priority queue, the [heapq](https://github.com/python/cpython/blob/3.9/Lib/heapq.py) library might be better.


## stacks

A stack is like a pile of items. You work with the top item only and there are two operations when working with the stack:
- `push`: putting something on the stack
- `pop`: removing something from the stack

The stack is said to be LiFo because you can only work with the top item. Due to the nature of the stack, there is no random access to items in the stack, nor is there access to anything at the bottom or in the middle.

Pushing and popping items from a stack is an O(1) operation. Stacks are commonly used for:
- execution of call stacks
- language parsing

To implement a stack, let's run through 3 possibilities that Python offers us using the standard library:
- list: simple and easy
- deque: more performant (no re-sizing cost)
- LifoQueue: threadsafe

### Using a list as a stack:

You can treat a regular `list` as a stack by using `.append()` for push and `.pop()` for pop operations. Note that lists are implemented as dynamic array structures and might resize as they grow. This is not something you would implement on a stack if you implement one from scratch.


```python
stack = []
stack.append("Learning Python")
stack.append("Automate the boring stuff with Python")
stack.append("Beyond the basic stuff with Python")

>>> stack
['Learning Python', 'Automate the boring stuff with Python', 'Beyond the basic stuff with Python']
>>> stack.pop()
'Beyond the basic stuff with Python'
>>> stack.pop()
'Automate the boring stuff with Python'
>>> stack
['Learning Python']
```

### Using deque as a stack:

Python's `collections.deque` provides us with a doubly-linked list that we can use as a stack or as a queue.

```python
from collections import deque
stack = deque()
stack.append("first")
stack.append("second")
stack.append("third")
>>> stack
deque(['first', 'second', 'third'])
>>> stack.pop()
'third'
>>> stack.pop()
'second'
```


### Using queue.LifoQueue as a (thread-safe) stack:

Python's `queue.LifoQueue` offers us a thread safe stack.

```python
from queue import LifoQueue
stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
>>> stack
<queue.LifoQueue object at 0x00000195D8561FA0>
>>> stack.get()
4
>>> stack.get()
3
>>> stack.get_nowait() 
2
>>> stack.get_nowait()
1
>>> stack.get_nowait()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python39\lib\queue.py", line 199, in get_nowait 
    return self.get(block=False)
  File "C:\Python39\lib\queue.py", line 168, in get        
    raise Empty
_queue.Empty
```

## queues

Queues, like the ones you stand in, are FiFo.

Queue oeprations in programmer parlance:
- `enqueue`: add to the queue, aka insert
- `dequeue`: remove from the queue, aka delete

The `enqueue` and `dequeue` operations are O(1). The queue does not offer random access. Queues are used for:
- scheduling
- breadth first search on a tree structure


To implement a queue, let's run through 3 possibilities that Python offers us using the standard library:
- `list`: simple and easy but slow, everything is in O(n) time
- `deque`: a lot faster, as it is a doubly-linked list (so O(1) time)
- `queue.Queue`: fast and threadsafe
- `multiprocessing.Queue`: fast and multiprocessing safe

### Using a list as a queue:

Use `append()` to enqueue and `pop(0)` to dequeue:

```python
queue = []
queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)
>>> queue
[0, 1, 2, 3]
>>> queue.pop(0)
0
>>> queue.pop(0)
1
>>> queue.pop(0)
2
>>> queue.pop(0)
3
>>> queue.pop(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>>
```

### Using deque as a queue:

Python's `collections.deque` provides us with a doubly-linked list that we can use as a stack or as a queue.

Use `.append()` to enqueue and `.popleft()` to dequeue:
```python
from collections import deque
queue = deque()
queue.append("first")
queue.append("second")
queue.append("third")
>>> queue
deque(['first', 'second', 'third'])
>>> queue.popleft()
'first'
>>> queue.popleft()
'second'
>>> queue.popleft()
'third'
>>> queue.popleft()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from an empty deque
```


### Using queue.Queue as a (thread-safe) queue:

```python
from queue import Queue
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
>>> queue
<queue.Queue object at 0x00000195D88EB550>
>>> queue.get()
1
>>> queue.get()
2
>>> queue.get_nowait() 
3
>>> queue.get_nowait()
4
>>> queue.get_nowait()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python39\lib\queue.py", line 199, in get_nowait 
    return self.get(block=False)
  File "C:\Python39\lib\queue.py", line 168, in get        
    raise Empty
_queue.Empty
```

## priority queue

A priority queue is a queue with ordering capabilities. This makes it more expensive when compared to a regular queue.

Priority queues are often used in:
- OS schedulers, to ensure important processes get to use the CPU before other processes
- network devices, to handle high prio packets before low prio packets


### Priority queues using lists

Error-prone, slow and not threadsafe:

```python
# prio is first item in the tuple
# low priority is better
>>> pq = [(0, "item-x"), (1, "item-y"), (2, "item-z")]
>>> pq
[(0, 'item-x'), (1, 'item-y'), (2, 'item-z')]
# add high prio item:
>>> pq.append((0, "item-a"))
# pq is no longer prioritized:
>>> pq
[(0, 'item-x'), (1, 'item-y'), (2, 'item-z'), (0, 'item-a')]
# sort manually to maintain prio:
>>> pq.sort()
>>> pq        
[(0, 'item-a'), (0, 'item-x'), (1, 'item-y'), (2, 'item-z')]
>>> pq.pop(0)
(0, 'item-a')
>>> pq.pop(0)
(0, 'item-x')
>>> pq.pop(0)
(1, 'item-y')
>>> pq.pop(0)
(2, 'item-z')
>>> pq.pop(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
```

### Priority queues using bisect.insort()

Using `bisect.insort()` can work with a list that is already sorted.

```python
from bisect import insort
# higher is more prio
pq = [(0, 'item-a'), (0, 'item-x'), (1, 'item-y'), (2, 'item-z')]
insort(pq, (0, "item-b"))
insort(pq, (10, "item-zz"))
>>> pq
[(0, 'item-a'), (0, 'item-b'), (0, 'item-x'), (1, 'item-y'), (2, 'item-z'), (10, 'item-zz')]
```

### Priority queues using heapq


```python
import heapq
pq = []
heapq.heappush(pq, (1, 'item-b'))
heapq.heappush(pq, (0, 'item-a'))
heapq.heappush(pq, (3, 'item-c'))
>>> pq
[(0, 'item-a'), (1, 'item-b'), (3, 'item-c')]
>>> heapq.heappop(pq)
(0, 'item-a')
>>> heapq.heappop(pq)
(1, 'item-b')
>>> heapq.heappop(pq)
(3, 'item-c')
>>> heapq.heappop(pq)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index out of range
```

When deleting items, you can use `heapq.heapify()` to return heap sorting order on the list.

When you need to move an item, fist delete the item form the list and then re-insert afterwards. 

For threadsafety, look at `queue.PriorityQueue`. This is a thread safe implemenation of `heapq`.