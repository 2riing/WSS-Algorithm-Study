import sys
sys.stdin = open('input.txt')

# a, b = map(int,input().split())
# while True:
#     print(a+b)
#     if a==0 and b==0:
    
#     break

while True:
    A, B=map(int,input().split())
    if A==0 and B == 0 :
        break
    print(A+B)