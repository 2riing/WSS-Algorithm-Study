import sys
sys.stdin= open('input.txt')

N = int(input())
arr = [list(input().split()) for _ in range(N)]

grade = []
for i in range(len(arr)):
    grade.append(int(arr[i][1]))

for j in range(len(arr)):
    if arr[j][1] == str(min(grade)):
        print(arr[j][0])
