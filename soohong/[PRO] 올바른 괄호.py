def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')

    if stack:
        return False
    else:
        return True