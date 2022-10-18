import sys
sys.stdin = open('1912input.txt')

N = int(input())
arr = list(map(int, input().split()))
ans = -1000
res = [0] * N


# for i in range(0, N):
#     new_res = []
#     for j in range(N,i,-1):
#         new_res.append(sum(arr[i:j]))
#     res[i] = max(new_res)
# print(max(res))

for i in range(0, N):
    for j in range(N,i,-1):
       if ans <= sum(arr[i:j]):
           ans = sum(arr[i:j])
print(ans)


# input = sys.stdin.readline
# n = int(input().rstrip())
# a = list(map(int, input().split()))
# res = [0] * n
# res[0] = a[0]
# for j in range(1, n):
#     resum = []
#     for i in range(j + 1):
#         resum.append(sum(a[j - i:j + 1]))
#     res[j] = max(resum + [res[j - 1]])
# print(res[n - 1])

# n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))

