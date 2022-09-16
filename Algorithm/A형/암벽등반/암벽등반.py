import sys
sys.stdin = open('input.txt')
from collections import deque


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int ,input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    max_answer = 0
    min_answer = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 3:
                max_answer = N-i-1
    start_x = N-1
    start_y = 0
    





    print(f'#{tc} {max_answer}')