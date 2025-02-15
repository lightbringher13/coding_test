import heapq

# If you already have a list of numbers,
# you can convert it into a heap in place
# using the heapq.heapify() function.
# The list will be rearranged
# so that the smallest element is at index 0.
numbers = [5, 3, 8, 1, 2]
# Rearranges numbers in-place to satisfy the heap property
heapq.heapify(numbers)
print("Heapified list:", numbers)
# Possible output: Heapified list: [1, 2, 8, 5, 3]

# To add a new element to the heap
# while maintaining the heap invariant, use heapq.heappush().
# This operation takes O(log n) time.
heap = [1, 2, 8, 5, 3]
heapq.heappush(heap, 0)
print("After heappush(0):", heap)
# Output might be: After heappush(0): [0, 1, 8, 5, 3, 2]

# To remove and return the smallest element from the heap,
# use heapq.heappop().
# This operation also takes O(log n) time.
smallest = heapq.heappop(heap)
print("Popped smallest element:", smallest)
print("Heap after heappop():", heap)
# Output might be: Popped smallest element: 0
# And then: Heap after heappop(): [1, 3, 8, 5, 2]

# max_heap
numbers = [5, 3, 8, 1, 2]
# Create a max-heap by negating all numbers.
max_heap = [-num for num in numbers]
heapq.heapify(max_heap)
print("Max-heap (negated):", max_heap)
# Output might be: Max-heap (negated): [-8, -5, -3, -1, -2]

# To get the maximum element (in normal order), pop and negate the value.
largest = -heapq.heappop(max_heap)
print("Largest element:", largest)
# Expected output: Largest element: 8

# If you have multiple sorted iterables,
# you can merge them into a single sorted iterator.
iterable1 = [1, 3, 5]
iterable2 = [2, 4, 6]
merged = heapq.merge(iterable1, iterable2)
print("Merged sorted iterables:", list(merged))
# Output: Merged sorted iterables: [1, 2, 3, 4, 5, 6]

# The heapq module also provides the functions
# nlargest() and nsmallest().
numbers = [5, 3, 8, 1, 2]
print("3 largest elements:", heapq.nlargest(3, numbers))
# Output: 3 largest elements: [8, 5, 3]

print("2 smallest elements:", heapq.nsmallest(2, numbers))
# Output: 2 smallest elements: [1, 2]
