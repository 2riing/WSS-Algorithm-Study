from collections import deque
import sys
sys.stdin=open('11725input.txt')

def bfs(new_arr):
    queue = deque([start])
    b_check = [False for _ in range(N+1)]
    b_check[start] = True
    while queue:
        v = queue.popleft()
        for i in arr[v]:
            if not b_check[i]:
                b_check[i] = True
                queue.append(i)
                new_arr[i].append(v)
    return new_arr



N = int(input())
arr = [[] for _ in range(N+1)]
new_arr = [[] for _ in range(N+1)]
for i in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    arr[A].append(B)
    arr[B].append(A)
start = 1
bfs(new_arr)
for i in range(2, len(new_arr)):
    print(*new_arr[i])

