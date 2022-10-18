import sys
sys.stdin = open('11655input.txt')

# a = 97 , A = 65 , Z = 90
N = list(map(str,input()))

# N[0] = 'a'
# print(N)
# print(type(N))
# print(type(chr(((ord(N[2])-96+13)%26)+96)))
for i in range(len(N)):
    if 123 > ord(N[i]) > 96:
        N[i] = chr(((ord(N[i])-96+13)%26)+96)
    if 91> ord(N[i]) > 64:
        N[i] = chr(((ord(N[i])-64+13)%26)+64)
    else:
        pass
print(*N, sep='')
# print(len(N))
