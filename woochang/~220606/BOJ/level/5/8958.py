import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T+1):
    arr =   list(map(str, input()))
    # total = 0
    # sum = 0

    cnt = 0
    total = 0
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt += 1
        elif arr[i] == 'X':
            total = cnt
            new_arr.append(total)
            cnt = 0
    total = cnt
    new_arr.append(total)

    n_total = 0
    for i in new_arr:
        n_total += i*(i+1)/2

    print ("%g" % (n_total))
