from collections import defaultdict


def solution(n, wires):
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs_count(start, no_edge):

        stack = []
        stack.append(start)
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neigh in graph[node]:
                if (node, neigh) == no_edge or (neigh, node) == no_edge:
                    continue
                if neigh not in visited:
                    stack.append(neigh)
        return len(visited)
    res = []
    for a, b in wires:
        count = dfs_count(a, (a, b))
        diff = abs(count - (n - count))
        res.append(diff)
    return min(res)
