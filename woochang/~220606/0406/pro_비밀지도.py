import sys
sys.stdin = open('input비밀지도.txt')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    new_arr1 = []

    for arr in arr1:
        for i in range(n):
            if arr % 2 == 1:
                new_arr1[i].append('#')
            else:
                new_arr1[i].append('')
            arr = arr // 2

    print(new_arr1)
    # if len(new_arr1)

        # print(new_arr1)
# 이진수 변환 bin() -> bin(arr1[i][2:])|