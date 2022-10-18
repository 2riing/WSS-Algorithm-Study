import sys
sys.stdin = open('14502input.txt')
from itertools import combinations
from collections import deque


def make_b(a):
    for i in a:
        arr[i[0]][i[1]] = 1
    spread_b()
    for i in a:
        arr[i[0]][i[1]] = 0



def spread_b():
    global max_num , two_count
    visited = [[False for _ in range(M)] for _ in range(N)]
    true_count = 0
    # print(visited)
    for s in start_list:
        visited[s[0]][s[1]] = True
    dt = [[-1,0],[1,0],[0,1],[0,-1]]

    q = deque(start_list)
    while q:
        n = q.popleft()
        for i in dt:
            dx, dy = n[0]+i[0] , n[1] + i[1]
            if 0<=dx<N and 0<=dy<M:
                if visited[dx][dy] == False and arr[dx][dy] == 0:
                    visited[dx][dy] = True
                    q.append([dx,dy])
    for i in range(N):
        for j in range(M):
            if visited[i][j] == True:
                true_count += 1
    if max_num < zero_count - 3 - true_count + two_count:
        max_num = zero_count - 3 - true_count + two_count

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
zero_count = 0
two_count = 0
zero_list = []
start_list = []
for i in range(N):
    for j in range(M):

        if arr[i][j] == 0:
            zero_count += 1
            zero_list.append([i,j])
        elif arr[i][j] == 2:
            two_count += 1
            start_list.append([i,j])

zero_three = list(combinations(zero_list,3))
# print(zero_three)
for i in range(len(zero_three)):
    make_b(zero_three[i])

print(max_num)












#
# 0이 있는 곳의 좌표를 다 스택에 넣어줌
# 그리고 조합 combinations 사용해서 스택에서 0 좌표 3개씩 빼네서 make_b에 넣음
# 그리고 spread_B -> BFS 돌려서 바이러스 퍼트림
# 그 다음에 다시 전체 돌려서 0 개수 찾아내줌
# 조합 1번 할때마다 카운트 갯수 세서 최댓값 나오면 갱신해줌
#
# 안 짜봐도 무조건 시간초과 나올 쓰레기 코드....
# 일줄알았는데 범위가 8x8이 최대라 할만할지도?