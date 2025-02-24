def solution(n, times):
    # 1. 이분 탐색 범위 설정
    left = 1                   # 최소 1분
    right = min(times) * n     # 가장 빠른 심사관이 n명을 전부 처리한다고 가정(최대치)
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 중간 시간

        # 2. mid 시간 동안 처리할 수 있는 사람 수 계산
        total = 0
        for t in times:
            total += mid // t
            if total >= n:    # 이미 충분한 사람을 처리한다면, 더 볼 필요 없이 break
                break

        # 3. 사람 수 판단 → 범위 조정
        if total >= n:
            # mid로도 n명을 처리 가능 → 더 짧은 시간도 가능할 수 있다
            answer = mid
            right = mid - 1
        else:
            # mid로는 n명을 못 채움 → 시간 더 필요
            left = mid + 1

    return answer
