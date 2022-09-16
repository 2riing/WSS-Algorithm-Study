import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(N-1):
            if arr[i][j] == 1 and i != 0 and j != 0:
                cnt += 1
                new_arr[i][j] = cnt
