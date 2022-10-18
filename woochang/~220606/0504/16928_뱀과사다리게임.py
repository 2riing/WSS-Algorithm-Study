import sys
sys.stdin = open('16928input.txt')
from collections import deque

N, M = map(int, input().split())
arr = []
snake = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a,b])
for _ in range(M):
    c, d = map(int, input().split())
    snake.append([c, d])
# print(arr)
# print(sum_arr)
min_count = 100
p = 0
q = 0
for i in range(N):
    c = (arr[i][0]-1) // 6 + 1
    d = (100 - arr[i][1]) // 6 + 1
    if c+d < min_count:
        min_count = c+d
        q = i
print(min_count)

#
#
#
#
#                       사다리
# 1 x 3 x x x 7 x x x  x 12
# 1 2 3 4 5 6 7 8 9 0 11 12