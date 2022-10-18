import sys
sys.stdin = open('11866input.txt')

# input = sys.stdin.readline

N, K = map(int, input().split())
yose = []
# new_yose = []
kill = []
for i in range(1, N+1):
    yose.append(i)
# new_yose = yose*8
# print(new_yose)
# yose.pop(3)
# print(yose)
# print(len(yose))
# print(new_yose)
# j = 1
index = K-1
# for i in range(N):
#     if new_yose[index] not in kill:
#         killed = new_yose[index]
#         kill.append(killed)
#         yose.pop(killed)
#         index += 3
#     else:
#         index += 1
#     if len(kill) == N:
#         break
# print(kill)

while True:
    if yose[index] not in kill:
        kill.append(yose[index])
        yose.pop(index)

        N -= 1
        if N <= 0:
            break
        index += K-1
        if index >= N:
            index = index % N
    else:
        index += 1
        if index >= N:
            index = index % N

# print(kill)
print('<', end='')
for i in range(len(kill)-1):
    print(kill[i], end=', ')
print(kill[-1], end='>')