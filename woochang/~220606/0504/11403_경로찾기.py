import sys
sys.stdin = open('11403input.txt')

def arrrr(a,b):
    for k in range(N):
        if arr[b][k] == 1 and new_arr[a][k] == 0:
            new_arr[a][k] = 1
            arrrr(a,k)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
new_arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            new_arr[i][j] = 1
            arrrr(i,j)

# print(new_arr)
for i in range(N):
    print(*new_arr[i])







# 1. for문으로 1줄씩 돌아서 new_arr에 바로 입력해주기
# 2. 1을 찾으면 new_arr에 1 입력해주고 함수 실행
# 3. 함수에서 값을 찾으면 그 값에 계속 넣어주기