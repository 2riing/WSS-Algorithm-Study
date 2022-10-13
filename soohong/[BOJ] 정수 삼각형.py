import sys
sys.stdin = open('input.txt')


n = int(input())
arr = []
for _ in range(n):
  temp = list(map(int, input().split()))
  arr.append(temp)

for i in range(1, n):
  for j in range(len(arr[i])):
    if j == 0 : # 첫번째일 경우
      arr[i][j] += arr[i-1][j]
    elif j == len(arr[i])-1:
      arr[i][j] += arr[i-1][-1]
    else:
      arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[-1]))