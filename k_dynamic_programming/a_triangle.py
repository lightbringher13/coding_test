def solution(triangle):
    dp = [[0]*(i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if i == j:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            elif j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])
    return max(dp[-1])
