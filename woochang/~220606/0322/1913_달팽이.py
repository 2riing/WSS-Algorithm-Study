import sys
sys.stdin = open('1913input.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]
M = N // 2 # center
dy_1 =[0, 1]
dx_1 =[-1,0]
dy_2 = [0, -1]
dx_2 = [1, 0]
dy = [0, 1, 0, -1]
dx = [-1,0, 1, 0 ]
arr[M][M] = 1
# for i in range(1,N+1):
#     M_x = M
#     M_y = M
#     if i % 2 :
#         for j in range(2):
#
#             arr[M_x+dx_1[j]][M_y+dy_1[j]] =arr[M][M] + i
#             M_x, M_y = M_x+dx_1[j], M_y+dy_1[j]
# print(arr)

for i in range(1, N*N):
    arr[M+dx][M+dy]
