N = int(input())

cnt = 0
if N % 5 == 0:
    cnt = N // 5
else:
    N = N % 5
    cnt = N // 5

if N % 3 == 0:
    cnt += N // 3
else:
    N += 5
if N % 3 == 0:
    cnt += N // 3
else:
    N += 5
if N % 3 == 0:
    cnt += N // 3
else:
    N += 5
if N % 3 == 0:
    cnt += N // 3
else:
    N += 5
print(cnt)