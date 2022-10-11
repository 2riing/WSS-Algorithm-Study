import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
for i in range(N):
    a = int(input())
    arr.append(a)
arr.sort()
for a in arr:
    print(a)