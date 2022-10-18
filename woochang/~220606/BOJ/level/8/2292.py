N = int(input())
x = 1
cnt = 1
for i in range(1,N):

    if N > x:
        cnt += 1
    else:

        break
    x += 6 * i
print(cnt)
