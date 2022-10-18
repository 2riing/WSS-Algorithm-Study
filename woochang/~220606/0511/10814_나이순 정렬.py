import sys
sys.stdin = open('10814input.txt')

N = int(input())
fn_list = []
age_list = []

for i in range(N):
    a = input()
    fn_list.append(a)
    if a[1] == ' ':
        age_list.append(int(a[0]))
    elif a[2] == ' ':
        age_list.append(int(a[0:1]))
    else:
        age_list.append(int(a[0:2]))
print(age_list)

for i in range(N):
    min_age = 201
    min_index = 0
    for j in range(N):
        if min_age > age_list[j]:
            min_age = age_list[j]
            min_index = j
    print(fn_list[min_index])
    age_list[min_index] = 200

# 시간초과 N^2 번 돌려서 그럴 듯 ...
# -------------------------------

