N = int(input()) # 3
a = 0
b = 0
for i in range(1,N+1):
    if N <= i:
        if i % 2 == 1:
            a = i - N + 1
            b = N
        else:
            a = N
            b = i - N + 1
        break
    else:
        N -= i
print(f'{a}/{b}')
