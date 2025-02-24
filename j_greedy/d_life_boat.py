def solution(people, limit):
    # Sort people in ascending order
    people.sort()

    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        # If the lightest (left) can pair with the heaviest (right), do it.
        if people[left] + people[right] <= limit:
            left += 1
        # In either case, the heaviest person at 'right' is always placed on a boat now.
        right -= 1
        boats += 1

    return boats


# Example test cases:
print(solution([70, 50, 80, 50], 100))  # Expected output: 3
print(solution([70, 80, 50], 100))      # Expected output: 3
