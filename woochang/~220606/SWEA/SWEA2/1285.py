import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    min_arr = 100000
    max_count = 0
    position = list(map(int,input().split()))
    for i in position:
        arr.append(abs(i))
    for j in arr:
        if j < min_arr:
            min_arr = j
    for k in arr:
        if k == min_arr:
            max_count += 1
    print(f'#{tc} {min_arr} {max_count}')