def solution(brown, yellow):
    answer = []
    n = brown + yellow
    yaksu = []
    for i in range(3, n // 2):
        if n % i == 0:
            yaksu.append(i)
    for i in yaksu:
        if (n // i) in yaksu:

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