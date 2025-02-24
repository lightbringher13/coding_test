from collections import defaultdict, deque


def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1 for _ in range(n+1)]
    distance[1] = 0
    q = deque([1])

    while q:
        node = q.popleft()
        for neigh in graph[node]:
            if distance[neigh] == -1:
                distance[neigh] = distance[node] + 1
                q.append(neigh)
    max_dist = max(distance)
    return distance.count(max_dist)
