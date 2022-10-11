import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
graph = [[0 for _ in range(M+1)] for _ in range(N+1)]
print(graph)
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


