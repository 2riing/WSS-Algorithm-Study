def solution(s):
    answer = 0
    stack = [0]
    for i in range(len(s)):
        if s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    if stack==[0]:
        answer += 1
    return answer