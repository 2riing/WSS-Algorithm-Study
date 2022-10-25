def yaksu(num):
    yak = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            yak.append(i)
    return yak


def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        ans_yak = yaksu(answer)
        ans2_yak = yaksu(arr[i])
        max_yak = 1
        for j in ans_yak:
            if j in ans2_yak:
                max_yak = j

        answer = (answer * arr[i]) // max_yak

    return answer

# 최소공배수 = 두수의 곱 // 최대공약수
# 시간초과 시벌것