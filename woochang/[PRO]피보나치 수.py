def solution(n):
    answer = 0
    li = list(0 for _ in range(n + 1))
    li[1] = 1
    # print(li)
    for i in range(2, n+1): # n까지
        li[i] = li[i-1] + li[i-2] # F(n) = F(n-1) + F(n-2)
    answer += (li[-1] % 1234567)
    return answer

# 디피 좋아요