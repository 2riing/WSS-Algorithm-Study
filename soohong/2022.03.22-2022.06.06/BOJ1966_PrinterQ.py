import sys
sys.stdin = open('../0518/input.txt')
from collections import deque

def PrintQ():
    global cnt
    # while q: # q가 존재하는 동안  while 실행
    while q:
        max_num = 0
        for i in range(len(q)): # 현재 존재하는 q들중에 max_num 구해주기
            if q[i][0] > max_num:
                max_num = q[i][0]
        if q[0][0] >= max_num:
            a = q.popleft() # 인쇄
            cnt += 1
            if a[1] == 1:
                print(cnt)
                break
        else:
            a = q.popleft()
            q.append(a)

T = int(input())
for _ in range(T):
    q = deque()
    cnt = 0
    N, M = map(int, input().split()) # 문서의 개수, 몇번째 놓여져있는지(현위치)
    temp = list(map(int, input().split()))
    for i in range(N):
        if i == M:
            q.append([temp[i], 1])
        else:
            q.append([temp[i], 0])
    PrintQ()










