import heapq


def solution(operations):
    # Two heaps: one for minimum values, one for maximum values.
    # Each inserted element is stored as a tuple: (value, index) for min_heap,
    # and (-value, index) for max_heap (to simulate a max-heap).
    min_heap = []
    max_heap = []

    # visited[i] indicates whether the element inserted with index i is still valid.
    visited = [False] * len(operations)
    index = 0  # A unique identifier for each inserted number.

    for op in operations:
        command, num_str = op.split()
        num = int(num_str)

        if command == "I":
            # Insert the number into both heaps.
            heapq.heappush(min_heap, (num, index))
            heapq.heappush(max_heap, (-num, index))
            visited[index] = True  # Mark this entry as valid.
            index += 1

        else:  # command == "D"
            if num == 1:
                # Delete the maximum value.
                # Clean up max_heap: remove invalid entries.
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    # Remove the current maximum.
                    _, idx = heapq.heappop(max_heap)
                    visited[idx] = False
            elif num == -1:
                # Delete the minimum value.
                # Clean up min_heap: remove invalid entries.
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    # Remove the current minimum.
                    _, idx = heapq.heappop(min_heap)
                    visited[idx] = False

    # After processing all operations, clean both heaps of invalid entries.
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # If either heap is empty, the queue is empty.
    if not min_heap or not max_heap:
        return [0, 0]
    else:
        # The current maximum is -max_heap[0][0] and the minimum is min_heap[0][0].
        return [-max_heap[0][0], min_heap[0][0]]


# Example Tests
# Expected output: [0, 0]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45",
      "I 97", "D 1", "D -1", "I 333"]))  # Expected output: [333, -45]
