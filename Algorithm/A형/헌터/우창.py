import sys
sys.stdin = open('input.txt')

# n은 재귀함수, loca는 현재위치(몬스터 1이면 loca==1, 클라이언트 1이면 loca==-1)
# dist는 현재까지 이동거리
def my_hunt(n, loca, dist):
    global result, cnt
    if n == cnt:
        if result  > dist:
            result = dist
        return

    # 현재 이동거리가 지금까지 최소 이동거리보다 커지면 return (백트래킹)
    if dist > result:
        return
    for i in range(1, cnt+1):
        if used[i]:
            continue
        used[i] = 1
        # 현재 i가 몬스터라면 (i <= cnt//2) 클라이언트에 방문할 수 있도록 used 배열 0으로 초기화
        if i <= cnt//2:
            used[i*(-1)] = 0
        my_hunt(n+1, i , dist + myGraph[loca][i])
        if i <= cnt//2:
            used[i*(-1)] = 1
        used[i] = 0
    return

T = int(input())

for tc in range(1, T+1):
    # 입력 받아 변수에 저장
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # cnt는 몬스터 + 클라이언트 수 저장
    cnt = 0
    result = 9999
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                cnt += 1

    # 맨해튼 거리 구하기 위한 좌표 저장
    # 각 포인트는 MAP에 저장된 값을 index로 가지는 위치에 좌표(x, y) 값이 저장됨
    # 몬스터의 index는 양수이므로 리스트의 앞쪽,
    # 이와 대칭되는 클라이언트는 음수이므로 리스트의 뒤쪽에서부터 저장되며 각각이 매칭됨
    # 0에는 사냥꾼의 위치 [0,0] 이 저장됨
    # points는 좌표 저장
    points = [[-1,-1] for _ in range(cnt+1)]

    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                points[MAP[r][c]][0] = r
                points[MAP[r][c]][1] = c

    # 각 몬스터와 클라이언트 간의 맨해튼 거리를 저장할 배열 선언
    myGraph = [[0 for _ in range(cnt+1)] for _ in range(cnt+1)]

    # 각 몬스터와 클라이언트 간의 맨해튼 거리 저장
    for i in range(1, cnt):
        for j in range(i+1, cnt+1):
            myGraph[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            myGraph[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    # 방문 배열 used 선언
    # 0은 쓰지않는 1로 채움
    # cnt//2 기준 앞은 몬스터, 뒤는 클라이언트임
    # 초기 상태는 클라이언트는 방문하지 않아야함(몬스터를 잡지 않았기 때문에)
    # 따라서 몬스터는 0, 클라이언트는 1로 초기화해주며
    # 이를 이용해 몬스터에 먼저 방문하고 클라이언트에 방문할 수 있도록 처리
    used = [1] + [0] *(cnt//2) + [1] * (cnt//2)

    # 처음 사냥꾼이 사냥을 할때는 몬스터만 방문함
    # 따라서 반복문의 범위는 1 ~ cnt//2 + 1
    for i in range(1, cnt//2 + 1):
        res = points[i][0] + points[i][1]
        used[i*(-1)] = 0
        used[i] = 1
        my_hunt(1, i ,res)
        used[i] = 0
        used[i*(-1)] = 1
    print(f'#{tc} {result}')