import sys
sys.stdin = open('18111input.txt')


def mine():
    global time, B, K
    for a in range(N):
        for b in range(M):
            if a == i and b == j:

                pass
            elif arr[i][j] > arr[a][b]:
                K = arr[i][j] - arr[a][b]
                if B >= K:
                    B = B-K
                    time += K
                else:
                    break
            elif arr[i][j] < arr[a][b]:
                K = arr[a][b] - arr[i][j]
                B += K
                time += 2*K



N, M, B = map(int ,input().split())
arr = [list(map(int, input().split()) )for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
height = 0
time = 0
time_min = 0
height_max = 0
K = 0
for i in range(N):
    for j in range(M):
        height = arr[i][j]
        time = 0
        if visited[i][j]:
            pass
        else:
            visited[i][j] = True
            mine()
            if height > height_max:
                height_max = height
                time_max = time
                height = 0
                time = 0
            # if time < time_min:
            #     time_min = time
            #     height_max = height
            #     height = 0
            #     time = 0



print(time_min ,height_max)




# 블록 제거는 2초 / 블록 추가는 1초 ( 인벤토리에 블록이 있어야됨)
# 블록 배치가 만약에
# 33 4 5 66
# 71 8 92 10
# 119 12 130 14
# 이런식으로 있으면 어디에 초점을 맞춰야되지
# 인벤토리가 얼마냐 있냐에 따라 나뉘겟는데
# 한 곳마다 중심 높이로 두고 완탐 돌려야되는듯
