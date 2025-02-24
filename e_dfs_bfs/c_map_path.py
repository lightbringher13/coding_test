from collections import deque


def solution(maps):
    n = len(maps)       # Number of rows
    m = len(maps[0])    # Number of columns

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Use a deque for BFS; each entry is a tuple: (row, column, distance)
    dq = deque()
    dq.append((0, 0, 1))  # Start at (0, 0) with an initial distance of 1

    # Mark the starting cell as visited by setting it to 0 (wall)
    maps[0][0] = 0

    while dq:
        x, y, d = dq.popleft()

        # Check if we have reached the destination (bottom-right)
        if x == n - 1 and y == m - 1:
            return d

        # Explore the adjacent cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the new position is within bounds and is not a wall
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                dq.append((nx, ny, d + 1))
                # Mark as visited to avoid revisiting
                maps[nx][ny] = 0

    # If destination is unreachable, return -1
    return -1
