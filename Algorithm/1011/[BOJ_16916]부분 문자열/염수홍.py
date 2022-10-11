import sys
sys.stdin = open('input1.txt')

S = input()
P = input()

if P in S:
    print(1)
else:
    print(0)
