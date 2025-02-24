from itertools import permutations


def solution(k, dungeons):
    max_count = 0
    # Try every permutation of the dungeons.
    for order in permutations(dungeons):
        fatigue = k
        count = 0
        # Simulate exploring dungeons in this order.
        for min_req, cost in order:
            if fatigue >= min_req:
                fatigue -= cost
                count += 1
            else:
                break  # Can't explore this dungeon; move on to the next order.
        max_count = max(max_count, count)
    return max_count


# Example test case:
print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # Expected output: 3
