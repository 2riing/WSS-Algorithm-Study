# T = int(input())
#
# for tc in range(T):
#     C, B = list(map(str, input().split()))
#     A = int(C)
#     arr = []
#
#     for i in range(len(B)):
#         arr.append(B[i]*A)
#
#     print(*arr, sep='',end='')
#
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)