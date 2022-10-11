import sys
sys.stdin = open('input.txt')


arr = list(map(int, input().split()))

arr.sort()

print(arr[1])
