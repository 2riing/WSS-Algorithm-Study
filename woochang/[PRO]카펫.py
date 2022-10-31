def solution(brown, yellow):
    answer = []
    n = brown + yellow
    yak = []
    for i in range(3, n // 2):
        if n % i == 0:
            yak.append(i)
    for i in yak:
        if (n // i) in yak:

            if i ** 2 == n:
                answer.append(i)
                answer.append(i)
                break
            else:
                j = n // i
                if (j - 2) * (i - 2) != yellow:
                    continue
                else:
                    answer.append(j)
                    answer.append(i)
                    break

    return answer