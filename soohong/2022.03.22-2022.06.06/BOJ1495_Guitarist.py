import sys
sys.stdin = open('../0420/input.txt')

N, S, M = map(int, input().split())
V = list(map(int,input().split()))
arr = [[0]*(M+1) for _ in range(N+1)]
arr[0][S] = 1 # 일단 초기 start volume을 채워줍니다.


for i in range(N):
    for j in range(M+1):
        if arr[i][j] == 1:
            if j + V[i] <= M: # 최대 볼륨을 넘지 않는다면 !
                arr[i+1][j+V[i]] = 1 # V[i]를 더해준 값
            if j - V[i] >= 0:
                arr[i+1][j-V[i]] = 1 # V[i]를 빼준 값

answer = -1 # 불가능할경우 -1을 출력해야하기 때문에
for i in range(M,-1,-1):
    if arr[N][i] == 1: # 가능하다면 answer에다가 i를 넣어줌
        answer = i
        break
print(answer)


