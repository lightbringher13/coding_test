"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 
가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 
[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 
return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.

중요 포인트
numbers의 원소는 0 이상 1,000 이하입니다.

정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예

numbers	
return

[6, 10, 2]	
"6210"

[3, 30, 34, 5, 9]	
"9534330"
"""


from functools import cmp_to_key


def solution(numbers):
    # Convert numbers to strings.
    str_nums = list(map(str, numbers))

    # Define a custom comparator.
    # If a+b > b+a, then a should come first.
    def compare(a, b):
        if a + b > b + a:
            return -1  # a should be before b
        elif a + b < b + a:
            return 1   # a should be after b
        else:
            return 0

    # Sort using the custom comparator.
    str_nums.sort(key=cmp_to_key(compare))

    # If the largest number is "0", return "0".
    if str_nums[0] == "0":
        return "0"

    # Join the sorted strings.
    return "".join(str_nums)


# Example tests:
print(solution([6, 10, 2]))         # Expected output: "6210"
print(solution([3, 30, 34, 5, 9]))   # Expected output: "9534330"


if __name__ == "__main__":
    numbers = [6, 10, 2]
    print(solution(numbers))
