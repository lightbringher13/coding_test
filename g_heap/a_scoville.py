import heapq


def solution(scoville, K):
    # Transform the list into a heap (min-heap)
    heapq.heapify(scoville)
    count = 0

    # While the smallest scoville is less than K:
    while scoville[0] < K:
        # If there's less than two foods, we cannot mix further.
        if len(scoville) < 2:
            return -1

        # Pop the two smallest scoville values.
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # Create a new food with the given formula.
        new_food = first + (second * 2)

        # Push the new food's scoville value into the heap.
        heapq.heappush(scoville, new_food)

        # Increase the count of operations.
        count += 1

    return count


# Example test cases:
print(solution([1, 2, 3, 9, 10, 12], 7))  # Expected output: 2
