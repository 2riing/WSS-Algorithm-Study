import sys
sys.stdin = open('0511input.txt')
from collections import deque

def search_dt():
    global d, x, y
    if d < 0:
        d += 4
    elif d >= 4:
        d -= 4

    if d == 0 :
        x, y = -1, 0
    elif d == 1 :
        x, y = 0, 1
    elif d == 2:
        x, y = 1, 0
    elif d == 3:
        x, y = 0, -1



def bfs():
    global d, cnt, x, y, flag

    visited[r][c] = 1
    q = deque([start])
    while q:
        now = q.popleft()
        flag = 0
        # if (visited[now[0]][now[1]] == 1 or arr[now[0]][now[1]] == 0) and (visited[now[0]][now[1]] == 1 or arr[now[0]][now[1]] == 0) and (visited[now[0]][now[1]] == 1 or arr[now[0]][now[1]] == 0) and (visited[now[0]][now[1]] == 1 or arr[now[0]][now[1]] == 0):

        # d -= 1
        # search_dt(dt)
        # nx, ny = now[0], now[1]
        # wx, wy = now[0]+dt[0], now[1]+dt[1] #서쪽 확인

        nx, ny = now[0], now[1]

        for i in range(4): # 2a가 4번 실행되는 경우 고려 for문 4번
            d -= 1
            search_dt()
            # nx, ny = now[0], now[1]  # 본 좌표
            wx, wy = now[0] + x, now[1] + y # 돌린 후 서쪽 좌표

            if 0<=wx<N and 0<=wy<M and arr[wx][wy] ==0 and visited[wx][wy] ==0:

                # d -= 1
                # search_dt(dt)
                # nx, ny =nx+dt[0], ny+dt[1]
                q.append([wx,wy])
                visited[wx][wy] = 1
                cnt += 1
                flag = 1
                break  # 본 좌표

        if flag == 0 :
            d -= 2
            search_dt()
            if arr[nx+x][ny+y] == 0 : # and 0 <= nx < N and 0 <= ny < N
                d += 2

                q.append([nx + x,ny + y])
            else:
                break

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 1  # 청소할때 cnt+= 1
visited = [[0]*M for _ in range(N)]
x= 0
y =0
flag = 0
start = [r, c]
bfs()
print(cnt)


# 함수 안에 d= 0, 1, 2, 3 일때 dt의 조건 만들어주기
# 또 다른 함수 설정
# [-1,0] 의 값이 벽 , no visited 이면 d -= 1 , dt 해줌

# 바라보는 방향 왼쪽 / 그래서 d를 -1 씩 하고 0 보다 작아지면 4 더해주는 식으로
# 1번으로 돌아가거나 후진하지 않고 2a가 4번 실행될경우 바로 뒤쪽이 벽이라면 작동을 멈춘다. 아니면 후진한다.
# 후진도 방향을 고려해서 d 조절해서 후진 후 d 원위치로 줘야됨