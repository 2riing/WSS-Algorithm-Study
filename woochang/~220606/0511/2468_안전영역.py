import sys
sys.stdin = open('2468input.txt')
from collections import deque

def bfs(a,b):
    global max_safe
    dt = [[1,0],[-1,0],[0,1],[0,-1]]
    visited[a][b] = 1
    q = deque([(a,b)])
    while q:
        (x,y) = q.popleft()
        for w in dt:
            nx, ny = x+w[0], y+w[1]
            if 0 <= nx < N and 0 <= ny < N and new_arr[nx][ny] != 0 and visited[nx][ny] ==0:
                q.append([nx,ny])
                visited[nx][ny] = 2

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_safe = 0 # 최종 정답
max_height = 0 # 제일 높은 층
for i in range(N):
    if max(arr[i]) > max_height:
        max_height = max(arr[i])

for i in range(1, max_height):
    new_arr = [[0]*N for _ in range(N)]
    # 안 잠긴 arr 만들어주기
    for j in range(N):
        for k in range(N):
            if arr[j][k] > i:
                new_arr[j][k] = arr[j][k]
    # print(new_arr)
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if new_arr[j][k] and visited[j][k] == 0 :
                bfs(j,k)
    cnt = 0
    for j in range(N):
        for k in range(N):
            if visited[j][k] == 1:
                cnt += 1
    if max_safe <= cnt :  # max_safe < cnt  일때 틀렸는데 <= 로 바꾸니까 맞음 ....... 얼탱이..
        max_safe = cnt
print(max_safe)



# max_num 찾아서 잠기는 범위 돌리는거를 2 ~ (max_num-1) 로 설정
# 만약 장마철 2다 그러면
# arr 2 아래는 0으로 다 만들어주고 시작
#
# 그리고 visited 랑 bfs 이용해서 숫자 있는 부분들 쭉 늘려가면서 세줄거
# visited에 1, 2, 3,  1, 2, 3,4, 1,2, 1, 이런식으로 셀거니까
# visited의 1 갯수 세주면 됨
#
# 그리고 전체에서 1 갯수의 최댓값인거 찾아주기