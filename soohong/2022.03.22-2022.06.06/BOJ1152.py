import sys
sys.stdin = open('private/input.txt')

S = input()
cnt = 0

if S[0] ==' ' or S[-1] == ' ':
    for i in range(1, len(S)-1):
        if S[i] == ' ':
            cnt += 1
else:
    for i in range(len(S)):
        if S[i] == ' ':
            cnt += 1
if S == ' ':
    print(0)
else:
    print(cnt+1)