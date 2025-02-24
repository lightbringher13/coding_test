def solution(number, k):
    stack = []
    rev = k
    for digit in number:

        while rev > 0 and stack and stack[-1] < digit:
            stack.pop()
            rev = rev - 1
        stack.append(digit)
    return "".join(stack[:len(number) - k])
