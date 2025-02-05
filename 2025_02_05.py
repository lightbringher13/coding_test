"""
1. 네트워크 (bfs,dfs)
네트워크(연결된 모든 노드)를 세는 문제 외딴섬도 포함

2. 야근 지수 (heapq) 
가장 큰 숫자에서 부터 빼면서 제곱하고 전부 더한다.
"""


import heapq


def network(n, computers):
    visited = [False] * n
    network_count = 0
    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for j in range(n):
                        if computers[node][j] and not visited[j]:
                            stack.append(j)
            network_count = network_count + 1
    return network_count


def work_fatigue(n, works):
    if sum(works) <= n:
        return 0

    max_heap = [-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        largest = heapq.heappop(max_heap)
        if largest == 0:
            heapq.heappush(max_heap, largest)
            break
        largest = largest + 1
        heapq.heappush(max_heap, largest)
    answer = sum(x**2 for x in max_heap)
    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(network(n, computers))
    works = [4, 3, 3]
    n = 4
    print(work_fatigue(n, works))
