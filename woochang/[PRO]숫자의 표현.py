

def solution(n):
    answer = 1  # 자기 자신인거 미리 더해줘버림
    k = n // 2
    print(k)
    for i in range(1, k + 1):
        summ = 0
        summ += i  # 1
        cnt = 0
        while summ < n:
            cnt += 1
            summ += (i + cnt)  # 1+1
        if summ == n:
            answer += 1

    return answer

n = 15
a= solution(n)

print(a)