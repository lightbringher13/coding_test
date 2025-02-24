def solution(distance, rocks, n):
    # Sort the rock positions.
    rocks.sort()

    # Set binary search boundaries:
    low, high = 1, distance  # minimum gap is at least 1, maximum is distance
    answer = 0

    while low <= high:
        mid = (low + high) // 2  # candidate minimum gap
        removed = 0  # count how many rocks must be removed
        prev = 0     # start at the starting point (position 0)

        # Check each rock:
        for rock in rocks:
            # If the gap from the last position to this rock is less than mid,
            # then remove this rock.
            if rock - prev < mid:
                removed += 1
            else:
                # Otherwise, keep the rock and update the previous position.
                prev = rock

        # Finally, check the gap from the last rock (or start) to the destination.
        if distance - prev < mid:
            removed += 1

        # If the number of removals is within the allowed limit,
        # then mid is feasible, so update answer and try for a larger gap.
        if removed <= n:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer


# Example test:
print(solution(25, [2, 14, 11, 21, 17], 2))  # Expected output: 4
