import heapq


def solution(jobs):
    heap = []
    jobs.sort(key=lambda x: x[0])
    n = len(jobs)
    processed = 0
    idx = 0
    total_turnaround_time = 0
    current_time = 0
    while processed < n:
        while idx < n and jobs[idx][0] <= current_time:
            s, l = jobs[idx]
            heapq.heappush(heap, (l, s))
            idx = idx + 1

        if heap:
            l, s = heapq.heappop(heap)
            current_time += l
            total_turnaround_time += current_time - s
            processed = processed + 1
        else:
            current_time = jobs[idx][0]
    return total_turnaround_time // n
