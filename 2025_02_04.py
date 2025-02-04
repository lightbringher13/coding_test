"""
1.
동영상 재싱기
시간들 전부 초로 통일
"mm:ss" -> seconds 변환 
seoconds -> "mm:ss"

max(),min()을 활용해서 시간이 짧으면 0, 길면 full

2.
삼각형의 꼭대기에서 바닥까지 이어지는 
경로 중, 거쳐간 숫자의 합이 가장 큰 경우

아래 리스트를 트리로 보는 감각
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
[
 [7],
 [3, 8], 
 [8, 1, 0], 
 [2, 7, 4, 4], 
 [4, 5, 2, 6, 5]
 ]
 edge case 설정 가장 왼쪽 가장 오른쪽

"""


def time_to_seconds(time_str):
    min, sec = map(int, time_str.split(":"))
    sec = min * 60 + sec
    print(sec)
    return sec


def seconds_to_time(sec):
    min = sec // 60
    sec = sec % 60
    return f"{min:02d}:{sec:02d}"


def path_sum(triangle):
    n = len(triangle)
    dp = [[0] * (i+1) for i in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    return max(dp[-1])


if __name__ == "__main__":

    # 시간변환
    time = "24:13"
    time_to_sec = time_to_seconds(time)
    sec_to_time = seconds_to_time(time_to_sec)
    print(sec_to_time)

    # 삼각형에서 경로합
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(path_sum(triangle))
