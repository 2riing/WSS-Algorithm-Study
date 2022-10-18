import sys
sys.stdin = open('16926input.txt')


N, M, R = map(int, input().split(' '))
matrix = [list(map(int, input().split(' '))) for _ in range(N)]

if N >= M:  # K = min(M, N)
    K = M
else:
    K = N
for _ in range(R): #R번 돌려줄거라서
    for i in range(K // 2):
        dx, dy = i, i
        s_value = matrix[dx][dy]

        for j in range(i + 1, N - i):  #좌
            dx = j
            prev_value = matrix[dx][dy] #위치의 기존값을 prev_value에 저장
            matrix[dx][dy] = s_value    #그리고 matrix에는 새로운 값에 기존값 대입
            s_value = prev_value          # 그리고 기존값이 s_value에 저장

        for j in range(i + 1, M - i):  #하
            dy = j
            prev_value = matrix[dx][dy]
            matrix[dx][dy] = s_value
            s_value = prev_value

        for j in range(i + 1, N - i):  #우
            dx = N - j - 1
            prev_value = matrix[dx][dy]
            matrix[dx][dy] = s_value
            s_value = prev_value

        for j in range(i + 1, M - i):  #상
            dy = M - j -1
            prev_value = matrix[dx][dy]
            matrix[dx][dy] = s_value
            s_value = prev_value

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=' ')
    print()