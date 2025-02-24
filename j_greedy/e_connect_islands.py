import heapq
from collections import defaultdict


def solution(n, costs):
    # Build the graph
    graph = defaultdict(list)
    for a, b, c in costs:
        graph[a].append((c, b))  # store as (cost, node)
        graph[b].append((c, a))  # undirected graph

    visited = [False] * n
    heap = [(0, 0)]  # start from node 0 with cost 0
    total_cost = 0

    while heap:
        cost, node = heapq.heappop(heap)
        if visited[node]:
            continue  # Skip already visited nodes
        visited[node] = True  # Mark current node as visited
        total_cost += cost

        # Add all edges from this node to the heap
        for edge_cost, neigh in graph[node]:
            if not visited[neigh]:
                heapq.heappush(heap, (edge_cost, neigh))

    # Optionally, check if all nodes were reached.
    # If not, the graph is not fully connected.
    if not all(visited):
        return None  # or raise an error

    return total_cost


# Example test:
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
