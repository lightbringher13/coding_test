def solution(n, computers):
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            count += 1  # Found a new network
            stack = [i]
            visited[i] = True  # Mark as visited when pushing

            while stack:
                node = stack.pop()
                # Explore all neighbors of 'node'
                for j in range(n):
                    if computers[node][j] == 1 and not visited[j]:
                        visited[j] = True  # Mark neighbor as visited
                        stack.append(j)

    return count
