def solution(n, a, b):
    answer = 0
    c = 0
    d = 0
    if a < b:
        c += a
        d += b
    else:
        c += b
        d += a
    print(c, d)
    while True:

        answer += 1
        if d % 2 == 0 and (d - c) == 1:
            break
        else:
            if c % 2 == 0:
                c = c // 2
            else:
                c = (c // 2) + 1
            if d % 2 == 0:
                d = d // 2
            else:
                d = (d // 2) + 1
            print(c, d)
    return answer

