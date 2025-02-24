from collections import deque


def solution(prices):
    prices = deque(prices)
    res = []

    while prices:
        price = prices.popleft()  # Get the current price and remove it.
        cnt = 0
        # Iterate over the remaining prices (which represent subsequent seconds).
        for pri in prices:
            if pri >= price:
                cnt += 1
            else:
                cnt += 1
                break
        res.append(cnt)
    return res


# Example test:
print(solution([1, 2, 3, 2, 3]))  # Expected output: [4, 3, 1, 1, 0]
