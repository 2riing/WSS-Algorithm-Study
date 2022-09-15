N = [5,4]
stages = [[2, 1, 2, 6, 2, 4, 3, 3],[4,4,4,4,4]]


def solution(N, stages):
    answer = []
    # stages.sort()
    p = [0 for _ in range(N + 1)]
    ans = []
    for i in stages:
        p[i - 1] += 1
    for i in range(N):
        if sum(p) != 0:
            pp = p[i]
            ans.append(pp / sum(p))
            p[i] = 0
        else:
            ans.append(0)
    print(ans)

    for i in range(N):
        min_ans = -1
        min_index = 0
        for j in range(N):
            if ans[j] > min_ans:
                min_ans = ans[j]
                min_index = j
        answer.append(min_index + 1)
        ans[min_index] = -1

    return answer


for i in range(len(N)):
    ans = solution(N[i], stages[i])
    print(ans)