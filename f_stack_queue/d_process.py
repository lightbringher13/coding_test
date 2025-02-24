from collections import deque


def solution(priorities, location):
    res = []
    for i in range(len(priorities)):
        res.append([priorities[i], i])
    res = deque(res)
    print(max(res)[0])
    cnt = 0
    while res:
        i = 0
        if res[i][0] != max(res)[0]:
            a = res.popleft()
            res.append(a)
            print(res)
        else:
            cnt = cnt + 1
            if res.popleft()[1] == location:
                return cnt
        i = i+1
