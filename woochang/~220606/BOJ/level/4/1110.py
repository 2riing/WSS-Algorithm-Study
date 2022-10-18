N = int(input())


def cycle(N):
    a = N // 10
    b = N % 10
    c = a + b
    new_N = 10*b + c % 10
    return new_N
a = N
cnt = 1
while True :
    if a != cycle(N):
        cnt += 1
        N = cycle(N)
    elif a == cycle(N):
        break
print(cnt)