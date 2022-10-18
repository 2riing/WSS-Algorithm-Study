import sys
sys.stdin = open('11279input.txt')
import heapq
# from collections import deque
#
# N = int(input())
# stack = []
# for i in range(N):
#     a = int(input())
#     if a == 0 :
#         if len(stack) != 0:
#             b = stack.pop(max(stack))
#             print(b)
#         else:
#             print('0')
#     else:
#         stack.append(a)


N = int(input())
heap =[]
for _ in range(N):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print('0')
    else:
        heapq.heappush(heap,[-num, num])