N = input()
cnt = 1
for i in range(len(N)):
    if N[i] == ' ':
        cnt += 1
if N[0] == ' ':
    cnt -= 1
if N[len(N)-1] == ' ':
    cnt -= 1
print(cnt)
