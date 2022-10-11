import sys
sys.stdin = open('../0511/input.txt')

import heapq

N = int(sys.stdin.readline()) # readline만 써주면 통과 코드
max_heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(max_heap) == 0:
            print('0')
            print(max_heap)
        else:
            print(-heapq.heappop(max_heap))
            print(max_heap)
    else:
        heapq.heappush(max_heap, -num)
        print(max_heap)

