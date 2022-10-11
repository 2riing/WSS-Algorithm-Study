from collections import deque
# 갈 수 없을 경우 -1
# 갈 수 있을 경우
#

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

def solution(maps):
    def BFS():
        q = deque()
        q.append([0,0])
        visited[0][0] = 1  # 방문체크
        while q:
            temp = q.popleft()
            row, col = temp[0], temp[1]
            for i in range(4):
                di, dj = row + ni[i], col + nj[i]
                if 0 <= di < n and 0 <= dj < m :
                    if visited[di][dj] == 0 and maps[di][dj] == 1:
                        visited[di][dj] = visited[row][col] + 1
                        q.append([di, dj])
                        if di == n - 1 and dj == m - 1:
                            return visited[di][dj]

    # 변수 선언
    ni, nj = [1, -1, 0, 0], [0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    answer = 0

    # 목적지의 한쪽이라도 뚫려있다면 bfs실행

    answer = BFS()
    # 정답 출력
    if visited[n-1][m-1] == 0:
        return -1
    else:
        return answer


print(solution(maps))
# DFS로 풀이 할 것
# 갈 수 있을 경우에 result에 append 해줌

