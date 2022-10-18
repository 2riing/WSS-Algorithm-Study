import sys
sys.stdin = open('11724input.txt')
# sys.setrecursionlimit(5000) # 재귀 함수 제한 두는거 ? 맥스가 10**6
# input = sys.stdin.readline

def dfs(s, d):
    visited[s] = True
    for i in arr[s]:
        if not visited[i]:
            dfs(i, d + 1)

N, M = map(int ,input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (1 + N)
cnt = 0

for i in range(1, N + 1):
    if not visited[i]:
        if not arr[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i, 0)
            cnt += 1


print(cnt)