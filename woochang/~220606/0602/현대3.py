

N = int(input())  # N = 3
cnt = 0
goyu = [[1,8], [2,7], [3,6], [4,5]]

for i in range(10**(N-1), 10**N): # 100~999
    n_list = []
    for j in range(N):
        n_list.append(i[j])
    if n_list not in 1 and n_list not in 8:
        cnt += 1
    elif n_list not in 2 and n_list not in 7:
        cnt += 1
    elif n_list not in 3 and n_list not in 6:
        cnt += 1
    elif n_list not in 4 and n_list not in 5:
        cnt += 1
    else:
        pass
print(cnt)


#
#     if sum_n //
#
#     pass

# 임의의 두 숫자 합했을때 9