import sys

sys.stdin = open('private/input.txt')


# 대소문자 아스키코드 차이 32
# 대문자 65- 90 소문자 97-122


def IsSame(num1, num2):  # 기존, 비교 할문자
    if 65 <= num2 <= 90:  # 대문자라면
        if num1 == num2 + 32 or num1 == num2:
            return 1
        else:
            return 0
    elif 97 <= num2 <= 122:  # 소문자라면
        if num1 == num2 - 32 or num1 == 2:
            return 1
        else:
            return 0
    else:
        return 0


S = list(input())
for i in range(len(S)):
    S[i] = ord(S[i])
S.sort()
max_cnt, cnt = 0, 0
temp = S[0]
max_index = []
for j in range(1, len(S)-1):
    if IsSame(temp, S[j]) == 1:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
            max_index.append(j)
            cnt = 0
        temp = S[j]
if max_cnt < cnt:
    max_cnt = cnt
if len(max_index) > 1:
    print('?')
else:
    print(chr(S[j]).upper())
