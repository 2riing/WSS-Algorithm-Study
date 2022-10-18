import sys
sys.stdin = open('22966input.txt')

N = int(input())
arr = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
ans = 5
ans_index = 0
for i in range(N):
    if int(arr[i][1]) < ans:
        ans = int(arr[i][1])
        ans_index = i
print(arr[ans_index][0])