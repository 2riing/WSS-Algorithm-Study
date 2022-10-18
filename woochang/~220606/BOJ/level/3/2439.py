N = int(input())
a = '*'
b = ' '
for i in range(1, N+1):
    print(b * (N-i), a * i , sep='')