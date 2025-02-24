def solution(n, results):
    wins = [[] for _ in range(n+1)]
    loses = [[] for _ in range(n+1)]

    for winner, loser in results:
        wins[winner].append(loser)
        loses[loser].append(winner)
    print(wins)
    print(loses)

    def bfs(start, graph):
        from collections import deque
        q = deque([start])
        visited = set()
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        return visited
    answer = 0
    for i in range(1, n+1):
        can_win = bfs(i, wins)
        can_los = bfs(i, loses)
        if len(can_win) + len(can_los) == n-1:
            answer = answer + 1
    return answer
