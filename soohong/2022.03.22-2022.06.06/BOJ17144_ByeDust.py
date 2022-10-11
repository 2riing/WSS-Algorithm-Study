import sys
sys.stdin = open('../0518/input.txt')

def Diffusion(point):
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    row, col = point
    cnt = 0
    for i in range(4):
        ni, nj = row + di[i], col + dj[i]
        if 0 <= ni < R and 0 <= nj < C:  # 범위안에 있고
            if room[ni][nj] != -1:  # 공청기가 아니면
                room[ni][nj] += int(room[row][col]/5)
                cnt += 1
    room[row][col] -= (int(room[row][col]/5) * cnt)
# 문제는 미먼이 동시에 확산해야함

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
# 공청기 -1 나머지 : 미세먼지의 양 / T초가 지난 후에 방에 남아있는 미세먼지의 양

# 공기 청정기가 있거나 '-1' 범위에 없으면 확산X
# 미세먼지 네방향 확산 A/5 소수점 버림
# 남은 미세먼지의 양 A - (A/5)*확산된 방향 개수

for k1 in range(R):
    for k2 in range(C):
        if room[k1][k2] > 0:
            Diffusion((k1, k2))
print(room)


# 새로운 room2를 만들어서 애들을 더해준다음에 room + room2를
# 하면 먼지가 동시에 확산되는것 을 구현할 수 있을 것