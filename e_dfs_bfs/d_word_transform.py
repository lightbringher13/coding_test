from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    deq = deque()
    deq.append([begin, 0])
    visited = [False] * len(words)

    while deq:
        word, step = deq.popleft()

        if word == target:
            return step

        for i in range(len(words)):
            cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        cnt += 1
            if cnt == 1:
                deq.append([words[i], step + 1])
                visited[i] = True

    # If target wasn't reached
    return 0


# Example tests:
# Expected output: 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# Expected output: 0
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
