def solution(N, stages):
    answer = []
    bucket = [0] * (N + 2)
    # 각 스테이지별 실패율 담아주기
    fails = []

    for stage in stages:
        bucket[stage] += 1
    # print(bucket)
    fail = bucket[1] / len(stages)
    fails.append(fail)
    for i in range(2, N + 1):
        if i == 1:
            fail = bucket[i] / (len(stages) - sum(bucket[1:i]))
        fails.append(fail)
    for i in range(N):

    return answer