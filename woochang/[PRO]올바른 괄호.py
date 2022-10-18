def solution(s):
    answer = True
    ans = 0
    for i in s:
        if ans < 0:  # 먼저 ans를 탐색 0보다 작으면 바로 false 하고 break 멈춤
            answer = False
            break

        if i == '(':
            ans += 1
        else:
            ans -= 1

    if ans != 0:  # 다 탐색했는데 다 안닫힌거면 false
        answer = False

    return answer

# 5분