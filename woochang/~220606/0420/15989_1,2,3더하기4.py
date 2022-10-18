import sys
sys.stdin = open('15989input.txt')
from collections import deque


def bfs():
    global ans
    q = deque([[1],[2],[3]])
    visited = []
    while q:

        a = q.popleft()
        visited.append(a)
        a_1 = a + [1]
        a_2 = a + [2]
        a_3 = a + [3]
        a_1.sort()
        a_2.sort()
        a_3.sort()



        if a_1 not in visited and sum(a_1) < n + 1:
            if sum(a_1) == n:
                ans += 1
                visited.append(a_2)
            else:
                visited.append(a_1)
                q.append(a_1)

        if a_2 not in visited and sum(a_2) < n + 1:
            if sum(a_2) == n:
                ans += 1
                visited.append(a_2)
            else:
                visited.append(a_2)
                q.append(a_2)

        if a_3 not in visited and sum(a_3) < n + 1:
            if sum(a_3) == n:
                ans += 1
                visited.append(a_3)
            else:
                visited.append(a_3)
                q.append(a_3)





        # sort_1 = q.popleft()
        #
        # for i in range(1,4):
        #
        #     sort_1.append(i)
        #     sort_1.sort()
        #     if sort_1 not in q and sum(sort_1) < n+1:
        #         if sum(sort_1) == n:
        #             ans += 1
        #         else:
        #             q.append(sort_1)
        #             sort_1.pop()






N = int(input())
for i in range(N):
    n = int(input())
    ans = 0
    bfs()
    print(ans)


# bfs 로다가 0부터 시작해서 1,2,3 q에 넣고
# 그걸 다시 1,2,3 더한거로 q에 넣고
# 반복 / 7이 되면 카운트 += 1
# 근데 이렇게 되면 1,2,1 이나 2,1,1 이나 같아지므로 얘는 패스
# 그러면 스택에 넣어서 sort를 계속 해주는식으로?
# 그러면 같은 경우의 수는 일단 지워지긴할텐데 매번 sort가 되나

# 는 해결했는데 시간초과..