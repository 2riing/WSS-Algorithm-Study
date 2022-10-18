def solution(n):
    answer = 0
    k = bin(n)[2:]
    ans1 = 0

    for i in k:
        if i == '1':
            ans1 += 1
    while True:
        n += 1
        ans2 = 0
        k = bin(n)[2:]
        for i in k:
            if i == '1':
                ans2 += 1
        if ans1 == ans2:
            answer += n
            break
    return answer