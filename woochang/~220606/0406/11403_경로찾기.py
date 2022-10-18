import sys
sys.stdin = open('11403input.txt')


def dfs(x):
    d_check[x] = True
    for i in stack[x]:
        if arr[x - 1][i] == 0 :
            arr[x-1][i] = 1
            dfs(i)
            if arr[x - 1][i] == 1:
                break


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
stack = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            stack[i+1].append(j+1)

d_check = [False for _ in range(N+1)]
for k in range(1, N+1):
    dfs(k)

print(stack)

# 문제는 이해를 했으나....
# 그냥 보던 트리 구조가 아니라 갑자기 순환형?? 이 튀어나와서
# 어떻게 풀이를 해줘야될지?
# 그냥 DFS로 노가다?