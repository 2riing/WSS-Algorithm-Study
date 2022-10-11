import sys
sys.stdin = open('../0606/input.txt')

def newLevel():
    for goal in range(257):
        temp = B
        new_ground = [g[:] for g in ground]
        sec = 0
        for i in range(N):
            for j in range(M):
                if new_ground[i][j] < goal: # 땅이 목표보다 작으면 추가 !
                    temp -= goal - new_ground[i][j]
                    sec += 1 * (goal - new_ground[i][j])
                    new_ground[i][j] = goal

                elif new_ground[i][j] > goal:
                    temp += new_ground[i][j] - goal
                    sec += 2 * (new_ground[i][j] - goal)
                    new_ground[i][j] = goal
                    
                else: # 같으면 아무것도 안해도 됨
                    pass
        if temp >= 0: # 음수이면 추가할 수 없음
            result.append((sec, goal))


input = sys.stdin.readline
N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)] # 땅을 고르게 만들어야 함
result = []

newLevel()
print(result)
sorted_result = result.sort()
print(*result[0])