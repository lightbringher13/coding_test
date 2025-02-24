def solution(numbers, target):
    stack = [[numbers[0], 0], [-numbers[0], 0]]
    cnt = 0
    while stack:
        num, idx = stack.pop()
        idx = idx + 1
        if idx < len(numbers):
            stack.append([num + numbers[idx], idx])
            stack.append([num - numbers[idx], idx])
        else:
            if num == target:
                cnt = cnt + 1
    return cnt
