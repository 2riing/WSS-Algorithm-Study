T = int(input())
lst = list(map(int, input().split()))
# print(max(lst))

for i in range(T-1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
max_lst = lst[T-1]
new_lst = []
sum_new_lst = 0
for i in lst:

    j = i / max_lst * 100
    new_lst.append(j)
for i in range(T):
    sum_new_lst += new_lst[i]
print(sum_new_lst / T)