import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    max_num = arr[N-1]
    cnt = 0
    for i in range(N-1,0, -1):
        if arr[i] < arr[i-1] and max_num < arr[i-1]:
            max_num = arr[i-1]
        
        else :
            total += (max_num - arr[i-1])
    print(f'#{tc} {total}')