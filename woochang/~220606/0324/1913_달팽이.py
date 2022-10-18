import sys
sys.stdin = open('1913input.txt')

# N = int(input())
# arr = [[0]*N for _ in range(N)]
# M = N // 2 # center
# dy_1 =[0, 1]
# dx_1 =[-1,0]
# dy_2 = [0, -1]
# dx_2 = [1, 0]
# dy = [0, 1, 0, -1]
# dx = [-1,0, 1, 0 ]
# arr[M][M] = 1
# for i in range(1,N+1):
#     M_x = M
#     M_y = M
#     if i % 2 :
#         for j in range(2):
#
#             arr[M_x+dx_1[j]][M_y+dy_1[j]] =arr[M][M] + i
#             M_x, M_y = M_x+dx_1[j], M_y+dy_1[j]
# print(arr)

def make_snail(n):
    global t_x, t_y
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    complete_snail = [[0 for _ in range(n)] for _ in range(n)]

    # 0,0 에서 초기화
    cnt = n ** 2
    direction = 0
    x, y = 0, 0
    complete_snail[x][y] = cnt
    cnt -= 1
    # cnt 가 모든 칸에 기록될때까지
    while cnt > 0:

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n and not complete_snail[nx][ny]:
            complete_snail[nx][ny] = cnt
            if cnt == target:
                t_x, t_y = nx, ny
            x, y = nx, ny
            cnt -= 1
        else:  # 진입 못하면 방향 시계방향 전환
            direction = (direction + 1) % 4
    return complete_snail


N = int(input())
target = int(input())
t_x, t_y = 0, 0
snail = make_snail(N)
for row in snail:
    print(*row)
print(t_x + 1, t_y + 1)
