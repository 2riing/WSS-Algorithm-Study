import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1,T+1):
    arr = list(map(int, input().split()))
    sum = 0
    avg = 0
    for i in range(1, len(arr)):
        sum += arr[i]
    avg = sum / arr[0]

    cnt = 0
    for i in range(1, len(arr)):
        if avg < arr[i]:
            cnt += 1

    print("%.3f%%" % (cnt / arr[0] * 100))
    # print(round(cnt / arr[0] * 100, 3))