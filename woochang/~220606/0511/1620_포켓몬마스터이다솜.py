import sys
sys.stdin=open('1620input.txt')

N, M = map(int, input().split())
pkm_list = [0]
for i in range(N):
    pkm_list.append(input())

for i in range(1,M+1):
    a = str(input())
    # print(a)
    # print(type(a))
    # print(chr(a))
    if a[0] == '0' or a[0] == '1' or a[0] == '2' or a[0] == '3' or a[0] == '4' or a[0] == '5' or a[0] == '6' or a[0] == '7' or a[0] == '8' or a[0] == '9':

        print(pkm_list[int(a)])
    else:
        for j in range(N+1):
            if pkm_list[j] == a:
                print(j)


# # a = 97 , A = 65 , Z = 90
# N = list(map(str,input()))
#
# # N[0] = 'a'
# # print(N)
# # print(type(N))
# # print(type(chr(((ord(N[2])-96+13)%26)+96)))
# for i in range(len(N)):
#     if 123 > ord(N[i]) > 96:
#         N[i] = chr(((ord(N[i])-96+13)%26)+96)
#     if 91> ord(N[i]) > 64:
#         N[i] = chr(((ord(N[i])-64+13)%26)+64)
#     else:
#         pass
# print(*N, sep='')
# # print(len(N))