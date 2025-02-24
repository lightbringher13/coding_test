def solution(s):
    stack = []
    for letter in s:
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
