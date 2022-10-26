def solution(n):
    answer = 0
    stack = [1, 2]
    if n <= 2:
        answer += n
    else:
        for i in range(2, n):
            k = stack[-1] + stack[-2]
            stack.append(k)
        answer += stack[-1]
        answer = answer % 1234567
    return answer