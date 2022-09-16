import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        a = list(map(int,input().split()))
        arr.append(a)
    visited = [[0 for _ in range(31)] for _ in range(31)]
    for i in arr:
        i[0] += 15
        i[1] += 15
    for i in range(31):
        for j in range(31):
            r = abs(arr[0][0] - i) + abs(arr[0][1] - j)
            if arr[0][2] >= r:
                visited[i][j] = 1
    for k in range(1,N):
        for i in range(31):
            for j in range(31):
                r = abs(arr[k][0] - i) + abs(arr[k][1] - j)
                if arr[k][2] >= r:
                    visited[i][j] += (k+1)
    p = 1
    for i in range(1, N+1):
        p *= i

    stack = []
    for i in range(31):
        for j in range(31):
            if visited[i][j] > 0 :
                stack.append([i,j])
    print(stack)


# 1.
# 모든 충전소 거리 싹다 구하고 그 거리에 맞는 놈들 싸그리 모은후
# 그거를 다시 돌려서 거리 계산한 것들중에 최솟값
# 근데 얘는 충전소 2개일때는 결국 계산이 안되서 1개일때 기준인 문제임

# 2.
# 모든 점들 기반으로 거리 구해보기
# 충전소 1개일때 , 2개일때 맞춰서 (2개일때는 조합으로 2개 찍어서)

# 3.
# 이 위 2개를 조합하면
# 모든 충전소 거리 싹다 구해서 나온 곳들의 모임 점들을 기반으로
# 충전소 1개일때 + 충전소 2개(조합) 으로 돌려서 거리를 다 구해준다.
# 충전소 1개일때는 그냥 최소거리 구해주고
# 충전소 2개일때는 최솟값인 곳들만 구해줘가지고
# 그렇게 다 더하면 값이 나오지 않을까?
# 하는데 무조건 시간초과 날것같은 문제임
# 그래서 이거 어케품? 말도안되

#1 2
#2 3
#3 36
#4 -1
#5 21