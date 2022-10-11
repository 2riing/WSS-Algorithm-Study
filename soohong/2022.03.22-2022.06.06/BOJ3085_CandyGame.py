import sys
sys.stdin = open('input.txt')

def Findmax(point):
    global max_cnt
    col, row = 1, 1
    n1, n2, n3, n4 = 1, 1, 1, 1
    i, j = point[0], point[1]

    while True:
        if j + n1 < N and candy[i][j] == candy[i][j + n1]:  # 가로 검사 (오른쪽으로)
            col += 1
            n1 += 1
        elif j - n3 >= 0 and candy[i][j] == candy[i][j - n3]:  # 가로 검사(왼쪽)
            col += 1
            n3 += 1
        elif i - n4 >= 0 and candy[i][j] == candy[i - n4][j]:  # 세로 (위)
            row += 1
            n4 += 1
        elif i + n2 < N and candy[i][j] == candy[i + n2][j]:  # 세로 검사 (아래로)
            row += 1
            n2 += 1
        else:
            if row > max_cnt:
                max_cnt = row
            elif col > max_cnt:
                max_cnt = col
            return

N = int(input())
candy = [[] for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(len(temp)):
        candy[i].append(temp[j])
max_cnt = 0

# 가로로 바꾸기
for i in range(N):
    for j in range(N - 1):
        if candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]  # 둘이 자리를 바꿔줌
            Findmax([i, j])
            Findmax([i, j + 1])
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]  # 원상복구
        elif candy[i][j] == candy[i][j+1]:
            Findmax([i,j])
            Findmax([i, j + 1])

# 세로로 바꾸기
for i in range(N-1):
    for j in range(N):
        if candy[i][j] != candy[i+1][j]:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            Findmax([i,j])
            Findmax([i+1, j])
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
        elif candy[i][j] == candy[i+1][j]:
            Findmax([i,j])
            Findmax([i + 1, j])

print(max_cnt)
