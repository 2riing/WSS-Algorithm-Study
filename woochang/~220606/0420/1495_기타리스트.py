import sys
sys.stdin = open('1495input.txt')
from collections import deque

def dp(a,b,i):

    q = deque(a)
    while q:
        n = q.popleft()

        # for _ in range(2):
        if n+b<=M:
            v_list[i].append(n+b)
        if 0<=n-b<=M:
            v_list[i].append(n - b)


N, S, M = map(int, input().split())
V = list(map(int,input().split()))
v_list = [[] for _ in range(N)]
# print(v_list)
v_list[0].append(S+V[0])
v_list[0].append(S-V[0])

for i in range(1,N):
    a = v_list[i-1]
    dp(a,V[i],i)

ans_list = v_list[N-1]
if len(ans_list) >0:
    print(max(ans_list))
else:
    print(-1)

# 메모리 초과 4%