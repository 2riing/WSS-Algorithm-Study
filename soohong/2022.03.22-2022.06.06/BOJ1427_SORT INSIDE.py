import sys
sys.stdin = open('input.txt')

num = list(map(int, input()))
num.sort(reverse=True)
for n in num:
    print(n, end='')