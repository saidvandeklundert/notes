import heapq

HEAP = [21, 2, 45, 78, 3, 5]
# Use heapify to rearrange the elements
heapq.heapify(HEAP)
print(HEAP)
heapq.heappush(HEAP, 1)
heapq.heappush(HEAP, 300)
print(HEAP)
heapq.heappop(HEAP)
print(HEAP)
heapq.heapreplace(HEAP, 0)
print(HEAP)
