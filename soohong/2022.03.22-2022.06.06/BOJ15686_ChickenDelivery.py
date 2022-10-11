import sys
sys.stdin = open('../0518/input.txt')

# 1은 집 2 는 치킨집
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

results = []
cnt = 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 2: # 치킨집을 찾으면
            temp = []
            for k1 in range(N):
                for k2 in range(N):
                    if city[k1][k2] == 1: # 집을 찾으면
                        temp.append(abs(i-k1) + abs(j-k2))
            results.append(temp)
print(results)

