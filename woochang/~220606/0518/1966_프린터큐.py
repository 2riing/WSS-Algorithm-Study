import sys
sys.stdin = open('1966input.txt')
from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q_list = []
    q = deque([])
    for i in arr:
        q.append(i)
    for i in range(M):
        a = q.popleft()
        if q:
            for j in q:
                if a < j:
                    q.append(a)
                else:
                    print(a)
                    
# 3번째 테케 때문에 어떻게 구현을 해줘야될지 모르겟음
# 사이즈 같은 queue를 하나 더 만들어서 인덱스로 투입해서 넣어야되나







