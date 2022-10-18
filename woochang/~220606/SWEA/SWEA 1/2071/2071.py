import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i]
    ans = round(cnt / len(arr))

    print(f'#{tc} {ans}')