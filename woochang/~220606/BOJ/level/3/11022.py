import sys
sys.stdin = open('input.txt')

a=int(input())
x = int(0)
for i in range(a):
    b,c=map(int,input().split())
    
    print("Case #",i+1,": ",b," + ",c," = ",b+c, sep='')