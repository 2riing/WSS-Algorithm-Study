import sys
sys.stdin = open('17413input.txt')

S = str(input())
k = len(S)
index = 0
new_s = []
# for i in range(k-1,-1,-1):
#     if S[i] != '<' or S[i] != '>' or S[i] != ' ':
#         if i <= index:
#             index = i
rev_s = []
while index < k:
    if S[index] == "<":
        new_s.append(S[index])
        index += 1
        for _ in range(100000):
            if S[index] != ">":
                new_s.append(S[index])
                index += 1
            else:
                new_s.append(S[index])
                index += 1
                break
        # while S[index] != ">":
        #     new_s.append(S[index])
        #     index += 1
        # new_s.append(S[index])
        # index += 1
    elif S[index] != '<' and S[index] != '>' and S[index] != ' ':
        start = index
        while index < k and  S[index] != '<' and S[index] != '>' and S[index] != ' ':
            rev_s.append(S[index])
            index += 1
        rev_s.reverse()
        for i in rev_s:
            new_s.append(i)
        rev_s = []

    else:
        new_s.append(S[index])
        index += 1
print(new_s)
print(*new_s , sep='')