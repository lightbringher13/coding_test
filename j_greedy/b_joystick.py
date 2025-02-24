def solution(name):
    answer = 0
    n = len(name)

    # 1. Calculate the vertical moves for each character.
    for c in name:
        # The cost is the minimum between moving forward or backward.
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

    # 2. Calculate the horizontal moves (minimizing left/right movement).
    move = n - 1  # Worst-case: move right one by one.
    for i in range(n):
        next_index = i + 1
        # Skip consecutive 'A's since they don't require changing.
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        # The two options:
        # Option 1: Move right to i, then go back left to cover the remainder.
        # Option 2: Move right, then reverse and go right again.
        move = min(move, 2 * i + n - next_index, i + 2 * (n - next_index))

    return answer + move


# Example test cases:
print(solution("JEROEN"))  # Expected output: 56
print(solution("JAN"))     # Expected output: 23
