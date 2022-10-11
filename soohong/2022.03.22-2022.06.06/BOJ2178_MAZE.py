import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(row, col):
    global visited
    q = deque()
    q.append([row, col])
    ni = [1, -1, 0, 0]
    nj = [0, 0, 1, -1]
    while q:
        temp = q.popleft()
        row, col = temp[0], temp[1]
        if row == N-1 and col == M-1:
            return visited[row][col]
        else:
            for i in range(4):
                di, dj = row + ni[i] , col + nj[i]
                if 0 <= di < N and 0 <= dj < M:
                    if visited[di][dj] == 0 and maze[di][dj] == 1:
                        visited[di][dj] = visited[row][col] + 1
                        q.append([di, dj])


# 기본 입력 및 선언
N, M = map(int, input().split()) # 도착지점, row, col
maze = [list(map(int,input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1


# 함수 실행
print(BFS(0,0))
