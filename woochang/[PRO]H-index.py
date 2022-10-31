def solution(citations):
    answer = 0
    k = len(citations)
    citations.sort()
    for i in range(k):
        if citations[i] >= k - i:
            return k - i

    return answer