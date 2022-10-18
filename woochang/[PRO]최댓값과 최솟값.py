def solution(s):
    answer = ''
    ss = list(map(int, s.split()))
    print(ss)
    answer += str(min(ss))
    answer += ' '
    answer += str(max(ss))

    return answer