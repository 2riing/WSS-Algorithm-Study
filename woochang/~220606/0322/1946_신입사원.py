import sys
sys.stdin = open('1946input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    sum_count = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][0] <= arr[j][0] or arr[i][1] <= arr[j][1]:
                cnt += 1
        if cnt == N:
            sum_count += 1
    print(sum_count)

# 시간초과... 이중포문은 절대안되는듯
