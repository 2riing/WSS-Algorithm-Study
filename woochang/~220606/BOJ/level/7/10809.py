S = input()

arr_list = [-1]*26
arr_l = []
for i in range(len(S)):
    arr_l.append(ord(S[i]))
# print(arr_l)

# arr_list는 0부터 25까지 쭉
# a의 ord는 97
#arr_l[i]-97
for i in range(len(S)):
    # print(ord(S[i])-97)
    # arr_list[ord(S[i])-97] = i
    if arr_list[ord(S[i])-97] != (-1):
        pass
    else:
        arr_list[ord(S[i]) - 97] = i #ord(S[i])-97
        # arr_list[ord(S[i]) - 97] -= 1

print(*arr_list)
